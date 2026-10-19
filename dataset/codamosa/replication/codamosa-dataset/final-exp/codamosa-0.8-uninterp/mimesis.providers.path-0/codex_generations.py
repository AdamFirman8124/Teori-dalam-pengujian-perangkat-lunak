

# Generated at 2022-06-14 00:20:43.024990
# Unit test for method user of class Path
def test_Path_user():
    """Test generate a random user."""

    path = Path()
    path.random.seed(0)

    assert path.user() == '/home/tucker'



# Generated at 2022-06-14 00:20:44.898283
# Unit test for method user of class Path
def test_Path_user():
    p=Path("linux")
    print(p.user())

# Generated at 2022-06-14 00:20:47.404827
# Unit test for method user of class Path
def test_Path_user():
    print(Path().user())


# Generated at 2022-06-14 00:20:53.392783
# Unit test for method user of class Path
def test_Path_user():
    p = Path(platform="win32")
    result = p.user()
    expected_result = "/Users/oretha"
    assert result == expected_result
    # Test
    p = Path(platform="linux")
    result = p.user()
    expected_result = "/home/oretha"
    assert result == expected_result


# Generated at 2022-06-14 00:20:57.363545
# Unit test for method user of class Path
def test_Path_user():
    """Test method user of class Path."""
    a = Path('linux').user()
    assert a == '/home/bao', a

# Generated at 2022-06-14 00:20:59.968844
# Unit test for method user of class Path
def test_Path_user():
    path = Path()
    result = path.user()
    print(result)


# Generated at 2022-06-14 00:21:04.009356
# Unit test for method user of class Path
def test_Path_user():
    x = Path()
    x.user()

# Generated at 2022-06-14 00:21:08.883576
# Unit test for method user of class Path
def test_Path_user():
    """Unit test for method user of class Path."""
    path = Path()
    result = path.user()
    assert result == '/home/jeanett'


# Generated at 2022-06-14 00:21:20.751154
# Unit test for method user of class Path
def test_Path_user():
    from mimesis.exceptions import NonEnumerableError
    from mimesis.enums import SpecialChar
    from mimesis.enums import Platform
    from mimesis.providers.path import Path
    from mimesis.enums import CardinalDirection
    from mimesis.providers.localization import Localization
    # Создаем объект для генерации чисел от 0 до 1000
    number = Localization(seed=12345)
    symbol = SpecialChar(seed=12345)

    # Пробуем изменить свойство объекта

# Generated at 2022-06-14 00:21:25.158333
# Unit test for method user of class Path
def test_Path_user():
    path = Path('linux')
    a = path.user()
    print(a)
    assert a == '/home/oretha'
