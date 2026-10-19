

# Generated at 2022-06-14 01:07:40.732354
# Unit test for function get_random_item
def test_get_random_item():
    from enum import Enum

    class Thing(Enum):
        ONE = 1
        TWO = 2
        THREE = 3

    for _ in range(10):
        item = get_random_item(Thing)
        assert isinstance(item, Thing)

# Generated at 2022-06-14 01:07:44.605811
# Unit test for function get_random_item
def test_get_random_item():
    from mimesis.enums import OperatingSystem, Gender
    assert isinstance(get_random_item(OperatingSystem), OperatingSystem)
    assert isinstance(get_random_item(Gender), Gender)



# Generated at 2022-06-14 01:07:47.098107
# Unit test for function get_random_item
def test_get_random_item():
    assert len(get_random_item({"a"})) == 1


# Generated at 2022-06-14 01:07:50.849652
# Unit test for function get_random_item
def test_get_random_item():
    class Enum(object):
        x, y, z = 1, 2, 3
    assert get_random_item(Enum) in [Enum.x, Enum.y, Enum.z]



# Generated at 2022-06-14 01:07:53.514337
# Unit test for function get_random_item
def test_get_random_item():
    assert isinstance(get_random_item(random), Random)
    assert isinstance(get_random_item(random, random_module), Random)

# Generated at 2022-06-14 01:07:56.062827
# Unit test for function get_random_item
def test_get_random_item():
    from mimesis.numbers import NumberSystem
    assert isinstance(get_random_item(NumberSystem), NumberSystem)

# Generated at 2022-06-14 01:08:07.797084
# Unit test for function get_random_item
def test_get_random_item():
    """Test get_random_item() function."""
    global get_random_item
    import mimesis

    _rnd = mimesis.Random()
    item1 = get_random_item(enum=mimesis.Person.GENDER, rnd=_rnd)
    item2 = get_random_item(enum=mimesis.Location.REGION, rnd=_rnd)
    item3 = get_random_item(enum=mimesis.Business.COMPANY, rnd=_rnd)
    assert all([item1, item2, item3])

    item4 = get_random_item(mimesis.Person.GENDER)
    item5 = get_random_item(mimesis.Location.REGION)

# Generated at 2022-06-14 01:08:10.998258
# Unit test for function get_random_item
def test_get_random_item():
    assert random.choice(list([1,2,3])) == get_random_item(list([1,2,3]))

# Generated at 2022-06-14 01:08:13.326246
# Unit test for function get_random_item
def test_get_random_item():
    from mimesis.enums import Gender
    assert isinstance(get_random_item(Gender), Gender)

# Generated at 2022-06-14 01:08:15.738036
# Unit test for function get_random_item
def test_get_random_item():
    assert callable(get_random_item)
    assert callable(get_random_item)