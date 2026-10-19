

# Generated at 2022-06-13 23:28:40.839985
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Unit test for method cpf of class BrazilSpecProvider"""
    brazil_spec_provider = BrazilSpecProvider(seed=1)

    cpf_list = []
    for _ in range(1):
        cpf_list.append(brazil_spec_provider.cpf())


# Generated at 2022-06-13 23:28:44.776150
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from mimesis.providers.brazil import BrazilSpecProvider as BS

    instance = BS()
    cnpj = instance.cnpj(with_mask = False)
    assert len(cnpj) == 14


# Generated at 2022-06-13 23:28:49.003048
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.providers.brazil_provider import BrazilSpecProvider
    br = BrazilSpecProvider()
    p1 = br.cpf()
    assert len(p1) == 14
    p2 = br.cpf(with_mask=0)
    assert len(p2) == 11


# Generated at 2022-06-13 23:28:52.077886
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    import mimesis

    d = mimesis.BrazilSpecProvider(seed=1337)

    assert d.cnpj(with_mask=True) == '64.024.728/0001-41'


# Generated at 2022-06-13 23:28:53.720964
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    assert BrazilSpecProvider().cpf() == '399.453.893-30'



# Generated at 2022-06-13 23:28:59.585496
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
  with open('cnpj.txt', 'r') as file_handle:
    cnpjs = file_handle.readlines()
    for i, line in enumerate(cnpjs):
      cnpj = line.strip()
      brazil_spec_provider = BrazilSpecProvider()
      assert cnpj == brazil_spec_provider.cnpj(with_mask=False)
      print("Success: {}".format(i))

if __name__ == '__main__':
    test_BrazilSpecProvider_cnpj()
    print("test cases ran successfully")

# Generated at 2022-06-13 23:29:02.082298
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    assert provider.cpf() == '001.137.297-40'


# Generated at 2022-06-13 23:29:13.429783
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Test for BrazilSpecProvider.cnpj()."""
    bsp = BrazilSpecProvider()
    cnpj = bsp.cnpj()
    assert len(cnpj) == 18
    assert bsp.cnpj() != bsp.cnpj()
    cnpj_without_dv = cnpj[:2] + cnpj[3:6] + cnpj[7:10] + cnpj[11:15]

    cnpj_without_dv = [int(i) for i in cnpj_without_dv]

    assert int(cnpj[16]) == bsp._calc_v1(cnpj_without_dv, [5, 4, 3, 2, 9, 8, 7,
                                                           6, 5, 4, 3, 2])


# Generated at 2022-06-13 23:29:19.735464
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test cpf method of BrazilSpecProvider class."""
    cpf_pattern = re.compile(r'\d{3}.\d{3}.\d{3}-\d{2}')
    brazil = BrazilSpecProvider()
    assert cpf_pattern.match(brazil.cpf())


# Generated at 2022-06-13 23:29:23.224656
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from mimesis.builtins import BrazilSpecProvider
    bsp = BrazilSpecProvider()
    assert bsp.cnpj() == bsp.cnpj()


# Generated at 2022-06-13 23:29:31.930315
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.builtins.brazil import BrazilSpecProvider
    brazil = BrazilSpecProvider()
    cpf =  brazil.cpf()
    print(cpf)
    assert len(cpf) == 14


# Generated at 2022-06-13 23:29:36.092849
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Test method cnpj of BrazilianSpecProvider class."""
    brazil_cnpj = BrazilSpecProvider().cnpj(False)
    assert len(brazil_cnpj) == 14

# Generated at 2022-06-13 23:29:40.577072
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    # given
    provider = BrazilSpecProvider()

    # when
    cpf = provider.cpf()

    # then
    assert len(cpf) == 14
    assert cpf == provider.cpf(with_mask=True)


# Generated at 2022-06-13 23:29:50.881286
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Test method cnpj of class BrazilSpecProvider."""
    from mimesis.providers.brazil import BrazilSpecProvider
    from mimesis.enums import Gender
    from mimesis.locales import Locale
    import re
    provider = BrazilSpecProvider(seed='123456789')
    # Test without mask
    cnpj = provider.cnpj(False)
    assert cnpj[-2:] == "08"
    cnpj = provider.cnpj() # With mask
    assert cnpj[-2:] == "08"
    assert re.match(r"([0-9]{2})\.?([0-9]{3})\.?([0-9]{3})\/?([0-9]{4})-?([0-9]{2})$", cnpj)


# Generated at 2022-06-13 23:29:54.038647
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test method BrazilSpecProvider.cpf."""
    assert BrazilSpecProvider().cpf(False) == '31944852797'
    assert BrazilSpecProvider().cpf(True) == '319.448.527-97'


# Generated at 2022-06-13 23:29:57.339004
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bsp = BrazilSpecProvider()
    assert len(bsp.cpf()) == 14
    assert len(bsp.cpf(with_mask=False)) == 11


# Generated at 2022-06-13 23:30:08.684921
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test for the BrazilSpecProvider.cpf() method."""
    provider = BrazilSpecProvider()

    cpf = provider.cpf()
    assert isinstance(cpf, str)
    assert len(cpf) == 14
    assert cpf[3] == '.'
    assert cpf[7] == '.'
    assert cpf[11] == '-'
    cpf_without_mask = cpf.replace('.', '').replace('-', '')
    assert cpf_without_mask.isdigit()
    assert len(cpf_without_mask) == 11

    cpf = provider.cpf(with_mask=False)
    assert isinstance(cpf, str)
    assert len(cpf) == 11
    assert cpf.isdigit()



# Generated at 2022-06-13 23:30:11.716422
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    cpf = provider.cpf()
    print("cpf: {}".format(cpf))
    assert cpf is not None


# Generated at 2022-06-13 23:30:12.963888
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    print("\n%s" % BrazilSpecProvider().cpf())


# Generated at 2022-06-13 23:30:19.545793
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    print("Testing BrazilSpecProvider.cnpj()")
    bsp = BrazilSpecProvider()
    cnpj1 = bsp.cnpj()
    print("Passed test. cnpj={}".format(cnpj1))
    cnpj2 = bsp.cnpj()
    print("Passed test. cnpj={}".format(cnpj2))


# Generated at 2022-06-13 23:30:38.731014
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test of the method cpf of class BrazilSpecProvider."""
    provider = BrazilSpecProvider

    cpf1 = provider.cpf(True)
    assert len(cpf1) == 14
    assert type(cpf1) == str

    cpf2 = provider.cpf(True)
    assert len(cpf2) == 14
    assert type(cpf2) == str


# Generated at 2022-06-13 23:30:42.305288
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.builtins import BrazilSpecProvider
    cpf = BrazilSpecProvider().cpf()
    assert len(cpf) == 14


# Generated at 2022-06-13 23:30:50.779371
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    cpf = BrazilSpecProvider().cpf()
    assert len(cpf) == 14
    assert cpf[3] == "."
    assert cpf[7] == "."
    assert cpf[11] == "-"
    assert cpf[:3].isdigit()
    assert cpf[4:7].isdigit()
    assert cpf[8:11].isdigit()
    assert cpf[12:].isdigit()
    assert cpf[12:] == BrazilSpecProvider().cpf(with_mask=False)[-2:]


# Generated at 2022-06-13 23:30:56.041000
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Test method cnpj of class BrazilSpecProvider."""
    bzsp = BrazilSpecProvider()
    cnpj_1 = bzsp.cnpj()
    assert len(cnpj_1) == 18

    cnpj_2 = bzsp.cnpj(with_mask=False)
    assert len(cnpj_2) == 14


# Generated at 2022-06-13 23:31:03.162299
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Unit test method cnpj of class BrazilSpecProvider."""
    import re
    brazil_provider = BrazilSpecProvider
    args = [True]
    cnpj_with_mask = brazil_provider(seed=42).cnpj(*args)
    assert len(cnpj_with_mask) == 18
    assert re.match(r"^\d{2}\.\d{3}\.\d{3}\/\d{4}\-\d{2}$", cnpj_with_mask)
    cnpj_without_mask = brazil_provider(seed=42).cnpj(with_mask=False)
    assert len(cnpj_without_mask) == 14
    assert re.match(r"^\d{14}$", cnpj_without_mask)

# Generated at 2022-06-13 23:31:06.551828
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    p = BrazilSpecProvider()
    for _ in range(5):
        cpf = p.cpf()
        assert cpf[3] == '.'
        assert cpf[7] == '.'
        assert cpf[11] == '-'


# Generated at 2022-06-13 23:31:09.850557
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    cpf = BrazilSpecProvider().cpf()
    print(cpf)
    if cpf != None and len(cpf) == 14:
        assert True
    else:
        assert False


# Generated at 2022-06-13 23:31:16.741574
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    cnpj = provider.cnpj(with_mask=False)
    print("CNPJ: {c}".format(c=cnpj))
    assert len(cnpj) == 14
    assert type(cnpj) == str

test_BrazilSpecProvider_cnpj()


# Generated at 2022-06-13 23:31:23.023539
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    t = BrazilSpecProvider()
    assert len(t.cpf()) == 14
    assert t.cpf(with_mask=False) is not None
    assert t.cpf(with_mask=False) != t.cpf(with_mask=False)
    assert t.cpf() != t.cpf()
    assert t.cpf(with_mask=False) != t.cpf(with_mask=True)


# Generated at 2022-06-13 23:31:28.166492
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    cpf = BrazilSpecProvider().cpf()
    assert len(cpf) == 14  # CPF has 11 digits + 3 dots + ending dash

    cpf = BrazilSpecProvider().cpf(False)
    assert len(cpf) == 11  # CPF has 11 digits



# Generated at 2022-06-13 23:31:57.180943
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    cpf = BrazilSpecProvider().cpf()
    assert cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-'
    

# Generated at 2022-06-13 23:32:00.312952
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    cnpjs = []
    bsp = BrazilSpecProvider()
    for _ in range(10):
        cnpjs.append(bsp.cnpj())
    assert cnpjs

# Generated at 2022-06-13 23:32:04.695554
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    b = BrazilSpecProvider()
    cpf = b.cpf()
    assert len(cpf) == 14
    assert cpf[3] == '.'
    assert cpf[7] == '.'
    assert cpf[11] == '-'
    cpf = b.cpf(with_mask=False)
    assert len(cpf) == 11
    dic = {}
    for _ in range(1000):
        cpf = b.cpf(with_mask=False)
        dic[cpf] = True
    assert len(dic) == 1000

# Generated at 2022-06-13 23:32:06.745184
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    assert BrazilSpecProvider().cpf() != BrazilSpecProvider().cpf()

# Generated at 2022-06-13 23:32:11.269588
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Unit test for method cpf of class BrazilSpecProvider."""
    x1 = BrazilSpecProvider.cpf(with_mask=False)
    x2 = BrazilSpecProvider.cpf(with_mask=True)
    assert x1 != x2


# Generated at 2022-06-13 23:32:15.698116
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Unit test for method cpf of class BrazilSpecProvider."""
    spec_ptbr = BrazilSpecProvider()

    assert len(spec_ptbr.cpf(with_mask=False)) == 11
    assert len(spec_ptbr.cpf()) == 14


# Generated at 2022-06-13 23:32:17.043228
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    br = BrazilSpecProvider()
    print(br.cnpj())

# Generated at 2022-06-13 23:32:20.947007
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider(seed=123)
    assert provider.cpf() == '231.419.871-94'
    assert provider.cpf(with_mask=False) == '2314198871'


# Generated at 2022-06-13 23:32:24.085295
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    brazil_provider = BrazilSpecProvider()
    random = brazil_provider.cnpj()
    assert len(random) == 18
    assert random[-2].isdigit()
    assert random[-1].isdigit()


# Generated at 2022-06-13 23:32:35.352453
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """
    Check if function cnpj generates a valid brazilian cnpj
    """
    from random import Random
    random = Random()
    from mimesis.providers.brazil_provider import BrazilSpecProvider
    bsp = BrazilSpecProvider(random)
    cnpj = bsp.cnpj()

    assert cnpj.count(".") == 2
    assert cnpj.count("-") == 1
    assert cnpj.count("/") == 1
    assert cnpj.count("0") == 13
    assert cnpj.count("1") == 13
    assert cnpj.count("2") == 13
    assert cnpj.count("3") == 13
    assert cnpj.count("4") == 13
    assert cnpj.count("5") == 13
    assert cnpj

# Generated at 2022-06-13 23:33:44.033480
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    # Case 1
    assert BrazilSpecProvider().cpf() == '755.837.998-75'

    # Case 2
    assert BrazilSpecProvider(seed=1).cpf() == "895.379.169-79"

    # Case 3
    assert BrazilSpecProvider().cpf(with_mask=False) == '14147082219'



# Generated at 2022-06-13 23:33:57.740151
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():

    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    p = Person('pt-br')

    # https://pt.wikipedia.org/wiki/C%C3%B3digo_de_inscri%C3%A7%C3%A3o_no_Cadastro_Nacional_de_Pessoas_Jur%C3%ADdicas
    # 0x1-0x2: Estado do Cadastro Nacional de Pessoas Jurídicas

    # Looping states
    states = p.address.us_state_abbr.keys()
    for state in states:
        cnpj = p.brazil_provider.cnpj(with_mask=False)
        cnpj = cnpj[0:2]

# Generated at 2022-06-13 23:34:00.418899
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    import pytest

    from mimesis.providers.brazil import BrazilSpecProvider

    b = BrazilSpecProvider()

    assert len(b.cpf().split('.')[-1].split('-')[-1]) == 2


# Generated at 2022-06-13 23:34:03.184019
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    obj = BrazilSpecProvider()
    x = obj.cpf(with_mask=True)
    assert len(x) == 14
    assert x[3] == x[7] == '.'
    assert x[11] == '-'


# Generated at 2022-06-13 23:34:08.189978
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test BrazilSpecProvider class and method cpf."""
    assert len(BrazilSpecProvider().cpf()) == 14
    assert len(BrazilSpecProvider().cpf(with_mask=False)) == 11
    assert BrazilSpecProvider().cpf() != BrazilSpecProvider().cpf()


# Generated at 2022-06-13 23:34:10.274583
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test method cpf from BrazilSpecProvider."""
    from mimesis.enums import Gender
    from mimesis.providers import Person

    person = Person('pt-br')
    gender = person.gender(gender=Gender.MALE)
    person.cpf(gender)
    person.cnpj()

# Generated at 2022-06-13 23:34:13.755288
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bras = BrazilSpecProvider()
    assert bras.cpf() == '838.915.588-09'
    assert bras.cpf(with_mask=False) == '83891558809'



# Generated at 2022-06-13 23:34:16.488918
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    result = provider.cnpj(with_mask=True)
    assert len(result) == 18
    assert result == "77.732.230/0001-70"

# Generated at 2022-06-13 23:34:22.363199
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    brazil = BrazilSpecProvider()
    cpf_without_mask = brazil.cpf(with_mask=False)
    print('CPF with no mask is', cpf_without_mask)
    cpf_with_mask = brazil.cpf(with_mask=True)
    print('CPF with mask is', cpf_with_mask)
    assert len(cpf_without_mask) == 11



# Generated at 2022-06-13 23:34:27.210941
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    c = BrazilSpecProvider()
    cnpj = c.cnpj()
    assert(len(cnpj) == 18)
    assert(cnpj[2] == '.')
    assert(cnpj[6] == '.')
    assert(cnpj[10] == '/')
    assert(cnpj[15] == '-')


# Generated at 2022-06-13 23:37:41.716896
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    spec = BrazilSpecProvider(seed=5)
    assert spec.cpf() == '957.674.560-75'


# Generated at 2022-06-13 23:37:44.294081
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from pprint import pprint

    provider = BrazilSpecProvider()
    pprint(provider.cpf())

# Generated at 2022-06-13 23:37:48.618834
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Unit test method cpf of class BrazilSpecProvider."""
    providers = BrazilSpecProvider()
    cpf = providers.cpf()
    assert len(cpf) == 14



# Generated at 2022-06-13 23:37:50.814873
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    cpf = provider.cpf(with_mask=False)
    assert cpf != ''


# Generated at 2022-06-13 23:37:56.853060
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Unit test for method cpf of class BrazilSpecProvider."""
    provider = BrazilSpecProvider()
    assert provider.cpf(True) == '51.972.257-57'


# Generated at 2022-06-13 23:38:03.984345
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    b = BrazilSpecProvider()
    cnpj = b.cnpj()
    assert len(cnpj) == 18
    assert cnpj.count('.') == 2
    assert cnpj.count('/') == 1
    assert cnpj.count('-') == 1
    cnpj = cnpj.replace('.', '')
    cnpj = cnpj.replace('/', '')
    cnpj = cnpj.replace('-', '')
    soma_1 = 0
    soma_2 = 0
    peso_1 = 5
    peso_2 = 6
    for digit in cnpj[:-2]:
        soma_1 += int(digit) * peso_1
        soma_2 += int(digit) * peso_2
        peso_1

# Generated at 2022-06-13 23:38:06.466159
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    cnpj = provider.cnpj()
    assert len(cnpj) == 18
    cnpj_no_mask = provider.cnpj(with_mask=False)
    assert len(cnpj_no_mask) == 14


# Generated at 2022-06-13 23:38:10.177511
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Test method cnpj of class BrazilSpecProvider."""
    provider = BrazilSpecProvider("seed")
    bs = lambda x: isinstance(x, str) and len(x) == 18
    assert all(bs(provider.cnpj()) for _ in range(1000))

# Generated at 2022-06-13 23:38:14.381324
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Unit test for method cpf of class BrazilSpecProvider."""
    b = BrazilSpecProvider()
    cpf = b.cpf()
    assert type(cpf) is str
    assert len(cpf) == 14 and len(cpf.replace(".", "").replace("-", "")) == 11
    

# Generated at 2022-06-13 23:38:19.205185
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    b = BrazilSpecProvider()
    expected = "063.628.077-81"
    generated_cpf = b.cpf()
    assert len(generated_cpf) == 14
    generated_cpf_without_mask = b.cpf(with_mask=False)
    assert len(generated_cpf_without_mask) == 11
    assert generated_cpf == expected, "CPF should be {}"

