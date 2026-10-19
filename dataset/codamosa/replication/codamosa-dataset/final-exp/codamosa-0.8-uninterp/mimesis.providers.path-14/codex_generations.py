

# Generated at 2022-06-14 00:20:41.902134
# Unit test for method user of class Path
def test_Path_user():
    path = Path()
    assert '/home/oretha' == path.user()


# Generated at 2022-06-14 00:20:43.268133
# Unit test for method user of class Path
def test_Path_user():
    path = Path()
    user = path.user()
    assert isinstance(user, str)


# Generated at 2022-06-14 00:20:56.458775
# Unit test for constructor of class Path
def test_Path():
    path = Path()
    print(path.root())
    print(path.home())
    print(path.user())
    print(path.users_folder())
    print(path.dev_dir())
    print(path.project_dir())
    print(path.__dict__)
    print(path.__class__.__doc__)
    print(path.__class__.__name__)
    print(path.__class__.Meta.name)
    print(path.__class__.__init__.__doc__)
    print(path.__class__.__init__.__annotations__)
    print(path.__class__.root.__doc__)
    print(path.__class__.root.__annotations__)
    print(path.__class__.home.__doc__)
   

# Generated at 2022-06-14 00:20:59.816407
# Unit test for constructor of class Path
def test_Path():
    """Unit test for constructor of class Path."""
    path = Path()
    assert path.platform == sys.platform
    assert path._pathlib_home != ''

# Generated at 2022-06-14 00:21:03.094352
# Unit test for constructor of class Path
def test_Path():
    P = Path()
    assert P.root() == '/'


# Generated at 2022-06-14 00:21:04.286853
# Unit test for constructor of class Path
def test_Path():
    p = Path()
    assert p is not None


# Generated at 2022-06-14 00:21:07.702323
# Unit test for method user of class Path
def test_Path_user():
    s = Path().user()
    assert type(s) == str


# Generated at 2022-06-14 00:21:10.052066
# Unit test for method user of class Path
def test_Path_user():
    path = Path('linux')
    result = path.user()
    assert result is not None
    assert isinstance(result, str)


# Generated at 2022-06-14 00:21:13.310944
# Unit test for method user of class Path
def test_Path_user():
    print("test_Path_user(): Start test method user of class Path")
    path_obj = Path()
    for _ in range(100):
        print(path_obj.user())


# Generated at 2022-06-14 00:21:20.839969
# Unit test for constructor of class Path
def test_Path():
    """Test method of class Path."""
    platform = 'win32'
    path = Path(platform)
    assert path.platform == platform
    assert path._pathlib_home.as_posix() == PLATFORMS[platform]['home']
    assert path.home() == PLATFORMS[platform]['home']
