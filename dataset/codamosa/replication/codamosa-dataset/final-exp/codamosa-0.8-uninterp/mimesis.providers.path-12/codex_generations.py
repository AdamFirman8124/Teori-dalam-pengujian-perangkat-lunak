

# Generated at 2022-06-14 00:20:41.360624
# Unit test for constructor of class Path
def test_Path():
    pass


# Generated at 2022-06-14 00:20:46.275138
# Unit test for constructor of class Path
def test_Path():
    path = Path()
    assert(len(path.root()) > 0)
    assert(len(path.home()) > 0)
    assert(len(path.user()) > 0)
    assert(len(path.users_folder()) > 0)
    assert(len(path.dev_dir()) > 0)
    assert(len(path.project_dir()) > 0)

# Generated at 2022-06-14 00:20:51.191478
# Unit test for method user of class Path
def test_Path_user():
    pl = Path('win32')
    lst = list(map(pl.user, range(1, 100)))
    assert lst[0] == 'C:\\Users\\Delta'
    assert lst[1] == 'C:\\Users\\Thea'


# Generated at 2022-06-14 00:20:53.146823
# Unit test for method user of class Path
def test_Path_user():
    path = Path()
    path.user()


# Generated at 2022-06-14 00:21:05.123096
# Unit test for method user of class Path
def test_Path_user():
    from mimesis.enums import Gender

    p = Path()
    assert p.user() == '/home/doyle'
    p = Path('Linux')
    assert p.user() == '/home/levon'
    p = Path('Windows')
    assert p.user() == 'C:\\Users\\Danyell'
    p = Path('Windows')
    p.seed(1234)
    assert p.user() == 'C:\\Users\\johnathon'
    p = Path('Windows')
    p.seed(56789)
    assert p.user() == 'C:\\Users\\manuel'
    p = Path('Windows')
    p.seed(98765)
    assert p.user() == 'C:\\Users\\felicia'
    p = Path('Windows')
    p.seed(1111)
   

# Generated at 2022-06-14 00:21:07.814859
# Unit test for constructor of class Path
def test_Path():
    a = Path()
    assert isinstance(a, Path)

# Generated at 2022-06-14 00:21:18.753439
# Unit test for method user of class Path
def test_Path_user():
    """ Unit test for method user of class Path """
    from mimesis.enums import Locale
    from mimesis.providers.path import Path

    # Default locale is 'en' => user: 'oretha'
    path0 = Path()
    user0 = path0.user()

    # es locale: => user: 'janita'
    path1 = Path(locale=Locale.ES)
    user1 = path1.user()

    # ru locale: => user: 'Лев'
    path2 = Path(locale=Locale.RU)
    user2 = path2.user()

    assert type(user0) is str
    assert type(user1) is str
    assert type(user2) is str

    assert user0 == 'oretha'
    assert user1 == 'janita'


# Generated at 2022-06-14 00:21:22.226895
# Unit test for constructor of class Path
def test_Path():
    print('Test for the constructor  of class Path')
    path = Path(platform='win32')
    print(path)
    path = Path(platform='win64')
    print(path)
    path = Path(platform='linux')
    print(path)
    path = Path(platform='darwin')
    print(path)


# Generated at 2022-06-14 00:21:24.201953
# Unit test for method user of class Path
def test_Path_user():
    p = Path()
    user = p.user()
    print(user)


# Generated at 2022-06-14 00:21:26.863350
# Unit test for constructor of class Path
def test_Path():
    path = Path()
    assert path._pathlib_home
