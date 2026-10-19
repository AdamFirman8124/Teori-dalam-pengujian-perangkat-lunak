

# Generated at 2022-06-13 23:28:41.198585
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    result = provider.snils()
    if not result.isdigit() or len(result) != 11:
        raise AssertionError('ERROR: invalid snils')


# Generated at 2022-06-13 23:28:51.387143
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    
    instances = 10000
    for i in range(0, instances):
        rus = RussiaSpecProvider()

        snils_result = rus.snils()
        snils = [snils_result[i:i+1] for i in range(0,9)]
        snils = [int(x) for x in snils]
        # 1. Number of digits are correct
        assert len(snils_result) == 11
        # 2. The first three digits are not equal to 777 or 999
        assert (snils[0] != 7) and (snils[1] != 7) and (snils[2] != 7) and (snils[0] != 9) and (snils[1] != 9) and (snils[2] != 9)
        # 3. The check sum is not equal to 00 (the last two digits

# Generated at 2022-06-13 23:28:55.816216
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    ru = RussiaSpecProvider()
    arr_snils = [ru.snils() for i in range(0, 100000)]
    d = {}
    for snils in arr_snils:
        d[snils] = d.get(snils, 0) + 1
    for snils in d.keys():
        assert 1 <= d[snils]


# Generated at 2022-06-13 23:29:06.893098
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    a = RussiaSpecProvider()
    b = RussiaSpecProvider()
    c = RussiaSpecProvider()
    # initializing flag with 'true'
    flag = True
    for _ in range(0, 10):
        # initializing flag with 'false'
        flag = False
        flag = True
        for _ in range(0, 10):
            if len(a.snils()) != len(b.snils()):
                # if any of snils lenght and others isn't equal
                # change flag to false
                flag = False
                break
        flag = True
        if flag:
            # If flag is still True do the same things but with other
            # snils
            for _ in range(0, 10):
                if len(a.snils()) != len(c.snils()):
                    flag = False
                    break


# Generated at 2022-06-13 23:29:09.575475
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()

    # Check exception
    assert provider.snils == '41917492600'

# Generated at 2022-06-13 23:29:13.512733
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    # Testing snils with length of 9 digits
    rsp = RussiaSpecProvider()
    snils = [rsp.snils() for i in range(0, 10)]
    for i in snils:
        assert len(i) == 11, "snils() has bad length"

# Generated at 2022-06-13 23:29:17.663602
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis import RussiaSpecProvider
    a = RussiaSpecProvider()
    b = [a.snils() for x in range(0, 10)]
    print(b)


# Generated at 2022-06-13 23:29:21.349008
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test snils method"""
    provider = RussiaSpecProvider()
    assert type(provider.snils()) is str
    assert len(provider.snils()) == 11


# Generated at 2022-06-13 23:29:23.668495
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rus = RussiaSpecProvider()
    assert rus.snils() != None


# Generated at 2022-06-13 23:29:26.329377
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
  """Method: test_RussiaSpecProvider_snils()"""
  db = RussiaSpecProvider()
  x = db.snils()
  print(x)

# Generated at 2022-06-13 23:29:45.743855
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    spec_provider = RussiaSpecProvider()
    assert len(spec_provider.snils()) == 11

# Generated at 2022-06-13 23:29:54.224939
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.providers.financial.russia_provider import RussiaSpecProvider
    import numpy as np
    provider = RussiaSpecProvider('ru')
    snils_lst = []
    for i in range(0,10000):
        snils_lst.append(provider.snils())
    snils_lst = np.unique(snils_lst)
    assert len(snils_lst) == 10000


# Generated at 2022-06-13 23:30:00.785497
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    obj = RussiaSpecProvider()
    snilses = []
    #test_instance = RussiaSpecProvider()
    for _ in range(10000):
        snilses.append(obj.snils())
    #assert obj.snils() == '41917492600'
    #print(snilses)


# Generated at 2022-06-13 23:30:05.614718
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()

    result = provider.snils()
    assert len(result) == 11

    result = provider.snils(seed = 123)
    assert result == '02923242600'



# Generated at 2022-06-13 23:30:07.039778
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    assert RussiaSpecProvider().snils() == '41917492600'


# Generated at 2022-06-13 23:30:15.329239
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.providers.base import BaseSpecProvider
    rus_provider = RussiaSpecProvider()
    spec = BaseSpecProvider()
    snils = rus_provider.snils()
    list_snils = list(snils)
    assert len(list_snils) == 11
    assert snils[9] == spec.get_digit(int(
        snils[0:9] + snils[1:9] + snils[2:9] + snils[3:9] +
        snils[4:9] + snils[5:9] + snils[6:9] + snils[7:9] +
        snils[8:9]) % 101 % 11 % 10)

# Generated at 2022-06-13 23:30:17.381056
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    assert RussiaSpecProvider().snils()[-2:] == RussiaSpecProvider().snils()[-2:]


# Generated at 2022-06-13 23:30:24.345590
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider

    :return: None
    """
    rs = RussiaSpecProvider()
    snils_list = list()
    for i in range(0, 1000001):
        snils_list.append(rs.snils())
    snils_list = set(snils_list)
    assert len(snils_list) > 999900

# Generated at 2022-06-13 23:30:26.486890
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    x = RussiaSpecProvider()
    assert len(str(x.snils())) == 11

# Generated at 2022-06-13 23:30:28.267507
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    print("get snils code: ")
    code = RussiaSpecProvider.snils()
    print(code)


# Generated at 2022-06-13 23:31:06.527728
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    obj = RussiaSpecProvider()
    assert len(obj.snils()) == 11


# Generated at 2022-06-13 23:31:20.066398
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test generating snils."""
    from pprint import pprint
    from time import time
    from IPython.display import display
    from mimesis.enums import Gender
    from mimesis.builtins import RussiaSpecProvider

    provider = RussiaSpecProvider(seed=42) # нотация PEP8 запрещает длинные строки
    # поэтому мы разбиваем их на несколько строк. В питоне всё отлично
    # работает, есл

# Generated at 2022-06-13 23:31:22.215541
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    a = RussiaSpecProvider()
    b = RussiaSpecProvider()
    assert a.snils() != b.snils()

# Generated at 2022-06-13 23:31:24.652486
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    x = RussiaSpecProvider()
    assert len(x.snils()) == 11


# Generated at 2022-06-13 23:31:27.057043
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rus = RussiaSpecProvider()
    assert rus.snils() == '41917492600'

# Generated at 2022-06-13 23:31:29.922403
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis import RussiaSpecProvider
    r = RussiaSpecProvider()
    assert r.snils() is not None


# Generated at 2022-06-13 23:31:38.912415
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():

    methodResult = RussiaSpecProvider().snils()
    assert type(methodResult) == str
    assert len(methodResult) == 11
    assert methodResult[0:3] == '419'
    assert methodResult[3] == '1'
    assert methodResult[4] == '7'
    assert methodResult[5:8] == '492'
    assert methodResult[8] == '6'
    assert methodResult[9:11] == '00'


# Generated at 2022-06-13 23:31:42.431032
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    prov = RussiaSpecProvider()
    #проверка на не менее 9 цифр
    assert len(prov.snils()) >= 9


# Generated at 2022-06-13 23:31:45.059136
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    test_object = RussiaSpecProvider()
    print(test_object.snils())


# Generated at 2022-06-13 23:31:51.261166
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider."""
    russia_provider = RussiaSpecProvider()
    snils = russia_provider.snils()
    assert len(snils) == 11
    assert snils[-2:] != '00'
    assert 0 <= int(snils) <= 999_999_999_99



# Generated at 2022-06-13 23:33:27.464078
# Unit test for method snils of class RussiaSpecProvider

# Generated at 2022-06-13 23:33:31.988110
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    r = RussiaSpecProvider()
    t = r.snils()
    assert(type(t) == str)
    assert(len(t) == 11)


# Generated at 2022-06-13 23:33:32.921638
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    RussiaSpecProvider.snils()

# Generated at 2022-06-13 23:33:37.233433
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    snils = provider.snils()
    assert snils.isdigit() is True
    assert len(snils) == 11

# Generated at 2022-06-13 23:33:41.503137
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    a = RussiaSpecProvider()
    snils = a.snils()
    if type(snils)!=str:
        raise Exception
    snils2 = a.snils(seed='seed')

# Generated at 2022-06-13 23:33:44.169971
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    prov = RussiaSpecProvider()
    assert prov.snils() != prov.snils()


# Generated at 2022-06-13 23:33:50.203452
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider.

    :return: None
    """
    inst = RussiaSpecProvider()
    assert isinstance(inst.snils(), str)
    assert len(inst.snils()) == 11

if __name__ == '__main__':
    test_RussiaSpecProvider_snils()

# Generated at 2022-06-13 23:33:59.962423
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    ru = RussiaSpecProvider()

    def calc_check_code(code):
        code = str(code)
        s = 0
        for i in range(9):
            s += (9-i)*int(code[i])

        if s in (100, 101):
            return 0
        elif s > 101:
            s = s % 101
            if s == 100:
                s = 0
        return s

    for i in range(100000):
        snils = ru.snils()
        print(snils)
        assert calc_check_code(snils[:-2]) == int(snils[-2:])

# Generated at 2022-06-13 23:34:06.220907
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():

    for _ in range(0, 10):
        rp = RussiaSpecProvider()
        snils = rp.snils()
        pre_snils = list(snils)
        for i in range(len(snils)):
            if snils[i] == '-':
                pre_snils.remove('-')
                pre_snils.insert(3, '-')
                pre_snils.insert(7, '-')
        pre_snils = int(''.join(pre_snils))

        # Test if len(snils) == 11
        assert len(snils) == 11

        # Test if snils is in range
        assert 1 <= pre_snils <= 999999


# Generated at 2022-06-13 23:34:17.812355
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test snils function of class RussiaSpecProvider.
    
    Checks the following:
    - Checks the length of the number.
    - Checks that the number is in the required range.
    - Checks the checksum of the number.
    """
    import RussiaData
    #import mimesis
    provider = RussiaSpecProvider()
    snils_list = []
    for i in range(100):
        snils_list.append(provider.snils())

    for snils in snils_list:
        assert len(snils) == 11
        for j in range(9):
            assert snils[j] in range(10)
        assert snils[9] in range(2)
        assert snils[10] in range(10)
        assert int(snils) in range(100000000, 1000000000)

# Generated at 2022-06-13 23:38:12.375305
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """
    Test snils method of class RussiaSpecProvider

    :return: None
    """
    spec = RussiaSpecProvider()

    assert len(spec.snils().split(".")) == 2


# Generated at 2022-06-13 23:38:20.228195
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider."""
    russia = RussiaSpecProvider()
    snils = russia.snils()
    snils_int = int(snils)
    numbers = []
    control_codes = []
    for i in range(0, 9):
        numbers.append(snils_int % 10)
        snils_int //= 10
    numbers.reverse()
    for i in range(9, 0, -1):
        control_codes.append(numbers[9 - i] * i)
    control_code = sum(control_codes)
    if str(control_code).endswith('00'):
        control_code = 0
    assert str(control_code) == snils[9:]

# Generated at 2022-06-13 23:38:25.079954
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test method snils of class RussiaSpecProvider."""
    rsp = RussiaSpecProvider()
    snils_1 = rsp.snils()
    snils_2 = rsp.snils()
    print(snils_1)
    print(snils_2)
