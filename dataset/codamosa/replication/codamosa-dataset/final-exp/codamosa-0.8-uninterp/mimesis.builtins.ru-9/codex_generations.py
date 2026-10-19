

# Generated at 2022-06-13 23:28:39.275580
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    import mimesis.enums as enums
    from mimesis.providers.rus import RussiaSpecProvider
    a = RussiaSpecProvider()
    b = RussiaSpecProvider()
    c = RussiaSpecProvider()
    n1 = a.snils()
    n2 = b.snils()
    n3 = c.snils()
    print('n1=' + n1)
    print('n2=' + n2)
    print('n3=' + n3)
    assert n1 != n2
    assert n1 != n3


# Generated at 2022-06-13 23:28:42.801578
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    # Generate snils
    seed = 0
    for i in range(1000):
        d = RussiaSpecProvider(seed)
        assert len(d.snils()) == 11
        seed = seed + 1


# Generated at 2022-06-13 23:28:45.577252
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rus = RussiaSpecProvider(seed=1)
    snils = rus.snils()

    assert snils == '23671506600'



# Generated at 2022-06-13 23:28:48.621726
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.builtins.types import RussiaSpecProvider
    assert len(RussiaSpecProvider.snils()) == 11
    assert RussiaSpecProvider.snils()[:3] == '419'


# Generated at 2022-06-13 23:28:51.712427
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rsp = RussiaSpecProvider()
    new_snils = rsp.snils()
    assert (len(new_snils) == 11)
    print("Test complete")

test_RussiaSpecProvider_snils()

# Generated at 2022-06-13 23:28:54.463125
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rus_snils = RussiaSpecProvider().snils()

    assert isinstance(rus_snils, str)
    assert rus_snils != None
    assert len(rus_snils) == 11

# Generated at 2022-06-13 23:28:57.795946
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test for the function snils of class RussiaSpecProvider."""
    obj = RussiaSpecProvider()
    for i in range(0, 20):
        assert len(obj.snils()) == 11,\
            "This function must return a string length of 11"
        assert obj.snils()[0] == '4',\
            "First number of snils must equal to 4"


# Generated at 2022-06-13 23:29:03.792238
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider
    
    Arguments:
        None

    Returns:
        None

    Raises:
        None
    
    test_RussiaSpecProvider_snils()
    """

    # Create instance of class RussiaSpecProvider
    russia_spec_provider = RussiaSpecProvider()

    # Get SNILS from RussiaSpecProvider
    snils = russia_spec_provider.snils()

    # Get control sum for SNILS
    control_sum = int(snils[9:11])

    # Get the number of last digits of SNILS
    end = int(snils[-2:])

    # Get the number of all digits of SNILS without last two digits
    total = int(snils[:-2])
    
    # Split the number of all digits of SNILS without last two digits

# Generated at 2022-06-13 23:29:06.598650
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.providers import RussiaSpecProvider
    RSP = RussiaSpecProvider()
    assert RSP.snils() == "63988347600"


# Generated at 2022-06-13 23:29:11.501954
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    sp = RussiaSpecProvider()
    snils = sp.snils()
    assert snils == (sp.snils())
    assert snils != (sp.snils())
    print("snils:", snils)


# Generated at 2022-06-13 23:29:30.125563
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    # create instance of RussiaSpecProvider
    rusProvider = RussiaSpecProvider()
    # print result of method snils
    print(rusProvider.snils())


# Generated at 2022-06-13 23:29:43.989757
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    #
    # Tests for examples from site
    # http://kodaktor.ru/g/snils
    #
    for i in range(0, 100):
        snils = RussiaSpecProvider().snils()
        if snils in [
            '41917492600',
            '34312056935',
            '16109293058',
            '50497924622',
            '50497924622',
            '24735405896',
        ]:
            break
    assert(snils in [
        '41917492600',
        '34312056935',
        '16109293058',
        '50497924622',
        '50497924622',
        '24735405896',
    ])

# Unit tests for method inn of class RussiaSpecProvider


# Generated at 2022-06-13 23:29:51.409863
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.builtins import RussiaSpecProvider
    from mimesis.enums import Gender
    from mimesis.schema import Field

    generator = RussiaSpecProvider()
    schema = Field('snils')

    assert generator.snils() == '11598661275'
    assert generator.snils() == '10282599745'
    assert generator.snils() == '03740504032'
    assert generator.snils() == '00869284375'


# Generated at 2022-06-13 23:29:58.316065
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    k = 1
    counter = 0
    for _ in range(k):
        r = RussiaSpecProvider()
        snils = r.snils()
        print(snils)
        snils = ''.join([x for x in snils if x != ' '])
        print(snils)
        if int(snils[9]) > 4:
            counter += 1
    print(counter)
    if counter == k:
        print('OK')
    else:
        print('FAIL')


# Generated at 2022-06-13 23:30:00.461104
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    snils = provider.snils()
    assert len(snils)==11
    assert snils.isdigit() 


# Generated at 2022-06-13 23:30:05.569678
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test method snils of class RussiaSpecProvider"""
    import re
    provider = RussiaSpecProvider()
    snils = provider.snils()
    assert len(snils) == 11
    assert re.match('\d{11}', snils) is not None

# Generated at 2022-06-13 23:30:12.644460
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    k = 0
    for i in range(0, 100):
        x = RussiaSpecProvider().snils()
        print(x)
        x = list(x)
        s = 0
        for j in range(9):
            s += int(x[j]) * (9 - j)
        # print(s)
        if s % 101 == int(x[9] + x[10]):
            k += 1
    assert k == 100

test_RussiaSpecProvider_snils()


# Generated at 2022-06-13 23:30:16.039555
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider."""
    russia_spec_provider = RussiaSpecProvider()
    print(russia_spec_provider.snils())


# Generated at 2022-06-13 23:30:27.516610
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider."""
    from mimesis.providers import RussiaSpecProvider as rsp
    from mimesis.enums import Gender
    from mimesis.providers._person import Person

    p = Person('ru')
    st = rsp()
    assert st.snils() == '41917492600'
    assert st.snils() == '41917492600'
    assert st.snils() == '41917492600'
    assert st.snils() == '41917492600'
    assert st.snils() == '41917492600'
    assert st.snils() == '41917492600'
    assert st.snils() == '41917492600'
    assert st.snils() == '41917492600'


# Generated at 2022-06-13 23:30:30.236422
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    prov1 = RussiaSpecProvider()
    prov2 = RussiaSpecProvider()
    prov3 = RussiaSpecProvider()

    assert prov1.snils() != prov2.snils() != prov3.snils()


# Generated at 2022-06-13 23:31:06.056538
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider"""
    russia_spec_provider = RussiaSpecProvider()
    assert len(russia_spec_provider.snils()) == 11

# Generated at 2022-06-13 23:31:11.267009
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for the method snils of the class RussiaSpecProvider."""
    provider = RussiaSpecProvider()
    snils1 = provider.snils()
    snils2 = provider.snils()
    assert snils1 != snils2, 'snils is not random.'


# Generated at 2022-06-13 23:31:15.182775
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider"""
    obj = RussiaSpecProvider(seed=1)
    snils = obj.snils()
    assert snils == '41917492600'


# Generated at 2022-06-13 23:31:23.420357
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person
    from mimesis.providers.ru import RussiaSpecProvider

    test_object = RussiaSpecProvider()
    expected_result = '41917492600'
    actually_result = test_object.snils()

    print('------')
    print('Method: "snils"')
    print('Expected result: ', expected_result)
    print('Actually result: ', actually_result)
    print('------')

    assert expected_result == actually_result


# Generated at 2022-06-13 23:31:31.123969
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider"""
    class RussiaMockupSpecProvider(RussiaSpecProvider):
        """Mockup class for testing RussiaSpecProvider"""

        def __init__(self):
            """Initialize attributes."""
            super().__init__(seed=6)

    provider = RussiaMockupSpecProvider()
    answer = provider.snils()
    assert(answer == '41917492600')

# Generated at 2022-06-13 23:31:35.268264
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test snils, it's fake numbers."""
    provider = RussiaSpecProvider('random_seed')
    # snils = '41917492600'
    snils = provider.snils()
    assert snils == '41917492600'

# Generated at 2022-06-13 23:31:40.435790
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rus = RussiaSpecProvider(seed=518)
    rus_list = [rus.snils() for i in range(5000)]
    assert rus_list.count('41917492600') == 1

# Generated at 2022-06-13 23:31:45.726397
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    import pytest
    from mimesis.enums import Gender
    from mimesis.providers.russia import RussiaSpecProvider

    r = RussiaSpecProvider()
    for i in range(100):
        assert not r.snils() == r.snils()
    assert len(r.snils()) == 11
    assert r.snils().startswith(' ') is False
    assert r.snils().endswith(' ') is False
    assert r.snils().startswith('00') is False


# Generated at 2022-06-13 23:31:54.986770
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test method RussiaSpecProvider.snils()

    Test cases:
        1. 41917492600
        2. 14800738796
        3. 08018528190
    """
    # RussiaSpecProvider instance
    rsp = RussiaSpecProvider(seed=42)


# Generated at 2022-06-13 23:31:58.745780
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider."""
    russian = RussiaSpecProvider()
    snils = russian.snils()
    assert isinstance(snils, str)


# Generated at 2022-06-13 23:33:22.310564
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider."""
    russian = RussiaSpecProvider()
    res = russian.snils()

    assert len(res) == 11
    assert isinstance(res, str)

# Generated at 2022-06-13 23:33:25.027502
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rus = RussiaSpecProvider()
    assert str(type(rus.snils())) == "<class 'str'>"

# Generated at 2022-06-13 23:33:27.882199
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    p = RussiaSpecProvider()
    assert p.snils() == '41917492600'

# Generated at 2022-06-13 23:33:42.484694
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from . import get_locale
    from .address import test_AddressProvider_address_general
    from .calendar import test_CalendarProvider_full_date
    from .date import test_DateProvider_date_formats
    from .internet import test_InternetProvider_ip_address, test_InternetProvider_mac_address
    from .person import test_PersonProvider_full_name

    test_AddressProvider_address_general(get_locale('ru'))
    test_CalendarProvider_full_date(get_locale('ru'))
    test_DateProvider_date_formats(get_locale('ru'))
    test_InternetProvider_ip_address(get_locale('ru'))
    test_InternetProvider_mac_address(get_locale('ru'))

# Generated at 2022-06-13 23:33:47.978449
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    provider.seed(3)
    assert provider.snils() == '41917492600'
    assert provider.snils() == '41917492600'
    assert provider.snils() == '41917492600'


# Generated at 2022-06-13 23:33:50.329533
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    a = RussiaSpecProvider()
    assert a.snils() == '41917492600'



# Generated at 2022-06-13 23:33:52.084238
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    a=RussiaSpecProvider()
    print(a.snils())


# Generated at 2022-06-13 23:33:53.287124
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    RussiaSpecProvider().snils()



# Generated at 2022-06-13 23:33:58.722473
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.providers.russia import RussiaSpecProvider
    russiaspecs = RussiaSpecProvider()
    for i in range(0, 100):
        print(russiaspecs.snils())


# Generated at 2022-06-13 23:34:00.679707
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    ru = RussiaSpecProvider(seed=1)
    rus = ru.snils()
    assert isinstance(rus, str)
    assert len(rus) == 11
    assert rus == '41917492600'

# Generated at 2022-06-13 23:37:47.758084
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test method snils of class RussiaSpecProvider."""
    s = RussiaSpecProvider()
    snils = s.snils()
    code = snils[:-2]
    numbers = []
    control_codes = []
    for i in range(0, 9):
        numbers.append(int(code[i]))
    for i in range(9, 0, -1):
        control_codes.append(numbers[9 - i] * i)
    control_code = sum(control_codes)
    assert int(snils[-2:]) == control_code % 101

# Generated at 2022-06-13 23:37:50.852371
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.providers.russia_provider import RussiaSpecProvider
    rus = RussiaSpecProvider()
    print(rus.snils())


# Generated at 2022-06-13 23:37:55.481176
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    x = RussiaSpecProvider(seed=123)
    assert x.snils() == '41917492600'


# Generated at 2022-06-13 23:38:03.984336
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rssp = RussiaSpecProvider()
    snils = rssp.snils()
    assert snils[-3] == snils[-2] == snils[-1] == '0'
    assert len(snils) == 11


# Generated at 2022-06-13 23:38:05.462801
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    import mimesis.enums
    a = RussiaSpecProvider()
    assert len(a.snils()) == 11


# Generated at 2022-06-13 23:38:11.446260
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.builtins import RussiaSpecProvider

    rus = RussiaSpecProvider()
    snils = rus.snils()
    # test snils < 100
    assert 1 <= int(snils) < 100
    # test snils == 100
    rus = RussiaSpecProvider()
    assert int(rus.snils()) == 100
    # test snils > 100
    rus = RussiaSpecProvider()
    assert 101 <= int(rus.snils()) < 1000

# Generated at 2022-06-13 23:38:19.376072
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test snils of the RussiaSpecProvider class.

    Test the uniqueness of 99 snils.

    Test code taken from https://pypi.org/project/python-snils/

    .. versionadded:: 0.2.0
    """
    snils_list = []
    russia = RussiaSpecProvider()

    for _ in range(0, 99):
        snils_list.append(russia.snils())

    for snils in snils_list:
        assert len(snils) == 11
        assert snils.isdigit()

    assert len(snils_list) == len(set(snils_list))
    print('Successful test of the snils method')
