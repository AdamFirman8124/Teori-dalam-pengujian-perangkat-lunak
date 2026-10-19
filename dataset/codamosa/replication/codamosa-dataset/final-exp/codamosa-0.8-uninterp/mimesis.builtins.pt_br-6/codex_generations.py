

# Generated at 2022-06-13 23:28:33.080971
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.enums import Gender
    
    brazilSpecProvider = BrazilSpecProvider()
    
    cpf = brazilSpecProvider.cpf()

    assert cpf is not None
    assert cpf != ''
    assert len(cpf) == 14


# Generated at 2022-06-13 23:28:35.855461
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    assert BrazilSpecProvider().cnpj() == '42.381.435/0001-18'
    assert BrazilSpecProvider().cnpj(with_mask=False) == '42381435000118'

# Generated at 2022-06-13 23:28:41.776243
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person
    from mimesis.providers.address import Address

    p = Person('pt_BR')
    address = Address('pt_BR')

    assert p.cnpj(with_mask=True) == '77.732.230/0001-70'

# Generated at 2022-06-13 23:28:48.296675
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from mimesis.providers.brazil import BrazilSpecProvider
    brazil_provider = BrazilSpecProvider()
    cnpj = brazil_provider.cnpj()
    cnpj_mask = brazil_provider.cnpj(with_mask=False)
    assert cnpj != cnpj_mask
    assert len(cnpj) == 18
    assert len(cnpj_mask) == 14

# Generated at 2022-06-13 23:28:50.049097
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    bsp = BrazilSpecProvider()
    assert len(bsp.cnpj()) == 18


# Generated at 2022-06-13 23:28:52.347113
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    b = BrazilSpecProvider()
    cpf = b.cpf()
    assert (cpf != "")


# Generated at 2022-06-13 23:28:55.375381
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():

    brazil_spec_provider = BrazilSpecProvider()
    print(brazil_spec_provider.cnpj(with_mask=True))
    print(brazil_spec_provider.cnpj(with_mask=False))

# Generated at 2022-06-13 23:29:00.075027
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from mimesis.enums import Gender

    test_BrazilSpecProvider = BrazilSpecProvider(seed=666)
    for i in range(20):
        cnpj = test_BrazilSpecProvider.cnpj(with_mask=False)
        assert type(cnpj) == str
        assert len(cnpj) == 14
        cnpj_convert = int(cnpj)
        assert cnpj_convert >= 1000000000000
        assert cnpj_convert <= 9999999999999
    cnpj_2 = test_BrazilSpecProvider.cnpj(with_mask=False)
    assert cnpj_2 == '47732309000170'


# Generated at 2022-06-13 23:29:03.753466
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.builtins.brazil import BrazilSpecProvider as bsp
    b = bsp()
    assert b.cpf(with_mask=True) != b.cpf(with_mask=False)


# Generated at 2022-06-13 23:29:12.248002
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    result_cnpj = BrazilSpecProvider().cnpj()
    assert len(result_cnpj) == 18
    first_part_cnpj = result_cnpj[:13]

    result_second_part = BrazilSpecProvider().cnpj()
    second_part_cnpj = result_second_part[13:]

    second_part_cnpj_result = BrazilSpecProvider().cnpj(first_part_cnpj)
    assert second_part_cnpj_result == second_part_cnpj


# Generated at 2022-06-13 23:29:29.787251
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Unit test for method cnpj of class BrazilSpecProvider."""
    # cnpj = BrazilSpecProvider().cnpj(with_mask = True)
    cnpj = BrazilSpecProvider().cnpj(with_mask = False)
    assert len(cnpj) == 14
    # assert len(cnpj) == 18


# Generated at 2022-06-13 23:29:43.744581
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.builtins.types import Field

    provider = BrazilSpecProvider()

    assert provider.cpf() is not None

    assert provider.cpf(with_mask=False) is not None

    assert len(provider.cpf()) == 14
    assert len(provider.cpf(with_mask=False)) == 11

    fn = provider.cpf
    assert list(map(lambda x: x.isdigit(), fn(with_mask=False))) == [True, True, True, True, True, True, True, True, True, True, True]
    assert list(map(lambda x: x.isdigit(), fn(with_mask=True).replace('.','',3).replace('-', '', 1))) == [True, True, True, True, True, True, True, True, True, True, True]

# Generated at 2022-06-13 23:29:49.968153
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    # initialize BrazilSpecProvider
    brazilSpecProvider = BrazilSpecProvider()

    # get random cpf
    cpf = brazilSpecProvider.cpf()

    # cpf must be formatted in ###.###.###-##
    assert len(cpf) == 14
    assert cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-'



# Generated at 2022-06-13 23:29:58.142626
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    # Setup
    brazil_provider = BrazilSpecProvider()

    # Exercise
    result = brazil_provider.cnpj()

    # Verify
    assert len(result) == 18
    assert result[-4] == '-'
    assert result[-9] == '/'
    assert result[-13] == '.'
    assert result[-15] == '.'
    assert 0 < int(result[-12:-9]) < 100
    assert 0 < int(result[-15:-13]) < 10
    assert 1000 < int(result[-18:-15]) < 10000


# Generated at 2022-06-13 23:30:06.151965
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Unit test for method cpf of class BrazilSpecProvider."""
    from mimesis.enums import Gender
    from mimesis.providers.person.pt_br import BrazilPersonProvider
    brazil_provider = BrazilPersonProvider(seed=42)
    brazil_provider.name('Daniela', Gender.FEMALE)
    brazil_provider.cpf()
    brazil_provider.srn(gender=Gender.FEMALE)


# Generated at 2022-06-13 23:30:09.712549
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    brazil_spec_provider = BrazilSpecProvider()

    assert len(brazil_spec_provider.cnpj()) == 18
    assert len(brazil_spec_provider.cnpj(False)) == 14


# Generated at 2022-06-13 23:30:14.545597
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    cpf1 = BrazilSpecProvider().cpf()
    assert len(cpf1) is 14
    assert cpf1[3] == '.'
    assert cpf1[7] == '.'
    assert cpf1[11] == '-'


# Generated at 2022-06-13 23:30:26.232483
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """test_BrazilSpecProvider_cnpj.

    Descrition:
    Test BrazilSpecProvider method cnpj.

    Procedure:
    Create BrazilSpecProvider class, call the metod cnpj 20 times and verify if the result has
    the right leght and if is a valid cnpj.

    """
    print('\nUnit test for method cnpj')
    brazil_provider = BrazilSpecProvider()
    i = 0

    while(i < 20):
        cnpj = brazil_provider.cnpj()
        cnpj_len = len(cnpj)
        if cnpj_len != 18:
            print('Incorrect length for cnpj: ', cnpj_len)
            print(cnpj)

        cnpj1 = cnpj[:13]
        c

# Generated at 2022-06-13 23:30:28.045447
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    x = BrazilSpecProvider()
    cnpj = x.cnpj(with_mask=False)
    assert len(cnpj) == 14

# Generated at 2022-06-13 23:30:36.532405
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    cnpj = provider.cnpj()
    assert len(cnpj) == 18
    assert cnpj[-2] != '-'
    assert cnpj[-3] != '-'
    assert cnpj[-4] != '-'
    assert cnpj[-5] != '-'
    assert cnpj[-6] != '-'
    assert cnpj[-7] != '-'
    assert cnpj[-8] != '-'
    assert cnpj[-9] != '-'



# Generated at 2022-06-13 23:30:58.052157
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    cnpj = BrazilSpecProvider.cnpj(with_mask=True)
    assert len(cnpj) == 18
    assert cnpj[2] == '.'
    assert cnpj[6] == '.'
    assert cnpj[10] == '/'
    assert cnpj[15] == '-'
    assert cnpj[0:2].isdigit()
    assert cnpj[3:6].isdigit()
    assert cnpj[7:10].isdigit()
    assert cnpj[11:15].isdigit()
    assert cnpj[16:18].isdigit()


# Generated at 2022-06-13 23:31:03.836341
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Unit test for method cpf of class BrazilSpecProvider."""
    import re
    pattern = r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}'
    assert re.match(pattern, BrazilSpecProvider().cpf())


# Generated at 2022-06-13 23:31:13.042328
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    # Create instance of BrazilSpecProvider class
    brazil_provider = BrazilSpecProvider()

    # Call the method cnpj()
    assert isinstance(brazil_provider.cnpj(), type(str()))
    assert len(brazil_provider.cnpj()) == 14
    assert brazil_provider.cnpj().count('-') == 1
    assert brazil_provider.cnpj().count('/') == 1
    assert brazil_provider.cnpj().count('.') == 2


# Generated at 2022-06-13 23:31:23.925044
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from mimesis import BrazilSpecProvider
    bsp = BrazilSpecProvider()
    assert len(bsp.cnpj()) == 18
    assert len(bsp.cnpj(with_mask=False)) == 14
    assert bsp.cnpj() == bsp.cnpj()  # if with_mask == True
    assert bsp.cnpj(with_mask=False) == bsp.cnpj(with_mask=False)  # if with_mask == False
    assert bsp.cnpj().count(".") == 2
    assert bsp.cnpj().count("-") == 1
    assert bsp.cnpj(with_mask=False).count(".") == 0
    assert bsp.cnpj(with_mask=False).count("-") == 0


# Generated at 2022-06-13 23:31:29.109733
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    brazil = BrazilSpecProvider()
    cpf = brazil.cpf(with_mask=False)
    assert len(cpf) == 11
    assert cpf.isdigit()
    assert '.' not in cpf
    assert '-' not in cpf


# Generated at 2022-06-13 23:31:33.858061
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    br = BrazilSpecProvider()
    cpf1 = br.cpf()
    cpf2 = br.cpf()
    assert type(cpf1) == str
    assert type(cpf2) == str
    assert cpf1 != cpf2


# Generated at 2022-06-13 23:31:39.385159
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Tests the method cnpj of class BrazilSpecProvider."""
    from mimesis.providers.identifiers import CNPJ
    # Test with_mask=True
    cnpj = BrazilSpecProvider().cnpj(True)
    assert True == CNPJ().is_valid(cnpj)
    # Test with_mask=False
    cnpj = BrazilSpecProvider().cnpj(False)
    assert True == CNPJ().is_valid(cnpj)



# Generated at 2022-06-13 23:31:42.336730
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    expected = '77.732.230/0001-70'
    provider = BrazilSpecProvider(seed=2761359)
    result = provider.cnpj()
    assert result == expected


# Generated at 2022-06-13 23:31:55.546223
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    import mimesis
    import random
    brazil = mimesis.BrazilSpecProvider()
    cpf = brazil.cpf(with_mask=False)
    # check len
    assert len(cpf) == 11
    # check type
    assert isinstance(cpf, str)
    # check digit
    digit = cpf[-2:]
    rcpf = cpf[:-2]
    s = 0
    for i in range(len(rcpf)):
        #print(rcpf[i])
        s += int(rcpf[i]) * (10 - i)
    r = 11 - (s % 11)
    if r > 9:
        r = 0
    first_digit = str(r)
    #print('rcpf: ' + rcpf)
    #print('first

# Generated at 2022-06-13 23:32:03.487307
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test method cpf of class BrazilSpecProvider"""
    from mimesis.enums import Gender

    brazil = BrazilSpecProvider()

    # get a random cpf
    cpf = brazil.cpf()
    assert len(cpf) == 14
    assert cpf == brazil.cpf()

    # get a random cpf with mask
    cpf_masked = brazil.cpf(with_mask=True)
    assert len(cpf_masked) == 14
    assert cpf_masked == brazil.cpf(with_mask=True)

    # get a valid cpf
    cpf = brazil.cpf(valid=True)
    assert brazil.validate_cpf(cpf)



# Generated at 2022-06-13 23:32:46.037580
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person
    person = Person('pt-br', Seed.random())
    cpfs = set()
    cnpjs = set()
    # Execute 99 times the cpf method of BrazilSpecProvider
    for _ in range(99):
        cpfs.add(person.cpf())
    # Execute 99 times the cnpj method of BrazilSpecProvider
    for _ in range(99):
        cnpjs.add(person.cnpj())
    # garantees the unique random cpfs
    assert len(cpfs) == 99
    # garantees the unique random cnpjs
    assert len(cnpjs) == 99
    # test the sample of string generated by the cpf method
    assert person.cpf(with_mask=True)

# Generated at 2022-06-13 23:32:53.082891
# Unit test for method cnpj of class BrazilSpecProvider

# Generated at 2022-06-13 23:32:58.232714
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Class that provides special data for Brazil."""
    Brazil = BrazilSpecProvider()
    assert Brazil.cnpj() == '77.732.230/0001-70'

# Generated at 2022-06-13 23:33:02.514323
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.providers.brazil_provider import BrazilSpecProvider
    provider = BrazilSpecProvider()
    
    cpf = provider.cpf(with_mask=False)
    assert len(cpf) == 11
    print('Test OK: method cpf of class BrazilSpecProvider')


# Generated at 2022-06-13 23:33:04.329650
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    assert len(BrazilSpecProvider().cpf()) == 14


# Generated at 2022-06-13 23:33:08.566015
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    brasilData = BrazilSpecProvider()
    n = brasilData.cnpj()
    print(f"\nCNPJ: {n}")
    assert len(n)==18

# Generated at 2022-06-13 23:33:10.235948
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
  bsp = BrazilSpecProvider()
  print(bsp.cnpj())

# Generated at 2022-06-13 23:33:23.070041
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():

    provider = BrazilSpecProvider()

    list_expected_results = [
        '010.858.390-10',
        '040.957.810-15',
        '084.803.200-97',
        '077.637.060-61',
        '069.918.190-74',
        '024.299.920-99',
        '089.063.130-30',
        '003.769.840-48',
        '010.821.440-64',
        '035.609.690-04',
    ]

    list_cpf = []
    for i in range(0, 10):
        list_cpf.append(provider.cpf())

    assert list_cpf != list_expected_results


# Generated at 2022-06-13 23:33:25.401786
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    a = BrazilSpecProvider()
    assert len(a.cnpj(with_mask=False)) == 14



# Generated at 2022-06-13 23:33:33.133893
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Unit test for method cnpj of class BrazilSpecProvider."""
    provider = BrazilSpecProvider()
    result = provider.cnpj()

    # Check if the result matches the mask
    assert "##.###.###/####-##" == result.replace("[^0-9]", "#")
    assert len(result) == 18


# Generated at 2022-06-13 23:34:31.312526
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis import BrazilSpecProvider
    brazil_spec_provider = BrazilSpecProvider()
    CPF = brazil_spec_provider.cpf()
    print(CPF)


# Generated at 2022-06-13 23:34:43.911510
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
  from mimesis.builtins import BrazilSpecProvider
  from mimesis.enums import Gender
  from mimesis.providers.person import Person
  # 种子
  seed = 'test_BrazilSpecProvider_cpf'
  # 实例化
  bsp = BrazilSpecProvider(seed=seed)
  p = Person(seed=seed)
  # 姓名
  name = p.full_name(gender=Gender.FEMALE)
  # cpf 数据
  cpf_data = bsp.cpf()
  # 断言
  assert cpf_data != None
  # 输出
  print(name)
  print(cpf_data)


# Generated at 2022-06-13 23:34:45.680531
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    b = BrazilSpecProvider()
    assert len(b.cnpj()) == 18


# Generated at 2022-06-13 23:34:51.707555
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test method cpf from class BrazilSpecProvider."""
    cpf = BrazilSpecProvider(seed=9234293)
    assert cpf.cpf(with_mask=False) == '15952268107'
    assert cpf.cpf() == '159.522.681-07'


# Generated at 2022-06-13 23:34:52.918505
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    assert provider.cpf() != provider.cpf()


# Generated at 2022-06-13 23:35:03.599592
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    data = BrazilSpecProvider(seed=None)
    resp = data.cnpj(with_mask=False)
    assert len(resp) == 14, "Invalid CNPJ not equal 14 numbers."
    resp = data.cnpj(with_mask=True)
    assert len(resp) == 18, "Invalid CNPJ not equal 18 numbers."
    resp = data.cnpj(with_mask=True)
    assert resp[2] == ".", "Invalid CNPJ format. Expected point, returned {}.".format(resp[2])
    resp = data.cnpj(with_mask=True)
    assert resp[6] == ".", "Invalid CNPJ format. Expected point, returned {}.".format(resp[6])
    resp = data.cnpj(with_mask=True)

# Generated at 2022-06-13 23:35:09.714914
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    cpf_with_mask = provider.cpf(with_mask=True)
    assert len(cpf_with_mask) == 14
    assert cpf_with_mask[3] == '.'
    assert cpf_with_mask[7] == '.'
    assert cpf_with_mask[11] == '-'

    cpf_without_mask = provider.cpf(with_mask=False)
    assert len(cpf_without_mask) == 11
    assert not cpf_with_mask[3] == '.'
    assert not cpf_with_mask[7] == '.'
    assert not cpf_with_mask[11] == '-'


# Generated at 2022-06-13 23:35:11.801986
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Test BrazilSpecProvider.cnpj."""
    bsp = BrazilSpecProvider()
    cnpj = bsp.cnpj()
    assert len(cnpj) == 18
    assert '-' in cnpj
    assert '.' in cnpj


# Generated at 2022-06-13 23:35:13.901581
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    assert provider.cpf() == '074.376.106-63'



# Generated at 2022-06-13 23:35:22.859840
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bsp = BrazilSpecProvider()
    cpf = bsp.cpf()

    assert len(cpf) == 14
    assert cpf[3] == '.'
    assert cpf[7] == '.'
    assert cpf[11] == '-'


# Generated at 2022-06-13 23:38:14.974949
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bsp = BrazilSpecProvider(seed=None)
    cpf = bsp.cpf()
    assert len(cpf) == 14
    cpf_without_mask = bsp.cpf(with_mask=False)
    assert len(cpf_without_mask) == 11


# Generated at 2022-06-13 23:38:18.268701
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Unit test for method BrazilSpecProvider.cnpj."""
    bsp = BrazilSpecProvider()
    cnpj = bsp.cnpj(with_mask=False)

    # Test if the length of cnpj is 14
    assert len(cnpj) == 14