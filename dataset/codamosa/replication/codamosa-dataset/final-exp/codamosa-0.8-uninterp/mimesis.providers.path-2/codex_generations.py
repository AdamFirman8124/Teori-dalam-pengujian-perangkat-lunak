

# Generated at 2022-06-14 00:20:44.165052
# Unit test for method user of class Path
def test_Path_user():
    print("Test for method user of class Path")
    for i in range(5):
        print("Test_{}:".format(i+1))
        test_path = Path()
        path = test_path.user()
        print("    path: {}".format(path))


# Generated at 2022-06-14 00:20:45.691868
# Unit test for constructor of class Path
def test_Path():
    path = Path()
    assert path is not None

# Generated at 2022-06-14 00:20:55.179916
# Unit test for method user of class Path
def test_Path_user():
    from mimesis.builtins import Random
    from mimesis.enums import Gender
    from mimesis.utils import IN_TRAVIS
    p = Path(platform='linux')
    p.random = Random()
    p.random.set_gender(Gender.MALE)
    p.random.seed(5)
    assert p.user() == '/home/Edmond'
    p.random.set_gender(Gender.FEMALE)
    p.random.seed(5)
    assert p.user() == '/home/Hassie'
    p.random.set_gender(Gender.NOT_APPLICABLE)
    p.random.seed(5)
    assert p.user() == '/home/ethel'
    if not IN_TRAVIS:
        p = Path(platform='win32')
        p

# Generated at 2022-06-14 00:20:58.175908
# Unit test for constructor of class Path
def test_Path():
    p = Path()
    p.platform
    p._pathlib_home
    p.random

# Generated at 2022-06-14 00:20:59.977715
# Unit test for method user of class Path
def test_Path_user():
  assert Path().user() != None


# Generated at 2022-06-14 00:21:11.492697
# Unit test for constructor of class Path
def test_Path():
    p = Path()
    p.platform = 'Win32'
    assert p.platform == 'Win32'
    assert p._pathlib_home.as_posix() == 'C:\\Users\\'
    assert p._pathlib_home.as_uri() == 'file:///C:/Users/'
    assert p._pathlib_home.anchor == 'C:'
    assert p._pathlib_home.drive == 'C:'
    assert p._pathlib_home.name == ''
    assert p._pathlib_home.parents[0].as_posix() == 'C:\\'
    assert p._pathlib_home.parents[0].as_uri() == 'file:///C:/'
    assert p._pathlib_home.parents[0].anchor == 'C:'
    assert p._pathlib_home.parents

# Generated at 2022-06-14 00:21:13.471569
# Unit test for method user of class Path
def test_Path_user():
    path = Path()
    path.user() == "/home/carmelo"
    return True


# Generated at 2022-06-14 00:21:18.099292
# Unit test for method user of class Path
def test_Path_user():
    p = Path()
    assert type(str(p.user())) == str
    assert len(str(p.user())) != 0

# Generated at 2022-06-14 00:21:20.834105
# Unit test for method user of class Path
def test_Path_user():
    # initialize
    p = Path()
    # call to method
    p.user()

# Generated at 2022-06-14 00:21:33.993309
# Unit test for constructor of class Path
def test_Path():
    path = Path()
    assert isinstance(path, Path)
    assert path.platform == sys.platform
    assert path._pathlib_home == PurePosixPath('/home')
    path = Path(platform='linux')
    assert isinstance(path, Path)
    assert path.platform == 'linux'
    assert path._pathlib_home == PurePosixPath('/home')
    path = Path(platform='win32')
    assert isinstance(path, Path)
    assert path.platform == 'win32'
    assert path._pathlib_home == PureWindowsPath('\\Users')
    path = Path(platform='darwin')
    assert isinstance(path, Path)
    assert path.platform == 'darwin'
    assert path._pathlib_home == PurePosixPath('/Users')