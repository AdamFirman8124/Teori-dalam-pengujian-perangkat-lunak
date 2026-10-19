

# Generated at 2022-06-22 11:50:47.638646
# Unit test for function do_vault
def test_do_vault():
    secret = "MySecret"
    data = "my data"
    salt = None
    vaultid = 'filter_default'
    wrap_object = True
    vault = do_vault(data, secret, salt=salt, vaultid=vaultid, wrap_object=wrap_object)
    assert type(vault) is AnsibleVaultEncryptedUnicode
    assert vault.do_decrypt is False
    assert vault.vault == None

# Generated at 2022-06-22 11:50:52.905380
# Unit test for function do_vault
def test_do_vault():
    '''
    Unit test for function do_vault
    '''

    vault = do_vault('vault_me', 'password', 'some_salt', vaultid='test_vaultid')
    assert isinstance(vault, string_types)
    assert '$ANSIBLE_VAULT' in vault
    assert 'some_salt' not in vault # no salt in the vault

    # special case of wrapping
    vault = do_vault('vault_me', 'password', wrap_object=True)
    assert isinstance(vault, AnsibleVaultEncryptedUnicode)
    assert '$ANSIBLE_VAULT' in vault.data


# Generated at 2022-06-22 11:50:53.554000
# Unit test for function do_unvault
def test_do_unvault():
    pass

# Generated at 2022-06-22 11:51:05.023525
# Unit test for function do_unvault
def test_do_unvault():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes


# Generated at 2022-06-22 11:51:15.898084
# Unit test for function do_unvault
def test_do_unvault():
    secret = "mysecret"
    vaultid = "test_id"
    vaulted = "!vault |" + vaultid + "|" + "AQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBA"
    assert do_unvault(vaulted, secret, vaultid) == "abcd"
    assert do_unvault("abcd", secret, vaultid) == "abcd"
    assert do_unvault("!vault", secret, vaultid) == "!vault"
    assert do_unvault("abc", secret, vaultid) == "abc"
    assert do_unvault("!vault|" + vaultid + "|", secret, vaultid) == "!vault|" + vault

# Generated at 2022-06-22 11:51:28.514016
# Unit test for function do_vault

# Generated at 2022-06-22 11:51:38.115419
# Unit test for function do_vault
def test_do_vault():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_text
    from ansible.module_utils.six import ensure_text
    plain_text = u"This is a test"

    # Create a module object to use when running basic tests
    basic._ANSIBLE_ARGS = basic.AnsibleOptions(
        connection='local',
        module_path='/dev/null',
        forks=10,
        become=None,
        become_method=None,
        become_user=None,
        check=False,
        diff=False,
    )

# Generated at 2022-06-22 11:51:51.326793
# Unit test for function do_vault
def test_do_vault():
    before = '''
---
sdafjklas;djf;laskjdf;laskjdf
askdjf;lakjsd;flkjasd
zxcv;lkasdjf;lkasjdf
'''

# Generated at 2022-06-22 11:52:03.190484
# Unit test for function do_vault
def test_do_vault():
    ansible_vault_password = to_bytes('cat')
    vault_id = 'filter_default'
    salt = None
    wrap_object = False

    # The data, which we want to encrypt
    data_plain = "I am an unencrypted string"
    data_vault = do_vault(data_plain, ansible_vault_password, salt, vault_id, wrap_object)

    assert data_vault
    assert data_vault != data_plain
    assert isinstance(data_vault, string_types)

    # Now check if we can decrypt the string
    data_plain_again = do_unvault(data_vault, ansible_vault_password, vault_id)
    assert data_plain_again == data_plain

    # Check of the unencrytped string returns the same

# Generated at 2022-06-22 11:52:13.103665
# Unit test for function do_unvault
def test_do_unvault():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import is_encrypted, VaultLib, VaultSecret
    from ansible.module_utils._text import to_native
    import crypt

    newpass = crypt.crypt("mysecret", crypt.mksalt(crypt.METHOD_SHA256))
    vs = VaultSecret(newpass)

    data = 'This is a test'
    # test unvault string to string
    vault = do_vault(data, newpass)
    assert (isinstance(vault, string_types))
    assert (is_encrypted(vault))
    assert (data == to_native(VaultLib().decrypt(vault)))
    assert (data == do_unvault(vault, newpass))

    #

# Generated at 2022-06-22 11:52:25.762182
# Unit test for function do_unvault
def test_do_unvault():
    from ansible.plugins.filter.vault import FilterModule
    import pytest

    fm = FilterModule()
    do_unvault = fm.filters()['unvault']

    # AnsibleVaultEncryptedUnicode
    #
    # Usage: {{ data | unvault( vault_password ) }}
    #
    # data is an AnsibleVaultEncryptedUnicode object.
    #
    # The AnsibleVaultEncryptedUnicode object is constructed by the vault
    # filter.
    #
    # Example usage:
    #
    #    - debug:
    #        msg: "{{ 'app_password' | vault }}"
    #
    # See http://docs.ansible.com/ansible/latest/dev_guide/vault.html#vault-decryption-in-

# Generated at 2022-06-22 11:52:37.366540
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('foo', 'secret', False) == '$ANSIBLE_VAULT;1.2;AES256;filter_default\n3938643636356466656263663334353366383461346332323365336362663833358303933613665\n62396366623635363866323337616234343337326535363632643231626436383638303130316166\n39303766396162366463396166663161633337643566616439303934313136336361323463613535\n62393466363539323169333535616464626338393938373031386139613835663238646262666138\n61383638343461636666\n'
    assert do

# Generated at 2022-06-22 11:52:46.085133
# Unit test for function do_unvault
def test_do_unvault():
    assert do_unvault('') == ''
    assert do_unvault('$ANSIBLE_VAULT;1.1;AES256\n63316263656437353331646237383330393131623263613661363136613239653835383033373534\n6565393762656436393731323362616136613531366235313532373662363963383539613936363938\n3734306432626331333138613335306638363366643530393061636164346363661616339636362346\n393835663035376637323066346331656532653765393735\n') == 'mysecret'

# Generated at 2022-06-22 11:52:52.992809
# Unit test for function do_unvault
def test_do_unvault():
    assert do_unvault("ANSIBLE_VAULT;1.2;AES256;ansible-vault\n656461333562366664363439396164396136336635383761633238316235363430320a623332303233613834336332393162313838643661386664376334656532333439\n", secret="secret") == "this is an encrypted vault"


# Generated at 2022-06-22 11:53:02.641442
# Unit test for function do_unvault

# Generated at 2022-06-22 11:53:08.049107
# Unit test for function do_unvault

# Generated at 2022-06-22 11:53:16.979053
# Unit test for function do_vault
def test_do_vault():
    ''' ansible.builtin.filter_plugins.do_vault '''

# Generated at 2022-06-22 11:53:29.169148
# Unit test for function do_vault
def test_do_vault():
    f = FilterModule()
    j = f.filters()['vault']

# Generated at 2022-06-22 11:53:39.658112
# Unit test for function do_vault

# Generated at 2022-06-22 11:53:46.965202
# Unit test for function do_unvault
def test_do_unvault():

    # ------------------------------------------------------------------------------------------------------------------
    # do_unvault test case 1
    print("\n# ------------------------------------------------------------------------------------------------------------------")
    print("# do_unvault test case 1")
    print("# Try to decrypt vault data without valid vaultid")

    secret = b"ansible"

# Generated at 2022-06-22 11:54:00.576579
# Unit test for function do_vault
def test_do_vault():
    data = {
        'ansible_net_api': 'cli',
        'ansible_net_user': 'admin',
        'ansible_net_password': 'admin',
        'ansible_net_host': 'vios01',
        'ansible_net_use_ssl': False,
        'ansible_net_port': 22,
    }


# Generated at 2022-06-22 11:54:11.777003
# Unit test for function do_vault

# Generated at 2022-06-22 11:54:20.269502
# Unit test for function do_unvault
def test_do_unvault():
    """Test do_unvault function"""

# Generated at 2022-06-22 11:54:22.711580
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('abc', 'abc') == '$ANSIBLE_VAULT;1.1;AES256\n'


# Generated at 2022-06-22 11:54:26.909574
# Unit test for function do_unvault
def test_do_unvault():
    assert do_unvault("$ANSIBLE_VAULT;1.2;AES;aes256;abc12345678901234567", "abc12345678901234567") == "aes256;abc12345678901234567"


# Generated at 2022-06-22 11:54:30.354653
# Unit test for function do_unvault
def test_do_unvault():
    # When vault is not encrypted
    vault = 'hello world'
    secret = 'world'
    expected = 'hello world'
    result = do_unvault(vault, secret)
    assert expected == result
    # When vault is not encrypted in AnsibleVaultEncryptedUnicode format
    vault = AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256;hello')
    secret = 'world'
    expected = 'hello world'
    result = do_unvault(vault, secret)
    assert expected == result
    # When vault is encrypted in AnsibleVaultEncryptedUnicode format
    vault = AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256;hello')
    secret = 'world'

# Generated at 2022-06-22 11:54:41.219263
# Unit test for function do_vault
def test_do_vault():

    # Test no secret
    assert do_vault('', '') is False, "No secret passed"
    assert do_vault('', 'supersecret') is False, "Passed empty string"

    # Test no data
    assert do_vault('', 'supersecret') is False, "Empty string passed"

    # Test with bad types
    try:
        do_vault(10, 'supersecret')
        assert False, "Expected error when data is not a string or undefined"
    except AnsibleFilterTypeError:
        assert True

    try:
        do_vault('', 10)
        assert False, "Expected error when secret is not a string or undefined"
    except AnsibleFilterTypeError:
        assert True

    # Test good cases
    data = do_vault('', 'supersecret')
    assert to_native

# Generated at 2022-06-22 11:54:43.362618
# Unit test for function do_vault
def test_do_vault():
    return "test_do_vault"

# Generated at 2022-06-22 11:54:54.072109
# Unit test for function do_unvault
def test_do_unvault():
    secret = "secret"
    secret_wrong = "wrong"
    data = "test"
    vault = "vault"
    vault_binary = "binary"
    vault_wrong = "wrong"

    assert do_unvault(vault, secret) == data
    assert do_unvault(vault_binary, secret) == data
    assert do_unvault(vault_wrong, secret) == u"wrong"

    try:
        do_unvault(vault, secret_wrong)
    except AnsibleFilterError as e:
        assert str(e) == "Unable to decrypt: unable to decrypt data with vault id filter_default (check your vault password!)"

# Generated at 2022-06-22 11:55:05.653805
# Unit test for function do_vault
def test_do_vault():
    secret = '$ANSIBLE_VAULT;1.2;AES256;ansible\n31336437323034303132316438663538663632323363303763366161326130656135633734386439\n356539336430656661623563636331346165383638313261396239340a3562333962373165626130\n31656438323164643637396135663466626661383564373834643963326564303937643434366635\n36393839663537333036633535\n'
    data = 'my_secret_password'
    vault = do_vault(data, secret, salt=None, vaultid='filter_default', wrap_object=False)
    assert vault

# Generated at 2022-06-22 11:55:18.411043
# Unit test for function do_unvault
def test_do_unvault():
    from ansible.module_utils._text import to_text as text
    from ansible.parsing.vault import VaultSecret
    from ansible.errors import AnsibleError
    from jinja2 import Undefined
    from jinja2.exceptions import UndefinedError

    def assertUnvaultException(lookup, secret, exception_type, exception_message):
        try:
            lookup.run('unvault', vault, secret, wrap_object=True)
        except exception_type as e:
            assert e.args[0] == exception_message
        else:
            assert False, "Exception of type '%s' was not raised" % exception_type

    # Setup
    secret = VaultSecret('secret')
    lookup = AnsibleVaultEncryptedUnicode.resolve('encryption_key')
    unvault

# Generated at 2022-06-22 11:55:30.141342
# Unit test for function do_vault
def test_do_vault():
    secret = 'secret'
    data = 'data'
    print('running function do_vault with secret: %s and data: %s' % (secret, data))
    data_vaulted = do_vault(data, secret)
    print('vaulted data: %s' % data_vaulted)
    print('running function do_unvault with secret: %s and data: %s' % (secret, data_vaulted))
    data_unvaulted = do_unvault(data_vaulted, secret)
    print('unvaulted data: %s' % data_unvaulted)
    if data_unvaulted != data:
        print('data unvaulted is different from data')
        exit(1)
    print('all tests passed')


# Generated at 2022-06-22 11:55:40.858483
# Unit test for function do_vault
def test_do_vault():
    ret = do_vault('test', 'vault')
    assert isinstance(ret, str)
    assert ret == b'$ANSIBLE_VAULT;1.1;AES256\n30623131626463303533663531316666356139626439306536386438663664363361643135306331\n32303263613664653565663737366639373664333039643733373965653538346462636662336166\n30646638633931653462653235316531373135313531333562626562623134353166623337653361\n65666635343961646337663761356132353033396635386364343565363330346636\n'
   

# Generated at 2022-06-22 11:55:53.024704
# Unit test for function do_vault
def test_do_vault():
    secret = "mysecret"
    data = "mydata"
    vault = do_vault(data, secret)

# Generated at 2022-06-22 11:56:03.661364
# Unit test for function do_vault
def test_do_vault():
    import os
    import random
    import binascii

    data = 'test_test_test_test'
    secret = 'this_is_secret'
    salt = binascii.hexlify(os.urandom(8))
    vaultId = 'filter_default'
    assert do_vault(data, secret, salt, vaultId)
    assert do_vault(data, secret, salt)
    assert do_vault(data, secret)
    assert do_vault(data, secret, salt, vaultId, True)
    assert do_vault(data, secret, salt, True)
    assert do_vault(data, secret, True)
    try:
        assert do_vault(1, secret)
        assert False
    except AnsibleFilterTypeError:
        pass

# Generated at 2022-06-22 11:56:12.967890
# Unit test for function do_vault

# Generated at 2022-06-22 11:56:17.477978
# Unit test for function do_vault
def test_do_vault():
    data = 'Hello World'
    vault_result = do_vault(data, 'secret', salt='salt')
    data_result = do_unvault(vault_result, 'secret', vaultid='filter_default')
    assert data == data_result

# Generated at 2022-06-22 11:56:28.698965
# Unit test for function do_vault
def test_do_vault():
    import os

    secret = os.getenv('ANSIBLE_VAULT_FILTER_SECRET')
    salt = os.getenv('ANSIBLE_VAULT_FILTER_SALT')
    vault_string = 'Hello, world!'
    vaulted_string = do_vault(vault_string, secret, salt)

    print('Encrypted string: %s' % vaulted_string)
    assert(vaulted_string != vault_string)

    unvaulted_string = do_unvault(vaulted_string, secret)
    print('Decrypted string: %s' % unvaulted_string)
    assert(unvaulted_string == vault_string)

if __name__ == '__main__':
    test_do_vault()

# Generated at 2022-06-22 11:56:39.287250
# Unit test for function do_vault
def test_do_vault():
    # Test for empty string
    try:
        do_vault("", "dummyPassword")
    except AnsibleFilterTypeError as e:
        assert 'Can only vault strings' in str(e)
    # Test for secret not string
    try:
        do_vault("dummy", 123)
    except AnsibleFilterTypeError as e:
        assert 'Secret passed is required to be a string' in str(e)
    # Test for undefined key
    try:
        do_vault("dummy", Undefined())
    except UndefinedError as e:
        assert 'Secret passed is required' in str(e)
    # Test for vault with salt and secret
    data = "dummy"
    secret = "dummyPassword"
    salt = "dummySalt"

# Generated at 2022-06-22 11:56:50.948459
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('test', 'secret') == '$ANSIBLE_VAULT;1.2;AES256;filter_default\n35303762396533643830346665396661626235376434646139643262346362393133636134356434\n37313166323135393764356262646430373230313538373337313361396362643765616236656566\n32396536666263323365613161323333613239646232626336306635303366383939663930643463\n33353039386238613861356132306234313361343466386237336634383139373738376262316238\n39656366383738646266\n'
   

# Generated at 2022-06-22 11:56:57.000421
# Unit test for function do_vault
def test_do_vault():
    result = do_vault('testdata', 'testsecret', 'testsalt')
    assert '$ANSIBLE_VAULT;' in result
    assert '\n' in result
    assert 'testdata' not in result


# Generated at 2022-06-22 11:57:00.041828
# Unit test for function do_vault
def test_do_vault():
    # Setup
    secret = 'secret'
    salt = 'salt'
    data = 'this should be encrypted'

    # Test
    result = do_vault(data, secret, salt)

    # Assert
    assert result == '$ANSIBLE_VAULT;1.1;AES256\n'
    assert type(result) == str


# Generated at 2022-06-22 11:57:09.270999
# Unit test for function do_vault
def test_do_vault():
    ansible_vault_data = '$ANSIBLE_VAULT;1.1;AES256;devops\n64353738646636313864353037613434653132653834336665323431363236306533386434653364\n34643636656431336536663437313138316266633235386638343735333634643939326538336339\n34353339653461316438373435626130653264636163316330356536393635626562343634663039\n373663316630343738393963633436653433353685\n'

    # normal usage with 'wrap_object=False'

# Generated at 2022-06-22 11:57:20.576589
# Unit test for function do_vault
def test_do_vault():
    data_in = u'this is the secret input'
    secret = 'mysecret'
    vaultid = 'vault_default'
    salt = u'foo'
    wrap_object = True


# Generated at 2022-06-22 11:57:23.578920
# Unit test for function do_vault
def test_do_vault():
    secret = "hello"
    data = "world"

    vault = do_vault(data, secret)

    assert(is_encrypted(vault) is True)


# Generated at 2022-06-22 11:57:32.671373
# Unit test for function do_unvault
def test_do_unvault():
    ''' Unit test for do_unvault method '''
    assert do_unvault("!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          343237323665323335393164393139396433323461623532353237663261353766303861386636\n          38313539373436313263623164306335623436303333336331330a38353866343733327a343739\n          726262386338612b6f343561367770373362666162343837343763366232303766646264333730\n          6633616433396136383832630a\n", "foo") == "bar"

# Generated at 2022-06-22 11:57:37.573755
# Unit test for function do_vault
def test_do_vault():
    ''' Unit test for do_vault '''
    actual_output = do_vault("mysecret", "mysecret", "mysecret", "filter_default", True)
    expected_output = '$ANSIBLE_VAULT;1.1;AES256\n363038613065653430626233333364376162363034373064626132613663643064343161666565\n3436353962633538373837612d6238362d343439622d393964352d313866323431633934323138\n613136336536626539636132313265\n'
    assert actual_output == expected_output

    actual_output = do_vault("mysecret", "mysecret", "mysecret", "filter_default", "")

# Generated at 2022-06-22 11:57:48.251063
# Unit test for function do_vault
def test_do_vault():
    test_data = 'test'
    test_secret = 'some_secret'
    test_salt = 'some_salt'
    test_vaultid = 'test_vault'
    expect_result = '$ANSIBLE_VAULT;1.2;AES256;test_vault;data;\n31333434646532333137303335643635366233636365646435383262343363666659643234643465\n32323365326534353033346536663936656532653336326337626665636162363830366437646166\n39353761303437376662626432643733313231336533663965376332626230366564373936383066\n34616666643866\n'

# Generated at 2022-06-22 11:58:00.486293
# Unit test for function do_vault
def test_do_vault():
    # Test for positive input
    test_string = "test_string"
    test_secret = "test_secret"
    test_salt = b"testsalt"
    test_vaultid = 'filter_default'
    test_wrap_object = False

# Generated at 2022-06-22 11:58:06.085039
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('secret', 'password') == '$ANSIBLE_VAULT;1.1;AES256\n336565383264356661326463643532343933393434316132313561626363663030373534363361\n323236656566616435393938616139613661663865323362653735306538653436363366313736\ntesting_vault_filter\n'


# Generated at 2022-06-22 11:58:17.071405
# Unit test for function do_unvault
def test_do_unvault():
    assert(do_unvault('$ANSIBLE_VAULT;1.2;AES256;xmldontmatter\n35653435363335643337396333386538643864623832643430663439623361653737643633633961633435\n65633338393335373365663738656634373463633065326137653233623837336665346463346261373862\n3462', 'secret') == '12345')
    assert(do_unvault('12345', 'secret') == '12345')


# Generated at 2022-06-22 11:58:22.014060
# Unit test for function do_unvault
def test_do_unvault():
    assert do_unvault('$ANSIBLE_VAULT;1.1;AES256\n000000000000000000000000000000000000000000000000000000000000000000000000000000000\n000000000000000000000000000000000000000000000000000000000000000000000000000000000\n0000000000000000000000000000000000000000000000000000', 'mysecret', '') == 'mydata'

# Generated at 2022-06-22 11:58:32.165786
# Unit test for function do_vault
def test_do_vault():
    """
    Performs unit tests on function do_vault
    """
    from ansible.module_utils._text import to_text


# Generated at 2022-06-22 11:58:44.140970
# Unit test for function do_vault
def test_do_vault():
    # Assume some data and secret
    data = 'this is a secret'
    secret = 'password'
    vault = do_vault(data, secret)
    # Assert that the result is an AnsibleVaultEncryptedUnicode object
    assert isinstance(vault, AnsibleVaultEncryptedUnicode)
    # Assert that the data returned is the same as the original data
    assert vault.data == data
    # Test different encrytion methods
    vault = do_vault(data, secret, salt='salt')
    vault = do_vault(data, secret, salt='salt', vaultid='filter_test_salt')

    # Test using the wrap_object flag
    vault = do_vault(data, secret, wrap_object=True)
    assert vault.data == data

    # Test using a

# Generated at 2022-06-22 11:58:55.490706
# Unit test for function do_vault
def test_do_vault():

    assert do_vault('ansible', 'secret') == '$ANSIBLE_VAULT;1.1;AES256\n30623237636334616661393131646331333662663761643338393937323164323266333133663661\n3262323066306437393031393431666233323134333234396464383136340a306664326465663365\n65303933623163616534653839313432646263323562393833386638346466303161326566663664\n6136663330323234373334643634353738653230396637306563\n'


# Generated at 2022-06-22 11:59:07.025590
# Unit test for function do_vault
def test_do_vault():

    data = 'ansible'
    secret = 'secret'
    salt = 'salt'
    vaultid = 'filter_default'
    wrap_object = False

    expected_output = '$ANSIBLE_VAULT;1.2;AES256;filter_default;5;5;YW5zaWJsZQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAsHn4W4BgGmaB7JogecYwBQdH8S+bpTWZVbBk4vfhW4H4O106jyV7cMMEw=='

    actual_output = do_vault(data, secret, salt, vaultid, wrap_object)
    assert expected_output == actual_output

    # Test input type of secret is not valid
    invalid_secret = True

# Generated at 2022-06-22 11:59:18.542932
# Unit test for function do_vault
def test_do_vault():
    import sys

    if sys.version_info.major == 2:
        print("Skipping test_do_vault under Python 2.x")
        return

    from ansible.module_utils._text import to_bytes

    def test_do_vault_valid(vault, secret, salt='default_salt'):
        print("test_do_vault_valid")
        print("vault:")
        print(vault)
        print("secret:")
        print(secret)
        print("salt:")
        print(salt)

        result = do_vault(to_bytes(vault), to_bytes(secret), salt=to_bytes(salt))
        print("result:")
        print(result)

        assert result is not None and result != ''


# Generated at 2022-06-22 11:59:28.375302
# Unit test for function do_vault
def test_do_vault():
    '''
    Unit test for function do_vault
    '''

# Generated at 2022-06-22 11:59:39.204426
# Unit test for function do_vault

# Generated at 2022-06-22 11:59:50.471115
# Unit test for function do_vault
def test_do_vault():
    msg_fail = 'do_vault: filter_default: filter_default:'
    secret = 'password'
    #  Test 1
    # Input
    data = 'mystring'
    salt = None
    vaultid = 'filter_default'
    wrap_object = False
    # Output
    output = do_vault(data, secret, salt, vaultid, wrap_object)
    # Comparison

# Generated at 2022-06-22 11:59:59.710439
# Unit test for function do_vault
def test_do_vault():
    do_vault('this is plain text', 'secret')


# Generated at 2022-06-22 12:00:11.034805
# Unit test for function do_vault
def test_do_vault():
    from ansible.parsing import vault
    from ansible.parsing.vault import VaultLib

    secret = 'foo'
    test_str = 'bar'
    salt = b'foo_bar_baz'
    vaultid = 'test_vaultid'

    ciphertext = do_vault(test_str, secret, salt=salt, vaultid=vaultid)
    assert ciphertext

    # By default, do_vault returns a string, not a AnsibleVaultEncryptedUnicode
    assert not isinstance(ciphertext, AnsibleVaultEncryptedUnicode)

    # By passing wrap_object to do_vault, we can get an AnsibleVaultEncryptedUnicode

# Generated at 2022-06-22 12:00:16.729492
# Unit test for function do_vault
def test_do_vault():
    '''
    Returns a string encrypted with the vault password
    '''
    unencrypted_string = 'this is a secret'
    vault_password = 'vault_password'
    encrypted_string = do_vault(unencrypted_string, vault_password)
    assert encrypted_string != unencrypted_string
    assert is_encrypted(encrypted_string)


# Generated at 2022-06-22 12:00:19.440528
# Unit test for function do_vault
def test_do_vault():
    secret = 'mypass'
    data = 'helloworld'
    vault = do_vault(data, secret)

    assert vault.startswith('$ANSIBLE_VAULT')


# Generated at 2022-06-22 12:00:28.166949
# Unit test for function do_vault
def test_do_vault():
    from ansible.parsing.vault import is_encrypted
    test_secret = "hunter2"
    test_data = "test_data"
    test_salt = "salt"
    test_vaultid = "test_vaultid"

    vault = do_vault(test_data, test_secret, test_salt, test_vaultid)

    assert isinstance(vault, string_types)
    assert is_encrypted(vault)
    # we can't check that the data was encrypted properly because the vault string
    # is generated randomly every time.


# Generated at 2022-06-22 12:00:39.976991
# Unit test for function do_vault
def test_do_vault():
    # Test if password, secret and salt are strings
    assert do_vault('test', 'test') == '$ANSIBLE_VAULT;1.1;AES256\n3564333235653336646338643065376362656331653235663965646161303137616334633961376330\n3933313730363737633835663633376631633735343866623565623837333739636461373764653436\nc3e3d15e50c929f67bcf92d2057f8291844a518d\n'