

# Generated at 2022-06-14 00:20:39.430871
# Unit test for method user of class Path
def test_Path_user():
    """Unit test for method user of class Path."""
    import random
    random.seed(0)
    p = Path()
    assert p.user() == '/home/qiana'

# Generated at 2022-06-14 00:20:41.897596
# Unit test for constructor of class Path
def test_Path():
    path = Path()
    assert path.platform is not None
    assert path.random is not None

# Generated at 2022-06-14 00:20:42.921078
# Unit test for constructor of class Path
def test_Path():
    assert Path().home() == '/home' or "C:\\Users"


# Generated at 2022-06-14 00:20:44.760861
# Unit test for method user of class Path
def test_Path_user():
    mimesis_path = Path(platform='linux')
    mimesis_path.platform = 'linux'
    assert mimesis_path.user() == '/home/renee'



# Generated at 2022-06-14 00:20:47.979518
# Unit test for constructor of class Path
def test_Path():
    print('Testing __init__ method of Path')
    obj = Path()
    assert(obj.platform == 'win32')


# Generated at 2022-06-14 00:20:59.279283
# Unit test for constructor of class Path
def test_Path():
    p = Path()
    assert p.platform == sys.platform
    assert type(p._pathlib_home) == PurePosixPath
    assert p._pathlib_home.parts == ('',)
    assert str(p._pathlib_home) == '/'

    p = Path(platform='linux')
    assert p.platform == 'linux'
    assert type(p._pathlib_home) == PurePosixPath
    assert p._pathlib_home.parts == ('', 'home')
    assert str(p._pathlib_home) == '/home'

    p = Path(platform='darwin')
    assert p.platform == 'darwin'
    assert type(p._pathlib_home) == PurePosixPath
    assert p._pathlib_home.parts == ('', 'home')

# Generated at 2022-06-14 00:21:04.261388
# Unit test for method user of class Path
def test_Path_user():
    p = Path()
    result = p.user()
    assert result == '/home/oretha' or result == '/home/taneka' \
           or result == '/home/sherrell' or result == '/home/sherika'


# Generated at 2022-06-14 00:21:08.145365
# Unit test for method user of class Path
def test_Path_user():
    p = Path()
    p.user()
    assert isinstance(p.user(), str)



# Generated at 2022-06-14 00:21:12.191977
# Unit test for method user of class Path
def test_Path_user():
    path = Path()
    user_0 = path.user()
    print(user_0)
    user_1 = path.user()
    print(user_1)
    user_2 = path.user()
    print(user_2)


# Generated at 2022-06-14 00:21:21.563083
# Unit test for method user of class Path
def test_Path_user():
    p = Path()
    name = p.user()

# Generated at 2022-06-14 00:21:30.701606
# Unit test for method user of class Path
def test_Path_user():
    # Initialize a Path object
    path = Path()
    # Generate a random user
    uname = path.user()
    assert uname == "/home/leora" or \
        uname == "/home/omar" or \
        uname == "/home/rosaura" or \
        uname == "/home/anabal" or \
        uname == "/home/leticia"

# Generated at 2022-06-14 00:21:32.900938
# Unit test for method user of class Path
def test_Path_user():
    path = Path()
    assert path.user() == str(path._pathlib_home / 'oretha')

# Generated at 2022-06-14 00:21:36.426142
# Unit test for method user of class Path
def test_Path_user():
    path = Path()
    user = path.user()
    assert user.startswith('/home')
    assert len(user.split('/')) == 3


# Generated at 2022-06-14 00:21:38.956376
# Unit test for method user of class Path
def test_Path_user():
    p = Path()
    user = p.user()
    assert user.startswith("/home")


# Generated at 2022-06-14 00:21:47.190591
# Unit test for method user of class Path
def test_Path_user():
    random.seed(0)
    path = Path(locale='en')
    for _ in range(100):
        assert path.user() in ['/home/marcelle', '/home/gardner', '/home/emerson', '/home/zarla', '/home/rhianna']


# Generated at 2022-06-14 00:21:49.860257
# Unit test for method user of class Path
def test_Path_user():
    path = Path()
    dev_dir = path.dev_dir()
    project_dir = path.project_dir()
    assert dev_dir != project_dir


# Generated at 2022-06-14 00:21:54.102448
# Unit test for method user of class Path
def test_Path_user():
    platform = sys.platform
    p = Path(platform)
    user_path = p.user()
    print(user_path)
    assert isinstance(user_path, str)
    assert user_path.count('/') == 2


# Generated at 2022-06-14 00:21:56.972800
# Unit test for method user of class Path
def test_Path_user():
    p = Path()
    p._random_system.choice = lambda a: a[2]
    assert p.user() == '/home/sherika'


# Generated at 2022-06-14 00:22:00.069217
# Unit test for method user of class Path
def test_Path_user():
    path = Path()
    user = path.user()
    assert user.startswith(path.root())

# Generated at 2022-06-14 00:22:01.522756
# Unit test for method user of class Path
def test_Path_user():
    path_object = Path()
    print("User's home:", path_object.user())

# Generated at 2022-06-14 00:22:06.558048
# Unit test for method user of class Path
def test_Path_user():
    for i in range(1000):
        print(Path().user())


# Generated at 2022-06-14 00:22:07.677888
# Unit test for method user of class Path
def test_Path_user():
  path = Path()
  assert isinstance(path.user(),str)


# Generated at 2022-06-14 00:22:11.690165
# Unit test for method user of class Path
def test_Path_user():
    path = Path()
    assert path.user() in ['/Users/Gregory', '/home/handy']

# Generated at 2022-06-14 00:22:19.547892
# Unit test for method user of class Path
def test_Path_user():
    from pprint import pprint as pp
    from mimesis.enums import Gender
    path = Path()
    path_prov = path.user()
    print('Created path: ', path_prov)
    assert path_prov == '/home/daryl', 'var path_prov is not set to the default value: /home/daryl'
    path = Path(gender=Gender.MALE)
    path_prov = path.user()
    print('Created path: ', path_prov)
    assert path_prov == "/home/daryl"


# Generated at 2022-06-14 00:22:22.828449
# Unit test for method user of class Path
def test_Path_user():
    path = Path()
    from mimesis.providers.path import Path
    path.random.seed(0)
    assert path.user() == '/home/kathryne'


# Generated at 2022-06-14 00:22:25.319160
# Unit test for method user of class Path
def test_Path_user():
    _Path = Path()
    assert _Path.user() == '/home/taneka', 'Test failed.'

# Generated at 2022-06-14 00:22:29.138005
# Unit test for method user of class Path
def test_Path_user():
    path = Path()
    user = path.user()
    assert isinstance(user, str)
    assert user == '/home/taneka'

# Generated at 2022-06-14 00:22:32.675252
# Unit test for method user of class Path
def test_Path_user():
    username = Path().user()
    assert isinstance(username, str)
    assert username.startswith('/home') or username.startswith('C:/Users')

# Generated at 2022-06-14 00:22:35.062526
# Unit test for method user of class Path
def test_Path_user():
    # Create instance of class Path
    path = Path()
    print(path.user())


# Generated at 2022-06-14 00:22:37.877644
# Unit test for method user of class Path
def test_Path_user():
    p = Path()
    path = p.user()
    assert path[0] == "/"
    assert "home" in path


# Generated at 2022-06-14 00:22:47.445790
# Unit test for method user of class Path
def test_Path_user():
    user_ = Path(platform = 'linux').user()
    assert isinstance(user_, str) and len(user_) > 0


# Generated at 2022-06-14 00:22:50.096636
# Unit test for method user of class Path
def test_Path_user():
    assert Path.user() == str(PureWindowsPath() if 'win' in sys.platform else PurePosixPath())



# Generated at 2022-06-14 00:23:00.351278
# Unit test for method user of class Path
def test_Path_user():
    filename = __file__
    print("file name: ", filename)
    print("file absolute path: ", file_path)
    print("path to file name: ", path_to_file)
    print("file path and name: ", file_path_name)
    print("parent directory: ", file_parent_dir_path)
    print("file name and extension: ", file_name_ext)
    print("file extension: ", file_extension)
    print("file name without extension: ", file_name_no_ext)
    print("file creation date: ", file_creation_date)
    print("file modification date: ", file_modification_date)

# Generated at 2022-06-14 00:23:01.317388
# Unit test for method user of class Path
def test_Path_user():
    assert Path().user() == '/home/noretha'


# Generated at 2022-06-14 00:23:03.789257
# Unit test for method user of class Path
def test_Path_user():
    p = Path()
    assert isinstance(p.user(), str)
    assert len(p.user()) > 0
    assert p.user().startswith(PLATFORMS[p.platform]['home'])

# Generated at 2022-06-14 00:23:05.626488
# Unit test for method user of class Path
def test_Path_user():
    p = Path()
    assert p.user() == "/home/oretha"



# Generated at 2022-06-14 00:23:11.902590
# Unit test for method user of class Path
def test_Path_user():
    p = Path()
    assert p.user() == "/home/christian"
    assert p.user() == "/home/sherrell"
    assert p.user() == "/home/deja"
    assert p.user() == "/home/duncan"
    assert p.user() == "/home/cordell"


# Generated at 2022-06-14 00:23:14.972107
# Unit test for method user of class Path
def test_Path_user():
    test = Path()
    assert any(test.user() for i in range (100))

# Generated at 2022-06-14 00:23:17.032375
# Unit test for method user of class Path
def test_Path_user():
    p = Path.Path(platform='linux')
    assert p.user() == '/home/tamar'

# Generated at 2022-06-14 00:23:19.361932
# Unit test for method user of class Path
def test_Path_user():
    p = Path()
    user = p.user()
    assert user == '/home/oretha'
