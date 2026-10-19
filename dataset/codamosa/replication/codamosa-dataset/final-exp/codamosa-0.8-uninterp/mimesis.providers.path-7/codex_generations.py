

# Generated at 2022-06-14 00:20:43.299021
# Unit test for constructor of class Path
def test_Path():
    p = Path(platform='linux')
    assert p.platform == 'linux'
    assert p.__class__.__name__ == 'Path'


# Generated at 2022-06-14 00:20:52.214236
# Unit test for constructor of class Path
def test_Path():
    path = Path(platform='win32')
    assert repr(path) == "<BaseProvider('path')>"
    assert repr(path.random) == "<Random()>"
    assert repr(path.datetime) == "<DateTime()>"
    assert repr(path.text) == "<Text()>"
    assert repr(path.numbers) == "<Numbers()>"
    assert path.platform == 'win32'
    assert path._pathlib_home == PureWindowsPath('C:\\Users')
    


# Generated at 2022-06-14 00:20:55.067733
# Unit test for constructor of class Path
def test_Path():
    for i in range(7):
        x = Path()
        print(x)


# Generated at 2022-06-14 00:20:57.562761
# Unit test for constructor of class Path
def test_Path():
    assert Path('win32').platform == sys.platform
    assert Path().platform == sys.platform

# Generated at 2022-06-14 00:21:01.612361
# Unit test for method user of class Path
def test_Path_user():
    p = Path()
    user = p.user()
    assert isinstance(user, str)
    assert user


# Generated at 2022-06-14 00:21:06.011798
# Unit test for constructor of class Path
def test_Path():
    # New instance is created
    instance = Path()

    # Instance has platform value
    assert instance.platform

    # Instance has attribute _pathlib_home
    assert hasattr(instance, '_pathlib_home')



# Generated at 2022-06-14 00:21:16.798836
# Unit test for constructor of class Path
def test_Path():
    p = Path()
    assert str(p._pathlib_home) == '/home'
    p2 = Path(platform='win32')
    assert str(p2._pathlib_home) == 'C:\\Users'

    # Unit test for method Path.root()
    def test_root():
        r = p.root()
        assert r == '/'

    # Unit test for method Path.home()
    def test_home():
        h = p.home()
        assert h == '/home'

    # Unit test for method Path.users_folder()
    def test_users_folder():
        uf = p.users_folder()
        assert uf.startswith('/home')
        assert uf.endswith('/Pictures')

    # Unit test for method Path.dev_dir()

# Generated at 2022-06-14 00:21:21.313037
# Unit test for constructor of class Path
def test_Path():
    p = Path(platform='linux')
    print(p.root())
    print(p.home())
    print(p.user())
    print(p.users_folder())
    print(p.dev_dir())
    print(p.project_dir())

if __name__ == '__main__':
    test_Path()

# Generated at 2022-06-14 00:21:24.902901
# Unit test for method user of class Path
def test_Path_user():
    """Unit test for method user of class Path."""
    path_provider = Path()
    path = path_provider.user()
    assert path.startswith('/home/')


# Generated at 2022-06-14 00:21:27.433619
# Unit test for constructor of class Path
def test_Path():
    class_ = Path()
    assert class_.platform == sys.platform
