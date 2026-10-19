

# Generated at 2022-06-13 23:28:41.966299
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    assert RussiaSpecProvider().snils() == "32517546523"


# Generated at 2022-06-13 23:28:49.403767
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    ru = RussiaSpecProvider()
    ru.seed(10)
    snils_num = ru.snils()
    control_code = 0
    snils_nums = []
    for x in snils_num:
        snils_nums.append(int(x))
    for i in range(9, 0, -1):
        control_code += snils_nums[9 - i] * i
    assert control_code % 101 == snils_nums[9] * 10 + snils_nums[10]


# Generated at 2022-06-13 23:28:52.835175
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    f = RussiaSpecProvider()
    assert len(f.snils()) == 11
    for i in range(0, 10):
        f = RussiaSpecProvider(seed=i)
        assert len(f.snils()) == 11


# Generated at 2022-06-13 23:28:57.904784
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    snils = provider.snils()
    assert snils[0:3] == '419'
    assert snils[3] == '-'
    assert snils[4:6] == '17'
    assert snils[6] == '-'
    assert snils[7:9] == '49'
    assert snils[9] == '-'
    assert snils[10:11] == '2'
    assert snils[11:12] == '6'
    assert snils[12:13] == '0'
    assert snils[13:14] == '0'

# Generated at 2022-06-13 23:29:00.605207
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    snils1 = provider.snils()
    snils2 = provider.snils()
    assert snils1 != snils2
    assert len(snils1) == 11
    assert len(snils2) == 11


# Generated at 2022-06-13 23:29:02.673574
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    result = provider.snils()
    assert len(result) == 11


# Generated at 2022-06-13 23:29:04.386113
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    r = RussiaSpecProvider()
    a = r.snils()
    assert len(a) == 11


# Generated at 2022-06-13 23:29:06.846668
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider."""
    a = RussiaSpecProvider()
    print(a.snils())

# Generated at 2022-06-13 23:29:16.448716
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    russian = RussiaSpecProvider()
    snils = russian.snils()

    def control_sum(nums: list, t: str) -> int:
        digits_dict = {
            'n2': [7, 2, 4, 10, 3, 5, 9, 4, 6, 8],
            'n1': [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8],
        }
        number = 0
        digits = digits_dict[t]

        for i, _ in enumerate(digits, start=0):
            number += nums[i] * digits[i]
        return number % 11 % 10

    def fsnils(snils: str) -> bool:
        numbers = [int(i) for i in snils]

# Generated at 2022-06-13 23:29:21.665789
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    for _ in range(100000):
        snils = provider.snils()
        assert len(snils) == 11
        for x in snils:
            assert int(x) in range(0, 9)


# Generated at 2022-06-13 23:29:43.436665
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    import random
    # 10 раз проверим на корректность функцию.
    for _ in range(10):
        random.seed()
        provider = RussiaSpecProvider(seed=random.randint(0, 10000000)) 
        assert (len(provider.snils()) == 11) and (provider.snils().isdigit())


# Generated at 2022-06-13 23:29:46.205430
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rp = RussiaSpecProvider()
    snils = rp.snils()
    assert snils == rp.snils()



# Generated at 2022-06-13 23:29:48.878520
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rs = RussiaSpecProvider()
    snils_1 = rs.snils() 
    snils_2 = rs.snils()
    assert snils_1 == snils_2


# Generated at 2022-06-13 23:29:50.871479
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    x = RussiaSpecProvider()
    assert x.snils() == '41917492600'

# Generated at 2022-06-13 23:29:54.034440
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rs = RussiaSpecProvider()
    result = rs.snils()
    assert len(result) == 11
    assert result.isnumeric() is True

if __name__ == '__main__':
    test_RussiaSpecProvider_snils()

# Generated at 2022-06-13 23:29:56.818606
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    res = provider.snils()
    curr = '41917492600'
    assert res == curr

# Generated at 2022-06-13 23:30:03.025897
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    snils = list()
    for _ in range(0, 5):
        rsp = RussiaSpecProvider()
        snils.append(rsp.snils())
    print(snils)


if __name__ == '__main__':
    test_RussiaSpecProvider_snils()

# Generated at 2022-06-13 23:30:08.945183
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test method snils of class RussiaSpecProvider."""
    rus_snils = RussiaSpecProvider()
    assert RussiaSpecProvider.snils.__doc__ == 'Generate snils with special algorithm.\n\n        :return: SNILS.\n\n        :Example:\n            41917492600.\n        '
    assert len(rus_snils.snils()) == 11


# Generated at 2022-06-13 23:30:12.684767
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    # Arrange
    provider = RussiaSpecProvider()
    expected_snils = '419174926'

    # Act
    result = provider.snils()

    # Assert
    assert result[0:9] == expected_snils


# Generated at 2022-06-13 23:30:18.545577
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test method snils() of class RussiaSpecProvider."""
    from mimesis.builtins import RussiaSpecProvider

    russia_provider = RussiaSpecProvider()
    # russian_snils = russia_provider.snils()
    russian_snils = russia_provider.snils()
    print(russian_snils)

# Generated at 2022-06-13 23:30:35.946544
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rsp = RussiaSpecProvider()
    snils = rsp.snils()
    assert len(snils) == 11

# Generated at 2022-06-13 23:30:38.060956
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    ru = RussiaSpecProvider()
    assert ru.snils() != ru.snils()



# Generated at 2022-06-13 23:30:44.318187
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    import re

    for provider in ['RussiaSpecProvider']:
        p = eval(provider)()
        snils = p.snils()
        for snils in [p.snils() for i in range(1000000)]:
            assert re.match(r'\d{9}', snils)

# Generated at 2022-06-13 23:30:52.040157
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    control_code = provider.snils()[9:11]
    control_code = int(control_code)
    if control_code in (100, 101):
        return '00'
    elif control_code < 100:
        return '{:02}'.format(control_code)
    elif control_code > 101:
        return '{:02}'.format(control_code % 101)
    else:
        return control_code


# Generated at 2022-06-13 23:31:00.636837
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rs = RussiaSpecProvider()
    code = rs.snils()
    code_digits = [int(c) for c in code]

    digits_dict = {
        'n2': [7, 2, 4, 10, 3, 5, 9, 4, 6, 8],
        'n1': [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8],
    }

    control_codes = []

    for i, _ in enumerate(digits_dict['n2'], start=0):
        control_codes.append(code_digits[i] * digits_dict['n2'][i])

    control_code = sum(control_codes)
    modulo = control_code % 101
    if modulo in (100, 101):
        assert code[9:] == '00'

# Generated at 2022-06-13 23:31:10.356028
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    for i in range(10):
        print("Test number: ", i)
        R = RussiaSpecProvider()
        snils_1 = R.snils()
        print("Generated snils: ", snils_1)
        numbers = []
        control_codes = []
        for i in range(0, 9):
            numbers.append(int(snils_1[i]))
        for i in range(9, 0, -1):
            control_codes.append(numbers[9 - i] * i)
        control_code = sum(control_codes)
        print("Sum of digits: ", control_code)
        if control_code in (100, 101):
            snils = ''.join([str(x) for x in numbers]) + '00'
            print("Correct snils: ", snils)

# Generated at 2022-06-13 23:31:23.204927
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
  # Initialize provider
  provider = RussiaSpecProvider()
  # Generate 3 snils
  s1 = provider.snils()
  s2 = provider.snils()
  s3 = provider.snils()

  # Count of numbers in snils
  n = 11
 
  # Tests
  assert len(s1) == n and not s1.__contains__(' ')
  assert len(s2) == n and not s2.__contains__(' ')
  assert len(s3) == n and not s3.__contains__(' ')
  assert s1 != s2 and s2 != s3 and s1 != s3

  assert not (s1.__contains__(' ') or s2.__contains__(' ') or s3.__contains__(' '))

# Unit test

# Generated at 2022-06-13 23:31:26.284006
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    r = RussiaSpecProvider()
    snils = r.snils()
    assert len(snils) == 11


# Generated at 2022-06-13 23:31:30.660523
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider."""
    assert RussiaSpecProvider().snils() == '41917492600'
    RussiaSpecProvider._seed = 213
    assert RussiaSpecProvider().snils() == '58281992100'

# Generated at 2022-06-13 23:31:43.278401
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.enums import Gender

    Russia = RussiaSpecProvider()
    Russia.seed(1)

    # Test with args
    assert Russia.snils() == '06656004905'
    assert Russia.snils(Gender.FEMALE) == '06357436707'
    assert Russia.snils(Gender.FEMALE) != '06357436709'
    assert Russia.snils(Gender.MALE) == '08438383311'
    assert Russia.snils(Gender.MALE) != '08438383301'

    # Test with kwargs
    assert Russia.snils(gender=Gender.FEMALE) == '06357436707'
    assert Russia.snils(gender=Gender.FEMALE) != '06357436709'

# Generated at 2022-06-13 23:32:12.666638
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test method snils"""
    rusc = RussiaSpecProvider()
    assert len(rusc.snils()) == 11
    

# Generated at 2022-06-13 23:32:17.285173
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    test_provider=RussiaSpecProvider()
    arr=[test_provider.snils() for x in range(0,10)]
    print(arr)
    def check_snils(num):
        num_str=str(num)
        num_arr=[int(s) for s in num_str]
        res=[x*y for x,y in zip(num_arr, range(0,9))]
        #print(res)
        return len(num_str)==11 and sum(res)<=101
    if all([check_snils(i) for i in arr]):
        print('Test "snils" - PASS')
    else:
        print('Test "snils" - FAIL')


# Generated at 2022-06-13 23:32:20.529123
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    russ = RussiaSpecProvider()
    for _ in range(10):
        russ.snils()
        assert type(russ) == type(RussiaSpecProvider())



# Generated at 2022-06-13 23:32:22.490416
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    p = RussiaSpecProvider()
    assert len(p.snils()) == 11
    assert isinstance(p.snils(), str)


# Generated at 2022-06-13 23:32:23.373308
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rus = RussiaSpecProvider()
    assert type(rus.snils()) == str


# Generated at 2022-06-13 23:32:26.582653
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.builtins import RussiaSpecProvider as SNILS
    from mimesis.enums import Gender
    obj_snils = SNILS()
    assert(len(obj_snils.snils()) == 11)
    assert(obj_snils.snils().isdigit())


# Generated at 2022-06-13 23:32:34.952156
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.builtins import RussiaSpecProvider
    russian_provider = RussiaSpecProvider()
    
    person = Person()
    person.first_name = russian_provider.first_name()
    person.patronymic = russian_provider.patronymic()
    person.last_name = russian_provider.last_name()
    person.passport_series_and_number = russian_provider.series_and_number()
    person.inn = russian_provider.inn()
    person.snils = russian_provider.snils()
    assert len(person.snils) == 11



# Generated at 2022-06-13 23:32:37.886578
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    ru = RussiaSpecProvider()
    print("SNILS = ", ru.snils())

# Generated at 2022-06-13 23:32:39.614710
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    assert len("41917492600") == 11
    assert type("41917492600") == str

# Generated at 2022-06-13 23:32:42.630527
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider"""
    ru_spec_provider = RussiaSpecProvider()

    snils = ru_spec_provider.snils()
    print(snils)
    assert snils is not None

# Generated at 2022-06-13 23:33:59.457457
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test method snils of class RussiaSpecProvider."""
    provider = RussiaSpecProvider()
    assert provider.snils() == '41917492600'
    assert provider.snils() == '24767983600'
    assert provider.snils() == '25339842600'
    assert provider.snils() == '80496720400'
    assert provider.snils() == '68766038000'
    assert provider.snils() == '50067340500'
    assert provider.snils() == '11593641300'
    assert provider.snils() == '64176567000'
    assert provider.snils() == '48852846800'
    assert provider.snils() == '17818967000'
    assert provider.snils() == '37880134000'
    assert provider

# Generated at 2022-06-13 23:34:05.724939
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test snils method of RussiaSpecProvider class.

    :return: Test result.
    """

    russia_spec_provider = RussiaSpecProvider()
    # Initialise list of snils numbers
    snils_numbers = []

    # Generate 1000 random snils
    for _ in range(1000):
        generated_snils = russia_spec_provider.snils()
        snils_numbers.append(generated_snils)

    # Check if all generated snils is unique
    snils_numbers_set = set(snils_numbers)
    assert len(snils_numbers) == len(snils_numbers_set)


# Generated at 2022-06-13 23:34:06.999832
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    assert RussiaSpecProvider().snils() == '41917492600'

# Generated at 2022-06-13 23:34:15.531548
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider."""
    # INITIALIZE CLASS AND CREATE SNILS
    rsp = RussiaSpecProvider()
    snils = rsp.snils()
    # INITIALIZE CLASS AND CREATE REAL SNILS
    rsp1 = RussiaSpecProvider()
    real_snils = rsp1.snils()
    # TEST EQUALITY OF THESE TWO SNILS
    assert snils == real_snils


# Generated at 2022-06-13 23:34:17.205994
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    snils = RussiaSpecProvider().snils()
    assert snils != None
    assert isinstance(snils, str)


# Generated at 2022-06-13 23:34:20.842190
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """
    Tests for the method snils of class RussiaSpecProvider.

    Returns:
        None.

    """
    russia_provider = RussiaSpecProvider()
    snils = russia_provider.snils()
    assert snils != None

# Generated at 2022-06-13 23:34:22.349821
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    snils = RussiaSpecProvider().snils()
    print(snils)


# Generated at 2022-06-13 23:34:25.087583
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider(seed=777)

    s = provider.snils()
    assert s == "41917492600"

# Generated at 2022-06-13 23:34:27.173769
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for snils() of class RussiaSpecProvider."""
    provider = RussiaSpecProvider()
    snils = provider.snils()
    assert len(snils) == 11

# Generated at 2022-06-13 23:34:28.727556
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    russian_provider = RussiaSpecProvider()

    assert type(russian_provider.snils()) == str

# Generated at 2022-06-13 23:37:50.152741
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    '''
    Test russia_provider.snils
    '''
    snils = RussiaSpecProvider().snils()
    print(snils)
    assert len(snils) == 11


# Generated at 2022-06-13 23:37:52.372391
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rus = RussiaSpecProvider()
    print(rus.snils())



# Generated at 2022-06-13 23:37:56.305006
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    snils = provider.snils()
    assert isinstance(snils, str)

# Generated at 2022-06-13 23:38:03.984842
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """RussiaSpecProvider.snils()."""
    seed = int('0xabcdefabcdefabcdefabcdefabcdefab', 16)
    russia_provider = RussiaSpecProvider(seed=seed)
    assert russia_provider.snils() == '18233090653'

# Generated at 2022-06-13 23:38:05.889909
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    check_sum = 0
    for _ in range(0, 9):
        check_sum += 41917492600 % 10

# Generated at 2022-06-13 23:38:08.058996
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider."""
    a = RussiaSpecProvider()
    assert(len(a.snils()) == 11)


# Generated at 2022-06-13 23:38:10.237937
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    assert provider.snils() == '41917492600'

# Generated at 2022-06-13 23:38:17.541182
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    
    s = RussiaSpecProvider()       # Seed="<random>"
    snils = s.snils()
    
    assert len(snils)==11
    assert snils[:-2].isdigit()
    assert snils[-2:].isdigit()
    
    s = RussiaSpecProvider(seed='1234567890')
    snils = s.snils()
  
    assert len(snils)==11
    assert snils[:-2].isdigit()
    assert snils[-2:].isdigit()

    assert snils=='38783150891'

# Generated at 2022-06-13 23:38:23.488262
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider"""
    russia_spec_provider = RussiaSpecProvider()
    snils = russia_spec_provider.snils()
    assert isinstance(snils, str)
    assert len(snils) == 11

