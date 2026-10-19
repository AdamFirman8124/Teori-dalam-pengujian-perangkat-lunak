

# Generated at 2022-06-14 00:20:41.582551
# Unit test for constructor of class Path
def test_Path():
    p = Path()
    print(p.root())
    print(p.home())
    print(p.user())
    print(p.users_folder())
    print(p.dev_dir())
    print(p.project_dir())


# Generated at 2022-06-14 00:20:42.600131
# Unit test for method user of class Path
def test_Path_user():
    assert Path().user() == '/home/taneka'

# Generated at 2022-06-14 00:20:44.810044
# Unit test for method user of class Path
def test_Path_user():
    p = Path('linux')
    result = p.user()
    assert result == '/home/blanca'


# Generated at 2022-06-14 00:20:55.066523
# Unit test for method user of class Path
def test_Path_user():
    from mimesis.enums import Platform

    provider = Path(platform=Platform.DARWIN)
    user = provider.user()
    assert len(user) > 13

    provider = Path(platform=Platform.LINUX)
    user = provider.user()
    assert len(user) > 13

    provider = Path(platform=Platform.WINDOWS)
    user = provider.user()
    assert len(user) > 12

    provider = Path(platform=Platform.WINDOWS_10)
    user = provider.user()
    assert len(user) > 12



# Generated at 2022-06-14 00:21:00.557230
# Unit test for constructor of class Path
def test_Path():
    path = Path('win64')
    print (path.root())
    print (path.home())
    print (path.user())
    print (path.users_folder())
    print (path.dev_dir())
    print (path.project_dir())
    return

# Generated at 2022-06-14 00:21:03.592078
# Unit test for method user of class Path
def test_Path_user():
    path = Path()
    path.user()
    print(path.user())


# Generated at 2022-06-14 00:21:14.298769
# Unit test for method user of class Path
def test_Path_user():
    """Test method user of class Path."""
    import os, inspect, mock
    import mimesis
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    path = os.path.dirname(os.path.abspath(filename))
    mock_value = '{}/../mimesis/data/users.json'.format(path)
    path_obj = mimesis.Path()
    with mock.patch('mimesis.Path.locales_manager._load') as mock_load:
        mock_load.return_value = mock_value
        res = path_obj.user()
        assert (res)

# Generated at 2022-06-14 00:21:17.562667
# Unit test for constructor of class Path
def test_Path():
    path = Path()
    assert path.platform == sys.platform

# Generated at 2022-06-14 00:21:19.504067
# Unit test for constructor of class Path
def test_Path():
    test_path = Path()
    assert test_path.platform == sys.platform

# Generated at 2022-06-14 00:21:24.924997
# Unit test for method user of class Path
def test_Path_user():
    path = Path()
    user = path.user()
    assert isinstance(user, str)