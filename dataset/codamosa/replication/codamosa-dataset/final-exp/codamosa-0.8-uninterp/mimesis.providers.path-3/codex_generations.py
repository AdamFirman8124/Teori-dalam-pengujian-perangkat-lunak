

# Generated at 2022-06-14 00:20:36.411112
# Unit test for constructor of class Path
def test_Path():
    p = Path()
    root_dir = p.root()
    assert root_dir == '/'


# Generated at 2022-06-14 00:20:37.932354
# Unit test for method user of class Path
def test_Path_user():
    p = Path()
    assert p.user() == '\\Users\\stella'

# Generated at 2022-06-14 00:20:42.034755
# Unit test for constructor of class Path
def test_Path():
    path = Path()
    assert path is not None
    assert isinstance(path, Path)
    assert path.platform == sys.platform

# Generated at 2022-06-14 00:20:43.058302
# Unit test for constructor of class Path
def test_Path():
    path = Path()
    path.platform
    

# Generated at 2022-06-14 00:20:44.418667
# Unit test for constructor of class Path
def test_Path():
    path = Path()
    assert(path is not None)

# Generated at 2022-06-14 00:20:45.948804
# Unit test for constructor of class Path
def test_Path():
    print(isinstance(Path(), Path))


# Generated at 2022-06-14 00:20:49.385545
# Unit test for constructor of class Path
def test_Path():
    assert Path().platform == sys.platform
    assert Path().platform == 'linux'
    assert Path(platform='darwin').platform == 'darwin'


# Generated at 2022-06-14 00:20:50.828517
# Unit test for constructor of class Path
def test_Path():
    provider=Path()
    assert hasattr(provider,'platform')

# Generated at 2022-06-14 00:20:52.203387
# Unit test for constructor of class Path
def test_Path():
    path = Path()
    assert isinstance(path, BaseProvider)



# Generated at 2022-06-14 00:20:55.071276
# Unit test for method user of class Path
def test_Path_user():
    expected = '/home/manual'
    actual = Path().user()
    assert actual == expected