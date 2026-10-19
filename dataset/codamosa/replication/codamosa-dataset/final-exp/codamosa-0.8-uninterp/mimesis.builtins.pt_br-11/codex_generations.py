

# Generated at 2022-06-13 23:28:36.280712
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test method cpf from BrazilSpecProvider class."""

    from mimesis.data import BRAZIL_PROVIDER

    brazil_provider = BRAZIL_PROVIDER()
    cpf = brazil_provider.cpf()
    assert len(cpf) == 14
    assert len(set(cpf)) != 1
    assert cpf == brazil_provider.cpf(with_mask=True)



# Generated at 2022-06-13 23:28:44.350750
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Unit test for method cnpj of class BrazilSpecProvider"""
    import unittest
    print('Testing BrazilSpecProvider.cnpj')
    provider = BrazilSpecProvider()
    cnpj = provider.cnpj()
    assert len(cnpj) == 18
    assert cnpj[2] == '.'
    assert cnpj[6] == '.'
    assert cnpj[10] == '/'
    assert cnpj[15] == '-'
    print('ok')


# Generated at 2022-06-13 23:28:47.494126
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    assert provider.cpf(with_mask=False) == '00113729740'
    assert provider.cpf() == '001.137.297-40'


# Generated at 2022-06-13 23:28:50.043283
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Unit test for method cnpj of class BrazilSpecProvider"""
    provider = BrazilSpecProvider()
    cnpj = provider.cnpj()

    assert cnpj is not None



# Generated at 2022-06-13 23:28:52.693220
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Tests the method cpf of class BrazilSpecProvider"""
    assert BrazilSpecProvider().cpf()[:-1] == BrazilSpecProvider().cpf()[:-1]


# Generated at 2022-06-13 23:28:54.371286
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    b = BrazilSpecProvider()
    assert '169.712.472-35' == b.cpf(True)


# Generated at 2022-06-13 23:28:56.527016
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    cpf = BrazilSpecProvider().cpf(with_mask=False)
    assert len(cpf) == 11
    assert cpf.isdigit()


# Generated at 2022-06-13 23:29:02.194987
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    # Test if the method 'cpf' of the class BrazilSpecProvider return a string.
    from mimesis.providers.spec.brazil import BrazilSpecProvider
    brazil_provider = BrazilSpecProvider()
    result = brazil_provider.cpf()
    assert isinstance(result, str)


# Generated at 2022-06-13 23:29:04.689036
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    bsp = BrazilSpecProvider()
    counter = 0
    while counter < 100:
        bsp.cnpj()
        counter = counter + 1



# Generated at 2022-06-13 23:29:11.347258
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    '''Test case: test_BrazilSpecProvider_cnpj
    '''
    # Arrange
    provider = BrazilSpecProvider()
    expected_result = '22.111.111/1111-22'

    # Act
    actual_result = provider.cnpj()

    # Assert
    assert(actual_result == expected_result)


# Generated at 2022-06-13 23:29:33.089006
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    b = BrazilSpecProvider()
    cpfs = [b.cpf() for _ in range(10000)]
    valid = 0
    for cpf in cpfs:
        if len(cpf) == 14:
            cpf = cpf.replace('.', '')
            cpf = cpf.replace('-', '')
            if len(cpf) == 11:
                cpf_list = list([int(i) for i in cpf])
                original_cpf = cpf_list[:]
                first_verifying_digit = b.get_verifying_digit_cpf(cpf_list, 10)
                cpf_list.append(first_verifying_digit)
                cpf = ''.join([str(i) for i in cpf_list])

                second_verifying_digit = b.get_

# Generated at 2022-06-13 23:29:35.567246
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bp = BrazilSpecProvider()
    assert bp.cpf(with_mask=True) == '109.376.074-21'


# Generated at 2022-06-13 23:29:43.348160
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    cpf = BrazilSpecProvider().cpf()
    assert len(cpf) == 14
    assert cpf.count('.') == 2
    assert cpf.count('-') == 1
    assert cpf[-2] != '-'
    assert cpf[-1] != '.'
    assert cpf[3] == '.'
    assert cpf[7] == '.'
    assert cpf[11] == '-'

    cpf = BrazilSpecProvider().cpf(False)
    assert len(cpf) == 11
    assert cpf.count('.') == 0
    assert cpf.count('-') == 0
    

# Generated at 2022-06-13 23:29:52.279691
# Unit test for method cnpj of class BrazilSpecProvider

# Generated at 2022-06-13 23:29:53.906009
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    brazil = BrazilSpecProvider()
    assert(len(brazil.cnpj()) == 18)
    

# Generated at 2022-06-13 23:29:56.720387
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    brazil_provider = BrazilSpecProvider()
    assert brazil_provider.cpf() == '001.137.297-40'


# Generated at 2022-06-13 23:30:08.258145
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Tests for function cnpj of class BrazilSpecProvider.
    """
    for i in range(100):
        cnpj1 = BrazilSpecProvider().cnpj()[:-1]
        if cnpj1 in set(['00000000000000', '11111111111111', '22222222222222', '33333333333333', '44444444444444', '55555555555555', '66666666666666', '77777777777777', '88888888888888', '99999999999999']):
            print(cnpj1)
            assert True
        else:
            assert False
        cnpj2 = BrazilSpecProvider().cnpj()[:-1]

# Generated at 2022-06-13 23:30:12.347298
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    cnpj = provider.cnpj()
    assert len(cnpj) == 18
    assert cnpj.count('.') == 2
    assert cnpj.count('/') == 1
    assert cnpj.count('-') == 1

# Generated at 2022-06-13 23:30:16.614237
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Test for method cnpj of class BrazilSpecProvider."""
    provider = BrazilSpecProvider(seed=42)

    cnpj = provider.cnpj(with_mask=True)
    assert cnpj == '64.090.723/0001-60'

# Generated at 2022-06-13 23:30:27.897493
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    c = BrazilSpecProvider()
    cpf = c.cpf()
    assert(len(cpf) == 14)
    firstdv = int(cpf[9])
    seconddv = int(cpf[10])
    cpf = [int(i) for i in cpf[0:9]]
    cpf.append(firstdv)
    def get_verifying_digit_cpf(cpf, peso):
        """Calculate the verifying digit for the CPF.

        :param cpf: List of integers with the CPF.
        :param peso: Integer with the weight for the modulo 11 calculate.
        :returns: The verifying digit for the CPF.
        """
        soma = 0

# Generated at 2022-06-13 23:31:03.633279
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    b = BrazilSpecProvider()
    for i in range(10):
        cnpj = b.cnpj(with_mask=False)
        assert int(cnpj[12]) == b.get_verifying_digit(cnpj[:12], 6)
        assert (int(cnpj[13]) == b.get_verifying_digit(cnpj[:13], 5))


# Generated at 2022-06-13 23:31:07.435702
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    brazil_provider = BrazilSpecProvider()
    with_mask = brazil_provider.cnpj()
    without_mask = brazil_provider.cnpj(with_mask=False)
    # like this...
    # 55.120.060/0001-45
    # 55120060000145


# Generated at 2022-06-13 23:31:10.177600
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    result = provider.cnpj(with_mask=True)

    assert result is not None


# Generated at 2022-06-13 23:31:17.198896
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Test for BrazilSpecProvider class."""
    assert BrazilSpecProvider().cnpj(with_mask=True) == BrazilSpecProvider().cnpj(with_mask=True)
    assert BrazilSpecProvider().cnpj(with_mask=False) == BrazilSpecProvider().cnpj(with_mask=False)


# Generated at 2022-06-13 23:31:25.389972
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from mimesis.providers.brazil_provider import BrazilSpecProvider
    brazil_provider = BrazilSpecProvider()
    cnpj = brazil_provider.cnpj()
    cnpj_parts = cnpj.split('-')
    cnpj_digits = list(map(int, cnpj_parts[0].replace('.', '')))
    assert len(cnpj_digits) == 12

    first_dv = cnpj_digits[-2]
    expected_first_dv = BrazilSpecProvider.get_verifying_digit_cnpj(cnpj_digits[:-1], 5)
    assert first_dv == expected_first_dv

    second_dv = cnpj_digits[-1]
    expected_second_dv = Brazil

# Generated at 2022-06-13 23:31:28.726645
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    # check a fake cnpj
    assert not provider.cnpj('35.243.078/7482-78') # a true cnpj number

# Generated at 2022-06-13 23:31:33.010551
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    data = BrazilSpecProvider(seed=123456).cpf()
    assert isinstance(data, str)
    assert len(data) == 14
    assert data == '711.842.896-99'


# Generated at 2022-06-13 23:31:35.611060
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    value = BrazilSpecProvider().cnpj()
    assert type(value) == str
    assert len(value) == 18


# Generated at 2022-06-13 23:31:42.416660
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    import inspect
    from mimesis.providers.brazil import BrazilSpecProvider
    provider = BrazilSpecProvider()
    cpf_result = provider.cpf()
    assert '-' in cpf_result
    assert len(cpf_result) == 14
    assert isinstance(cpf_result, str)
    assert inspect.isfunction(provider.cpf)


# Generated at 2022-06-13 23:31:50.560696
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    provider = BrazilSpecProvider()
    person = Person('en')

    id = person.identifier(gender=Gender.MALE)
    expected = ('{0}.{1}.{2}-{3}'.format(id[0:3], id[3:6], id[6:9], id[10:11]),)
    assert provider.cpf() in expected



# Generated at 2022-06-13 23:33:10.769557
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Generate a random CPF and check if it is a valid CPF."""
    bsp = BrazilSpecProvider()
    cpf =  bsp.cpf()
    assert len(cpf) == 14
    assert cpf[:3].isdecimal()
    assert cpf[4:7].isdecimal()
    assert cpf[8:11].isdecimal()
    assert cpf[-2:].isdecimal()
    assert cpf[3] == '.'
    assert cpf[7] == '.'
    assert cpf[11] == '-'


# Generated at 2022-06-13 23:33:14.520420
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    test_cpf = BrazilSpecProvider()
    my_CPF = test_cpf.cpf()
    print(my_CPF)


# Generated at 2022-06-13 23:33:18.915863
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    x = provider.cnpj()
    assert isinstance(x, str)
    assert x == '77.732.230/0001-70'


# Generated at 2022-06-13 23:33:28.470298
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    # Format CRN, with mask
    crn = BrazilSpecProvider().cpf()
    assert crn[3] == '.', "The separator between the seconde and the third block of numbers must be the character '.', got '{}'".format(crn[3])
    assert crn[7] == '.', "The separator between the third and the fourth block of numbers must be the character '.', got '{}'".format(crn[7])
    assert crn[11] == '-', "The separator between the fourth block of numbers and the validator must be the character '-', got '{}'".format(crn[11])
    assert len(crn)-1 == 14, "The CPF must have 14 characters, got '{}'".format(len(crn)-1)

    # Format CRN

# Generated at 2022-06-13 23:33:31.959803
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    assert len(provider.cpf(with_mask=False)) == 11
    assert len(provider.cpf(with_mask=True)) == 14



# Generated at 2022-06-13 23:33:35.949350
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    obj = BrazilSpecProvider()
    cpf_with_mask = obj.cpf()
    digits = ''.join([str(i) for i in cpf_with_mask if str(i).isdigit()])
    assert len(digits) == 11, 'The CPF length is not valid ' + digits


# Generated at 2022-06-13 23:33:38.890514
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    assert len(provider.cpf()) == 14

# Generated at 2022-06-13 23:33:43.030319
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bz = BrazilSpecProvider()
    # 1.137.297-40
    cpf = bz.cpf()
    assert isinstance(cpf, str)
    # 0011312974
    cpf = bz.cpf(with_mask=False)
    assert isinstance(cpf, str)


# Generated at 2022-06-13 23:33:55.289613
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    import re
    import pytest
    from random import randint
    x = randint(1, 100)
    if x > 50:
        with_mask = True
    else:
        with_mask = False
    cnpj = BrazilSpecProvider().cnpj(with_mask)
    assert re.match('[0-9]{13,14}', cnpj)
    if with_mask:
        assert re.match('[0-9]{2}.[0-9]{3}.[0-9]{3}/[0-9]{4}-[0-9]{2}', cnpj)
    else:
        assert re.match('[0-9]{14}', cnpj)


# Generated at 2022-06-13 23:34:00.538716
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
	assert BrazilSpecProvider().cnpj() in [
		'52.896.597/0001-14',
		'34.054.637/0001-93',
		'47.141.727/0001-45',
		'44.932.233/0001-83',
		'97.184.373/0001-94'
	]

# Generated at 2022-06-13 23:37:25.477469
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from mimesis.providers.person.en import NLP
    nlp = NLP()
    bp = BrazilSpecProvider()
    assert isinstance(bp.cnpj(), str)
    assert len(bp.cnpj()) == 18
    assert len(bp.cnpj(False)) == 14
    assert nlp.is_valid_cnpj(bp.cnpj())
test_BrazilSpecProvider_cnpj()


# Generated at 2022-06-13 23:37:27.156951
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    cpf = BrazilSpecProvider().cpf()
    assert len(cpf) == 14


# Generated at 2022-06-13 23:37:35.264641
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    br = BrazilSpecProvider()
    cnpj = br.cnpj()

    cnpj_without_mask = cnpj.replace('.', '').replace('-', '').replace('/', '')
    cnpj_without_dv = cnpj_without_mask[:-2]

    first_dv = br._get_verifying_digit(cnpj_without_dv, 5)
    second_dv = br._get_verifying_digit(cnpj_without_dv + str(first_dv), 6)

    assert cnpj_without_mask[-2:] == str(first_dv) + str(second_dv)

# Generated at 2022-06-13 23:37:40.162208
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    assert len(provider.cpf()) == 14
    assert len(provider.cpf(with_mask=False)) == 11
    assert provider.cpf() == '556.881.358-96'
    assert provider.cpf(with_mask=False) == '55688135896'


# Generated at 2022-06-13 23:37:45.500588
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    b = BrazilSpecProvider(seed=0)
    assert b.cnpj(with_mask=True) == '77.732.230/0001-70'
    assert b.cnpj(with_mask=False) == '77732230000170'


# Generated at 2022-06-13 23:37:51.378765
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    instance = BrazilSpecProvider()

    # Check whether the result is a CNPJ
    pattern = re.compile(r'[0-9]{2}\.[0-9]{3}\.[0-9]{3}\/[0-9]{4}-[0-9]{2}')
    assert pattern.match(instance.cnpj())

    # Check whether the result is a CNPJ without mask
    pattern = re.compile(r'[0-9]{14}')
    assert pattern.match(instance.cnpj(with_mask=False))

# Generated at 2022-06-13 23:37:56.118878
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    expect = '77.732.230/0001-70'
    actual = BrazilSpecProvider().cnpj()
    assert expect == actual

# Generated at 2022-06-13 23:38:03.984024
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    assert BrazilSpecProvider().cnpj(with_mask = False) == '77732230000170'


# Generated at 2022-06-13 23:38:07.107726
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    cpf = provider.cpf()
    assert len(cpf) == 14 and cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-'

# Generated at 2022-06-13 23:38:09.006279
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    loc = BrazilSpecProvider(seed=1)
    assert loc.cnpj() == '77.732.230/0001-70'
