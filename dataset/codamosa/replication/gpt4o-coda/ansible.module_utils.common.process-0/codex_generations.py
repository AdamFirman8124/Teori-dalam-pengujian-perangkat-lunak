

# Generated at 2024-05-31 00:41:34.159671
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in opt_dirs
    opt_dirs = ['/usr/local/bin']
    assert get_bin_path('custom_executable', opt_dirs=opt_dirs) == '/usr/local/bin/custom_executable'

    # Test when the executable is not found
    try:
        get_bin_path('non_existent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "non_existent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('sbin_executable', opt_dirs=['/sbin']) == '/sbin/sbin_executable'


# Generated at 2024-05-31 00:41:37.626731
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls' or get_bin_path('ls') == '/usr/bin/ls'

    # Test when the executable is found in the optional directories
    opt_dirs = ['/usr/local/bin']
    assert get_bin_path('custom_executable', opt_dirs=opt_dirs) == '/usr/local/bin/custom_executable'

    # Test when the executable is not found and should raise ValueError
    try:
        get_bin_path('non_existent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "non_existent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'
    assert get_bin_path

# Generated at 2024-05-31 00:41:41.181979
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in the optional directories
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/local/bin'
    assert get_bin_path('ifconfig', opt_dirs=['/sbin']) == '/sbin/ifconfig'


# Generated at 2024-05-31 00:41:44.791027
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls' or get_bin_path('ls') == '/usr/bin/ls'

    # Test when the executable is found in the optional directories
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/local/bin'
    assert get_bin_path('ifconfig', opt_dirs=['/sbin']) == '/sbin/ifconfig' or get_bin

# Generated at 2024-05-31 00:41:47.614433
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in opt_dirs
    assert get_bin_path('custom_exec', opt_dirs=['/opt/custom/bin']) == '/opt/custom/bin/custom_exec'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_exec')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_exec" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'
    assert get_bin_path('ifconfig') == '/sbin/ifconfig'


# Generated at 2024-05-31 00:41:51.069203
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in the optional directories
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'
    assert get_bin_path('ifconfig') == '/sbin/ifconfig'


# Generated at 2024-05-31 00:41:54.719349
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls' or get_bin_path('ls') == '/usr/bin/ls'

    # Test when the executable is found in the optional directories
    opt_dirs = ['/usr/local/bin']
    assert get_bin_path('custom_executable', opt_dirs=opt_dirs) == '/usr/local/bin/custom_executable'

    # Test when the executable is not found
    try:
        get_bin_path('non_existent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "non_existent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'

# Generated at 2024-05-31 00:41:57.768753
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in opt_dirs
    assert get_bin_path('my_executable', opt_dirs=['/opt/my_bin']) == '/opt/my_bin/my_executable'

    # Test when the executable is not found
    try:
        get_bin_path('non_existent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "non_existent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ifconfig') == '/sbin/ifconfig'


# Generated at 2024-05-31 00:42:00.629663
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in the optional directories
    assert get_bin_path('my_executable', opt_dirs=['/opt/bin']) == '/opt/bin/my_executable'

    # Test when the executable is not found and raises ValueError
    try:
        get_bin_path('non_existent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "non_existent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'
    assert get_bin_path('ifconfig') == '/sbin/ifconfig'


# Generated at 2024-05-31 00:42:03.939324
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:42:10.099988
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in the optional directories
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'
    assert get_bin_path('ifconfig') == '/sbin/ifconfig'


# Generated at 2024-05-31 00:42:13.534292
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in the optional directories
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'
    assert get_bin_path('ifconfig') == '/sbin/ifconfig'


# Generated at 2024-05-31 00:42:16.665984
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in the optional directories
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'
    assert get_bin_path('ifconfig') == '/sbin/ifconfig'


# Generated at 2024-05-31 00:42:20.013765
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls' or get_bin_path('ls') == '/usr/bin/ls'

    # Test when the executable is found in the optional directories
    opt_dirs = ['/usr/local/bin']
    assert get_bin_path('custom_executable', opt_dirs=opt_dirs) == '/usr/local/bin/custom_executable'

    # Test when the executable is not found
    try:
        get_bin_path('non_existent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "non_existent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'

# Generated at 2024-05-31 00:42:22.944912
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in the optional directories
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/local/bin'
    assert get_bin_path('ifconfig', opt_dirs=['/sbin']) == '/sbin/ifconfig'


# Generated at 2024-05-31 00:42:26.302100
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls' or get_bin_path('ls') == '/usr/bin/ls'

    # Test when the executable is found in the optional directories
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'

# Generated at 2024-05-31 00:42:29.728864
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in the optional directories
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'
    assert get_bin_path('ifconfig') == '/sbin/ifconfig'


# Generated at 2024-05-31 00:42:33.373919
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls' or get_bin_path('ls') == '/usr/bin/ls'

    # Test when the executable is found in the optional directories
    opt_dirs = ['/usr/local/bin']
    assert get_bin_path('custom_executable', opt_dirs=opt_dirs) == '/usr/local/bin/custom_executable'

    # Test when the executable is not found and should raise ValueError
    try:
        get_bin_path('non_existent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "non_existent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in the sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'
    assert get_bin

# Generated at 2024-05-31 00:42:36.606021
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls' or get_bin_path('ls') == '/usr/bin/ls'

    # Test when the executable is found in the optional directories
    opt_dirs = ['/usr/local/bin']
    assert get_bin_path('custom_executable', opt_dirs=opt_dirs) == '/usr/local/bin/custom_executable'

    # Test when the executable is not found
    try:
        get_bin_path('non_existent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "non_existent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'

# Generated at 2024-05-31 00:42:39.763950
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in the optional directories
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/local/bin'
    assert get_bin_path('ifconfig', opt_dirs=['/sbin']) == '/sbin/ifconfig'


# Generated at 2024-05-31 00:42:48.723237
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls' or get_bin_path('ls') == '/usr/bin/ls'

    # Test when the executable is found in the optional directories
    opt_dirs = ['/usr/local/bin']
    assert get_bin_path('custom_executable', opt_dirs=opt_dirs) == '/usr/local/bin/custom_executable'

    # Test when the executable is not found
    try:
        get_bin_path('non_existent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "non_existent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'

# Generated at 2024-05-31 00:42:52.044564
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in the optional directories
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/local/bin'
    assert get_bin_path('ifconfig', opt_dirs=['/sbin']) == '/sbin/ifconfig'


# Generated at 2024-05-31 00:42:56.050857
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in the optional directories
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/local/bin'
    assert get_bin_path('ifconfig', opt_dirs=['/sbin']) == '/sbin/ifconfig'


# Generated at 2024-05-31 00:42:59.669367
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls' or get_bin_path('ls') == '/usr/bin/ls'

    # Test when the executable is found in the optional directories
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in the sbin directories
    os.environ['PATH'] = '/usr/sbin:/sbin'

# Generated at 2024-05-31 00:43:03.205948
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls' or get_bin_path('ls') == '/usr/bin/ls'

    # Test when the executable is found in the optional directories
    opt_dirs = ['/usr/local/bin']
    assert get_bin_path('custom_executable', opt_dirs=opt_dirs) == '/usr/local/bin/custom_executable'

    # Test when the executable is not found
    try:
        get_bin_path('non_existent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "non_existent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'

# Generated at 2024-05-31 00:43:06.262391
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in the optional directories
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/local/bin'
    assert get_bin_path('ifconfig', opt_dirs=['/sbin']) == '/sbin/ifconfig'


# Generated at 2024-05-31 00:43:10.219179
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls' or get_bin_path('ls') == '/usr/bin/ls'

    # Test when the executable is found in the optional directories
    opt_dirs = ['/usr/local/bin']
    assert get_bin_path('custom_executable', opt_dirs=opt_dirs) == '/usr/local/bin/custom_executable'

    # Test when the executable is not found and should raise ValueError
    try:
        get_bin_path('non_existent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "non_existent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in the sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'
    assert get_bin

# Generated at 2024-05-31 00:43:14.906531
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in the optional directories
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/local/bin'
    assert get_bin_path('ifconfig', opt_dirs=['/sbin']) == '/sbin/ifconfig'


# Generated at 2024-05-31 00:43:18.630665
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:43:22.005467
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:43:31.106743
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:43:34.263932
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in the optional directories
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'
    assert get_bin_path('ifconfig') == '/sbin/ifconfig'


# Generated at 2024-05-31 00:43:39.616526
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:43:42.361680
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in opt_dirs
    assert get_bin_path('custom_exec', opt_dirs=['/opt/bin']) == '/opt/bin/custom_exec'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_exec')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_exec" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('sbin_exec', opt_dirs=['/sbin']) == '/sbin/sbin_exec'


# Generated at 2024-05-31 00:43:45.102193
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in opt_dirs
    assert get_bin_path('custom_exec', opt_dirs=['/opt/bin']) == '/opt/bin/custom_exec'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_exec')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_exec" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'
    assert get_bin_path('ifconfig') == '/sbin/ifconfig'


# Generated at 2024-05-31 00:43:48.555631
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in the optional directories
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'
    assert get_bin_path('ifconfig') == '/sbin/ifconfig'


# Generated at 2024-05-31 00:43:53.411337
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:43:56.689447
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:43:59.768304
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in the optional directories
    assert get_bin_path('my_executable', opt_dirs=['/opt/bin']) == '/opt/bin/my_executable'

    # Test when the executable is not found and should raise ValueError
    try:
        get_bin_path('non_existent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "non_existent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('sbin_executable', opt_dirs=['/sbin']) == '/sbin/sbin_executable'


# Generated at 2024-05-31 00:44:02.835554
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:44:11.840503
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:44:16.491013
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls' or get_bin_path('ls') == '/usr/bin/ls'

    # Test when the executable is found in opt_dirs
    opt_dirs = ['/usr/local/bin']
    assert get_bin_path('custom_executable', opt_dirs=opt_dirs) == '/usr/local/bin/custom_executable'

    # Test when the executable is not found
    try:
        get_bin_path('non_existent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "non_existent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/bin:/bin'

# Generated at 2024-05-31 00:44:20.596271
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls' or get_bin_path('ls') == '/usr/bin/ls'

    # Test when the executable is found in the optional directories
    opt_dirs = ['/usr/local/bin']
    assert get_bin_path('custom_executable', opt_dirs=opt_dirs) == '/usr/local/bin/custom_executable'

    # Test when the executable is not found
    try:
        get_bin_path('non_existent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "non_existent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'

# Generated at 2024-05-31 00:44:24.018120
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:44:27.221419
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:44:30.588556
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:44:34.028425
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:44:38.304393
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in the optional directories
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'
    assert get_bin_path('ifconfig') == '/sbin/ifconfig'


# Generated at 2024-05-31 00:44:45.295930
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:44:48.914472
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:44:59.021246
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in the optional directories
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'
    assert get_bin_path('ifconfig') == '/sbin/ifconfig'


# Generated at 2024-05-31 00:45:04.238897
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls' or get_bin_path('ls') == '/usr/bin/ls'

    # Test when the executable is found in the optional directories
    opt_dirs = ['/usr/local/bin']
    assert get_bin_path('custom_executable', opt_dirs=opt_dirs) == '/usr/local/bin/custom_executable'

    # Test when the executable is not found and should raise ValueError
    try:
        get_bin_path('non_existent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "non_existent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'
    assert get_bin_path

# Generated at 2024-05-31 00:45:08.530864
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls' or get_bin_path('ls') == '/usr/bin/ls'

    # Test when the executable is found in the optional directories
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/local/sbin:/usr/sbin:/sbin:/usr/bin:/bin'

# Generated at 2024-05-31 00:45:11.830782
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in the optional directories
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'
    assert get_bin_path('ifconfig') == '/sbin/ifconfig'


# Generated at 2024-05-31 00:45:15.351665
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls' or get_bin_path('ls') == '/usr/bin/ls'

    # Test when the executable is found in the optional directories
    opt_dirs = ['/usr/local/bin']
    assert get_bin_path('custom_executable', opt_dirs=opt_dirs) == '/usr/local/bin/custom_executable'

    # Test when the executable is not found
    try:
        get_bin_path('non_existent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "non_existent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'

# Generated at 2024-05-31 00:45:18.923119
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls' or get_bin_path('ls') == '/usr/bin/ls'

    # Test when the executable is found in the optional directories
    opt_dirs = ['/usr/local/bin']
    assert get_bin_path('custom_executable', opt_dirs=opt_dirs) == '/usr/local/bin/custom_executable'

    # Test when the executable is not found
    try:
        get_bin_path('non_existent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "non_existent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'

# Generated at 2024-05-31 00:45:22.519308
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:45:27.221005
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:45:30.525957
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:45:33.967936
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:45:42.539033
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:45:47.262433
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls' or get_bin_path('ls') == '/usr/bin/ls'

    # Test when the executable is found in opt_dirs
    opt_dirs = ['/usr/local/bin']
    assert get_bin_path('custom_executable', opt_dirs=opt_dirs) == '/usr/local/bin/custom_executable'

    # Test when the executable is not found
    try:
        get_bin_path('non_existent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "non_existent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/bin:/bin'

# Generated at 2024-05-31 00:45:51.975915
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:45:55.162862
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:46:01.987831
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in the optional directories
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/local/bin'
    assert get_bin_path('ifconfig', opt_dirs=['/sbin']) == '/sbin/ifconfig'


# Generated at 2024-05-31 00:46:05.343795
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls' or get_bin_path('ls') == '/usr/bin/ls'

    # Test when the executable is found in opt_dirs
    opt_dirs = ['/usr/local/bin']
    assert get_bin_path('custom_executable', opt_dirs=opt_dirs) == '/usr/local/bin/custom_executable'

    # Test when the executable is not found
    try:
        get_bin_path('non_existent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "non_existent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'

# Generated at 2024-05-31 00:46:09.212550
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:46:12.878186
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:46:16.598135
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls' or get_bin_path('ls') == '/usr/bin/ls'

    # Test when the executable is found in the optional directories
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'

# Generated at 2024-05-31 00:46:19.396636
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in the optional directories
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'
    assert get_bin_path('ifconfig') == '/sbin/ifconfig'


# Generated at 2024-05-31 00:46:27.990281
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:46:31.477253
# Unit test for function get_bin_path
def test_get_bin_path():    import tempfile

# Generated at 2024-05-31 00:46:34.241609
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls' or get_bin_path('ls') == '/usr/bin/ls'

    # Test when the executable is found in opt_dirs
    opt_dirs = ['/usr/local/bin']
    assert get_bin_path('custom_executable', opt_dirs=opt_dirs) == '/usr/local/bin/custom_executable'

    # Test when the executable is not found
    try:
        get_bin_path('non_existent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "non_existent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'

# Generated at 2024-05-31 00:46:37.675183
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls' or get_bin_path('ls') == '/usr/bin/ls'

    # Test when the executable is found in the optional directories
    opt_dirs = ['/usr/local/bin']
    assert get_bin_path('custom_executable', opt_dirs=opt_dirs) == '/usr/local/bin/custom_executable'

    # Test when the executable is not found
    try:
        get_bin_path('non_existent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "non_existent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'

# Generated at 2024-05-31 00:46:40.737332
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls' or get_bin_path('ls') == '/usr/bin/ls'

    # Test when the executable is found in opt_dirs
    opt_dirs = ['/usr/local/bin']
    assert get_bin_path('custom_executable', opt_dirs=opt_dirs) == '/usr/local/bin/custom_executable'

    # Test when the executable is not found
    try:
        get_bin_path('non_existent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "non_existent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/bin:/bin'

# Generated at 2024-05-31 00:46:43.745440
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:46:47.278495
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls' or get_bin_path('ls') == '/usr/bin/ls'

    # Test when the executable is found in opt_dirs
    opt_dirs = ['/usr/local/bin']
    assert get_bin_path('custom_executable', opt_dirs=opt_dirs) == '/usr/local/bin/custom_executable'

    # Test when the executable is not found
    try:
        get_bin_path('non_existent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "non_existent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/bin:/bin'

# Generated at 2024-05-31 00:46:53.778183
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls' or get_bin_path('ls') == '/usr/bin/ls'

    # Test when the executable is found in the optional directories
    opt_dirs = ['/usr/local/bin']
    assert get_bin_path('custom_executable', opt_dirs=opt_dirs) == '/usr/local/bin/custom_executable'

    # Test when the executable is not found
    try:
        get_bin_path('non_existent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "non_existent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'

# Generated at 2024-05-31 00:46:58.040866
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:47:03.145414
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:47:11.534907
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in the optional directories
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'
    assert get_bin_path('ifconfig') == '/sbin/ifconfig'


# Generated at 2024-05-31 00:47:17.466386
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:47:21.595350
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in the optional directories
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/local/bin'
    assert get_bin_path('ifconfig', opt_dirs=['/sbin']) == '/sbin/ifconfig'


# Generated at 2024-05-31 00:47:25.032661
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:47:28.302082
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:47:31.417819
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls' or get_bin_path('ls') == '/usr/bin/ls'

    # Test when the executable is found in opt_dirs
    opt_dirs = ['/usr/local/bin']
    assert get_bin_path('custom_executable', opt_dirs=opt_dirs) == '/usr/local/bin/custom_executable'

    # Test when the executable is not found
    try:
        get_bin_path('non_existent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "non_existent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/bin:/bin'

# Generated at 2024-05-31 00:47:34.816728
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in opt_dirs
    assert get_bin_path('custom_exec', opt_dirs=['/opt/custom/bin']) == '/opt/custom/bin/custom_exec'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_exec')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_exec" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('sbin_exec', opt_dirs=['/sbin']) == '/sbin/sbin_exec'


# Generated at 2024-05-31 00:47:38.238485
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:47:43.108618
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:47:46.009655
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in the optional directories
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/local/bin'
    assert get_bin_path('ifconfig', opt_dirs=['/sbin']) == '/sbin/ifconfig'


# Generated at 2024-05-31 00:47:57.865067
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:48:02.917078
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:48:06.152790
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:48:08.809040
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in the optional directories
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/local/bin'
    assert get_bin_path('ifconfig', opt_dirs=['/sbin']) == '/sbin/ifconfig'


# Generated at 2024-05-31 00:48:13.270405
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in the optional directories
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'
    assert get_bin_path('ifconfig') == '/sbin/ifconfig'


# Generated at 2024-05-31 00:48:18.559642
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:48:22.176184
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls' or get_bin_path('ls') == '/usr/bin/ls'

    # Test when the executable is found in the optional directories
    opt_dirs = ['/usr/local/bin']
    assert get_bin_path('custom_executable', opt_dirs=opt_dirs) == '/usr/local/bin/custom_executable'

    # Test when the executable is not found and should raise ValueError
    try:
        get_bin_path('non_existent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "non_existent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/bin:/bin'

# Generated at 2024-05-31 00:48:27.524066
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls' or get_bin_path('ls') == '/usr/bin/ls'

    # Test when the executable is found in the optional directories
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'

# Generated at 2024-05-31 00:48:30.868563
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in the optional directories
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/local/bin'
    assert get_bin_path('ifconfig', opt_dirs=['/sbin']) == '/sbin/ifconfig'


# Generated at 2024-05-31 00:48:36.826678
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:48:54.379352
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in opt_dirs
    assert get_bin_path('custom_exec', opt_dirs=['/opt/bin']) == '/opt/bin/custom_exec'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_exec')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_exec" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('sbin_exec', opt_dirs=['/sbin']) == '/sbin/sbin_exec'


# Generated at 2024-05-31 00:48:57.579592
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:49:00.804466
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:49:05.770678
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:49:09.460375
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in the optional directories
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/local/bin'
    assert get_bin_path('ifconfig', opt_dirs=['/sbin']) == '/sbin/ifconfig'


# Generated at 2024-05-31 00:49:13.200487
# Unit test for function get_bin_path

# Generated at 2024-05-31 00:49:17.191472
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls' or get_bin_path('ls') == '/usr/bin/ls'

    # Test when the executable is found in the optional directories
    opt_dirs = ['/usr/local/bin']
    assert get_bin_path('custom_executable', opt_dirs=opt_dirs) == '/usr/local/bin/custom_executable'

    # Test when the executable is not found
    try:
        get_bin_path('non_existent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "non_existent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'

# Generated at 2024-05-31 00:49:20.935699
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:49:23.915429
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in opt_dirs
    assert get_bin_path('custom_exec', opt_dirs=['/opt/bin']) == '/opt/bin/custom_exec'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_exec')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_exec" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('sbin_exec', opt_dirs=['/sbin']) == '/sbin/sbin_exec'


# Generated at 2024-05-31 00:49:27.562232
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls' or get_bin_path('ls') == '/usr/bin/ls'

    # Test when the executable is found in the optional directories
    opt_dirs = ['/usr/local/bin']
    assert get_bin_path('custom_executable', opt_dirs=opt_dirs) == '/usr/local/bin/custom_executable'

    # Test when the executable is not found
    try:
        get_bin_path('non_existent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "non_existent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'

# Generated at 2024-05-31 00:49:45.790105
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in opt_dirs
    assert get_bin_path('custom_exec', opt_dirs=['/opt/bin']) == '/opt/bin/custom_exec'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_exec')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_exec" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('sbin_exec', opt_dirs=['/sbin']) == '/sbin/sbin_exec'


# Generated at 2024-05-31 00:49:48.899299
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in the optional directories
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'
    assert get_bin_path('ifconfig') == '/sbin/ifconfig'


# Generated at 2024-05-31 00:49:51.989252
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls' or get_bin_path('ls') == '/usr/bin/ls'

    # Test when the executable is found in opt_dirs
    assert get_bin_path('ls', opt_dirs=['/bin']) == '/bin/ls'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/local/bin'

# Generated at 2024-05-31 00:49:55.210726
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:49:59.301360
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:50:02.293575
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in opt_dirs
    assert get_bin_path('my_executable', opt_dirs=['/opt/my_bin']) == '/opt/my_bin/my_executable'

    # Test when the executable is not found
    try:
        get_bin_path('non_existent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "non_existent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ifconfig') == '/sbin/ifconfig'


# Generated at 2024-05-31 00:50:05.264400
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in opt_dirs
    assert get_bin_path('my_executable', opt_dirs=['/opt/bin']) == '/opt/bin/my_executable'

    # Test when the executable is not found
    try:
        get_bin_path('non_existent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "non_existent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('sbin_executable', opt_dirs=['/sbin']) == '/sbin/sbin_executable'


# Generated at 2024-05-31 00:50:08.875375
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:50:11.924206
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls' or get_bin_path('ls') == '/usr/bin/ls'

    # Test when the executable is found in opt_dirs
    opt_dirs = ['/usr/local/bin']
    assert get_bin_path('custom_executable', opt_dirs=opt_dirs) == '/usr/local/bin/custom_executable'

    # Test when the executable is not found
    try:
        get_bin_path('non_existent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "non_existent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/bin:/bin'

# Generated at 2024-05-31 00:50:15.102185
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:50:34.615971
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:50:37.650888
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls' or get_bin_path('ls') == '/usr/bin/ls'

    # Test when the executable is found in opt_dirs
    assert get_bin_path('ls', opt_dirs=['/bin']) == '/bin/ls'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/bin:/bin'

# Generated at 2024-05-31 00:50:41.137044
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls' or get_bin_path('ls') == '/usr/bin/ls'

    # Test when the executable is found in the optional directories
    opt_dirs = ['/usr/local/bin']
    assert get_bin_path('custom_executable', opt_dirs=opt_dirs) == '/usr/local/bin/custom_executable'

    # Test when the executable is not found
    try:
        get_bin_path('non_existent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "non_existent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'

# Generated at 2024-05-31 00:50:44.390820
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:50:48.331834
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls' or get_bin_path('ls') == '/usr/bin/ls'

    # Test when the executable is found in opt_dirs
    opt_dirs = ['/usr/local/bin']
    assert get_bin_path('custom_executable', opt_dirs=opt_dirs) == '/usr/local/bin/custom_executable'

    # Test when the executable is not found
    try:
        get_bin_path('non_existent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "non_existent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/bin:/bin'

# Generated at 2024-05-31 00:50:53.296288
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls' or get_bin_path('ls') == '/usr/bin/ls'

    # Test when the executable is found in opt_dirs
    opt_dirs = ['/usr/local/bin']
    assert get_bin_path('custom_executable', opt_dirs=opt_dirs) == '/usr/local/bin/custom_executable'

    # Test when the executable is not found
    try:
        get_bin_path('non_existent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "non_existent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/bin:/bin'

# Generated at 2024-05-31 00:50:56.756667
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls' or get_bin_path('ls') == '/usr/bin/ls'

    # Test when the executable is found in the optional directories
    opt_dirs = ['/usr/local/bin']
    assert get_bin_path('custom_executable', opt_dirs=opt_dirs) == '/usr/local/bin/custom_executable'

    # Test when the executable is not found and should raise ValueError
    try:
        get_bin_path('non_existent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "non_existent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'
    assert get_bin_path

# Generated at 2024-05-31 00:51:00.556893
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:51:04.001124
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls'

    # Test when the executable is found in the optional directories
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'

    # Test when the executable is not found
    try:
        get_bin_path('nonexistent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nonexistent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/local/bin'
    assert get_bin_path('ifconfig', opt_dirs=['/sbin']) == '/sbin/ifconfig'


# Generated at 2024-05-31 00:51:06.987253
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest

# Generated at 2024-05-31 00:51:25.292086
# Unit test for function get_bin_path
def test_get_bin_path():    # Test when the executable is found in the PATH
    os.environ['PATH'] = '/usr/bin:/bin'
    assert get_bin_path('ls') == '/bin/ls' or get_bin_path('ls') == '/usr/bin/ls'

    # Test when the executable is found in the optional directories
    opt_dirs = ['/usr/local/bin']
    assert get_bin_path('custom_executable', opt_dirs=opt_dirs) == '/usr/local/bin/custom_executable'

    # Test when the executable is not found and should raise ValueError
    try:
        get_bin_path('non_existent_executable')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "non_existent_executable" in paths: /usr/bin:/bin'

    # Test when the executable is found in sbin paths
    os.environ['PATH'] = '/usr/sbin:/sbin'
    assert get_bin_path

# Generated at 2024-05-31 00:51:28.926054
# Unit test for function get_bin_path
def test_get_bin_path():    import pytest