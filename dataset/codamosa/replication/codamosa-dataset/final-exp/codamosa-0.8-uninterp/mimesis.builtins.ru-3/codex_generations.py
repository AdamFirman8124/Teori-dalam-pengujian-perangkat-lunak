

# Generated at 2022-06-13 23:28:39.685439
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    # Создать экземпляр класса
    rs = RussiaSpecProvider()
    # Запустить функцию snils()
    # Проверить, что вернулась строка
    assert isinstance(rs.snils(), str)
    # Проверить, что длина строки равна 11
    assert len(rs.snils()) == 11


# Generated at 2022-06-13 23:28:41.503032
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    snils = RussiaSpecProvider()
    print(snils.snils())



# Generated at 2022-06-13 23:28:45.101369
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    russia_provider = RussiaSpecProvider()
    print(russia_provider.snils())
    russia_provider.seed(1)
    print(russia_provider.snils())

# Generated at 2022-06-13 23:28:47.403710
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    assert len(provider.snils()) == 11
    assert provider.snils().isdigit()


# Generated at 2022-06-13 23:28:49.443473
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    instance = RussiaSpecProvider()
    result = instance.snils()
    assert result is not None
    assert type(result) is str



# Generated at 2022-06-13 23:28:51.808269
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    data = provider.snils()
    print(data)

test_RussiaSpecProvider_snils()


# Generated at 2022-06-13 23:28:54.548833
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    actual = RussiaSpecProvider.snils(RussiaSpecProvider)
    expected = 41917492600
    assert (type(int(actual)) == int)
    assert (int(actual) == expected)


# Generated at 2022-06-13 23:28:57.549201
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    # Check provider
    provider = RussiaSpecProvider()

    snils_list = list()
    # Generate 1000 snils
    for i in range(0, 1000):
        snils_list.append(provider.snils())

    snils_set = set(snils_list)

    # Check length of set of snils
    assert len(snils_set) == 1000
    print('Success!')



# Generated at 2022-06-13 23:28:58.953138
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    r = RussiaSpecProvider()
    assert r.snils() == '46306481800'


# Generated at 2022-06-13 23:29:01.983118
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    r = RussiaSpecProvider()
    assert r.snils() == '41917492600'

# Generated at 2022-06-13 23:29:30.698872
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from random import Random
    from mimesis.random import Fake
    from mimesis.providers.russia import RussiaSpecProvider

    fake = Fake('en')
    fake.add_provider(RussiaSpecProvider(Random(12)))

    result = fake.russia_provider.snils()

    import hashlib
    seed = str(hashlib.sha256(str(12).encode()).hexdigest())
    import mimesis.data
    import pickle

    pkl_file = mimesis.data.find(
        'providers/russia_provider.json',
        False
    )

    with open(pkl_file, 'rb') as pklfile:
        data = pickle.load(pklfile)

    def snils(seed):
        numbers = []
        control_codes

# Generated at 2022-06-13 23:29:33.812608
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider."""
    provider = RussiaSpecProvider()
    result = provider.snils()
    assert isinstance(result, str)
    assert len(result) == 11

# Generated at 2022-06-13 23:29:43.598359
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    ru = RussiaSpecProvider()
    snils = ru.snils()

    # List of valid snils

# Generated at 2022-06-13 23:29:46.249942
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    for _ in range(0, 1000):
        sp = RussiaSpecProvider()
        assert len(sp.snils()) == 11


# Generated at 2022-06-13 23:29:52.957965
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.enums import Gender
    from mimesis.schema import Field, Schema
    from mimesis.providers.person import Person

    person = Person('ru_RU')
    person.create_morning_snils()

    schema = Schema(fields=[
        Field('SNILS', provider=person, pattern='morning_snils')
    ])
    
    assert schema.create(iterations=5000)

# Generated at 2022-06-13 23:29:59.818010
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    result = [RussiaSpecProvider().snils() for i in range(1,11)]
    expected = [
        "23483098100",
        "65198164100",
        "96533259900",
        "39602813600",
        "09089332100",
        "89129357400",
        "67733033000",
        "06302608200",
        "38253397900",
        "96493154600",
    ]
    assert result == expected


# Generated at 2022-06-13 23:30:09.443711
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from re import match
    provider = RussiaSpecProvider(seed=9898981)
    snils = provider.snils()
    assert match('\d{3}-\d{3}-\d{3}', snils)
    provider = RussiaSpecProvider(seed=11111)
    snils = provider.snils()
    assert match('\d{3}-\d{3}-\d{3}', snils)
    provider = RussiaSpecProvider(seed=111111)
    snils = provider.snils()
    assert match('\d{3}-\d{3}-\d{3}', snils)
    provider = RussiaSpecProvider(seed=1111111)
    snils = provider.snils()

# Generated at 2022-06-13 23:30:11.464272
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rus = RussiaSpecProvider()
    assert rus.snils() in list(range(10000000000, 100000000000))

# Generated at 2022-06-13 23:30:15.070749
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    russian_provider = RussiaSpecProvider()
    assert russian_provider.snils() in ['41917492600', '64447044800']


# Generated at 2022-06-13 23:30:17.413364
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test RussiaSpecProvider.snils()"."""
    assert RussiaSpecProvider().snils() == "85712099900"

# Generated at 2022-06-13 23:30:52.404788
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test for method snils of class RussiaSpecProvider."""
    assert RussiaSpecProvider().snils() == '41917492600'

# Generated at 2022-06-13 23:30:55.623489
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    tmp = RussiaSpecProvider()
    with open('ru_provider/test_snils.txt', 'w') as f:
        for i in range(1000000):
            f.write(tmp.snils() + '\n')
    f.close()

# Generated at 2022-06-13 23:31:01.398815
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """
    Test snils of class RussiaSpecProvider.

    :return:
    """
    import unittest

    class TestRussiaSpecProvider(unittest.TestCase):
        def setUp(self):
            self.provider = RussiaSpecProvider(seed='библиотека')

        def test_RussiaSpecProvider_snils(self):
            self.assertEqual(self.provider.snils(), '41917492600')

        def tearDown(self) -> None:
            pass

    unittest.main()

# Generated at 2022-06-13 23:31:02.684851
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    r = RussiaSpecProvider(seed=42)
    s = '41917492600'
    assert r.snils() == s

# Generated at 2022-06-13 23:31:04.249588
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    assert RussiaSpecProvider().snils() == '72595069600'


# Generated at 2022-06-13 23:31:06.141309
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    snils = RussiaSpecProvider().snils()
    assert snils.__class__ == str
    assert len(snils) == 11


# Generated at 2022-06-13 23:31:09.396063
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    assert len(provider.snils()) == 11
    # Check, if the function works correctly
    assert provider.snils() == '41917492600'


# Generated at 2022-06-13 23:31:12.194395
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    snils = provider.snils()
    print(snils)

# Generated at 2022-06-13 23:31:14.996076
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test method snils of class RussiaSpecProvider.

    :see: test/test_russia_spec_provider.py
    """
    pass

# Generated at 2022-06-13 23:31:21.549010
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider."""
    result_list=[]
    for x in range(10):
        rus = RussiaSpecProvider()
        result=rus.snils()
        result_list.append(result)
    print(result_list)
    assert len(result_list)==10


# Generated at 2022-06-13 23:32:32.589076
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider(None)
    assert provider.snils() in ['84717683778', '94462973289']



# Generated at 2022-06-13 23:32:33.942131
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    b = RussiaSpecProvider()
    assert b.snils() == '29424646338'

# Generated at 2022-06-13 23:32:45.972828
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from os import system
    from sys import argv
    from time import time
    from time import sleep
    test_snils = []
    test_total = []
    test_status = []
    a = 0
    b = 0
    c = 0
    start = time()
    end = time()
    error = ''
    if len(argv) != 2:
        error = 'Usage: python3 -m mimesis.providers.russia_provider.py [total]'
        print(error)
    else:
        # Set parameters
        test_total = int(argv[1])
        test = RussiaSpecProvider()
        # Run the test
        while b <= test_total:
            b += 1
            test_snils.append(test.snils())

# Generated at 2022-06-13 23:32:48.324689
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    import tests.fixtures.ru_spec_provider_fixtures as fixtures
    p = RussiaSpecProvider()

    snils = p.snils()
    assert snils in fixtures.snilses

# Generated at 2022-06-13 23:32:49.014562
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    pass

# Generated at 2022-06-13 23:32:50.329069
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    assert RussiaSpecProvider().snils() == '41917492600'


# Generated at 2022-06-13 23:32:54.621880
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider."""
    snils1 = RussiaSpecProvider().snils()
    snils2 = RussiaSpecProvider().snils()
    assert snils1 != snils2

# Generated at 2022-06-13 23:32:57.987442
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rsp = RussiaSpecProvider()
    print(rsp.snils())

# Generated at 2022-06-13 23:33:01.138706
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    assert len(RussiaSpecProvider().snils()) == 11
    assert RussiaSpecProvider().snils()[-2:] == '00'

# Generated at 2022-06-13 23:33:04.523895
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rsp = RussiaSpecProvider(seed=511387947)
    result = rsp.snils()
    assert result == '41917492600'