

# Generated at 2022-06-13 23:28:34.393932
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    for _ in range(0, 100):
        assert len(RussiaSpecProvider().snils()) == 11


# Generated at 2022-06-13 23:28:36.564012
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test method snils of class RussiaSpecProvider."""
    provider = RussiaSpecProvider()
    assert len(provider.snils()) == 11


# Generated at 2022-06-13 23:28:40.479579
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    import datetime
    rp = RussiaSpecProvider()
    assert int(rp.snils()) >= 10019980000 and int(rp.snils())<= 99998999999


# Generated at 2022-06-13 23:28:45.257673
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test method snils of class RussiaSpecProvider.

    For all possible combinations of parameters
    and values sets.

    """
    # Create Fake object
    instance = RussiaSpecProvider()
    # Call method
    result = instance.snils()

    assert len(result) == 11
    assert result[-1] != '0'

# Generated at 2022-06-13 23:28:51.035682
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():

    # Unit test for method snils of class RussiaSpecProvider
    # Test 1
    assert RussiaSpecProvider().snils() == '41917492600'

    # Test 2
    assert RussiaSpecProvider().snils() == '41917492600'

    # Test 3
    assert RussiaSpecProvider().snils() == '41917492600'

    # Test 4
    assert RussiaSpecProvider().snils() == '41917492600'






# Generated at 2022-06-13 23:28:52.394584
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    assert RussiaSpecProvider().snils() == '41917492600'


# Generated at 2022-06-13 23:28:56.684818
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    x = RussiaSpecProvider()
    assert x.snils() in ('41917492600', '41917492611', '41917492622', '41917492633', '41917492644', '41917492655', '41917492666', '41917492677', '41917492688', '41917492699')


# Generated at 2022-06-13 23:29:00.680786
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    snils = provider.snils()
    print(snils)
    assert len(snils) == 11


# Generated at 2022-06-13 23:29:05.670428
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """This method is testing snils method of class RussiaSpecProvider."""
    provider = RussiaSpecProvider()
    temp_number = provider.snils()
    assert len(temp_number) == 11
    assert temp_number.isdigit()
    assert temp_number != '0' * 11
    assert temp_number != '7' * 11


# Generated at 2022-06-13 23:29:10.466140
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    seed = 1
    provider = RussiaSpecProvider(seed)
    for _ in range(0, 12):
        numb = RussiaSpecProvider(seed).snils()
        print(numb)
        assert len(numb) == 11


# Generated at 2022-06-13 23:29:22.640857
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    import sys
    import pytest
    from mimesis.providers.russia import Russia
    # Create unit tests for snils method of class RussiaSpecProvider
    # Success of exception
    # Success of type
    # Success of length
    # Success of regular match
    ru = Russia()
    ru.snils()

# Generated at 2022-06-13 23:29:25.070509
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rsp = RussiaSpecProvider()
    for _ in range(0, 10):
        print (rsp.snils())


# Generated at 2022-06-13 23:29:28.691901
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rus = RussiaSpecProvider()
    snil = rus.snils()
    assert snil == '41917492600', 'snil == "41917492600"'


# Generated at 2022-06-13 23:29:43.325917
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider
    :return True if test success else False
    :rtype: bool"""

    data = []
    rsp = RussiaSpecProvider()

    for _ in range(0, 100):
        snils = rsp.snils()
        num_sum = 0

        for number in snils[0:9]:
            num_sum += int(number)
            if num_sum > 101:
                num_sum %= 101
        if num_sum == 100:
            num_sum = 0
        if num_sum == 101:
            num_sum = 00

        if snils == '{}{}'.format(snils[0:9], num_sum):
            data.append(True)
        else:
            data.append(False)

    return all(data)

# Generated at 2022-06-13 23:29:47.671614
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test snils"""
    ru = RussiaSpecProvider()
    snils = ru.snils()
    rounded_snils = int(snils) % 100
    if not 0 <= rounded_snils <= 100:
        raise ValueError(f'snils {snils} not correct')

# Generated at 2022-06-13 23:29:56.097881
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.enums import Gender

    p = RussiaSpecProvider()
    doc_gender = Gender.MALE
    doc_surname = p.surname(gender=doc_gender)
    doc_name = p.name(gender=doc_gender)
    doc_patronymic = p.patronymic(gender=doc_gender)

    num = p.snils().split(".")

    print("snils: {0}.{1}.{2}.{3}".format(num[0], num[1], num[2], num[3]))

    pass

# Generated at 2022-06-13 23:29:58.958105
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    assert len(provider.snils()) == 11


# Generated at 2022-06-13 23:30:01.898409
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    s = RussiaSpecProvider().snils()
    assert len(s) == 11


# Generated at 2022-06-13 23:30:09.969052
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    # Проверка на адекватность
    prov = RussiaSpecProvider(seed=42)
    snilses = [prov.snils() for i in range(0, 20)]
    snilses = set(snilses)
    assert len(snilses) == len(set(snilses))

    # Проверка на корректный паттерн
    prov = RussiaSpecProvider()
    snils = prov.snils()
    assert len(snils) == 11
    prov = RussiaSpecProvider(seed=42)
    snils = prov.snils()
    assert snils == '41917492600'


# Generated at 2022-06-13 23:30:13.881100
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test for method snils of class RussiaSpecProvider."""
    rp = RussiaSpecProvider()
    for i in range(0, 10):
        snils = rp.snils()
        assert len(snils) == 11
        assert snils not in ('00000000000', '12345678900')


# Generated at 2022-06-13 23:30:26.738043
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    assert (provider.snils() in provider._data['snils'])


# Generated at 2022-06-13 23:30:28.764951
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    x = RussiaSpecProvider(seed=123456789)
    r = x.snils()
    assert r == '41917492600'


# Generated at 2022-06-13 23:30:30.668407
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    assert RussiaSpecProvider().snils() == '41918494300'


# Generated at 2022-06-13 23:30:32.251688
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    fr = RussiaSpecProvider()
    fr.snils()


# Generated at 2022-06-13 23:30:33.614606
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    assert 10662369707 == RussiaSpecProvider().snils()



# Generated at 2022-06-13 23:30:36.626633
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    r = RussiaSpecProvider()
    def func():
        return {r.snils() for i in range(10)}
    assert len(func()) == 10

# Generated at 2022-06-13 23:30:38.911215
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rsp = RussiaSpecProvider()
    s = rsp.snils()
    print(s)
    assert len(s)==11


# Generated at 2022-06-13 23:30:44.547274
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test for snils of class RussiaSpecProvider"""
    from mimesis.builtins import RussiaSpecProvider
    from mimesis.enums import Gender
    rus = RussiaSpecProvider()

    assert len(str(rus.snils())) == 11
    assert type(rus.snils()) == str


# Generated at 2022-06-13 23:30:46.164869
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rsp = RussiaSpecProvider(seed=42)

    assert rsp.snils() == '41917492600'

# Generated at 2022-06-13 23:30:49.188713
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider"""
    assert (russiaspecprovider.snils() != '')


# Generated at 2022-06-13 23:31:20.455358
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Check snils of class RussiaSpecProvider"""
    for i in range(1, 10):
        rsp = RussiaSpecProvider()
        snils = rsp.snils()

        first_part_sum = 0
        for i in range(9):
            first_part_sum += int(snils[i]) * (9 - i)
        control_snils = str(first_part_sum % 101)

        if control_snils == '100':
            control_snils = '00'
        elif control_snils == '101':
            control_snils = '01'
        else:
            control_snils = '{:02}'.format(first_part_sum % 101)

        assert snils[-2:] == control_snils

# Generated at 2022-06-13 23:31:26.177449
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.providers.russia_provider import RussiaSpecProvider
    from random import randint

    for i in range(10):
        snils = RussiaSpecProvider().snils()
        assert len(snils) == 11, "Количество цифр в снилс должно быть 11"
        assert snils[0] != 0, "Первая цифра в снилс должна быть отлична от 0"
        
        n = [int(j) for j in snils]
        assert sum(j*i for i,j in enumerate(n,1))

# Generated at 2022-06-13 23:31:33.557771
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():

    # Russian provider
    provider = RussiaSpecProvider()
    test_snils = provider.snils()
    # Russian numbers
    numbers = range(0, 10)
    # Len of snils
    len_ = 11
    # Check len of snils
    assert len(test_snils) == len_
    # Check snils for digit numbers
    for i in range(0, len_):
        assert int(test_snils[i]) in numbers

# Generated at 2022-06-13 23:31:36.610953
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    random_snils = RussiaSpecProvider().snils()
    assert random_snils


assert test_RussiaSpecProvider_snils()

# Generated at 2022-06-13 23:31:40.761389
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    r = RussiaSpecProvider()
    snils = r.snils()
    print('snils = ',snils)
    assert len(snils)==11


# Generated at 2022-06-13 23:31:42.057318
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    obj = RussiaSpecProvider()
    assert obj.snils()

# Generated at 2022-06-13 23:31:48.081912
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rsp = RussiaSpecProvider()
    result = rsp.snils()
    print("Проверка генерации СНИЛСа: " + result)
    assert len(result) == 11
    assert result.isdigit()


# Generated at 2022-06-13 23:31:50.302162
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.providers.person import Person
    person = Person('ru')
    assert person.snils() != person.snils()


# Generated at 2022-06-13 23:32:01.522997
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.enums import Gender

    provider = RussiaSpecProvider()
    assert provider.snils() == '47071588645'

    provider = RussiaSpecProvider('ru')
    assert provider.snils() == '23338881300'

    provider = RussiaSpecProvider(gender=Gender.MALE)
    assert provider.snils() == '78790113200'

    provider = RussiaSpecProvider('ru', gender=Gender.FEMALE)
    assert provider.snils() == '43327131100'

    provider = RussiaSpecProvider(gender=Gender.NOT_APPLICABLE)
    assert provider.snils() == '84226829800'

    provider = RussiaSpecProvider('ru', gender=Gender.NOT_APPLICABLE)
    assert provider.snils() == '64396009800'

# Unit test

# Generated at 2022-06-13 23:32:06.276613
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test method snils of class RussiaSpecProvider."""
    provider_ru = RussiaSpecProvider()
    provider_ru.seed(seed=1)
    snils = provider_ru.snils()
    assert snils == '41917492600'


# Generated at 2022-06-13 23:32:54.608947
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rsp = RussiaSpecProvider()
    s = rsp.snils()
    assert len(s) == 11 # snils have 11 digits
    assert s.isdigit() # and consist only digits

# Generated at 2022-06-13 23:32:57.906261
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    RussiaProvider = RussiaSpecProvider()
    print(RussiaProvider.snils())

# Generated at 2022-06-13 23:33:03.098441
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.providers import RussiaSpecProvider
    rsp = RussiaSpecProvider("en")
    snils_list = []

    for i in range(0, 100):
        snils_list.append(rsp.snils())

    assert snils_list[0] != snils_list[1]
    assert snils_list[2] != snils_list[1]


# Generated at 2022-06-13 23:33:05.431447
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    assert provider.snils() == '41917492600'

# Generated at 2022-06-13 23:33:19.903465
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.providers.russia import RussiaSpecProvider
    rs = RussiaSpecProvider()
    print(rs.snils())
    print(rs.snils())
    print(rs.snils())
    print(rs.snils())
    print(rs.snils())
    print(rs.snils())
    print(rs.snils())
    print(rs.snils())
    print(rs.snils())
    print(rs.snils())
    print(rs.snils())
    print(rs.snils())
    print(rs.snils())
    print(rs.snils())
    print(rs.snils())
    print(rs.snils())
    print(rs.snils())
    print(rs.snils())
    print(rs.snils())

# Generated at 2022-06-13 23:33:21.225822
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    assert RussiaSpecProvider().snils() == '41917492600'

# Generated at 2022-06-13 23:33:27.095371
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.providers.russia_provider import RussiaSpecProvider
    from mimesis.enums import Gender

    r = RussiaSpecProvider(seed=123456789)
    assert r.snils() == '41917492600'



# Generated at 2022-06-13 23:33:30.554061
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    r = RussiaSpecProvider()
    snils = r.snils()
    assert len(snils) == 11


# Generated at 2022-06-13 23:33:40.622349
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """ Unit test for method snils of class RussiaSpecProvider """
    # Arrange
    r = RussiaSpecProvider()
    snils_list = []

    # Act
    for _ in range(0, 100):
        snils_list.append(r.snils())

    # Assert
    for snils in snils_list:
        assert snils[-3] == str(control_sum(snils[0:9]))


# Generated at 2022-06-13 23:33:43.232692
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider."""
    val = RussiaSpecProvider()
    assert len(val.snils()) == 11
    assert val.snils().isdigit()


# Generated at 2022-06-13 23:35:31.446160
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    snils = RussiaSpecProvider.snils()
    rezult = len(snils)
    expected = 11
    assert rezult == expected, f"Expect {expected}, but get {rezult}."

# Generated at 2022-06-13 23:35:33.279303
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider(seed=1)
    assert provider.snils() == '4958464000'

# Generated at 2022-06-13 23:35:35.869251
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    s = 0
    for i in range(1, 9):
        s += random.randint(0, 9) * i
    return s % 11 % 10


# Generated at 2022-06-13 23:35:45.210431
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    for _ in range(0, 100):
        snils = RussiaSpecProvider().snils()
        assert isinstance(snils, str)
        numbers = snils[:-2]
        control_code = snils[-2:]
        control_code_array = []
        for i in range(9, 0, -1):
            control_code_array.append(int(numbers[9 - i]) * int(i))
        control_code_array = sum(control_code_array)
        if control_code_array in (100, 101):
            assert control_code == '00'
        elif control_code_array < 100:
            assert str(control_code_array) in control_code
        elif control_code_array > 101:
            control_code_array = control_code_array % 101

# Generated at 2022-06-13 23:35:49.194347
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test function of method snils in class RussiaSpecProvider"""
    test_obj = RussiaSpecProvider()
    snils = test_obj.snils()
    assert len(snils) == 11

    import re
    pattern = r'^\d{11}$'
    assert re.match(pattern, snils) is not None


# Generated at 2022-06-13 23:35:50.399565
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    a = provider.snils()
    assert len(a) == 11


# Generated at 2022-06-13 23:35:57.146257
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method 'RussiaSpecProvider._snils'"""
    import subprocess
    import re
    
    def assert_value(val):
        pattern = re.compile(r'^\d\d\d\d\d\d\d\d\d\d$')
        if pattern.match(val):
            return True
        else:
            return False
    
    if __name__ == '__main__':
        res = subprocess.check_output(["python", "./mimesis/providers/person/ru/snils.py"])
        res = res.decode("utf-8")
        res = res.split()
        for value in res:
            assert assert_value(value), 'Method "RussiaSpecProvider._snils" does not work'

# Generated at 2022-06-13 23:35:58.699820
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test method snils of class RussiaSpecProvider."""
    rsp = RussiaSpecProvider()
    snils = rsp.snils()
    assert snils != None


# Generated at 2022-06-13 23:36:02.502968
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    ru_provider = RussiaSpecProvider()
    ru_provider.seed(5)
    assert ru_provider.snils() == "82723265800"


# Generated at 2022-06-13 23:36:11.184367
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    snils = provider.snils()
    
    # Check length of snils
    if len(snils) != 11:
        raise Exception
    # Check type of snils
    if not isinstance(snils, str):
        raise Exception
   
    # Check digits
    for i in snils:
        if not i.isdigit():
            raise Exception
    return 
