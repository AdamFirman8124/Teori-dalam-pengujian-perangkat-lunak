

# Generated at 2022-06-14 00:20:40.837049
# Unit test for method user of class Path
def test_Path_user():
    path_ = Path('win32')
    assert path_.user() == r'C:\Users\tamara'


# Generated at 2022-06-14 00:20:42.251513
# Unit test for method user of class Path
def test_Path_user():
    p = Path()
    assert len(p.user())


# Generated at 2022-06-14 00:20:46.274577
# Unit test for method user of class Path
def test_Path_user():
    path = Path()
    user = path.user()

    assert isinstance(user, str)
    assert '/' in user
    assert not user.endswith('/')
    assert not user.endswith('\\')
    assert user.strip('/').strip('\\') in USERNAMES

# Generated at 2022-06-14 00:20:58.842478
# Unit test for method user of class Path

# Generated at 2022-06-14 00:21:01.104488
# Unit test for method user of class Path
def test_Path_user():
    path = Path()
    for _ in range(20):
        assert '/home/' in path.user()



# Generated at 2022-06-14 00:21:08.452234
# Unit test for method user of class Path
def test_Path_user():
    from collections import Counter

    TEST_NUM = 10000
    test_set = set()

    for i in range(TEST_NUM):
        path = Path()
        assert path.user() not in test_set
        test_set.add(path.user())

        with open('path_user_test.txt', 'w') as f:
            for data in test_set:
                f.write(data + '\n')

    print('All paths are unique.')


# Generated at 2022-06-14 00:21:09.517657
# Unit test for method user of class Path
def test_Path_user():
    assert Path().user() != None


# Generated at 2022-06-14 00:21:11.440852
# Unit test for method user of class Path
def test_Path_user():
    path = Path()
    assert path.user() == '/home/taneka'


# Generated at 2022-06-14 00:21:15.444534
# Unit test for method user of class Path
def test_Path_user():
    path = Path()
    user = path.user()
    flag = False
    for i in USERNAMES:
        if i in user and PLATFORMS[path.platform]['home'] in user:
            flag = True
    return flag


# Generated at 2022-06-14 00:21:18.511321
# Unit test for method user of class Path
def test_Path_user():
    platform = 'linux'
    print("Path.user(): " + Path(platform).user())
    assert Path(platform).user() == '/home/isidro'