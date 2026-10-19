

# Generated at 2022-06-22 11:50:48.061166
# Unit test for function do_unvault
def test_do_unvault():
    import jinja2
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.vault import VaultEditor
    from ansible.utils.path import unfrackpath

    filter_plugin = FilterModule()
    env = jinja2.Environment()
    env.filters.update(filter_plugin.filters())

    plain_text = AnsibleUnicode('Hello World')
    secret = unfrackpath('~/.vault_pass.txt')
    vaultid = 'test'

    # Encrypt and decrypt
    plain = AnsibleUnicode(do_unvault(do_vault(plain_text, secret, vaultid), secret, vaultid))
    assert plain == plain_text, 'Unvaulting does not produce the same value for plain text'

    #

# Generated at 2022-06-22 11:50:56.413737
# Unit test for function do_unvault

# Generated at 2022-06-22 11:51:07.272667
# Unit test for function do_vault
def test_do_vault():
    from ansible.plugins.filter import vault as vault_filter
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    # typical vault string

# Generated at 2022-06-22 11:51:18.760572
# Unit test for function do_unvault

# Generated at 2022-06-22 11:51:31.263059
# Unit test for function do_unvault

# Generated at 2022-06-22 11:51:39.327040
# Unit test for function do_unvault
def test_do_unvault():
    import pytest

    secret = 'This is a big secret'

    with pytest.raises(AnsibleFilterTypeError) as excinfo:
        do_unvault(42, secret)

    assert "Vault should be in the form of a string, instead we got" in str(excinfo.value), "Testcase TypError failed"

    with pytest.raises(AnsibleFilterTypeError) as excinfo:
        do_unvault("vault", 42)

    assert "Secret passed is required to be as string, instead we got" in str(excinfo.value), "Testcase TypError failed"

    vault = do_vault("This is a secret", secret)

    assert do_unvault(vault, secret) == "This is a secret"

    # Wrong secret, should fail

# Generated at 2022-06-22 11:51:45.489813
# Unit test for function do_unvault
def test_do_unvault():
    assert do_unvault("$ANSIBLE_VAULT;9.9;AES256;vault8371689910\nc2FtcGxlCg==\n", secret="ouaf") == "sample"
    assert do_unvault("sample", secret="ouaf") == "sample"

# Generated at 2022-06-22 11:51:55.718750
# Unit test for function do_unvault

# Generated at 2022-06-22 11:52:07.787243
# Unit test for function do_unvault

# Generated at 2022-06-22 11:52:15.160934
# Unit test for function do_unvault
def test_do_unvault():
    from nose.tools import assert_equals

    # Test with wrapped secret

# Generated at 2022-06-22 11:52:26.636777
# Unit test for function do_unvault

# Generated at 2022-06-22 11:52:38.140406
# Unit test for function do_vault

# Generated at 2022-06-22 11:52:51.280491
# Unit test for function do_vault

# Generated at 2022-06-22 11:52:55.493933
# Unit test for function do_vault
def test_do_vault():
    result = do_vault('value', 'secret')
    assert isinstance(result, AnsibleVaultEncryptedUnicode)

    result = do_vault('value', 'secret', wrap_object=False)
    assert isinstance(result, string_types)


# Generated at 2022-06-22 11:53:06.352659
# Unit test for function do_vault
def test_do_vault():
    secret = 'secret'
    salt = 'salt'
    data = 'data'
    test = do_vault(data, secret, salt)
    if test != "$ANSIBLE_VAULT;1.1;AES256\r\n30616566306538613933356161396137656436396135653034326166623265366639366336386232\r\n61633565346337656366326438393833386462633166383435633032323337666535363730613062\r\n303631376236313866626162633665623661633535333366653734303635323536\r\n":
        raise AssertionError


# Generated at 2022-06-22 11:53:11.496859
# Unit test for function do_unvault
def test_do_unvault():
    data = '54321'
    passwd = '12345'
    try:
        result = do_vault(data, passwd, wrap_object=False)
        assert is_encrypted(result)
        assert do_unvault(result, passwd) == data
    except Exception as e:
        assert False

# Generated at 2022-06-22 11:53:17.703896
# Unit test for function do_vault
def test_do_vault():
    data = "mytest"
    secret = "mysecret"

    vault = do_vault(data, secret)
    assert isinstance(vault, string_types)
    assert is_encrypted(vault)
    assert vault != data

    vault = do_vault(data, secret, wrap_object=True)
    assert isinstance(vault, AnsibleVaultEncryptedUnicode)
    assert is_encrypted(vault)
    assert vault.data == data
    assert vault != data



# Generated at 2022-06-22 11:53:29.902196
# Unit test for function do_unvault
def test_do_unvault():
    vault_secrets = []
    vault_secrets.append(VaultSecret('foo'))
    vault_secrets.append(VaultSecret('bar'))
    vault_secrets.append(VaultSecret('baz'))
    vault_lib = VaultLib(vault_secrets)

    test_string = u'example plain string'

# Generated at 2022-06-22 11:53:40.293470
# Unit test for function do_vault
def test_do_vault():
    assert do_vault("foobar", "vault_password", "salt") == '$ANSIBLE_VAULT;1.1;AES256;salt\npOGf1Sn6yjC6bP0Lkav2xjK5o5ZV+5u5J5qV7wvKj+g=\n'
    assert do_vault("foobar", "vault_password") == '$ANSIBLE_VAULT;1.1;AES256\nuAiYY4z4ZdYKjHzkShQuJF6Cvw6/cK6CiU/Gof/6QvM=\n'

# Generated at 2022-06-22 11:53:47.224055
# Unit test for function do_unvault
def test_do_unvault():
    # case 1: plain text
    plain = to_native("this is a plain text")
    assert plain == do_unvault(plain, "password")
    # case 2: vault with encoding: utf8

# Generated at 2022-06-22 11:53:59.616467
# Unit test for function do_vault
def test_do_vault():
    secret = 'dude'
    data = 'mydata'
    vault = do_vault(data, secret)
    # vault should be an instance of AnsibleVaultEncryptedUnicode
    assert type(vault) == AnsibleVaultEncryptedUnicode
    assert vault.data == data
    assert vault.vault == None
    # 2nd argument is not a string
    try:
        vault = do_vault(data, 1)
    except AnsibleFilterTypeError as e:
        pass
    # 3rd argument is not a string
    try:
        vault = do_vault(data, secret, 1)
    except AnsibleFilterTypeError as e:
        pass


# Generated at 2022-06-22 11:54:11.002798
# Unit test for function do_vault
def test_do_vault():
    vault_secret = do_vault('example', 'ansible')
    assert vault_secret == '$ANSIBLE_VAULT;1.1;AES256\n313166376136313963343933613364333730666530333366356530653233663234616537336230\n3539323039373063333466613632376264616336620a6465366333623763333462613961376364\n613162333731623662646336633036383832623166643639356162636131393433376435313663\n6332653035393031'
    # Decrypt the vault secret
    plain_secret = do_unvault(vault_secret, 'ansible')
    assert plain_secret == 'example'

# Generated at 2022-06-22 11:54:19.893825
# Unit test for function do_unvault

# Generated at 2022-06-22 11:54:30.773165
# Unit test for function do_vault
def test_do_vault():
    import jinja2
    env = jinja2.Environment()
    # test 1
    secret = 'secret'
    text = 'data to encrypt'

# Generated at 2022-06-22 11:54:41.418144
# Unit test for function do_unvault

# Generated at 2022-06-22 11:54:53.459108
# Unit test for function do_unvault
def test_do_unvault():
  secret = 'password'
  vaultid = 'filter_default'
  vault = '$ANSIBLE_VAULT;1.1;AES256\n35653435306531666362316665333433663533366632323338303533623031643134303562303130\n3463646566623863623961303937386534376562393064393432663233643033346331356437343064\n3962333132613362323964383032376434303564353565643734396234393331396264383363396639\n64346334353436356564653835643336396234343265663962'
  expected = 'The quick brown fox jumps over the lazy dog.'
  result = do_unv

# Generated at 2022-06-22 11:55:05.070955
# Unit test for function do_unvault
def test_do_unvault():
    from ansible.module_utils.parsing.convert_bool import boolean

# Generated at 2022-06-22 11:55:13.028880
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('foo', 'bar', wrap_object=True) == '$ANSIBLE_VAULT;1.2;AES256;default;default\n396333336138653839383764663133326130373462366537333066326164646666666363366\n363333666303964653537616232633564363132366431323832643463373763346634646466\n6535393161336138613231656336653961\n'

# Generated at 2022-06-22 11:55:24.473419
# Unit test for function do_vault
def test_do_vault():
    secret = "thisismysecret"
    data = "thisisthedata"
    salt = "0123456789abcdef"
    vault = do_vault(data, secret, salt)

# Generated at 2022-06-22 11:55:32.224657
# Unit test for function do_vault
def test_do_vault():
    f = FilterModule()
    actual = f.filters()['vault']('foobar', 'foosecret', wrap_object=False)
    expected = '$ANSIBLE_VAULT;1.2;AES256;default\n32336262356262316538323937303933376633376231326139323231646330303433633162316537\n313633303466636432353539313331613266623165656639303365353062376366363336339626533\n36333739343063326133666438663036313766346466323430343339396466636363323230656431\n346665336462383737646634376431\n'
    assert actual == expected

    actual

# Generated at 2022-06-22 11:55:43.788135
# Unit test for function do_unvault

# Generated at 2022-06-22 11:55:55.332939
# Unit test for function do_unvault
def test_do_unvault():
    assert do_unvault('$ANSIBLE_VAULT;1.1;AES256;test\n63306134363866303264653763396666653135316439636561316432353636386539343834633563\n30363166393132633139623761636663376139663436356637660a35343164633138666134626365\n62343835653936363631376665303466303638656430333932356662363263323933326137303265\n6638643666396265633361640a323465353364343039383262623532643861306635656565613737\n3533666661663612', 'test') == 'hello world!'


# Generated at 2022-06-22 11:55:57.265678
# Unit test for function do_vault
def test_do_vault():
    secret = str("testpass")
    assert do_vault("hello world", secret) != "hello world"


# Generated at 2022-06-22 11:56:02.244505
# Unit test for function do_unvault
def test_do_unvault():
    test_vault = '$ANSIBLE_VAULT;1.1;AES256'
    test_secret = 'hunter2'
    test_vaultid = 'filter_default'
    assert do_unvault(test_vault, test_secret, test_vaultid) == ''

# Generated at 2022-06-22 11:56:10.768692
# Unit test for function do_unvault
def test_do_unvault():
    secret = 'secret'
    vaultid = 'filter_default'

# Generated at 2022-06-22 11:56:22.774103
# Unit test for function do_vault
def test_do_vault():
    secret = "tajneHasloTajneHasloTajneHasloTajneHaslo"
    data="HelloWorld"

# Generated at 2022-06-22 11:56:34.745365
# Unit test for function do_unvault
def test_do_unvault():
    assert do_unvault("$ANSIBLE_VAULT;1.1;AES256;test\n38333934636530363131303937613831376330396233346765333330663332356237396532623761\n336161633139613661346266313566616232333831376236630a3565376436363837343765643932\n37643533663061663039393538666437623663616261366431646231396236633038653236643865\n656639643466306437610a", "test") == "test"

# Generated at 2022-06-22 11:56:44.423224
# Unit test for function do_vault
def test_do_vault():
    # Valid case
    secret = 'passw0rd'
    data = 'hello world'
    expected = '$ANSIBLE_VAULT;1.2;AES256;filter_default\n353038333163346632383537353839326262383766373161633238633834613861336637363835623839\n62336536653536343766346230663338346665383635653035343033626634623531653133363965666461\n6435633866643262366631613761336266323336653964353335343939653563307d0a'
    actual = do_vault(data, secret)
    assert expected == actual
    # Valid case: with salt
    salt = 'this is salt'


# Generated at 2022-06-22 11:56:55.969917
# Unit test for function do_vault

# Generated at 2022-06-22 11:57:06.731117
# Unit test for function do_unvault
def test_do_unvault():
    secret = "secret"

# Generated at 2022-06-22 11:57:16.100426
# Unit test for function do_unvault
def test_do_unvault():
    assert do_unvault('$ANSIBLE_VAULT;1.1;AES256;ansible\r\n35393662383262643133313239656232303237613566363464333839633363383961626537\r\n39376661306466393933353465336336626537623661303439653361306639336138623265\r\n32653532616335623062616662393961623233313\r\n', 'topsecret') == '1234567890'

# Generated at 2022-06-22 11:57:27.011762
# Unit test for function do_unvault
def test_do_unvault():
    vault = '$ANSIBLE_VAULT;1.1;AES256;jdoe'
    salt = binascii.unhexlify(b'4d29a0cf1f4e1a84')
    hmac = binascii.unhexlify(b'c47ebdc1574be291a0e3b0f7a3c35a2255b908c3f3a7d3e8b2e7e03a66b88daf')
    iv = binascii.unhexlify(b'567bd8226f95e5c68d2a5cce27f87944')

# Generated at 2022-06-22 11:57:39.310503
# Unit test for function do_unvault
def test_do_unvault():
    import os

    # TODO: Improve this test.
    secretFiles = [
        '~/.vault_pass.txt',
        '~/ansible_test.txt',
        '~/ansible_test.yml'
    ]

    for file in secretFiles:
        if os.path.isfile(os.path.expanduser(file)):
            os.remove(os.path.expanduser(file))

    secrets = {
        '12345678': 'secret_password',
        '87654321': 'other_password',
        '123': 'simple_password'
    }

    passwdfile = open(os.path.expanduser(secretFiles[0]), 'a')

# Generated at 2022-06-22 11:57:48.944857
# Unit test for function do_unvault
def test_do_unvault():
    # Case 1: argument of vault as string
    secret = "12345678901234567890123456789012"
    vaultid = "test_default"

# Generated at 2022-06-22 11:57:53.512310
# Unit test for function do_vault
def test_do_vault():
    display.debug("Testing Ansible Vault Jinja2 filters")
    vault_string = do_vault('foo', 'bar', 'salt')
    assert is_encrypted(vault_string)
    assert '$ANSIBLE_VAULT;' in vault_string


# Generated at 2022-06-22 11:58:00.907212
# Unit test for function do_unvault
def test_do_unvault():
    assert do_unvault('$ANSIBLE_VAULT;1.1;AES256\n633565343332353065626134333965663037316533633238636233326238613062316362333934\n323239386131613238393335653137343462373465393638393838326137356664653739663065\n333261366265\n', 'testsecret') == 'this is my secret'

# Generated at 2022-06-22 11:58:07.863942
# Unit test for function do_vault

# Generated at 2022-06-22 11:58:19.784213
# Unit test for function do_vault
def test_do_vault():
    # Check to see that we encrypt a string correctly
    test_vault = do_vault(data='this is some stuff to encrypt', secret='password', wrap_object=False)

# Generated at 2022-06-22 11:58:31.162912
# Unit test for function do_vault
def test_do_vault():
    testdata = 'hello world'
    testsecret = 'ansible'
    vault = do_vault(testdata, testsecret)

# Generated at 2022-06-22 11:58:39.043700
# Unit test for function do_unvault
def test_do_unvault():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    test_value = b'$ANSIBLE_VAULT;1.1;AES256\n66393636326135623532363739353437633231653361626234333166636639386136613835316464\n31366362323964363334623835313332633761396435383464396662663866303235356634393233\n343731383038396665326336343662623631396334366566633066366262616132000a\n'
    result = do_unvault(test_value, 'foo')
    assert result == 'junk'


# Generated at 2022-06-22 11:58:52.364430
# Unit test for function do_unvault
def test_do_unvault():
    secret = "somepassword"
    vault = "$ANSIBLE_VAULT;1.1;AES256\n353737653366313139366565363439353734333132313832316539303361616637336562396365\n346537643636323162656136633431366162373239373735303230393634333035643834653534\n33346633306234303533300a303233376531383439333830323535333531343466313436393466\n646239393239616139333332623535363765303562356332646538343838326263303335366635\n3030326336393565383032\n"

# Generated at 2022-06-22 11:59:03.758877
# Unit test for function do_vault
def test_do_vault():
    from ansible.plugins.filter.vault import FilterModule
    import pytest


# Generated at 2022-06-22 11:59:11.969138
# Unit test for function do_unvault
def test_do_unvault():
    secret = 'SECRET_KEY'

# Generated at 2022-06-22 11:59:17.350053
# Unit test for function do_vault
def test_do_vault():
    secret = 'password'
    salt = 'secret'
    vaultid = 'filter_default'
    plain_data = 'Ansible is awesome!'

# Generated at 2022-06-22 11:59:20.584897
# Unit test for function do_vault
def test_do_vault():
    secret = 'some-secret'
    input_data = 'some-data'
    result = do_vault(input_data, secret)
    assert '$ANSIBLE_VAULT' in result


# Generated at 2022-06-22 11:59:29.646543
# Unit test for function do_vault

# Generated at 2022-06-22 11:59:39.957819
# Unit test for function do_vault
def test_do_vault():
    import ansible.module_utils.vault
    import copy
    secret = 'test'
    salt = 'test'
    vaultid = 'filter_default'
    try:
        ansible.module_utils.vault.do_vault(secret, secret, salt, vaultid)
    except Exception as e:
        assert isinstance(e, AnsibleFilterTypeError)
    data = 'test'
    assert len(ansible.module_utils.vault.do_vault(data, secret, salt, vaultid)) == 125
    assert ansible.module_utils.vault.do_vault(data, secret, salt, vaultid, wrap_object=True).type == 'ANSIBLE_VAULT'
    salt = 'test'
    secret = VaultSecret(secret)

# Generated at 2022-06-22 11:59:51.151301
# Unit test for function do_vault
def test_do_vault():

    # Test 1
    data1 = do_vault('test', 'ansible')
    assert data1.startswith('$ANSIBLE_VAULT;') is True

    # Test 2
    data2 = 'test'
    assert is_encrypted(data2) is False
    assert isinstance(data2, string_types) is True

    data2 = do_vault(data2, 'ansible')
    assert is_encrypted(data2) is True
    assert isinstance(data2, string_types) is True
    assert data2.startswith('$ANSIBLE_VAULT;') is True

    # Test 3
    data3 = do_vault('test', 'ansible', wrap_object=True)
    assert data3.startswith('$ANSIBLE_VAULT;') is True

# Generated at 2022-06-22 12:00:00.757666
# Unit test for function do_vault

# Generated at 2022-06-22 12:00:12.658734
# Unit test for function do_vault
def test_do_vault():

    import os
    import pytest
    import binascii
    import yaml

    from ansible.module_utils.yaml import AnsibleVaultEncryptedUnicode, VaultSecret

    plain_text_1 = "this is a plaintext string"
    plain_text_2 = "this is another plaintext string"
    plain_text_3 = "this is one more plaintext string"

    secret = binascii.hexlify(os.urandom(16)).decode('utf-8')
    vaultid = 'test_vault'

    # test with secret as string
    vault1 = do_vault(plain_text_1, secret, vaultid=vaultid)
    assert plain_text_1 == do_unvault(vault1, secret, vaultid)

    # test with secret as string, and

# Generated at 2022-06-22 12:00:26.658213
# Unit test for function do_vault
def test_do_vault():
    secret = 'dummy_secret'
    salt = 'dummy_salt'
    data = 'dummy_data'
    vaultid = 'filter_default'
    wrap_object = True

    # Test case: function do_vault with secret, salt and wrap_object
    assert do_vault(data, secret, salt, vaultid, wrap_object) == AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256;'
                                                                                               'dummy_salt\r\ndummy_id\r\n'
                                                                                               '1343219111973924261537972036689353992319574546407926975088\r\n')

    # Test case: function do_vault with secret, salt and no wrap_object

# Generated at 2022-06-22 12:00:38.818661
# Unit test for function do_unvault
def test_do_unvault():
    assert do_unvault(do_vault('foobar', 'secret', 'salt', 'filter_default', wrap_object=False), 'secret', 'filter_default') == 'foobar'
    assert do_unvault(do_vault('foobar', 'secret', 'salt', 'filter_default', wrap_object=False), 'secret', 'filter_default') != 'someotherthing'
    assert do_unvault(do_vault('foobar', 'secret', 'salt', 'filter_default', wrap_object=False), 'somesecret', 'filter_default') == ''
    assert do_unvault(do_vault('foobar', 'secret', 'salt', 'filter_default', wrap_object=False), 'somesecret', 'filter_default') != 'foobar'

# Unit