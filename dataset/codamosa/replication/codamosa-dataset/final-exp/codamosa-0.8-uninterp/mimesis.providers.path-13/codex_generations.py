

# Generated at 2022-06-14 00:20:45.379494
# Unit test for constructor of class Path
def test_Path():
    """Unit test for constructor of class Path."""
    path = Path()
    print(path.project_dir())
    print(path.dev_dir())
    print(path.users_folder())
    print(path.user())
    print(path.home())
    print(path.root())

if __name__ == '__main__':
    test_Path()

# Generated at 2022-06-14 00:20:52.630603
# Unit test for constructor of class Path
def test_Path():
    # darwin path
    path1 = Path('darwin')
    assert path1.platform == 'darwin'
    assert path1._pathlib_home.parent / PLATFORMS['darwin']['home'] == PurePosixPath('/Users/')

    # win32/64 path
    path2 = Path('win32')
    assert path2.platform == 'win32'
    assert path2._pathlib_home.parent / PLATFORMS['win32']['home'] == PureWindowsPath('C:\\Users\\')



# Generated at 2022-06-14 00:20:58.906030
# Unit test for method user of class Path
def test_Path_user():
    path = Path()
    for i in range(100):
        result = path.user()
        assert isinstance(result, str)
        assert len(result.split('/')) == 3


# Generated at 2022-06-14 00:21:04.586913
# Unit test for constructor of class Path
def test_Path():
    if __name__ == "__main__":
        path = Path()
        print(path.root())
        print(path.home())
        print(path.user())
        print(path.users_folder())
        print(path.dev_dir())
        print(path.project_dir())

# Generated at 2022-06-14 00:21:07.702063
# Unit test for method user of class Path
def test_Path_user():
    assert Path().user() == '/home/chung'


# Generated at 2022-06-14 00:21:10.243518
# Unit test for method user of class Path
def test_Path_user():
    p = Path(platform='darwin')
    assert p.user() == '/home/oretha'
    assert p.user() == '/home/glenn'
    assert p.user() == '/home/marcella'

# Generated at 2022-06-14 00:21:12.191150
# Unit test for method user of class Path
def test_Path_user():
    r=Path(platform='linux').user()
    assert r == '/home/krystina'

# Generated at 2022-06-14 00:21:21.564247
# Unit test for method user of class Path
def test_Path_user():
    """Test method user of class Path."""
    path = Path()
    path.random.seed(0)
    user = path.user()
    assert user == '/home/wilhelmina'
    user = path.user()
    assert user == '/home/quentin'
    user = path.user()
    assert user == '/home/georgianna'
    user = path.user()
    assert user == '/home/nella'
    user = path.user()
    assert user == '/home/frank'
    user = path.user()
    assert user == '/home/colin'
    user = path.user()
    assert user == '/home/cathey'
    user = path.user()
    assert user == '/home/luisa'
    user = path.user()

# Generated at 2022-06-14 00:21:23.521148
# Unit test for method user of class Path
def test_Path_user():
    p = Path()
    user_ = p.user()
    print(user_)


# Generated at 2022-06-14 00:21:27.718288
# Unit test for method user of class Path
def test_Path_user():
    """Testing for Path.user"""
    test_Path = Path()
    test_user = test_Path.user()
    print(test_user)

