

# Generated at 2022-06-13 23:28:37.520049
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider."""
    provider = RussiaSpecProvider()
    snils = provider.snils()
    assert len(snils) == 11
    assert snils[0] != 0


# Generated at 2022-06-13 23:28:48.792716
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    import pandas as pd

    r = RussiaSpecProvider()
    result = []
    unlabeled_df = pd.DataFrame(columns=['snils'])

    for i in range(0, 10000):
        snils = r.snils()
        result.append(snils)
        unlabeled_df.loc[i] = [snils]

    from sklearn.model_selection import train_test_split

    unlabeled_train_df, unlabeled_test_df = train_test_split(unlabeled_df, test_size=0.33, random_state=42)

    # визуализация
    import matplotlib.pyplot as plt
    fig = plt.figure()
    unlabeled_train_df.sn

# Generated at 2022-06-13 23:28:52.609054
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    assert provider.snils() == provider.snils()
    assert len(provider.snils()) == 11
    assert provider.snils()[3:] != '0000'
    assert provider.snils() != provider.snils()


# Generated at 2022-06-13 23:28:54.337953
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    assert(len(set([RussiaSpecProvider().snils() for i in range(1000)])) == 1000)

# Generated at 2022-06-13 23:28:56.487898
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rus = RussiaSpecProvider()
    s = rus.snils()
    assert len(s) == 11
    assert int(s) < 10000000000


# Generated at 2022-06-13 23:28:58.239316
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider."""
    o = RussiaSpecProvider()

    assert o.snils() is str

# Generated at 2022-06-13 23:29:03.193698
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    print(provider.snils())
    assert provider.snils()
print("\ntest_RussiaSpecProvider_snils() for RussiaSpecProvider is passed")


# Generated at 2022-06-13 23:29:11.780260
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    '''
    This test checks the snils method in class RussiaSpecProvider.
    '''
    from mimesis.providers.russia import RussiaSpecProvider
    import pytest
    from mimesis.enums import Gender
    russia = RussiaSpecProvider()
    snils = russia.snils()
    gender = [Gender.MALE, Gender.FEMALE]
    good_value = ['41917492600', '41917492600', '41917492600']
    assert snils in good_value


# Generated at 2022-06-13 23:29:25.659468
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider."""
    def test_snils(snils):
        """Unit test for method snils of class RussiaSpecProvider."""
        numbers = list(
            int(x) for x in snils[:-2]
        )  # Отрезаем двузначную контрольную сумму

        control_codes = []
        for i in range(9, 0, -1):
            control_codes.append(numbers[9 - i] * i)

        control_code = sum(control_codes)

        if control_code in (100, 101):
            return snils[-2:] == '00'

        if control_code < 100:
            return

# Generated at 2022-06-13 23:29:28.765157
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    x = RussiaSpecProvider()
    y = x.snils()
    print("x=", x)
    print("y=", y)


# Generated at 2022-06-13 23:29:50.316482
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider."""

    provider = RussiaSpecProvider()
    for _ in range(0, 1000):
        assert (len(provider.snils()) == 11)



# Generated at 2022-06-13 23:29:52.492745
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis import RussiaSpecProvider

    provider = RussiaSpecProvider()
    assert len(provider.snils()) == 11



# Generated at 2022-06-13 23:30:01.040232
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test for method snils of class RussiaSpecProvider"""
    dictionary = {}

    def test_for_seed(seed):
        """Create RussiaSpecProvider and test snils method with seed"""
        rs = RussiaSpecProvider()
        rs.random.seed(seed)
        snils = rs.snils()
        if snils in dictionary:
            return False
        else:
            dictionary[snils] = True
        return True

    ok = True
    global ok # pylint: disable=global-statement
    for _ in range(1000): # Create 1000 objects and test snils method
        ok = ok and test_for_seed(rs.random.randint(0, 100000))
    return ok


# Generated at 2022-06-13 23:30:08.167486
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.providers.general import RussiaSpecProvider
    tester = RussiaSpecProvider()
    snils = tester.snils()
    formatted_snils = '{} {} {} {}'.format(snils[:3],
                                           snils[3:6],
                                           snils[6:9],
                                           snils[9:])
    print(formatted_snils)

# Generated at 2022-06-13 23:30:16.707766
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.builtins.base import BaseSpecProvider
    from mimesis.enums import Gender

    rsp = RussiaSpecProvider(seed = 'test')
    spec_provider = BaseSpecProvider(seed = 'test')
    gender = Gender.FEMALE

    # Test for method snils of class RussiaSpecProvider
    assert(rsp.snils() == '41917492600')
    assert(rsp.patronymic(gender) == 'Ивановна')
    assert(rsp.patronymic(gender) == 'Петровна')
    assert(rsp.patronymic(gender) == 'Владимировна')

# Generated at 2022-06-13 23:30:27.902386
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    control_sum = 0
    control_codes = []
    numbers = []
    for i in range(0, 9):
        numbers.append(provider.random.randint(0, 9))

    for i in range(9, 0, -1):
        control_codes.append(numbers[9 - i] * i)

    control_sum_1 = sum(control_codes)
    snils = ''.join(str(number) for number in numbers)
    if control_sum_1 in (100, 101):
        snils = snils + '00'

    if control_sum_1 < 100:
        snils = snils + str(control_sum_1)

    if control_sum_1 > 101:
        control_sum_1 = control_sum_1 % 101
       

# Generated at 2022-06-13 23:30:29.031941
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    assert RussiaSpecProvider().snils() == '41917492600'


# Generated at 2022-06-13 23:30:38.425257
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """
    Тестовый случай для проверки того, что метод snils класса RussiaSpecProvider
    не выдает СНИЛС, начинающийся с цифры 0
    """

    r = RussiaSpecProvider()
    res = r.snils()

    assert res[0] != '0'

# Generated at 2022-06-13 23:30:41.864409
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    r = RussiaSpecProvider()
    assert r.snils() == "41917492600"
    return "ok"


# Generated at 2022-06-13 23:30:45.022140
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    ru = RussiaSpecProvider()
    ru.random.seed(4232432)
    snils = ru.snils()
    assert(snils == '41917492600')

# Generated at 2022-06-13 23:31:29.921825
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """
    Unit test for method snils of class RussiaSpecProvider
    """
    russiaSpecProvider = RussiaSpecProvider(seed=1)
    assert isinstance(russiaSpecProvider.snils(), str), "Returns wrong type"
    assert (len(russiaSpecProvider.snils()) == 11), "Returns wrong length"
    assert (russiaSpecProvider.snils() == '41917492600'), "Returns wrong value"



# Generated at 2022-06-13 23:31:32.125645
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():

    rs = RussiaSpecProvider()
    assert isinstance(rs.snils(), str)


# Generated at 2022-06-13 23:31:34.318336
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    ru_snils = RussiaSpecProvider()
    assert ru_snils.snils() == '41917492600'

# Generated at 2022-06-13 23:31:36.289366
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider."""
    russiaspp = RussiaSpecProvider()
    print(russiaspp.snils())



# Generated at 2022-06-13 23:31:41.280437
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test RussiaSpecProvider for snils."""
    bsp = RussiaSpecProvider()
    snils = bsp.snils()
    assert int(snils[-2:]) == bsp._test_sum(snils[:-2])


# Generated at 2022-06-13 23:31:43.344447
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider"""
    rs_p = RussiaSpecProvider()
    assert len(rs_p.snils()) == 11


# Generated at 2022-06-13 23:31:47.031344
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    r = RussiaSpecProvider()
    k = r.snils()
    print(k)
    assert len(k) == 11
    assert type(int(k)) is int

# Generated at 2022-06-13 23:31:49.298235
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """
    Unit test for method snils of class RuSpecProvider
    """
    from mimesis.providers.russia_provider import RussiaSpecProvider
    r = RussiaSpecProvider()
    result = r.snils()
    assert result in range(0, 10**11)


# Generated at 2022-06-13 23:31:51.491687
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    prov = RussiaSpecProvider()
    a = prov.snils()
    print(a)


# Generated at 2022-06-13 23:31:58.461031
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    __snils = provider.snils()

    # Test length of snils
    assert (len(__snils)) == 11

    # Test the first three characters of snils
    assert __snils[0:3].isdigit()

    # Test the last two characters of snils
    assert __snils[-2:].isdigit()



# Generated at 2022-06-13 23:33:26.713449
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """
    This method unit test __init__ method of class RussiaSpecProvider.
    """
    instance = RussiaSpecProvider()
    instance_two = RussiaSpecProvider()
    snils_one = instance.snils()
    snils_two = instance_two.snils()
    assert snils_one != snils_two

# Generated at 2022-06-13 23:33:29.317685
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider."""
    rsp = RussiaSpecProvider()
    s = rsp.snils()
    assert len(s) == 11, "SNILS must have 11 digits"


# Generated at 2022-06-13 23:33:39.634354
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """ Test snils method of class RussiaSpecProvider.

    :return:
    """
    import unittest
    import regex

    class TestRussiaSpecProvider(unittest.TestCase):
        """ Test snils method of class RussiaSpecProvider."""

        def test_snils(self):
            """ Test snils method of class RussiaSpecProvider."""

            rsp = RussiaSpecProvider()
            for i in range(0, 100):
                snils = rsp.snils()
                self.assertIsInstance(snils, str)
                self.assertEqual(len(snils), 11)
                self.assertTrue(regex.search('\d{11}', snils))

    unittest.main()

# Generated at 2022-06-13 23:33:41.684033
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    r = RussiaSpecProvider()
    assert r.snils() == '41917492600'

# Generated at 2022-06-13 23:33:54.477966
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider."""
    ru = RussiaSpecProvider()
    snils = ru.snils()
    assert snils[9] == str(int(snils[0] + snils[1] + snils[2] + snils[3] + snils[4] + snils[5] + snils[6] + snils[7] + snils[8]) % 101 % 100 // 10)
    assert snils[10] == str(int(snils[0] + snils[1] + snils[2] + snils[3] + snils[4] + snils[5] + snils[6] + snils[7] + snils[8]) % 101 % 100 % 10)


# Generated at 2022-06-13 23:34:01.229104
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """A unit test for method snils of class RussiaSpecProvider.

    :return: True if the test succeeds, otherwise False.
    :rtype: bool
    """
    snils = '111-222-333 33'
    provider = RussiaSpecProvider()
    result = provider.snils()
    if result == snils:
        return True
    return False

# Base unit test for a class RussiaSpecProvider

# Generated at 2022-06-13 23:34:02.767057
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    assert RussiaSpecProvider(seed=1).snils() == '51917492600'


# Generated at 2022-06-13 23:34:05.536214
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider(seed=10)
    snils = provider.snils()
    assert snils == "41917492600"

# Generated at 2022-06-13 23:34:17.320886
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.providers.identification import Identification
    from mimesis.enums import Gender
    from pymongo import MongoClient

    client = MongoClient('mongodb://192.168.2.153:27017')
    db = client.bot
    db_snils = db.snils

    rsp = Identification('ru')
    male_rsp = RussiaSpecProvider(seed=rsp.seed)
    female_rsp = RussiaSpecProvider(seed=rsp.seed)
    snils_list = []

    for _ in range(0, 1000):
        male_snils = male_rsp.snils()
        female_snils = female_rsp.snils()

        if male_snils not in snils_list:
            snils_list.append(male_snils)


# Generated at 2022-06-13 23:34:20.879868
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider."""
    russia_spec_provider = RussiaSpecProvider()
    snils = russia_spec_provider.snils()
    print(snils)
