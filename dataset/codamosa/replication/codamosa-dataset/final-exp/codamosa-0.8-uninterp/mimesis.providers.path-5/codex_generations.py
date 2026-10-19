

# Generated at 2022-06-14 00:20:35.299299
# Unit test for method user of class Path
def test_Path_user():
    assert ("/home/devora" in Path().user())

# Generated at 2022-06-14 00:20:41.669842
# Unit test for method user of class Path
def test_Path_user():
    """Test for method user of class Path"""
    path = Path()
    result = path.user()
    assert result == str(path._pathlib_home / "Peter") or result == str(path._pathlib_home / "peter")
    assert isinstance(result, str)


# Generated at 2022-06-14 00:20:43.494784
# Unit test for constructor of class Path
def test_Path():
    path = Path()
    assert isinstance(path, Path)
    assert path.platform == sys.platform


# Generated at 2022-06-14 00:20:47.636211
# Unit test for method user of class Path
def test_Path_user():
    path = Path()
    assert path._pathlib_home.parent == PurePath().parent
    assert path._pathlib_home == PurePath('/home')
    assert path.user() == '/home/Suzann'

# Generated at 2022-06-14 00:20:50.441196
# Unit test for method user of class Path
def test_Path_user():
    p = Path()
    assert p.user() in USERNAMES
    assert p.user() in [x.capitalize() for x in USERNAMES]

# Generated at 2022-06-14 00:20:54.036463
# Unit test for method user of class Path
def test_Path_user():
    p = Path()
    path = p.user()

    if(path is not None):
        print(f"The path is {path}")


# Generated at 2022-06-14 00:20:58.238845
# Unit test for method user of class Path
def test_Path_user():
    path = Path('win32')
    user = path.user()

    assert isinstance(user, str)
    assert user.startswith('\\Users\\')


# Generated at 2022-06-14 00:21:03.065999
# Unit test for constructor of class Path
def test_Path():
    # pylint: disable=C0103
    path = Path(platform='win32', seed=8)
    assert path.platform == 'win32'
    assert path.random.randint(0, 1) == 1
    assert path.random.randint(0, 1) == 0
    assert path.random.randint(0, 1) == 0
    assert path.random.randint(0, 1) == 1
    assert path._pathlib_home == PureWindowsPath('C:\\Users')


# Generated at 2022-06-14 00:21:04.889141
# Unit test for constructor of class Path
def test_Path():
    path = Path()
    assert path.platform == sys.platform
    assert path._pathlib_home is not None

# Generated at 2022-06-14 00:21:09.465968
# Unit test for method user of class Path
def test_Path_user():
    print('Testing Path_user')
    p = Path()
    assert p.user() == '/home/oretha'
    print('test_Path_user success!')

test_Path_user()
