

# Generated at 2022-06-12 21:14:57.172410
# Unit test for function read_utf8_file
def test_read_utf8_file():
    # Test read a non-existed file
    assert read_utf8_file('non-existed-file') is None

# Generated at 2022-06-12 21:15:04.763240
# Unit test for function read_utf8_file
def test_read_utf8_file():
    assert read_utf8_file('tests/test.file') == 'test\n'
    assert read_utf8_file('tests/test.file', 'ascii') == 'test\n'

    with open('tests/test.file', 'wb') as fd:
        fd.write('\xe5\n'.encode('utf-8'))

    assert read_utf8_file('tests/test.file') == '\xe5\n'
    assert read_utf8_file('tests/test.file', 'ascii') == '\xe5\n'

# Generated at 2022-06-12 21:15:06.049415
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()
    assert info == {'platform_dist_result': ['', '', ''], 'osrelease_content': None}

# Generated at 2022-06-12 21:15:08.500306
# Unit test for function read_utf8_file
def test_read_utf8_file():
    assert read_utf8_file('/etc/os-release')
    assert read_utf8_file('./nonexistent') is None

# Generated at 2022-06-12 21:15:09.757346
# Unit test for function read_utf8_file
def test_read_utf8_file():
    assert read_utf8_file('/etc/os-release') is not None

# Generated at 2022-06-12 21:15:18.000887
# Unit test for function get_platform_info

# Generated at 2022-06-12 21:15:20.135722
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()

    assert info['platform_dist_result'] == []
    assert info['osrelease_content'] is not None

# Generated at 2022-06-12 21:15:22.111583
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()
    assert info['platform_dist_result'] == []
    assert 'osrelease_content' in info

# Generated at 2022-06-12 21:15:23.368967
# Unit test for function get_platform_info
def test_get_platform_info():
    assert isinstance(get_platform_info(), dict)

# Generated at 2022-06-12 21:15:31.425300
# Unit test for function get_platform_info
def test_get_platform_info():
    import platform
    import json

    # set up
    def mock_platform_dist_func(*args):
        return ['CentOS-7.4', 'Core', '7.4.1708', 'Core']

    info = get_platform_info()

    # run function
    platform.dist = mock_platform_dist_func
    info = get_platform_info()

    # assert
    assert info == {
        'osrelease_content': None,
        'platform_dist_result': ['CentOS-7.4', 'Core', '7.4.1708', 'Core']
    }

# Generated at 2022-06-12 21:15:39.372082
# Unit test for function read_utf8_file
def test_read_utf8_file():
    with io.open('tmpfile', 'w', encoding='utf-8') as fd:
        fd.write(u'\u59d3\u540d\uff1a\u5415\u4f9d\u51e4')
        fd.close()
    assert read_utf8_file('tmpfile') == u'\u59d3\u540d\uff1a\u5415\u4f9d\u51e4'
    assert read_utf8_file('tmpfile', 'gbk') == '姓名：吕以谦'
    os.remove('tmpfile')

# Generated at 2022-06-12 21:15:41.248653
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()

    assert info['platform_dist_result']
    assert info['osrelease_content']

# Generated at 2022-06-12 21:15:46.572505
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()
    info_keys = ['platform_dist_result', 'osrelease_content']

    assert len(info.keys()) == len(info_keys)
    assert info['platform_dist_result'] == platform.dist()
    assert info['osrelease_content'] == read_utf8_file('/etc/os-release')

# Generated at 2022-06-12 21:15:57.271622
# Unit test for function read_utf8_file

# Generated at 2022-06-12 21:15:59.843204
# Unit test for function get_platform_info
def test_get_platform_info():
    """
    Unit test for function get_platform_info
    """
    assert get_platform_info() == dict(platform_dist_result=[], osrelease_content="")

# Generated at 2022-06-12 21:16:01.995524
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()
    assert 'platform_dist_result' in info
    assert type(info['platform_dist_result']) is list
    assert 'osrelease_content' in info

# Generated at 2022-06-12 21:16:14.104030
# Unit test for function read_utf8_file
def test_read_utf8_file():
    # Test reading a file that exists
    existing_file_path = 'tests/module_utils/platform.py'
    file_contents = read_utf8_file(existing_file_path)
    assert file_contents
    assert file_contents.startswith('# Unit test for function read_utf8_file')
    assert '\n' in file_contents

    # Test reading a file that does not exist
    non_existing_file_path = 'non_existing_file_path.py'
    file_contents = read_utf8_file(non_existing_file_path)
    assert file_contents is None

    # Test reading a non readable file
    non_readable_file_path = 'ansible/module_utils/distro.py'

# Generated at 2022-06-12 21:16:24.124666
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()
    assert info['osrelease_content'] == 'NAME="Ubuntu"\nVERSION="18.04.1 LTS (Bionic Beaver)"\nID=ubuntu\nID_LIKE=debian\nPRETTY_NAME="Ubuntu 18.04.1 LTS"\nVERSION_ID="18.04"\nHOME_URL="https://www.ubuntu.com/"\nSUPPORT_URL="https://help.ubuntu.com/"\nBUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"\nPRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"\nVERSION_CODENAME=bionic\nUBUNTU_CODENAME=bionic\n'
    assert info

# Generated at 2022-06-12 21:16:31.096015
# Unit test for function read_utf8_file
def test_read_utf8_file():
    # create temp file
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(u"This is to test read utf8 file function\n")
    temp_file.close()
    # open file and compare
    with open(temp_file.name, "r") as f:
        result = f.read()
        assert result == read_utf8_file(temp_file.name)
    # unlink temp file
    os.unlink(temp_file.name)


# Generated at 2022-06-12 21:16:33.577241
# Unit test for function get_platform_info
def test_get_platform_info():
    result = get_platform_info()

    assert isinstance(result, dict)
    assert result['osrelease_content']
    assert isinstance(result['platform_dist_result'], list)

# Generated at 2022-06-12 21:16:36.933141
# Unit test for function get_platform_info
def test_get_platform_info():
    assert len(get_platform_info()) == 2

# Generated at 2022-06-12 21:16:42.503609
# Unit test for function read_utf8_file
def test_read_utf8_file():
    # Make sure that when we pass an invalid path, it returns None
    assert read_utf8_file('/usr/lib/os-release.bad') is None
    # Make sure that we correctly read a file without a BOM
    assert read_utf8_file('./test_read_utf8_file.txt') == 'This file contains no BOM.\n'


# Generated at 2022-06-12 21:16:46.848571
# Unit test for function read_utf8_file
def test_read_utf8_file():
    with open('/tmp/test_utf8_file', 'w') as f:
        f.write('the quick brown fox jumps over the lazy dog')
    assert read_utf8_file('/tmp/test_utf8_file') == 'the quick brown fox jumps over the lazy dog'

# Generated at 2022-06-12 21:16:53.776796
# Unit test for function read_utf8_file
def test_read_utf8_file():
    # Test for file not present
    assert read_utf8_file('/nofile') is None

    # Test for a file existing but not readable
    # This simulates a protected file not readable by ansible
    with open('/tmp/test_file', 'w') as fp:
        fp.write('test file')
    os.chmod('/tmp/test_file', 0o000)
    assert read_utf8_file('/tmp/test_file') is None
    os.unlink('/tmp/test_file')

# Generated at 2022-06-12 21:16:54.696535
# Unit test for function get_platform_info
def test_get_platform_info():

    assert get_platform_info() is not None

# Generated at 2022-06-12 21:17:06.245080
# Unit test for function read_utf8_file
def test_read_utf8_file():
    import tempfile
    import os

    tmpdir = tempfile.mkdtemp()
    filepath = os.path.join(tmpdir, 'test-platform-info.txt')
    expected_content = 'test'
    # test that non-existing files return empty string
    assert read_utf8_file('/tmp/non-existing') == None
    # create a test file
    with io.open(filepath, 'w', encoding='utf-8') as fd:
        fd.write(expected_content)
    # test reading a file with utf-8 encoding
    assert read_utf8_file(filepath) == expected_content
    # test reading a file with latin-1 encoding
    assert read_utf8_file(filepath, encoding='latin-1') == expected_content
    import shutil
    shut

# Generated at 2022-06-12 21:17:10.347686
# Unit test for function read_utf8_file
def test_read_utf8_file():
    # Test file exists
    # Test file read successfully
    path = './get_platform_info.py'
    assert read_utf8_file(path)
    # Test file read failed
    path = 'foo.bar'
    assert not read_utf8_file(path)

# Generated at 2022-06-12 21:17:12.481311
# Unit test for function get_platform_info
def test_get_platform_info():
    platform_info = get_platform_info()
    assert isinstance(platform_info, dict)

# Generated at 2022-06-12 21:17:13.801439
# Unit test for function get_platform_info
def test_get_platform_info():
    assert isinstance(get_platform_info(), dict)


# Generated at 2022-06-12 21:17:17.914684
# Unit test for function read_utf8_file
def test_read_utf8_file():
    test_str = '!#/usr/bin/env python\n# -*- coding: utf-8 -*-'
    with open('/tmp/test_file', 'wb') as fd:
        fd.write(test_str)
    assert read_utf8_file('/tmp/test_file') == test_str



# Generated at 2022-06-12 21:17:30.867110
# Unit test for function get_platform_info
def test_get_platform_info():

    m_open = mock_open()
    m_open.return_value = 'debian'
    with patch('platform_utils.open', m_open, create=True):
        with patch('platform.dist', return_value=('debian','','','')):
            info = get_platform_info()
            assert len(info['platform_dist_result']) == 4
            assert len(info['osrelease_content']) == 7


    m_open = mock_open()
    m_open.return_value = 'debian'
    with patch('platform_utils.open', m_open, create=True):
        with patch('platform.dist', side_effect=Exception()):
            info = get_platform_info()
            assert len(info['platform_dist_result']) == 0

# Generated at 2022-06-12 21:17:33.443184
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()
    assert info['platform_dist_result'] != []
    assert info['osrelease_content'] != None

# Generated at 2022-06-12 21:17:39.200606
# Unit test for function get_platform_info
def test_get_platform_info():
    try:
        from __main__ import get_platform_info
    except:
        from platform_info import get_platform_info
    assert isinstance(get_platform_info(), dict)
    # we do not assert the specific content of the returned object as this may change with the
    # distribution and version of the platform we are running on.

# Generated at 2022-06-12 21:17:44.159455
# Unit test for function read_utf8_file
def test_read_utf8_file():
    test_file = 'test.txt'

    with io.open(test_file, 'w+', encoding='utf-8') as fd:
        fd.write('test123')

    assert read_utf8_file(test_file) == 'test123'

    with io.open(test_file, 'w+', encoding='utf-8') as fd:
        fd.write('test123é')

    assert read_utf8_file(test_file) == 'test123é'

    os.remove(test_file)

# Generated at 2022-06-12 21:17:53.053384
# Unit test for function get_platform_info
def test_get_platform_info():
    info = {'osrelease_content': 'NAME="Ubuntu"\nVERSION="14.04.5 LTS, Trusty Tahr"\nID=ubuntu\nID_LIKE=debian\nPRETTY_NAME="Ubuntu 14.04.5 LTS"\nVERSION_ID="14.04"\nHOME_URL="http://www.ubuntu.com/"\nSUPPORT_URL="http://help.ubuntu.com/"\nBUG_REPORT_URL="http://bugs.launchpad.net/ubuntu/"',
            'platform_dist_result': ['Ubuntu', '14.04', 'trusty']}

    result = get_platform_info()

    assert result == info

# Generated at 2022-06-12 21:17:58.213497
# Unit test for function read_utf8_file
def test_read_utf8_file():
    f = open('test.txt', 'w')
    f.write(u'Hello World !')
    f.close()
    assert read_utf8_file('test.txt') == u'Hello World !'
    # Remove test file
    os.remove('test.txt')
    assert read_utf8_file('test.txt') == None



# Generated at 2022-06-12 21:18:00.002656
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()
    assert info['platform_dist_result'] != ''
    assert info['osrelease_content'] != ''

# Generated at 2022-06-12 21:18:03.068507
# Unit test for function get_platform_info
def test_get_platform_info():
    result = get_platform_info()
    assert(result['platform_dist_result'] == platform.dist())
    assert(result['osrelease_content'] == read_utf8_file('/etc/os-release'))

# Generated at 2022-06-12 21:18:05.259810
# Unit test for function get_platform_info
def test_get_platform_info():
    result = get_platform_info()
    assert result['platform_dist_result'] == ('', '', '')
    assert result['osrelease_content'].startswith('NAME=')

# Generated at 2022-06-12 21:18:17.165572
# Unit test for function get_platform_info
def test_get_platform_info():

    platform_dist_result = [u'Ubuntu', u'16.04', u'xenial']
    osrelease_content = (u'NAME="Ubuntu"\n'
                         u'VERSION="16.04.6 LTS (Xenial Xerus)"\n'
                         u'ID=ubuntu\n'
                         u'ID_LIKE=debian\n'
                         u'PRETTY_NAME="Ubuntu 16.04.6 LTS"\n'
                         u'VERSION_ID="16.04"\n'
                         u'HOME_URL="http://www.ubuntu.com/"\n'
                         u'SUPPORT_URL="http://help.ubuntu.com/"\n'
                         u'BUG_REPORT_URL="http://bugs.launchpad.net/ubuntu/"\n')

    assert get_platform_info

# Generated at 2022-06-12 21:18:27.530127
# Unit test for function read_utf8_file

# Generated at 2022-06-12 21:18:29.620521
# Unit test for function get_platform_info
def test_get_platform_info():

    # Return value of function get_platform_info
    assert get_platform_info() != dict()

# Generated at 2022-06-12 21:18:32.827296
# Unit test for function read_utf8_file
def test_read_utf8_file():
    test_content1 = read_utf8_file('testdata', 'utf-8')
    assert(test_content1)
    assert(test_content1 == os.linesep)

# Generated at 2022-06-12 21:18:35.475189
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()
    assert info['platform_dist_result'] == platform.dist()
    assert info['osrelease_content'] is not None


# Generated at 2022-06-12 21:18:39.736588
# Unit test for function get_platform_info
def test_get_platform_info():
    os_release_content = """
NAME="CentOS Linux"
VERSION="7 (Core)"
ID="centos"
ID_LIKE="rhel fedora"
VERSION_ID="7"
PRETTY_NAME="CentOS Linux 7 (Core)"
ANSI_COLOR="0;31"
CPE_NAME="cpe:/o:centos:centos:7"
HOME_URL="https://www.centos.org/"
BUG_REPORT_URL="https://bugs.centos.org/"

CENTOS_MANTISBT_PROJECT="CentOS-7"
CENTOS_MANTISBT_PROJECT_VERSION="7"
REDHAT_SUPPORT_PRODUCT="centos"
REDHAT_SUPPORT_PRODUCT_VERSION="7"
"""

# Generated at 2022-06-12 21:18:41.073159
# Unit test for function get_platform_info
def test_get_platform_info():
    assert 3 == len(get_platform_info()['platform_dist_result'])

# Generated at 2022-06-12 21:18:48.638177
# Unit test for function read_utf8_file
def test_read_utf8_file():
    import tempfile
    import os

    assert read_utf8_file(os.path.join(os.sep, 'does', 'not', 'exist')) is None

    fd, tmp_file = tempfile.mkstemp()
    with io.open(tmp_file, 'w', encoding='utf-8', newline='\n') as f:
        f.write(u'This is a test\n')
    test_content = read_utf8_file(tmp_file)
    assert test_content == "This is a test\n"

    os.close(fd)
    os.unlink(tmp_file)



# Generated at 2022-06-12 21:18:49.855007
# Unit test for function read_utf8_file
def test_read_utf8_file():
    assert read_utf8_file('/tmp/fileme') == None

# Generated at 2022-06-12 21:18:55.842462
# Unit test for function get_platform_info
def test_get_platform_info():
    assert get_platform_info() == '{"osrelease_content": null, "platform_dist_result": []}'
    assert get_platform_info() == '{"osrelease_content": "", "platform_dist_result": []}'
    assert get_platform_info() == '{"osrelease_content": "test", "platform_dist_result": []}'

# Generated at 2022-06-12 21:19:00.342369
# Unit test for function read_utf8_file
def test_read_utf8_file():
    file_name = 'test_reading.txt'
    with open(file_name, 'w') as fd:
        fd.write('Test reading')

    content = read_utf8_file(file_name)
    os.remove(file_name)
    if content == 'Test reading':
        assert True
    else:
        assert False

# Generated at 2022-06-12 21:19:04.794383
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()
    assert len(info['platform_dist_result']) > 0
    assert len(info['osrelease_content']) > 0

# Generated at 2022-06-12 21:19:06.527812
# Unit test for function read_utf8_file
def test_read_utf8_file():
    result = read_utf8_file("test.txt")
    assert result != None


# Generated at 2022-06-12 21:19:12.249273
# Unit test for function read_utf8_file
def test_read_utf8_file():
    test_string = "this is a test"
    file_path = "test_file"
    with open(file_path, "w") as f:
        f.write(test_string)
    assert read_utf8_file(file_path) == test_string
    os.remove(file_path)



# Generated at 2022-06-12 21:19:24.231107
# Unit test for function get_platform_info
def test_get_platform_info():

    from ansible.module_utils import basic

    m = basic.AnsibleModule({})
    info = get_platform_info()

    if os.path.isfile('/etc/os-release'):
        with open('/etc/os-release', 'r') as file:
            os_rel = file.read()
    else:
        os_rel = None


# Generated at 2022-06-12 21:19:25.667373
# Unit test for function get_platform_info
def test_get_platform_info():
    assert get_platform_info() == {'platform_dist_result': [], 'osrelease_content': None}

# Generated at 2022-06-12 21:19:27.337994
# Unit test for function read_utf8_file
def test_read_utf8_file():
    path = 'fixtures/os-release'
    content = read_utf8_file(path)
    assert content == 'NAME="Atlantis"\n'

# Generated at 2022-06-12 21:19:34.378598
# Unit test for function read_utf8_file
def test_read_utf8_file():
    # test with proper context
    with open('/etc/os-release', 'w') as fd:
        fd.write('test content')

    test_result = read_utf8_file('/etc/os-release')
    assert test_result == 'test content'

    # test with improper context
    test_result = read_utf8_file('/etc/os-release')
    assert test_result is None

# Generated at 2022-06-12 21:19:36.746904
# Unit test for function read_utf8_file
def test_read_utf8_file():
    # test for file not found
    assert(read_utf8_file('missing_file.txt') is None)

    text = 'Γεια σου Κόσμε\n'
    with open('./test_file.txt', 'w') as f:
        f.write(text)
    assert(read_utf8_file('./test_file.txt') == text)

# Generated at 2022-06-12 21:19:44.574007
# Unit test for function get_platform_info
def test_get_platform_info():
    assert get_platform_info() == {'osrelease_content': 'NAME="Ubuntu"\nVERSION="16.04.4 LTS (Xenial Xerus)"\nID=ubuntu\nID_LIKE=debian\nPRETTY_NAME="Ubuntu 16.04.4 LTS"\nVERSION_ID="16.04"\nHOME_URL="http://www.ubuntu.com/"\nSUPPORT_URL="http://help.ubuntu.com/"\nBUG_REPORT_URL="http://bugs.launchpad.net/ubuntu/"\nVERSION_CODENAME=xenial\nUBUNTU_CODENAME=xenial\n', 'platform_dist_result': [u'Ubuntu', u'16.04', u'xenial']}

# Generated at 2022-06-12 21:19:47.476074
# Unit test for function get_platform_info
def test_get_platform_info():
    with open('tests/test_system/test_platform_info.json') as json_file:
        test_data = json.load(json_file)
        assert test_data == get_platform_info()

# Generated at 2022-06-12 21:19:57.185141
# Unit test for function get_platform_info
def test_get_platform_info():

    # Expect only the platform_dist_result to be set
    expected_result = dict(platform_dist_result=platform.dist(),
                osrelease_content=None)
    result = get_platform_info()
    assert result == expected_result

    # Override the os-release file being read by the get_platform_info function
    def os_release_decorator(path):
        if path == '/etc/os-release' or path == '/usr/lib/os-release':
            return 'NAME="OS Release"'
        else:
            return None

    with os.scandir.patch('open', os_release_decorator):
        expected_result = dict(platform_dist_result=platform.dist(),
                    osrelease_content='NAME="OS Release"')
        result = get_platform_info()

# Generated at 2022-06-12 21:19:58.823270
# Unit test for function get_platform_info
def test_get_platform_info():
    assert ('redhat-7.4' ==
           get_platform_info()['osrelease_content'].splitlines()[0])

# Generated at 2022-06-12 21:20:05.606140
# Unit test for function read_utf8_file
def test_read_utf8_file():
    assert read_utf8_file('/tmp/test_utf8_file') == None
    file('/tmp/test_utf8_file', 'w').write('test_utf8_file')
    assert read_utf8_file('/tmp/test_utf8_file') == 'test_utf8_file'
    os.remove('/tmp/test_utf8_file')

# Generated at 2022-06-12 21:20:08.902206
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()

    assert info['platform_dist_result'] == platform.dist()
    assert info['osrelease_content'] != None

# Generated at 2022-06-12 21:20:14.880578
# Unit test for function read_utf8_file
def test_read_utf8_file():
    (fd, path) = tempfile.mkstemp(text=True)
    original = u'Iñtërnâtiônàlizætiøn'
    try:
        os.write(fd, original.encode('utf-8'))
        os.close(fd)
        assert read_utf8_file(path) == original
    finally:
        os.remove(path)


# Generated at 2022-06-12 21:20:18.889565
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()

    # If it's not a dictionnary, we have an error
    assert type(info) is dict

    # Check if we have a list of platform_dist
    assert type(info['platform_dist_result']) is list

    # Check if we have osrelease content
    assert type(info['osrelease_content']) is str

# Generated at 2022-06-12 21:20:22.026121
# Unit test for function read_utf8_file
def test_read_utf8_file():
    with open('/tmp/test_read_utf8_file', 'w') as f:
        f.write('test_read_utf8_file_content')

    # Test with non-existing file
    assert read_utf8_file('/tmp/non_existing') is None

    # Test with existing file
    assert read_utf8_file('/tmp/test_read_utf8_file') == 'test_read_utf8_file_content'

# Generated at 2022-06-12 21:20:27.217307
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()
    assert type(info) == dict
    # Test for Debian
    info = get_platform_info()
    assert info['platform_dist_result'][0] == 'debian'
    assert info['platform_dist_result'][1] == '9'
    assert info['platform_dist_result'][2] == '9'

# Generated at 2022-06-12 21:20:37.910156
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()
    assert info['osrelease_content'] == 'NAME="Ubuntu"\nVERSION="16.04.3 LTS (Xenial Xerus)"\nID=ubuntu\nID_LIKE=debian\nPRETTY_NAME="Ubuntu 16.04.3 LTS"\nVERSION_ID="16.04"\nHOME_URL="http://www.ubuntu.com/"\nSUPPORT_URL="http://help.ubuntu.com/"\nBUG_REPORT_URL="http://bugs.launchpad.net/ubuntu/"\nVERSION_CODENAME=xenial\nUBUNTU_CODENAME=xenial\n'
    assert info['platform_dist_result'] == ('Ubuntu', '16.04', 'xenial')

# Generated at 2022-06-12 21:20:38.745752
# Unit test for function get_platform_info
def test_get_platform_info():
    result = get_platform_info()
    assert result is not None

# Generated at 2022-06-12 21:20:41.635955
# Unit test for function get_platform_info
def test_get_platform_info():
    assert get_platform_info() == dict(platform_dist_result=['', '', ''], osrelease_content=None)

# Generated at 2022-06-12 21:20:53.219530
# Unit test for function get_platform_info

# Generated at 2022-06-12 21:20:56.665853
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()

    assert info['platform_dist_result'] == []

    assert info['osrelease_content'] is not None
    assert info['osrelease_content'] == read_utf8_file('/etc/os-release')

# Generated at 2022-06-12 21:20:57.570729
# Unit test for function get_platform_info
def test_get_platform_info():
    assert isinstance(get_platform_info(), dict)

# Generated at 2022-06-12 21:21:09.198450
# Unit test for function read_utf8_file
def test_read_utf8_file():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils.common.distro import get_platform_info
    from ansible.module_utils.common.distro import read_utf8_file

    # test with non existent file
    res = read_utf8_file('/some/non/existent/file')
    assert res is None

    # test with encoding other than utf-8
    fd = open('/etc/os-release', 'rb')
    data = fd.read()
    fd.close()
    tmpfile_path = '/tmp/non-utf8-file'
    fd = open(tmpfile_path, 'wb')
    fd.write(data)
    fd.close

# Generated at 2022-06-12 21:21:13.877093
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()
    assert isinstance(info, dict)
    assert isinstance(info['platform_dist_result'], list)
    assert isinstance(info['osrelease_content'], str)

# Generated at 2022-06-12 21:21:19.214733
# Unit test for function read_utf8_file
def test_read_utf8_file():
    file_name = 'test.txt'
    content = 'test\n'
    try:
        # Create a new file if it doesn't exist
        with open(file_name, 'w') as fd:
            fd.write(content)

        assert(read_utf8_file(file_name) == content)
    finally:
        # Remove the file
        os.remove(file_name)

# Generated at 2022-06-12 21:21:21.280025
# Unit test for function read_utf8_file
def test_read_utf8_file():
    content = read_utf8_file('/etc/os-release')
    assert isinstance(content, str)

# Generated at 2022-06-12 21:21:30.868717
# Unit test for function read_utf8_file
def test_read_utf8_file():
    file_content = u'dummy_file_content'
    dummy_file = '/tmp/test_read_utf8_file'
    assert not os.access(dummy_file, os.R_OK)

    with io.open(dummy_file, 'w', encoding='utf-8') as f:
        f.write(file_content)
    assert os.access(dummy_file, os.R_OK)

    read_file_content = read_utf8_file(dummy_file)
    assert file_content == read_file_content

    os.remove(dummy_file)
    assert not os.access(dummy_file, os.R_OK)

# Generated at 2022-06-12 21:21:32.234350
# Unit test for function get_platform_info
def test_get_platform_info():
    result = get_platform_info()
    assert result['osrelease_content']

# Generated at 2022-06-12 21:21:38.377129
# Unit test for function read_utf8_file
def test_read_utf8_file():
    assert read_utf8_file("/usr/bin/python") is not None
    assert read_utf8_file("/usr/no_python") is None
    assert read_utf8_file("/usr/bin/python", encoding="latin-1") is not None

# Generated at 2022-06-12 21:21:46.035715
# Unit test for function get_platform_info
def test_get_platform_info():
    expected_osrelease_content = '''NAME="Amazon Linux AMI"
VERSION="2018.03"
ID="amzn"
ID_LIKE="rhel fedora"
VERSION_ID="2018.03"
PRETTY_NAME="Amazon Linux AMI 2018.03"
ANSI_COLOR="0;33"
CPE_NAME="cpe:/o:amazon:linux:2018.03:ga"
HOME_URL="http://aws.amazon.com/amazon-linux-ami/"
'''
    expected_platform_dist_result = ('', '', '')

    actual_info = get_platform_info()
    assert(actual_info['osrelease_content'] == expected_osrelease_content)
    assert(actual_info['platform_dist_result'] == expected_platform_dist_result)

# Generated at 2022-06-12 21:21:48.837360
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()
    assert isinstance(info, dict)
    assert isinstance(info['platform_dist_result'], list)
    assert isinstance(info['osrelease_content'], type(None))

# Generated at 2022-06-12 21:21:51.515265
# Unit test for function read_utf8_file
def test_read_utf8_file():
    file_path = '/etc/os-release'
    assert read_utf8_file(file_path)



# Generated at 2022-06-12 21:21:56.659459
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()
    assert type(info) == dict
    assert 'platform_dist_result' in info
    assert 'osrelease_content' in info
    assert type(info['platform_dist_result']) == list
    assert type(info['osrelease_content']) == str

# Generated at 2022-06-12 21:22:01.214214
# Unit test for function read_utf8_file
def test_read_utf8_file():
    test_file = "platform_test_file.txt"
    test_content = "test content"
    with io.open(test_file, 'w', encoding='utf-8') as fd:
        fd.write(u"%s" % test_content)
    assert read_utf8_file(test_file) == test_content
    os.remove(test_file)

# Generated at 2022-06-12 21:22:06.174823
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()

    assert 'platform_dist_result' in info
    assert 'osrelease_content' in info
    assert info['osrelease_content'] != ''
    assert type(info['platform_dist_result']) is tuple
    assert len(info['platform_dist_result']) == 5

# Generated at 2022-06-12 21:22:08.492613
# Unit test for function get_platform_info
def test_get_platform_info():
    res = {'platform_dist_result': [], 'osrelease_content': ''}
    assert get_platform_info() == res

# Generated at 2022-06-12 21:22:18.853701
# Unit test for function read_utf8_file
def test_read_utf8_file():
    from tempfile import mkstemp
    from os import write, close, environ
    from shutil import rmtree

    # If a temp directory is already defined, preserve it for the test function
    # and reset it at the end of the test.
    env_save = None
    if 'TMPDIR' in environ:
        env_save = environ['TMPDIR']


# Generated at 2022-06-12 21:22:21.009126
# Unit test for function read_utf8_file
def test_read_utf8_file():
    result = read_utf8_file('/etc/os-release')

    assert open('/etc/os-release', 'r').read() == result

# Generated at 2022-06-12 21:22:36.341172
# Unit test for function get_platform_info
def test_get_platform_info():
    import sys
    import tempfile
    from ansible_collections.testns.testcoll.tests.unit.compat.mock import Mock, patch

    tmp = tempfile.TemporaryDirectory()

    def cleanup():
        tmp.cleanup()

    request = Mock()
    request.configure_mock(**{'addfinalizer.side_effect': cleanup})

    with patch('os.access', Mock(return_value=True)):
        with patch('os.path.exists', Mock(return_value=True)):
            with patch('io.open', Mock(return_value=True)):
                with patch.object(sys.modules['__main__'], 'read_utf8_file', Mock(return_value=True)):
                    result = get_platform_info()
                    assert result['platform_dist_result']

# Generated at 2022-06-12 21:22:38.815919
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()
    assert len(info['platform_dist_result']) > 0
    assert len(info['osrelease_content']) > 0

# Generated at 2022-06-12 21:22:47.204035
# Unit test for function get_platform_info
def test_get_platform_info():
    import mock
    import imp
    import sys

    if sys.version_info < (2, 7):
        import unittest2 as unittest
    else:
        import unittest

    m_module = imp.new_module('platform')
    m_module.dist = lambda: ('ansible_distro', 'ansible_version', 'ansible_id')
    platform = mock.MagicMock()
    platform.dist = m_module.dist
    sys.modules['platform'] = platform

    class TestPlatformTestCase(unittest.TestCase):

        def setUp(self):
            pass

        def tearDown(self):
            pass


# Generated at 2022-06-12 21:22:48.479801
# Unit test for function read_utf8_file
def test_read_utf8_file():
    assert(read_utf8_file('/etc/os-release'))

# Generated at 2022-06-12 21:22:54.221408
# Unit test for function read_utf8_file
def test_read_utf8_file():
    assert read_utf8_file('/etc/environment') is not None
    assert read_utf8_file('/etc/example_test_file') is None
    assert read_utf8_file('/etc/os-release') is not None
    assert read_utf8_file('/usr/lib/os-release') is not None


# Generated at 2022-06-12 21:22:56.762587
# Unit test for function get_platform_info
def test_get_platform_info():

    info = get_platform_info()
    assert 'platform_dist_result' in info
    assert 'osrelease_content' in info

# Generated at 2022-06-12 21:23:06.124454
# Unit test for function read_utf8_file
def test_read_utf8_file():
    assert read_utf8_file('/etc/redhat-release') == "Red Hat Enterprise Linux Server release 6.10 (Santiago)\n"

# Generated at 2022-06-12 21:23:14.950089
# Unit test for function get_platform_info
def test_get_platform_info():
    expected_result = {'platform_dist_result': [], 'osrelease_content': 'NAME="Ubuntu"\nVERSION="16.04.6 LTS (Xenial Xerus)"\nID=ubuntu\nID_LIKE=debian\nPRETTY_NAME="Ubuntu 16.04.6 LTS"\nVERSION_ID="16.04"\nHOME_URL="http://www.ubuntu.com/"\nSUPPORT_URL="http://help.ubuntu.com/"\nBUG_REPORT_URL="http://bugs.launchpad.net/ubuntu/"\nVERSION_CODENAME=xenial\nUBUNTU_CODENAME=xenial\n\n'}
    assert get_platform_info() == expected_result

# Generated at 2022-06-12 21:23:16.381748
# Unit test for function get_platform_info
def test_get_platform_info():
    # This test requires an existing file
    assert os.path.isfile('/etc/os-release')

# Generated at 2022-06-12 21:23:25.879314
# Unit test for function get_platform_info
def test_get_platform_info():
    from ansible.module_utils.facts.system.distribution import get_platform_info
    from ansible.module_utils.facts.system.distribution import read_utf8_file

    # Test entry point for main program
    # Test get_platform_info return value for Ubuntu 16.04.4

# Generated at 2022-06-12 21:23:32.837847
# Unit test for function read_utf8_file
def test_read_utf8_file():
    # Call function read_utf8_file with a non-exist path.
    content = read_utf8_file('/nonexist/path')
    assert content == None
    # Call function read_utf8_file with /etc/os-release "os-release"
    content = read_utf8_file('/etc/os-release')
    assert content



# Generated at 2022-06-12 21:23:35.166057
# Unit test for function read_utf8_file
def test_read_utf8_file():
    result = read_utf8_file('non-existent-file.txt')
    assert result is None



# Generated at 2022-06-12 21:23:40.321353
# Unit test for function get_platform_info
def test_get_platform_info():

    info = get_platform_info()

    assert len(info) == 2
    assert info['osrelease_content']
    if not info['osrelease_content']:
        assert len(info['platform_dist_result']) == 0
    else:
        assert len(info['platform_dist_result']) == 3

# Generated at 2022-06-12 21:23:46.006322
# Unit test for function read_utf8_file
def test_read_utf8_file():
  assert read_utf8_file('./osrelease_content.sample') == 'NAME="Kali GNU/Linux"\nVERSION="2017.1"\nID=kali\nID_LIKE=debian\nPRETTY_NAME="Kali GNU/Linux Rolling"\nVERSION_ID="2017.1"\nHOME_URL="http://www.kali.org/"\nSUPPORT_URL="http://forums.kali.org/"\nBUG_REPORT_URL="http://bugs.kali.org/"\n'

# Generated at 2022-06-12 21:23:48.365605
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()
    assert info['platform_dist_result'] != []
    assert info['osrelease_content'] != None

# Generated at 2022-06-12 21:23:51.243469
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()
    assert info.get('platform_dist_result') == ['']*5
    assert info.get('osrelease_content') == None

# Generated at 2022-06-12 21:23:52.913508
# Unit test for function get_platform_info
def test_get_platform_info():
    assert get_platform_info()['osrelease_content']

# Generated at 2022-06-12 21:23:55.408592
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()
    assert isinstance(info['platform_dist_result'], list)
    assert isinstance(info['osrelease_content'], str)

# Generated at 2022-06-12 21:23:58.424678
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()
    # os-release is in /etc/
    osrelease_content = read_utf8_file('/etc/os-release')
    # try to fall back to /usr/lib/os-release
    if not osrelease_content:
        osrelease_content = read_utf8_file('/usr/lib/os-release')
    assert osrelease_content == info['osrelease_content']

# Generated at 2022-06-12 21:24:02.688237
# Unit test for function read_utf8_file
def test_read_utf8_file():
    test_string = "Test string\n"
    filename = 'test_file'
    with open(filename, 'w') as f:
        f.write(test_string)
    open_file_str = read_utf8_file(filename)
    assert test_string == open_file_str
    os.remove(filename)

# Generated at 2022-06-12 21:24:07.865445
# Unit test for function get_platform_info
def test_get_platform_info():
    assert isinstance(get_platform_info(), dict)

# Generated at 2022-06-12 21:24:12.529799
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()

    info_keys = ['platform_dist_result', 'osrelease_content']

    # Check if the info has all the keys present
    for k in info_keys:
        assert k in info, "Key %s not present in get_platform_info output" % k

# Generated at 2022-06-12 21:24:13.925542
# Unit test for function get_platform_info
def test_get_platform_info():
    actual_platform_info = get_platform_info()
    assert actual_platform_info

# Generated at 2022-06-12 21:24:19.036205
# Unit test for function read_utf8_file
def test_read_utf8_file():

    assert None == read_utf8_file('/nofile')
    assert 'foobar' == read_utf8_file('tests/files/foobar')
    assert '\n' == read_utf8_file('tests/files/newline')
    assert 'foobar\n' == read_utf8_file('tests/files/line')

# Generated at 2022-06-12 21:24:30.770293
# Unit test for function get_platform_info
def test_get_platform_info():

    # This is for CentOS7
    info_centos7 = get_platform_info()
    assert len(info_centos7) == 2
    assert info_centos7['platform_dist_result'] == ('centos', '7.2.1511', 'Core')
    assert 'LANG=en_US.UTF-8' in info_centos7['osrelease_content']

    # This is for Ubuntu 16.04
    info_ubuntu = get_platform_info()
    assert len(info_ubuntu) == 2
    assert info_ubuntu['platform_dist_result'] == ('Ubuntu', '16.04', 'xenial')
    assert 'NAME="Ubuntu"' in info_ubuntu['osrelease_content']

    # This is for Darwin
    info_darwin = get_platform_info()

# Generated at 2022-06-12 21:24:32.381400
# Unit test for function get_platform_info
def test_get_platform_info():
    result = get_platform_info()
    assert result.get('osrelease_content', None) is not None

# Generated at 2022-06-12 21:24:44.247002
# Unit test for function get_platform_info
def test_get_platform_info():
    # Need to create file for testing
    file_name = './os-release'
    with open(file_name, 'w') as outfile:
        outfile.write("ID=centos\n")
        outfile.write("VERSION_ID=7.5.1804\n")
        outfile.write("VERSION=\"7 (Core)\"\n")
        outfile.write("PRETTY_NAME=\"CentOS Linux 7 (Core)\"\n")
        outfile.write("ANSI_COLOR=\"0;31\"\n")
        outfile.write("CPE_NAME=\"cpe:/o:centos:centos:7\"\n")
        outfile.write("HOME_URL=\"https://www.centos.org/\"\n")

# Generated at 2022-06-12 21:24:50.495995
# Unit test for function get_platform_info
def test_get_platform_info():
    info = get_platform_info()

    assert 'osrelease_content' in info
    assert 'platform_dist_result' in info

    # The os release content should be a utf-8 encoded str
    assert isinstance(info['osrelease_content'], str)
    # The platform dist result should be a list
    assert isinstance(info['platform_dist_result'], list)

# Generated at 2022-06-12 21:24:54.402187
# Unit test for function get_platform_info
def test_get_platform_info():
    # This test relies on platform.dist returning None (ie, on Windows)
    result = get_platform_info()

    assert len(result['platform_dist_result']) == 0
    assert len(result['osrelease_content']) == 0