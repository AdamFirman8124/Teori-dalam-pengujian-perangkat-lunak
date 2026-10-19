

# Generated at 2022-06-14 00:20:37.646626
# Unit test for method user of class Path
def test_Path_user():
    p = Path()
    print(p.user())

test_Path_user()

# Generated at 2022-06-14 00:20:39.134479
# Unit test for method user of class Path
def test_Path_user():
    pass


# Generated at 2022-06-14 00:20:43.706146
# Unit test for constructor of class Path
def test_Path():
    a = Path(platform='darwin')
    print(a.root())
    print(a.home())
    print(a.user())
    print(a.dev_dir())
    print(a.users_folder())
    print(a.project_dir())

if __name__ == "__main__":
    test_Path()

# Generated at 2022-06-14 00:20:56.855773
# Unit test for constructor of class Path
def test_Path():
    path = Path()
    # repeat some function calls as there seems to be a random element involved
    assert path.root() in ['/', 'C:\\' ] # not sure whether 'C:\\' is always correct
    assert path.home() in ['/home', '/Users', 'C:\\Users', 'C:\\Documents and Settings']
    #assert path.user() in ['/home/emanuela', '/Users/barton', 'C:\\Users\\jaclyn', 'C:\\Documents and Settings\\ardelia']
    assert path.users_folder() in ['/home/emanuela/Desktop', '/Users/barton/Music', 'C:\\Users\\jaclyn\\Downloads', 'C:\\Documents and Settings\\ardelia\\Templates']

# Generated at 2022-06-14 00:21:06.339254
# Unit test for constructor of class Path
def test_Path():
    """Unit test of class Path()  using the Python console"""
    from mimesis.enums import Platform
    from mimesis.data import PLATFORMS
    from mimesis.providers.path import Path
    
    platform = Platform(sys.platform)

    a_path = Path()
    print(f"\nInstantiating Path() object with no args\n")
    print(f"Generating a random root path: {a_path.root()}")
    print(f"Generating a random home path: {a_path.home()}")
    print(f"Generating a random users path: {a_path.user()}")
    print(f"Generating a random path to a users folder: {a_path.users_folder()}")

# Generated at 2022-06-14 00:21:09.314977
# Unit test for method user of class Path
def test_Path_user():
    pp = Path()
    users = ["/home/oretha", "/home/taneka", "/home/sherrell", "/home/sherika"]
    for iter in range(100):
        assert (pp.user() in users)


# Generated at 2022-06-14 00:21:12.236661
# Unit test for constructor of class Path
def test_Path():
    path = Path()
    path = Path(platform='null')
    str(path.root())
    str(path.home())
    str(path.user())
    str(path.users_folder())
    str(path.dev_dir())
    str(path.project_dir())

# Generated at 2022-06-14 00:21:17.300833
# Unit test for method user of class Path
def test_Path_user():
    path = Path()
    user = path.user()
    assert len(user) > 0
    assert user[0] == '/' if 'posix' in str(path._pathlib_home) else user[0].isalpha()
    assert user[1] == ':' if 'nt' in str(path._pathlib_home) else user[1] == '/'


# Generated at 2022-06-14 00:21:25.914799
# Unit test for constructor of class Path
def test_Path():
    # test argument: platform
    path_info = Path('linux')
    assert path_info.platform == 'linux'

    # test argument: platform, seed
    path_info = Path('linux', seed=12345)
    assert path_info.platform == 'linux'
    assert path_info.seed == 12345

    # test argument: platform, seed, use_defaults
    path_info = Path('linux', seed=12345, use_defaults=False)
    assert path_info.platform == 'linux'
    assert path_info.seed == 12345
    assert path_info.use_defaults == False


# Generated at 2022-06-14 00:21:32.161972
# Unit test for constructor of class Path
def test_Path():
    assert Path().Platform == 'win32'
    assert Path().user() == 'C:\\Users\\Иван'
    assert Path(platform='win64').root() == 'C:\\'
    assert Path().home() == 'C:\\Users'
    assert Path().users_folder() == 'C:\\Users\\Александр\\Pictures'
    assert Path().dev_dir() == 'C:\\Users\\Дмитрий\\Development\\C\\ATL'
    assert Path(platform='linux').project_dir() == '/home/sherika/Development/C#/scuba'
    assert Path().project_dir() == 'C:\\Users\\Евгений\\Development\\Fortran/77/mishap'