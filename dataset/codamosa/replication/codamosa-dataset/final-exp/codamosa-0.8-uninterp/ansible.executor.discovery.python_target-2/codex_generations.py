

# Generated at 2022-06-12 21:15:00.068364
# Unit test for function read_utf8_file
def test_read_utf8_file():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    result = read_utf8_file('/home')
    print(result)

# Generated at 2022-06-12 21:15:08.919064
# Unit test for function get_platform_info
def test_get_platform_info():
    # Assert that the function returns values from platform.dist() and outer-release contents if the files are present
    assert get_platform_info() == {'platform_dist_result': ('', '', ''), 'osrelease_content': 'NAME="Gentoo Base System release 2.6"\n' 'ID=gentoo\n' 'PRETTY_NAME="Gentoo/Linux"\n' 'ANSI_COLOR="1;32"\n' 'HOME_URL="https://www.gentoo.org/"\n' 'SUPPORT_URL="https://wiki.gentoo.org/wiki/Sections/Support"\n' 'BUG_REPORT_URL="https://bugs.gentoo.org/"\n'}

# Generated at 2022-06-12 21:15:11.509828
# Unit test for function read_utf8_file
def test_read_utf8_file():
    result = read_utf8_file('docs/docsite/index.rst')
    assert result is not None
    assert "Welcome to Ansible's documentation!" in result
    assert ".. toctree::" in result

# Generated at 2022-06-12 21:15:19.358845
# Unit test for function get_platform_info
def test_get_platform_info():
    # Test case where there is no distribution info
    osrelease_content = 'PRETEND_OS_RELEASE'
    osrelease_file_content = """PRETEND_OS_RELEASE"""
    assert os.access('/etc/os-release', os.R_OK) == True
    os.unlink('/etc/os-release')
    assert os.access('/etc/os-release', os.R_OK) == False
    assert get_platform_info() == {'platform_dist_result': [], 'osrelease_content': None}
    os.mkfifo('/etc/os-release')
    assert get_platform_info() == {'platform_dist_result': [], 'osrelease_content': None}
    os.unlink('/etc/os-release')

# Generated at 2022-06-12 21:15:25.494884
# Unit test for function get_platform_info
def test_get_platform_info():
    info_dict = get_platform_info()
    if 'platform_dist_result' in info_dict:
        platform_dist_result = info_dict['platform_dist_result']
    else:
        platform_dist_result = ""
    assert platform_dist_result != ""
    if 'osrelease_content' in info_dict:
        osrelease_content = info_dict['osrelease_content']
    else:
        osrelease_content = ""
    assert osrelease_content != ""

# Generated at 2022-06-12 21:15:33.522782
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()
    assert type(info['platform_dist_result']) == list
    assert type(info['osrelease_content']) == str
    assert info['platform_dist_result'][0] == 'Linux'
    assert info['platform_dist_result'][1] == '4.15.0-20-generic'
    assert info['platform_dist_result'][2] == 'xenial'
    assert 'ID=ubuntu' in info['osrelease_content']
    assert 'VERSION_ID="16.04"' in info['osrelease_content']

# Generated at 2022-06-12 21:15:34.877219
# Unit test for function get_platform_info
def test_get_platform_info():
    result = get_platform_info()
    assert result['osrelease_content'] != ""

# Generated at 2022-06-12 21:15:39.540461
# Unit test for function read_utf8_file
def test_read_utf8_file():
    assert read_utf8_file('/path/to/invalid/file.txt') is None
    assert read_utf8_file('/usr/bin/python') is not None
    # The next line is to check that non-ascii characters are handled properly
    # Test file is generated using:
    #   echo -n 'Hello, Данило!' > /tmp/test.txt
    assert read_utf8_file('/tmp/test.txt') == u'Hello, Данило!'

# Generated at 2022-06-12 21:15:44.607816
# Unit test for function read_utf8_file
def test_read_utf8_file():
    with open("test_read_utf8_file", "w") as f:
        f.write("test_read_utf8_file_content")

    result = read_utf8_file("test_read_utf8_file", "utf-8")
    assert result == "test_read_utf8_file_content"

# Generated at 2022-06-12 21:15:45.962230
# Unit test for function get_platform_info
def test_get_platform_info():
    assert get_platform_info()['platform_dist_result'] == []

# Generated at 2022-06-12 21:15:51.714875
# Unit test for function get_platform_info
def test_get_platform_info():
    data = get_platform_info()
    assert isinstance(data, dict)
    assert 'platform_dist_result' in data
    assert 'osrelease_content' in data
    assert isinstance(data['platform_dist_result'], list)
    assert isinstance(data['osrelease_content'], str)

# Generated at 2022-06-12 21:16:01.683583
# Unit test for function read_utf8_file
def test_read_utf8_file():
    test_file_name = './__test_read_utf8_file__'

    # Ensure file does not exist
    if os.path.exists(test_file_name):
        os.remove(test_file_name)
    assert(not os.path.exists(test_file_name))

    # File does not exists, expect None
    assert(read_utf8_file(test_file_name) == None)

    # Write content into file and read it back
    test_file_content = 'abc'
    with open(test_file_name, 'w') as test_file:
        test_file.write(test_file_content)
    assert(read_utf8_file(test_file_name) == test_file_content)

    # Cleanup

# Generated at 2022-06-12 21:16:12.569905
# Unit test for function read_utf8_file
def test_read_utf8_file():
    from ansible.module_utils.distro import read_utf8_file
    from ansible.module_utils._text import to_native

    assert read_utf8_file(__file__)
    assert read_utf8_file('/dev/null') is None
    assert read_utf8_file(os.path.join(os.path.sep, 'etc', 'passwd'))
    assert read_utf8_file(to_native(__file__))
    assert read_utf8_file(to_native('/dev/null')) is None
    assert read_utf8_file(to_native(os.path.join(os.path.sep, 'etc', 'passwd')))

# Generated at 2022-06-12 21:16:17.972517
# Unit test for function read_utf8_file
def test_read_utf8_file():
    name_file   = '/tmp/test_file'
    content_tmp = 'This is test'
    try:
        with open(name_file, 'w') as f:
            f.write(content_tmp)

        assert(read_utf8_file(name_file) == content_tmp)
    finally:
        os.remove(name_file)


# Generated at 2022-06-12 21:16:25.112510
# Unit test for function get_platform_info
def test_get_platform_info():

    # Mock os-release file
    os_release = """NAME="A Sample Linux"
ID=samplinux
ID_LIKE=fedora debian
VERSION_ID=1.1
"""

    expected = {
        "platform_dist_result": [],
        "osrelease_content": os_release
    }

    if os.path.exists('/etc/os-release'):
        os.remove('/etc/os-release')

    # Create os-release file
    with open('/etc/os-release', 'w') as f:
        f.write(os_release)

    assert get_platform_info() == expected

# Generated at 2022-06-12 21:16:36.887460
# Unit test for function get_platform_info
def test_get_platform_info():
    from collections import namedtuple

    class MockIoOpen:
        def __init__(self, filename, mode, encoding):
            self.filename = filename
            self.mode = mode
            self.encoding = encoding

# Generated at 2022-06-12 21:16:44.053304
# Unit test for function get_platform_info
def test_get_platform_info():
    assert get_platform_info() == dict(osrelease_content=u'NAME="Amazon Linux AMI"\nVERSION="2018.03"\nID="amzn"\nID_LIKE="rhel fedora"\nVERSION_ID="2018.03"\nPRETTY_NAME="Amazon Linux AMI 2018.03"\nANSI_COLOR="0;33"\nCPE_NAME="cpe:/o:amazon:linux:2018.03:ga"\nHOME_URL="http://aws.amazon.com/amazon-linux-ami/"\n', platform_dist_result=('amazon', '2', '2018.03'))



# Generated at 2022-06-12 21:16:45.058325
# Unit test for function read_utf8_file
def test_read_utf8_file():
    data = read_utf8_file('a.txt')

# Generated at 2022-06-12 21:16:47.732919
# Unit test for function get_platform_info
def test_get_platform_info():
    assert(get_platform_info() == {
        'osrelease_content': None,
        'platform_dist_result': []
    })

# Generated at 2022-06-12 21:16:49.461640
# Unit test for function read_utf8_file
def test_read_utf8_file():
    assert read_utf8_file('ping.py') is not None

# Generated at 2022-06-12 21:16:56.116425
# Unit test for function read_utf8_file
def test_read_utf8_file():
    os.environ['ANSIBLE_TEST_CP_DATA_PATH'] = os.path.dirname(os.path.abspath(__file__))
    data = read_utf8_file('README.md')
    assert data is not None

    # Test file with no permissions
    os.chmod('README.md', 0000)
    data = read_utf8_file('README.md')
    assert data is None
    os.chmod('README.md', 0o644)

# Generated at 2022-06-12 21:17:00.818230
# Unit test for function read_utf8_file
def test_read_utf8_file():
    assert read_utf8_file('./test_notexist') == None
    assert read_utf8_file('./test_utf8.txt') == u'\u00E9\u00E0\u00E9\n'


# Generated at 2022-06-12 21:17:03.994352
# Unit test for function get_platform_info
def test_get_platform_info():
    result = get_platform_info()
    assert(type(result) == dict)
    assert('platform_dist_result' in result)
    assert('osrelease_content' in result)

# Generated at 2022-06-12 21:17:06.162894
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()
    assert info == {'platform_dist_result': [], 'osrelease_content': ''}

# Generated at 2022-06-12 21:17:13.248739
# Unit test for function get_platform_info
def test_get_platform_info():
    assert get_platform_info()['osrelease_content'] == None
    assert len(get_platform_info()['platform_dist_result']) == 3
    assert isinstance(get_platform_info()['platform_dist_result'], list)
    assert get_platform_info()['platform_dist_result'][0] == ''
    assert get_platform_info()['platform_dist_result'][1] == ''
    assert get_platform_info()['platform_dist_result'][2] <= 9

# Generated at 2022-06-12 21:17:18.360755
# Unit test for function read_utf8_file
def test_read_utf8_file():
    assert read_utf8_file('test.txt') == None
    assert read_utf8_file('test_read_utf8_file.py', 'utf-16') == None

# Generated at 2022-06-12 21:17:27.379269
# Unit test for function read_utf8_file
def test_read_utf8_file():
    info = read_utf8_file('/tmp')
    assert info is None
    info = read_utf8_file('/etc')
    assert info is not None
    info = read_utf8_file('/etc')
    assert info is not None
    # test a non-utf8 file
    info = read_utf8_file('/usr/share/X11/xkb/rules/evdev')
    assert info is not None
    # test a non-existing file
    info = read_utf8_file('/tmp/does-not-exist')
    assert info is None

# Generated at 2022-06-12 21:17:38.929596
# Unit test for function get_platform_info
def test_get_platform_info():
    import sys
    import shutil

    if sys.version_info[:2] == (2, 6):
        import unittest2 as unittest
    else:
        import unittest

    path_to_open = '/etc/os-release'
    path_to_fallback = '/usr/lib/os-release'

    class TestGetPlatformInfo(unittest.TestCase):
        def setUp(self):
            os.makedirs('/etc', exist_ok=True)
            os.makedirs('/usr/lib', exist_ok=True)

            with open(path_to_open, 'w') as f:
                f.write('ID=ubuntu')


# Generated at 2022-06-12 21:17:40.787913
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()

    assert 'platform_dist_result' in info
    assert 'osrelease_content' in info

# Generated at 2022-06-12 21:17:51.981095
# Unit test for function get_platform_info

# Generated at 2022-06-12 21:17:57.646692
# Unit test for function read_utf8_file
def test_read_utf8_file():
    assert read_utf8_file('fixtures/test_read_utf8_file') == 'foobar\n'
    assert read_utf8_file('fixtures/test_read_utf8_file_unicode', 'utf-8-sig') == u'a \u00a9 b \u00ae\n'

# Generated at 2022-06-12 21:18:03.765687
# Unit test for function get_platform_info
def test_get_platform_info():

    expected = {
        u'osrelease_content': u'NAME="Ubuntu"\nVERSION="14.04.5 LTS, Trusty Tahr"\nID=ubuntu\nID_LIKE=debian\nPRETTY_NAME="Ubuntu 14.04.5 LTS"\nVERSION_ID="14.04"\nHOME_URL="http://www.ubuntu.com/"\nSUPPORT_URL="http://help.ubuntu.com/"\nBUG_REPORT_URL="http://bugs.launchpad.net/ubuntu/"',
        u'platform_dist_result': [u'', u'', u'']
    }

    assert get_platform_info() == expected

# Generated at 2022-06-12 21:18:15.493235
# Unit test for function get_platform_info
def test_get_platform_info():
    import os
    import tempfile
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.platform import get_platform_info
    from ansible.module_utils.six import PY2

    module = AnsibleModule(argument_spec={})
    platform_info = get_platform_info()
    if PY2:
        module.fail_json(msg='platform.py not supported on Python 2')


# Generated at 2022-06-12 21:18:17.165758
# Unit test for function get_platform_info
def test_get_platform_info():
    result = get_platform_info()
    assert result['platform_dist_result'] == platform.dist()

# Generated at 2022-06-12 21:18:19.002942
# Unit test for function read_utf8_file
def test_read_utf8_file():
    assert read_utf8_file('/etc/os-release') is not None


# Generated at 2022-06-12 21:18:22.781206
# Unit test for function get_platform_info
def test_get_platform_info():
    data = get_platform_info()
    assert isinstance(data['osrelease_content'], str)
    assert len(data['platform_dist_result']) == 3
    assert len(data['platform_dist_result'][0]) > 0



# Generated at 2022-06-12 21:18:24.089582
# Unit test for function read_utf8_file
def test_read_utf8_file():
    result = read_utf8_file('/etc/os-release')
    assert result is not None


# Generated at 2022-06-12 21:18:28.397365
# Unit test for function read_utf8_file
def test_read_utf8_file():
    temp = 'test/test_distro/file_temp'
    assert read_utf8_file(temp) is None
    with io.open(temp, 'w', encoding='utf-8') as fd:
        fd.write(u'Test string for read_utf8_file function\n')
    assert read_utf8_file(temp) == u'Test string for read_utf8_file function\n'
    os.unlink(temp)


# Generated at 2022-06-12 21:18:35.672681
# Unit test for function get_platform_info
def test_get_platform_info():
    information = get_platform_info()
    assert isinstance(information, dict)
    assert 'platform_dist_result' in information
    if information['platform_dist_result']:
        assert isinstance(information['platform_dist_result'], list)
        assert len(information['platform_dist_result']) > 0
    assert 'osrelease_content' in information
    if information['osrelease_content']:
        assert isinstance(information['osrelease_content'], str)

# Generated at 2022-06-12 21:18:38.784538
# Unit test for function read_utf8_file
def test_read_utf8_file():
    path = 'data.txt'
    with open(path, 'w') as writer:
        writer.write('abcd')
    content = read_utf8_file(path)
    os.remove(path)
    assert content == 'abcd'

# Generated at 2022-06-12 21:18:47.410735
# Unit test for function read_utf8_file
def test_read_utf8_file():
    import tempfile
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes

    module = AnsibleModule(
        argument_spec=dict(),
    )

    with tempfile.NamedTemporaryFile() as tmpfile:
        tmpfile.write(to_bytes("foobar", encoding='utf-8'))
        tmpfile.flush()
        assert read_utf8_file(tmpfile.name) == "foobar"

# Generated at 2022-06-12 21:18:53.999053
# Unit test for function read_utf8_file
def test_read_utf8_file():
    encoded_data = b'\xc2\xbc'
    encoded_utf8 = encoded_data.decode('utf-8')
    filepath = '/tmp/ansible_test_utf8_file.txt'

    with open(filepath, 'wb') as f:
        f.write(encoded_data)
    content = read_utf8_file(filepath)
    os.remove(filepath)

    assert content == encoded_utf8

# Generated at 2022-06-12 21:18:56.524194
# Unit test for function read_utf8_file
def test_read_utf8_file():
    assert read_utf8_file('/etc/os-release')
    assert not read_utf8_file('/etc/os-releasefake')



# Generated at 2022-06-12 21:18:58.786286
# Unit test for function read_utf8_file
def test_read_utf8_file():
    result = read_utf8_file('/etc/os-release')
    assert isinstance(result, str)


# Generated at 2022-06-12 21:19:09.440828
# Unit test for function get_platform_info
def test_get_platform_info():
    test_platform_dist_result = 'test'
    test_osrelease_content = 'test'
    test_result = {'platform_dist_result': test_platform_dist_result,
                   'osrelease_content': test_osrelease_content}

    test_platform = type('', (), {'dist': lambda self: test_platform_dist_result})
    test_platform.dist = lambda self: test_platform_dist_result
    test_os = type('', (), {'path': type('', (), {'exists': lambda self, filename: True})})
    test_os.path.exists = lambda self, filename: True
    test_io = type('', (), {'open': type('', (), {'read': lambda self: test_osrelease_content})})
    test_io.open.read = lambda self: test

# Generated at 2022-06-12 21:19:10.971756
# Unit test for function get_platform_info
def test_get_platform_info():
    assert isinstance(get_platform_info(), dict)

# Generated at 2022-06-12 21:19:12.538038
# Unit test for function read_utf8_file
def test_read_utf8_file():
    assert read_utf8_file(__file__) is not None

# Generated at 2022-06-12 21:19:21.660566
# Unit test for function read_utf8_file
def test_read_utf8_file():

    # setup for test
    some_file = 'foo'
    with io.open(some_file, 'w', encoding='utf-8') as fd:
        fd.write(u'bar')

    # read a file that exists as utf-8 string
    result = read_utf8_file(some_file)
    assert result == 'bar'

    # clean up
    try:
        os.remove(some_file)
    except OSError:
        pass



# Generated at 2022-06-12 21:19:23.715302
# Unit test for function get_platform_info
def test_get_platform_info():
    assert len(get_platform_info()['platform_dist_result']) == 3
    assert get_platform_info()['osrelease_content'] != ''

# Generated at 2022-06-12 21:19:25.779167
# Unit test for function get_platform_info
def test_get_platform_info():
    result = get_platform_info()
    expected_result = dict(platform_dist_result=[], osrelease_content='')
    assert result == expected_result

# Generated at 2022-06-12 21:19:35.586492
# Unit test for function read_utf8_file
def test_read_utf8_file():
    assert read_utf8_file('/tmp/404file') is None

    with open('/tmp/test_file', 'w') as f:
        f.write(u'test_data')

    data = read_utf8_file('/tmp/test_file')
    assert data == 'test_data'

    os.remove('/tmp/test_file')



# Generated at 2022-06-12 21:19:44.092862
# Unit test for function read_utf8_file

# Generated at 2022-06-12 21:19:48.117822
# Unit test for function get_platform_info
def test_get_platform_info():
    osrelease_content = read_utf8_file('/etc/os-release')
    platform_dist_result = platform.dist()

    assert osrelease_content == get_platform_info()['osrelease_content'] and platform_dist_result == get_platform_info()['platform_dist_result']

# Generated at 2022-06-12 21:19:51.915664
# Unit test for function read_utf8_file
def test_read_utf8_file():
    assert read_utf8_file(path='/etc/os-release') == read_utf8_file(path='/etc/os-release')
    assert read_utf8_file(path='/etc/os-release').startswith('NAME="Amazon Linux"') == True


# Generated at 2022-06-12 21:19:55.755951
# Unit test for function get_platform_info
def test_get_platform_info():
    results = get_platform_info()
    assert results['osrelease_content'].startswith('NAME=')
    assert len(results['platform_dist_result']) == 3
    assert len(results['platform_dist_result'][0]) > 0
    assert len(results['platform_dist_result'][1]) > 0
    assert len(results['platform_dist_result'][2]) > 0

# Generated at 2022-06-12 21:19:56.967062
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()
    assert info['osrelease_content']

# Generated at 2022-06-12 21:20:04.304116
# Unit test for function read_utf8_file
def test_read_utf8_file():
    fail_path = '/tmp/path_that_does_not_exist'
    success_path = '/etc/os-release'
    if os.path.isfile(success_path):
        assert read_utf8_file(success_path)
        assert read_utf8_file(success_path, 'utf-8')
        assert not read_utf8_file(fail_path)
        assert not read_utf8_file(fail_path, 'utf-8')


# Generated at 2022-06-12 21:20:05.702237
# Unit test for function read_utf8_file
def test_read_utf8_file():
    assert read_utf8_file("example.txt") == "example"

# Generated at 2022-06-12 21:20:10.860968
# Unit test for function read_utf8_file
def test_read_utf8_file():

    # Create a test file
    import tempfile
    test_file = tempfile.NamedTemporaryFile(mode='w+t', encoding='utf-8', delete=False)
    test_file.write('abc')
    test_file.close()

    # Test if the file exists
    assert(os.path.exists(test_file.name))
    assert(read_utf8_file(test_file.name) == 'abc')

    # cleanup
    os.unlink(test_file.name)


test_read_utf8_file()

# Generated at 2022-06-12 21:20:13.745035
# Unit test for function get_platform_info
def test_get_platform_info():
    result = get_platform_info()

    assert len(result['platform_dist_result']) == 3
    assert result['osrelease_content']

# Generated at 2022-06-12 21:20:22.560509
# Unit test for function read_utf8_file
def test_read_utf8_file():
    assert read_utf8_file('/etc/os-release') is not None
    assert read_utf8_file('/usr/lib/os-release') is not None
    assert read_utf8_file('/idontexist') is None

# Generated at 2022-06-12 21:20:25.674782
# Unit test for function read_utf8_file
def test_read_utf8_file():
    assert read_utf8_file("test/test_file.txt") == "sample file\n"
    assert read_utf8_file("test/test_file.txt") != "sample file1\n"

# Generated at 2022-06-12 21:20:30.582923
# Unit test for function get_platform_info
def test_get_platform_info():
    return_value = get_platform_info()
    assert isinstance(return_value['platform_dist_result'], tuple)
    assert isinstance(return_value['osrelease_content'], str)
    assert return_value['osrelease_content'].startswith('ID=')

# Generated at 2022-06-12 21:20:39.736397
# Unit test for function get_platform_info
def test_get_platform_info():
    """
    Tests the returned values of the platform info given
    specific test data

    """

    # test data is stored in test_platform_info.json
    with open('test_platform_info.json', 'r') as test_data:
        data = json.load(test_data)

    osrelease_content = read_utf8_file(data['osrelease_path'])
    result = dict(platform_dist_result=[])
    result['platform_dist_result'] = platform.dist(supported_dists=data['supported_dists'],
                                                   full_distribution_name=data['full_distribution_name'])
    result['osrelease_content'] = osrelease_content

    assert result == data, 'test_get_platform_info() failed'

# Generated at 2022-06-12 21:20:43.193822
# Unit test for function read_utf8_file
def test_read_utf8_file():
    assert read_utf8_file(os.path.join(os.path.dirname(__file__), 'test_data/utf8_file.txt'), 'utf-8') == u'баба мимими'

# Generated at 2022-06-12 21:20:47.120216
# Unit test for function get_platform_info
def test_get_platform_info():
    with open('test_get_platform_info.json', 'r') as test_values:
        expected_result = json.load(test_values)
    result = get_platform_info()
    assert expected_result == result

# Generated at 2022-06-12 21:20:49.644684
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()
    assert isinstance(info['platform_dist_result'], list)
    assert info['osrelease_content'] != ''

# Generated at 2022-06-12 21:20:59.112511
# Unit test for function get_platform_info
def test_get_platform_info():
    from mock import patch

    mocks = {
        '/etc/os-release': 'ID=ubuntu\nPRETTY_NAME="Ubuntu 16.04"',
        '/usr/lib/os-release': 'ID=ubuntu\nPRETTY_NAME="Ubuntu 16.04"',
    }

    for path, content in mocks.items():
        with patch('ansible.module_utils.facts.platform_impl.read_utf8_file') as _read_utf8_file:
            _read_utf8_file.return_value = content
            info = get_platform_info()

            assert info['osrelease_content'] == content


# Generated at 2022-06-12 21:21:02.965092
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()
    assert info['platform_dist_result'] == []
    assert not info['osrelease_content']

# Generated at 2022-06-12 21:21:06.762684
# Unit test for function read_utf8_file
def test_read_utf8_file():
    assert not read_utf8_file('/tmp')
    path = os.path.join(os.path.dirname(__file__), 'ansible_facts.py')
    assert read_utf8_file(path).startswith('#!/usr/bin/env python')


# Generated at 2022-06-12 21:21:20.462445
# Unit test for function get_platform_info
def test_get_platform_info():
    from ansible_collections.ansible.community.plugins.module_utils.distro import os_release_info
    from ansible_collections.ansible.community.plugins.module_utils.distro import platform_distro_info
    from ansible_collections.ansible.community.plugins.module_utils.distro import get_os_from_platform_distro_info

    os_release_info_mock = os_release_info.OsReleaseInfo.from_content(read_utf8_file('/etc/os-release'))


# Generated at 2022-06-12 21:21:25.257688
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()

    # FUTURE: this could be expanded to include more cases for
    # other distributions at the same time.

    assert info['platform_dist_result'] == []
    assert 'NAME="Red Hat Enterprise Linux Server"' in info['osrelease_content']

# Generated at 2022-06-12 21:21:25.858385
# Unit test for function read_utf8_file
def test_read_utf8_file():
    assert read_utf8_file('/bin/cat') == None

# Generated at 2022-06-12 21:21:28.278006
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()
    assert info.get('osrelease_content') is not None

# Generated at 2022-06-12 21:21:31.040170
# Unit test for function get_platform_info
def test_get_platform_info():
    assert isinstance(get_platform_info(), dict)
    assert isinstance(get_platform_info()["platform_dist_result"], list)
    assert isinstance(get_platform_info()["osrelease_content"], str)

# Generated at 2022-06-12 21:21:33.227186
# Unit test for function get_platform_info
def test_get_platform_info():
    assert 'platform_dist_result' in get_platform_info()
    assert 'osrelease_content' in get_platform_info()

# Generated at 2022-06-12 21:21:43.733020
# Unit test for function get_platform_info
def test_get_platform_info():
    fake_distro_info = ['RhEL', '5.5', 'Santiago', '1', 'x86_64']
    fake_osrelease_content = '''ID=rhel
VERSION_ID=5.5
PRETTY_NAME="Red Hat Enterprise Linux Server release 5.5 (Tikanga)"
NAME=Red Hat Enterprise Linux
VERSION=5.5
'''

    def fake_distro(distname='', version='', id='', release='', codename=''):
        return (distname, version, id, release, codename)

    def fake_read_utf8_file(path, encoding='utf-8'):
        return fake_osrelease_content


# Generated at 2022-06-12 21:21:45.513171
# Unit test for function get_platform_info
def test_get_platform_info():
    result = get_platform_info()

    assert result['osrelease_content'] == ""

# Generated at 2022-06-12 21:21:46.701238
# Unit test for function get_platform_info
def test_get_platform_info():
    result = get_platform_info()
    assert result is not None

# Generated at 2022-06-12 21:21:50.886574
# Unit test for function read_utf8_file
def test_read_utf8_file():
    test_file = '/tmp/delegation_test'
    with open(test_file, 'w') as f:
        f.write('hello')
    with open(test_file, 'r') as f:
        res = f.read()
    assert(res == 'hello')

# Generated at 2022-06-12 21:21:57.945162
# Unit test for function get_platform_info
def test_get_platform_info():

    with open('test_data/os-release', 'r') as fd:
        test_osrelease_content = fd.read()

    with open('test_data/platform_info.json', 'r') as fd:
        test_result = json.load(fd)

    assert(test_result == get_platform_info())

# Generated at 2022-06-12 21:22:00.384615
# Unit test for function read_utf8_file
def test_read_utf8_file():
    assert read_utf8_file('file.txt', 'utf-8') == None
    assert read_utf8_file('/etc/os-release') != None

# Generated at 2022-06-12 21:22:11.979724
# Unit test for function get_platform_info

# Generated at 2022-06-12 21:22:15.718965
# Unit test for function get_platform_info
def test_get_platform_info():
    info = {}
    info = get_platform_info()
    assert 'platform_dist_result' in info
    assert info['platform_dist_result'] == platform.dist()
    assert 'osrelease_content' in info


test_get_platform_info()

# Generated at 2022-06-12 21:22:17.060443
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()
    assert info['platform_dist_result']

# Generated at 2022-06-12 21:22:25.743337
# Unit test for function get_platform_info
def test_get_platform_info():
    # Test without /etc/os-release
    if os.path.isfile('/etc/os-release'):
        os.rename('/etc/os-release', '/tmp/os-release')

    result = get_platform_info()

    assert result == {'osrelease_content': None, 'platform_dist_result': []}
    os.rename('/tmp/os-release', '/etc/os-release')
    result = get_platform_info()

# Generated at 2022-06-12 21:22:34.032904
# Unit test for function get_platform_info
def test_get_platform_info():
    
    def read_utf8_file_mock(path, encoding='utf-8'):
        if not os.access(path, os.R_OK):
            return None
        with io.open(path, 'r', encoding=encoding) as fd:
            content = fd.read()

    platform.dist = dist_mock
    info = get_platform_info()
    assert info['platform_dist_result'] == ['Ubuntu', '18.04', 'bionic']
    assert info['osrelease_content'] == 'Ubuntu 18.04.3 LTS'

# Generated at 2022-06-12 21:22:36.977189
# Unit test for function get_platform_info
def test_get_platform_info():
    result = get_platform_info()
    assert result['platform_dist_result'] != []
    assert result['osrelease_content'] != []

# Generated at 2022-06-12 21:22:39.440757
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()
    assert 'platform_dist_result' in info
    assert 'osrelease_content' in info
    assert info['osrelease_content'] is not None

# Generated at 2022-06-12 21:22:44.160085
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()

    if len(info['platform_dist_result']) == 0:
        assert info['osrelease_content'] is not None, "No /etc/os-release"

    if len(info['platform_dist_result']) > 0:
        assert info['osrelease_content'] is None, "Unnecessary parsing of /etc/os-release"

# Generated at 2022-06-12 21:22:51.919953
# Unit test for function read_utf8_file
def test_read_utf8_file():
    # Test for a existing file
    my_data = read_utf8_file("./scripts/get_platform_info.py")
    assert my_data

    # Test for a non existing file
    my_data = read_utf8_file("./not_existing_file")
    assert my_data is None

# Generated at 2022-06-12 21:22:53.540569
# Unit test for function read_utf8_file
def test_read_utf8_file():
    assert isinstance(read_utf8_file('/etc/os-release'), str)

# Generated at 2022-06-12 21:22:57.293733
# Unit test for function read_utf8_file
def test_read_utf8_file():
    path = '/tmp/test'
    path_content = 'test content'
    file = open(path, 'w')
    file.write(path_content)
    file.close()
    assert read_utf8_file(path) == path_content

# Generated at 2022-06-12 21:23:03.085129
# Unit test for function get_platform_info
def test_get_platform_info():
    tmp_platform_dist = platform.dist
    platform.dist = lambda: ['hello', 'world', '1.2.3', 'n/a']

    expected = dict(platform_dist_result=['hello', 'world', '1.2.3', 'n/a'],
                    osrelease_content='')

    assert expected == get_platform_info()

    platform.dist = tmp_platform_dist



# Generated at 2022-06-12 21:23:04.902453
# Unit test for function get_platform_info
def test_get_platform_info():
    result = get_platform_info()
    assert result['platform_dist_result'] == []
    assert result['osrelease_content'] is not None

# Generated at 2022-06-12 21:23:11.289433
# Unit test for function read_utf8_file
def test_read_utf8_file():
    # make sure '/etc' is listed in os.environ['PATH']
    assert any(['/etc' in x for x in os.environ['PATH'].split(':')])
    # This file should exists in '/etc'
    assert os.path.isfile('/etc/os-release')
    # The content of '/etc/os-release' should contain 'NAME="Ubuntu"'
    assert 'NAME="Ubuntu"' in read_utf8_file('/etc/os-release')

# Generated at 2022-06-12 21:23:13.738750
# Unit test for function get_platform_info
def test_get_platform_info():
    content = get_platform_info()
    assert content is not None
    assert 'platform_dist_result' in content
    assert 'osrelease_content' in content

# Generated at 2022-06-12 21:23:16.497308
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()
    assert type(info) == dict
    for key in info:
        assert type(info[key]) != None

if __name__ == '__main__':
    test_get_platform_info()
    main()

# Generated at 2022-06-12 21:23:19.126704
# Unit test for function read_utf8_file
def test_read_utf8_file():
    assert read_utf8_file('/etc/os-release')
    assert read_utf8_file('/usr/lib/os-release')

# Generated at 2022-06-12 21:23:22.454132
# Unit test for function read_utf8_file
def test_read_utf8_file():
    path = "./test_file"
    expected_result = "test"
    file_handle = open(path, "w")
    file_handle.write("test")
    file_handle.close()
    result = read_utf8_file(path)
    assert result == expected_result
    os.remove(path)

# Generated at 2022-06-12 21:23:29.263792
# Unit test for function get_platform_info
def test_get_platform_info():
    # Test platform_dist_result
    info = get_platform_info()
    test_list = ['A', 'B', '']
    assert info['platform_dist_result'] == test_list, 'Failed to get platform_dist_result'

# Generated at 2022-06-12 21:23:31.788298
# Unit test for function get_platform_info
def test_get_platform_info():
    result = get_platform_info()

    assert 'osrelease_content' in result
    assert 'platform_dist_result' in result
    if result['platform_dist_result']:
        assert isinstance(result['platform_dist_result'], list)

# Generated at 2022-06-12 21:23:34.271878
# Unit test for function read_utf8_file
def test_read_utf8_file():
    assert read_utf8_file('/etc/os-release') is not None


# Generated at 2022-06-12 21:23:39.424875
# Unit test for function read_utf8_file
def test_read_utf8_file():
    assert read_utf8_file("/etc/hosts")
    # test non existing file
    assert not read_utf8_file("/no/such/file")
    # test file with non utf-8 chars
    assert read_utf8_file("/etc/locale.conf")


# Generated at 2022-06-12 21:23:41.960807
# Unit test for function read_utf8_file
def test_read_utf8_file():
    # Test for non-existent file and normal file
    assert (read_utf8_file("/non-existent")) == None
    assert (read_utf8_file("/etc/os-release"))

# Generated at 2022-06-12 21:23:48.647921
# Unit test for function get_platform_info
def test_get_platform_info():
    osrelease_content = read_utf8_file('/etc/os-release')
    osrelease_dict = {}
    for line in osrelease_content.splitlines():
        key, _, value = line.partition("=")
        osrelease_dict[key] = value

    info = get_platform_info()
    assert isinstance(info, dict)
    assert info['osrelease_content'] == osrelease_content
    assert info['platform_dist_result'][0] == osrelease_dict["NAME"]
    assert info['platform_dist_result'][1] == osrelease_dict["VERSION_ID"]
    assert info['platform_dist_result'][2] == ""

# Generated at 2022-06-12 21:23:51.616843
# Unit test for function read_utf8_file
def test_read_utf8_file():
    path = './.test_read_utf8_file'
    with io.open(path, 'w', encoding='utf-8') as fd:
        fd.write('test_read_utf8_file')

    content = read_utf8_file(path)

    assert (content == 'test_read_utf8_file')

# Generated at 2022-06-12 21:23:59.342254
# Unit test for function get_platform_info
def test_get_platform_info():

    # unit test for get_platform_info function
    def _get_content(filename):
        with open(filename) as file:
            return file.read()

    result = get_platform_info()
    if os.path.isfile('/etc/os-release'):
        assert result['osrelease_content'] == _get_content('/etc/os-release')
    else:
        assert result['osrelease_content'] == _get_content('/usr/lib/os-release')

# Generated at 2022-06-12 21:24:01.032243
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()
    assert info.get('osrelease_content').find('Red Hat') > -1

# Generated at 2022-06-12 21:24:05.534995
# Unit test for function get_platform_info
def test_get_platform_info():
    result = get_platform_info()

    assert 'osrelease_content' in result
    assert result['osrelease_content']

    assert 'platform_dist_result' in result
    assert len(result['platform_dist_result']) > 1
    assert result['platform_dist_result'][0] == platform.dist()[0]
    assert result['platform_dist_result'][1] == platform.dist()[1]

# Generated at 2022-06-12 21:24:21.986080
# Unit test for function read_utf8_file
def test_read_utf8_file():
    # Given an empty file in a temporary directory
    import tempfile
    dirpath = tempfile.mkdtemp()
    f = os.path.join(dirpath, 'empty')

    # When we read the file
    content = read_utf8_file(f)

    assert content == None, 'Content should be None for an empty file'

    # Given a non-empty file in a temporary directory
    f = os.path.join(dirpath, 'full')
    with open(f, 'w') as fd:
        fd.write('FOO\n')

    # When we read the file
    content = read_utf8_file(f)

    # Then the content should be correct
    assert content == 'FOO\n', 'Content should be the content of the file'

# Generated at 2022-06-12 21:24:25.087768
# Unit test for function get_platform_info
def test_get_platform_info():
    assert get_platform_info() == {
        'platform_dist_result': [],
        'osrelease_content': u''
    }

# Generated at 2022-06-12 21:24:29.065334
# Unit test for function read_utf8_file
def test_read_utf8_file():
    fd, path = tempfile.mkstemp()
    os.write(fd, b'foo')
    os.close(fd)

    assert read_utf8_file(path) == 'foo'

    os.remove(path)

# Generated at 2022-06-12 21:24:39.711433
# Unit test for function read_utf8_file
def test_read_utf8_file():
    # Create and write to a file
    sample_file_name = 'test_file'
    sample_content_utf8 = u'ÖØöø\n'
    sample_content_bytes = sample_content_utf8.encode('utf-8')

    # Create the file
    with io.open(sample_file_name, 'w', encoding='utf-8') as fd:
        fd.write(sample_content_utf8)

    # Read the file using function under test
    content = read_utf8_file(sample_file_name)

    # Clean up the file
    os.unlink(sample_file_name)

    assert content == sample_content_utf8
    assert content.encode('utf-8') == sample_content_bytes


# Generated at 2022-06-12 21:24:41.402938
# Unit test for function get_platform_info
def test_get_platform_info():
    expected = dict(platform_dist_result=[], osrelease_content=None)
    assert get_platform_info() == expected

# Generated at 2022-06-12 21:24:44.332994
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()
    assert 'platform_dist_result' in info
    assert 'osrelease_content' in info

# Generated at 2022-06-12 21:24:52.181645
# Unit test for function get_platform_info
def test_get_platform_info():
    assert '/usr/lib/os-release' in open("/proc/self/mounts").read()
    assert 'arch' in platform.platform()
    assert 'Arch' in platform.uname()[2]
    assert 'osrelease_content' in get_platform_info().keys()
    assert 'os-release' in get_platform_info()['osrelease_content']
    assert '_HasKeys' in get_platform_info().keys()



# Generated at 2022-06-12 21:24:59.910762
# Unit test for function get_platform_info
def test_get_platform_info():
    result = get_platform_info()
    assert os.path.exists('/etc/os-release'), 'This test can only be run on Debian based systems'
    assert result['platform_dist_result'][0] == 'debian'
    assert 'VERSION="9 (stretch)"' in result['osrelease_content']

    # write a fake os-release file
    with io.open('/tmp/os-release', 'w') as fd:
        fd.write(u'NAME="fake"')

    # fake out platform.dist() which will return a tuple of None
    def fake_dist():
        return None

    # Monkey patch
    platform.dist = fake_dist

    # now test that our fake os-release file works
    result = get_platform_info()