

# Generated at 2022-06-14 00:20:45.093780
# Unit test for constructor of class Path
def test_Path():  
    path = Path()
    root = path.root()
    assert(root == "\\")
    home = path.home()
    assert(home == "\\Users")
    user = path.user()
    assert(len(user) > 0)
    users_folder = path.users_folder()
    assert(len(users_folder) > 0)
    dev_dir = path.dev_dir()
    assert(len(dev_dir) > 0)
    project_dir = path.project_dir()
    assert(len(project_dir) > 0)
    
# Testing
#test_Path()

# Generated at 2022-06-14 00:20:51.783288
# Unit test for constructor of class Path
def test_Path():
    objPath = Path()
    print(objPath.root())
    print(objPath.home())
    print(objPath.user())
    print(objPath.users_folder())
    print(objPath.dev_dir())
    print(objPath.project_dir())

# Unit test
if __name__ == "__main__":
    test_Path()

# Generated at 2022-06-14 00:20:56.743097
# Unit test for method user of class Path
def test_Path_user():
    p = Path()
    u_list = []
    for i in range(50):
        t = p.user()
        if t in u_list:
            pass
        else:
            u_list.append(t)

    assert len(u_list) > 0


# Generated at 2022-06-14 00:21:03.039100
# Unit test for constructor of class Path
def test_Path():
    p = Path()
    assert p._pathlib_home == PurePosixPath()
    assert p.platform == 'linux'

    p = Path('win32')
    assert p._pathlib_home == PureWindowsPath('')
    assert p.platform == 'win32'


# Generated at 2022-06-14 00:21:06.163423
# Unit test for constructor of class Path
def test_Path():
    path = Path(platform=sys.platform)
    assert path is not None
    assert path.platform == sys.platform
    assert path._pathlib_home == PureWindowsPath()
    assert path._pathlib_home / PLATFORMS[path.platform]['home'] == PureWindowsPath()


# Generated at 2022-06-14 00:21:09.911173
# Unit test for constructor of class Path
def test_Path():
    p = Path()
    print(p.home())
    print(p.users_folder())
    print(p.user())
    print(p.dev_dir())
    print(p.project_dir())

# The main function
if __name__ == '__main__':
    test_Path()

# Generated at 2022-06-14 00:21:11.011041
# Unit test for constructor of class Path
def test_Path():
    a = Path()
    assert a


# Generated at 2022-06-14 00:21:14.114611
# Unit test for method user of class Path
def test_Path_user():
    assert Path().user() == '/home/hong'

# Generated at 2022-06-14 00:21:20.944748
# Unit test for method user of class Path
def test_Path_user():
    """Unit test for method user of class Path."""
    path = Path()
    username = path.user().split('/')[-1]
    result = path.random.choice(USERNAMES, 1)[0]
    result = result.capitalize() if 'win' in path.platform else result.lower()
    assert username == result


# Generated at 2022-06-14 00:21:24.137240
# Unit test for method user of class Path
def test_Path_user():
    """Test for method user of class Path"""
    obj = Path()
    str_ = obj.user()
    if str_:
        assert isinstance(str_, str)