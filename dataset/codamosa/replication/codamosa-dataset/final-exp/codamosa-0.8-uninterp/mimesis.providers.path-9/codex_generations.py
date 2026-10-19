

# Generated at 2022-06-14 00:20:41.968263
# Unit test for method user of class Path
def test_Path_user():
    path = Path()
    user = path.user()
    assert user == '/home/oretha'

# Generated at 2022-06-14 00:20:43.455511
# Unit test for method user of class Path
def test_Path_user():
    p = Path(platform = 'win32')
    print(p.user())


# Generated at 2022-06-14 00:20:46.000118
# Unit test for method user of class Path
def test_Path_user():
	path = Path()
	assert all([isinstance(path.user(),str) is True])


# Generated at 2022-06-14 00:20:48.426692
# Unit test for method user of class Path
def test_Path_user():
    Path.seed()
    assert Path.user() == '/home/anastasia'


# Generated at 2022-06-14 00:20:50.261230
# Unit test for method user of class Path
def test_Path_user():
    provider = Path()
    user = provider.user()
    print(user, type(user))


# Generated at 2022-06-14 00:20:53.207824
# Unit test for method user of class Path
def test_Path_user():
    user = Path().user()
    assert (user == '/home/oretha') or (user == 'C:\\Users\\oretha')


# Generated at 2022-06-14 00:20:55.321923
# Unit test for method user of class Path
def test_Path_user():
    # expected result
    assert Path().user() == '/home/jameel'


# Generated at 2022-06-14 00:21:00.335908
# Unit test for method user of class Path
def test_Path_user():
    """Test for method user of class Path."""
    # Initialize object
    path = Path()
    assert len(path.user()) > 0
    path.__init__(platform='win32')
    assert len(path.user()) > 0

# Generated at 2022-06-14 00:21:04.989672
# Unit test for method user of class Path
def test_Path_user():
    _path = Path()
    result = _path.user()
    assert result == '/home/oretha'


# Generated at 2022-06-14 00:21:09.465722
# Unit test for method user of class Path
def test_Path_user():
    test_path_provider = Path()
    try:
        test_path_provider.user()
    except Exception:
        test_path_provider.home() # raises if this is not a path