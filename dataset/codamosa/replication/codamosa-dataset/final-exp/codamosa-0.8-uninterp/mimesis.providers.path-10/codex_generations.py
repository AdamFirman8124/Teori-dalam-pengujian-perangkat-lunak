

# Generated at 2022-06-14 00:20:44.338254
# Unit test for constructor of class Path
def test_Path():
  path = Path()
  path.dev_dir()
  path.home()
  path.project_dir()
  path.root()
  path.users_folder()
  path.user()

# Generated at 2022-06-14 00:20:46.962147
# Unit test for method user of class Path
def test_Path_user():
    p1 = Path()
    assert p1.user() == '/home/taneka'


# Generated at 2022-06-14 00:20:49.322742
# Unit test for constructor of class Path
def test_Path():
    class PathTest:
        def test_Path(self):
            test = Path()
            assert type(test) == Path

# Generated at 2022-06-14 00:20:55.739244
# Unit test for method user of class Path
def test_Path_user():
    # initialize Path instance
    mypath = Path()
    # get path
    path = mypath.user()
    # Check if it is a string
    assert isinstance(path, str)
    # Check if it is in the list of paths
    assert path in ['/home/dino', '/home/billy', '/home/tameika', '/home/stefan', '/home/kristy']


# Generated at 2022-06-14 00:20:58.239217
# Unit test for constructor of class Path
def test_Path():
    p = Path()
    assert p.platform == sys.platform



# Generated at 2022-06-14 00:21:00.447201
# Unit test for method user of class Path
def test_Path_user():
    assert Path().user() == '/home/taneka'


# Generated at 2022-06-14 00:21:05.562511
# Unit test for constructor of class Path
def test_Path():
    print('Testing the constructor of Path class.')
    path = Path()
    path2 = Path('win32')
    assert 'Path' == path.__class__.Meta.name
    assert 'Path' == path2.__class__.Meta.name
    assert sys.platform == path.platform
    assert 'win32' == path2.platform


# Generated at 2022-06-14 00:21:17.021621
# Unit test for constructor of class Path
def test_Path():
    assert Path().root() == '/'
    assert Path().home() == '/home'
    assert Path('linux').home() == Path().home()
    assert Path('win32').home() == 'C:\\Users'
    # Generate a random user
    assert Path('linux').user() == '/home/oretha'
    assert Path('win32').user() == 'C:\\Users\\Sherika'
    # Generate a random path to user's folders
    assert Path().users_folder() == '/home/taneka/Pictures'
    assert Path('win32').users_folder() == 'C:\\Users\\Sherrell\\Videos'
    # Generate a random path to development directory
    assert Path().dev_dir() == '/home/sherrell/Development/Python'

# Generated at 2022-06-14 00:21:21.708280
# Unit test for method user of class Path
def test_Path_user():
    from mimesis.enums import Gender
    counter = 0
    for i in range(0, 1000):
        path = Path(platform='linux')
        if path.random.from_enum(Gender) == Gender.FEMALE:
            assert path.user() == '/home/oretha'
            counter += 1
        else:
            assert path.user() == '/home/sherrell'
            counter += 1
    assert counter == 1000


# Generated at 2022-06-14 00:21:23.210806
# Unit test for constructor of class Path
def test_Path():
    """
    Test method Path.__init__:
    """
    assert Path()