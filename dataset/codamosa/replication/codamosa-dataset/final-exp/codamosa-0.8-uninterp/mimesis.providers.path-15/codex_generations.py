

# Generated at 2022-06-14 00:20:43.012869
# Unit test for method user of class Path
def test_Path_user():
    path = Path()
    print(path.user())

# Generated at 2022-06-14 00:20:44.835614
# Unit test for method user of class Path
def test_Path_user():
    _path = Path()
    assert _path.user() == '/home/oretha'

# Generated at 2022-06-14 00:20:48.028035
# Unit test for constructor of class Path
def test_Path():
    path = Path()
    assert isinstance(path, Path)

# Generated at 2022-06-14 00:20:49.257389
# Unit test for constructor of class Path
def test_Path():
    path = Path()
    assert path is not None

# Generated at 2022-06-14 00:20:51.858134
# Unit test for constructor of class Path
def test_Path():
    path = Path()
    path1 = Path('linux')
    path2 = Path(platform='linux')
    path3 = Path('windows')
    p = Path(platform='linux')

# Generated at 2022-06-14 00:20:56.194311
# Unit test for constructor of class Path
def test_Path():
    path = Path()
    print(path.home())
    print(path.user())
    print(path.users_folder())
    print(path.dev_dir())
    print(path.project_dir())


# Generated at 2022-06-14 00:20:58.175113
# Unit test for method user of class Path
def test_Path_user():
    path = Path()
    assert path.user() != ""

# Generated at 2022-06-14 00:21:02.014173
# Unit test for constructor of class Path
def test_Path():
    path = Path()
    assert path.platform in PLATFORMS.keys(), "platform error"
    assert path._pathlib_home.parent.name == PLATFORMS[path.platform]['root']
    assert path._pathlib_home.name == PLATFORMS[path.platform]['home']


# Generated at 2022-06-14 00:21:06.222952
# Unit test for constructor of class Path
def test_Path():
    path = Path()
    assert path.platform == sys.platform
    assert path._pathlib_home == PureWindowsPath() if 'win' in sys.platform else PurePosixPath()
    assert path._pathlib_home == PureWindowsPath() / PLATFORMS[sys.platform]['home']
    assert isinstance(path, BaseProvider)


# Generated at 2022-06-14 00:21:09.209516
# Unit test for constructor of class Path
def test_Path():
    p1 = Path("linux")
    p2 = Path("darwin")
    p3 = Path("windows")
    assert p1.platform == 'linux'
    # print("Unit test test_Path() is complete!!!\n")
