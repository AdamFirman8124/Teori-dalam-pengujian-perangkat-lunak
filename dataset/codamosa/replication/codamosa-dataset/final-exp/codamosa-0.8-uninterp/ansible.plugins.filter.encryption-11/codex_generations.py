

# Generated at 2022-06-22 11:50:41.145740
# Unit test for function do_vault
def test_do_vault():
    secret = 'very_secret'
    data = 'my_data'
    vault = do_vault(data, secret)
    assert vault != ''


# Generated at 2022-06-22 11:50:51.091147
# Unit test for function do_vault
def test_do_vault():
    import jinja2
    env = jinja2.Environment()

# Generated at 2022-06-22 11:51:00.486608
# Unit test for function do_vault

# Generated at 2022-06-22 11:51:12.520092
# Unit test for function do_unvault

# Generated at 2022-06-22 11:51:25.724546
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('secret', 'password') == '$ANSIBLE_VAULT;1.1;AES256\n326565353862613664316133653337613235326136653733343831353832653066316135363130\n323537376538396664376331326530323665643765663037656538376361633864633765653634\n33393533623465383338\n'

# Generated at 2022-06-22 11:51:36.459580
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('{"key": "value"}', 'secret') == '$ANSIBLE_VAULT;1.1;AES256\n373635343735342d34656261372d343833352d393737302d3834323036643766323561306a0a\n623363373362613461396130633236366236633531323265326531323334653037363564356303\n646133613034353161623631666334323262623032363831623031636237396535633362616134\n663439336630\n'

    # Unit test for function do_unvault

# Generated at 2022-06-22 11:51:47.574350
# Unit test for function do_unvault
def test_do_unvault():
    secret = "test"
    data = "This is a test string"
    vl = VaultLib()
    encrypted_data = vl.encrypt(data, secret)

    # base case - return data as string
    assert isinstance(do_unvault(encrypted_data, secret), string_types)
    # test with AnsibleVaultEncryptedUnicode
    assert isinstance(do_unvault(AnsibleVaultEncryptedUnicode(encrypted_data), secret), string_types)
    # test with non-encrypted data
    assert isinstance(do_unvault(data, secret), string_types)



# Generated at 2022-06-22 11:51:57.430315
# Unit test for function do_unvault
def test_do_unvault():
    from ansible.module_utils.six import BytesIO
    class fake_vs(object):
        def __init__(self, secret):
            self.secret = secret
        def get_unseal_keys_and_reset(self):
            return [(BytesIO(self.secret), BytesIO(self.secret))]
    class fake_vl(object):
        def __init__(self, vs):
            self.vs = vs
        def decrypt(self, seal_data):
            return 'fake_decrypt'

    secret = b'fake_secret'
    wrong_secret = b'fake_wrong_secret'
    vault = b'fake_seal_data'
    data = b'fake_data'

    def _test_do_unvault_with_args(secret, vault):
        vs = fake_vs

# Generated at 2022-06-22 11:52:03.677115
# Unit test for function do_unvault
def test_do_unvault():
    unvaulted = do_unvault("$ANSIBLE_VAULT;1.1;AES256;ansible_filter_default\n643120616461316133313162366639663564313666313633663538346639356365366564383436\n393164656535663832646332623832623237336632333835663936653734393734363230613562\n633534336462623165323532353239\n", "testing")
    assert(unvaulted == "testing_is_good")

# Generated at 2022-06-22 11:52:05.947211
# Unit test for function do_vault
def test_do_vault():
    pass


# Generated at 2022-06-22 11:52:15.584302
# Unit test for function do_unvault

# Generated at 2022-06-22 11:52:19.627480
# Unit test for function do_vault
def test_do_vault():
    secret = "secret"
    data = "data"
    vault = do_vault(data, secret)
    data2 = do_unvault(vault, secret)
    assert data == data2


# Generated at 2022-06-22 11:52:32.062020
# Unit test for function do_vault
def test_do_vault():
   assert do_vault(None, None) == ''
   assert do_vault(None, "secret") == ''
   assert do_vault("string", None) == ''
   assert do_vault("string", "secret") == "ENC[AES256_GCM,data:0J6TFpDXjkDzSy1giCkWGw==,iv:eP/mZHafrns1Mn8EIgXtLQ==,tag:zW/A8tT/TMSRIIjNpZBbWw==,type:str]\n"

# Generated at 2022-06-22 11:52:42.683673
# Unit test for function do_vault
def test_do_vault():
    secret = "foo"
    data = "bar"

    vault_test = do_vault(data, secret)

# Generated at 2022-06-22 11:52:53.673570
# Unit test for function do_vault
def test_do_vault():
    """ Unit test for function do_vault()
    """

    # Stat test for function do_vault
    def do_test(data, secret, salt=None, vaultid='filter_default', wrap_object=False):
        vault_data = do_vault(data, secret, salt, vaultid, wrap_object)
        unvault_data = do_unvault(vault_data, secret, vaultid)

        assert unvault_data == data

    # Test, should not raise any error
    do_test("hello", "12345")
    do_test("hello", "12345", wrap_object=True)

    # Test, should raise AnsibleFilterTypeError
    try:
        do_test(123, "12345")
        assert False
    except AnsibleFilterTypeError:
        pass

    # Test

# Generated at 2022-06-22 11:53:03.220225
# Unit test for function do_vault
def test_do_vault():
    from jinja2 import Environment, StrictUndefined
    env = Environment(undefined=StrictUndefined)
    env.filters['vault'] = do_vault

    # Correct password:
    template_string = '{{"this is a secret"|vault("password")}}'
    template = env.from_string(template_string)

# Generated at 2022-06-22 11:53:14.767177
# Unit test for function do_unvault
def test_do_unvault():
    assert(do_unvault("$ANSIBLE_VAULT;1.2;AES256;default\n633134383262626532376361666130353733636162316538356466613561323137623762393364\n326534653635313662343863366532393262316664343835646431356666393234376631356536\n346631613061613630643366336333303262376431666239643162363833386463323436313139\n323663356136623439336634356266633038363665353033", "decrypt") == "THIS IS AN UNENCRYPTED STRING")

# Generated at 2022-06-22 11:53:26.828104
# Unit test for function do_vault
def test_do_vault():
    secret_string = 'this is the vault password'
    vault_string = '{{ "this is some test data" | vault("this is the vault password") }}'
    data_string = 'this is some test data'
    salt_string = 'this is the salt'
    vaultid_name = 'test_vaultid'

# Generated at 2022-06-22 11:53:38.118940
# Unit test for function do_vault
def test_do_vault():
    """ test_do_vault() function tests the function do_vault """
    module = FilterModule()
    filters = module.filters()
    assert filters['vault']('encrypt_me', 'secret') == '$ANSIBLE_VAULT;1.1;AES256\n31653365356662643233616231353962643033323135336231393261613463363332303861636165\n39666363656332376161333435623137623762616539393066653637303231393865313932333662\n34623133653839313336353262636639663035354366316332323037636165386262343438363830\n'


# Generated at 2022-06-22 11:53:46.325807
# Unit test for function do_vault
def test_do_vault():
    #
    # Test invalid parameters
    #

    # Test invalid type for secret
    import pytest
    from ansible.module_utils.six import PY3

    expected_err_msg = "Secret passed is required to be a string, instead we got: <(class|type) 'bool'>"
    with pytest.raises(AnsibleFilterTypeError, match=expected_err_msg):
        do_vault('hello', True)
    with pytest.raises(AnsibleFilterTypeError, match=expected_err_msg):
        do_vault('hello', False)
    with pytest.raises(AnsibleFilterTypeError, match=expected_err_msg):
        do_vault('hello', 1)

# Generated at 2022-06-22 11:54:00.267354
# Unit test for function do_vault
def test_do_vault():

    assert do_vault("foo", "bar") == "!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          30643161356633313563376337336364356536393834383665663463316461376262656234633761\n          30373038353334623331643261366134316661346262633963606637646234623166623238623861\n          30336639633331366133663936653438333566326638643534306438663263363536633864333534\n          3564333939386162643832656236653039336130616134336535\n" == do_vault("foo", "bar")

# Generated at 2022-06-22 11:54:06.258788
# Unit test for function do_vault
def test_do_vault():
    secret = 'mysecret'
    data = 'mydata'
    wrapped = do_vault(data, secret, wrap_object=True)
    unwrapped = do_vault(data, secret, wrap_object=False)
    assert isinstance(wrapped, AnsibleVaultEncryptedUnicode)
    assert isinstance(unwrapped, string_types)

# Generated at 2022-06-22 11:54:13.076922
# Unit test for function do_vault
def test_do_vault():
    # Example string content to encrypt
    data = 'This is secret data. I am encrypting with the vault filter, and you cannot see it!'

    # Example secret key to use with vault filter
    secret = 'password'

    # Example salt (should be random)
    salt = 'salt'

    # Example vault id (should be unique)
    vaultid = 'vault'

    # Set to True to wrap the encrypted output with an AnsibleVaultEncryptedUnicode object
    wrap_object = False

    encrypted = do_vault(data, secret, salt, vaultid, wrap_object)
    assert encrypted != data and encrypted != None


# Generated at 2022-06-22 11:54:14.416108
# Unit test for function do_unvault
def test_do_unvault():
    assert do_unvault('ansible', 'vault') == 'ansible'

# Generated at 2022-06-22 11:54:21.960183
# Unit test for function do_vault
def test_do_vault():
    assert do_vault("test", "password") == '$ANSIBLE_VAULT;1.1;AES256\n3539373236663761623030373864343737643834363532353762313730303264643633653632326\n3643536663539336464626431306537656439433238323865386566346431\n'
    assert do_vault("", "password") == '$ANSIBLE_VAULT;1.1;AES256\n3539373236663761623030373864343737643834363532353762313730303264643633653632326\n3643536663539336464626431306537656439433238323865386566346431\n'
    assert do_

# Generated at 2022-06-22 11:54:34.170782
# Unit test for function do_vault

# Generated at 2022-06-22 11:54:43.584005
# Unit test for function do_vault

# Generated at 2022-06-22 11:54:54.675220
# Unit test for function do_vault
def test_do_vault():
    from ansible_collections.ansible.community.plugins.module_utils.vault.crypto import resolve_secret_type
    from ansible.parsing.vault_lib import VaultLib

# Generated at 2022-06-22 11:55:06.137984
# Unit test for function do_vault
def test_do_vault():
    salt = "SALT"
    vaultid = "unittest"
    secret = "secret"

# Generated at 2022-06-22 11:55:13.550982
# Unit test for function do_vault

# Generated at 2022-06-22 11:55:25.558102
# Unit test for function do_vault
def test_do_vault():
    secret = "ansible"
    vault = do_vault("ansible123", secret)
    assert vault == "$ANSIBLE_VAULT;1.2;AES256;ansible\n32333561633632363162656638353730306161333861643438396535336536646330633832343137\n61366565396635653834333934303837613639336330303536656362310a30393433356631393266\n626430336536663762623233636262626331613864666161383762316562383965626662376132\n38366439"


# Generated at 2022-06-22 11:55:37.664776
# Unit test for function do_vault

# Generated at 2022-06-22 11:55:44.976348
# Unit test for function do_vault
def test_do_vault():
    # Setup
    class TestFilterModule():
        ''' Test implementation of Ansible vault jinja2 filters '''
        def filters(self):
            filters = {
                'vault': do_vault,
            }
            return filters
    test_filter_module = TestFilterModule()

    # Execute
    data = 'test-data'
    secret = 'test-secret'
    vaultid = 'test-vaultid'
    vault = do_vault(data, secret, vaultid=vaultid, wrap_object=True).data

    # Verify
    vs = VaultSecret(secret)
    vl = VaultLib()
    data_decrypted = vl.decrypt(vault.encode())

    assert data == data_decrypted

# Generated at 2022-06-22 11:55:56.523901
# Unit test for function do_vault
def test_do_vault():
    test_text = 'This is a test'
    test_secret = 'secret'

# Generated at 2022-06-22 11:56:07.724564
# Unit test for function do_vault

# Generated at 2022-06-22 11:56:15.344028
# Unit test for function do_vault
def test_do_vault():
    secret = 'mys3cr3t'
    data = 's3cr3tdata'
    salt = 'salt'

    non_vault = do_vault(data, '', salt)
    assert isinstance(non_vault, string_types)
    non_vault = do_vault(data, '', salt, wrap_object=True)
    assert isinstance(non_vault, AnsibleVaultEncryptedUnicode)
    assert non_vault.data == data

    vault = do_vault(data, secret, salt)
    assert isinstance(vault, string_types)
    vault = do_vault(data, secret, salt, wrap_object=True)
    assert isinstance(vault, AnsibleVaultEncryptedUnicode)


# Generated at 2022-06-22 11:56:17.793524
# Unit test for function do_vault
def test_do_vault():
    data = "Normal String"
    secret = "super secret password"
    assert do_vault(data, secret) != ''


# Generated at 2022-06-22 11:56:27.457040
# Unit test for function do_vault
def test_do_vault():

    secret = 'hunter'
    salt = None
    vaultid = None
    wrap_object = False
    # vault: data, secret, salt=None, vaultid='filter_default', wrap_object=False
    result = do_vault('hunter', secret, salt, vaultid, wrap_object)

# Generated at 2022-06-22 11:56:36.798643
# Unit test for function do_vault
def test_do_vault():
    # Setup
    vaulttext = "!vault "
    vaultid = "filter_default"
    secret = b"secret"
    salt = b"salt"
    data = "data"
    wrap_object = True
    # Test
    result = do_vault(data, secret, salt, vaultid, wrap_object)
    assert isinstance(result, AnsibleVaultEncryptedUnicode)
    assert result.vault == vaultid
    assert result.data == data
    assert result.secret == secret
    assert result.salt == salt
    assert str(result).startswith(vaulttext)
    assert not result.unwrapped


# Generated at 2022-06-22 11:56:45.122037
# Unit test for function do_vault
def test_do_vault():

    # Test for vault being undefined
    vault = do_vault(None, 'abc', 'abc')
    assert vault == ''

    # Test for secret being undefined
    try:
        do_vault('abc', None, 'abc')
    except Exception as e:
        assert type(e) == AnsibleFilterTypeError

    # Test for secret being of wrong type
    try:
        do_vault('abc', 12345, 'abc')
    except Exception as e:
        assert type(e) == AnsibleFilterTypeError

    # Test for salt being of wrong type
    try:
        do_vault('abc', 'abc', [1,2,3])
    except Exception as e:
        assert type(e) == AnsibleFilterError

    # Test for invalid vaultid

# Generated at 2022-06-22 11:56:54.298316
# Unit test for function do_vault
def test_do_vault():
    secret = 'secret'
    salt = 'salt'
    data = 'data'

    result = do_vault(data, secret, salt)

# Generated at 2022-06-22 11:56:58.446563
# Unit test for function do_vault
def test_do_vault():
    secret = 'hello'
    data = 'world'
    result = do_vault(data, secret)
    if not isinstance(result, AnsibleVaultEncryptedUnicode):
        raise AssertionError("do_vault returned an invalid result")


# Generated at 2022-06-22 11:57:08.496102
# Unit test for function do_vault
def test_do_vault():
    from ansible.vars.manager import VariableManager
    from ansible.parsing.vault import VaultSecret, VaultLib
    from ansible.parsing.yaml.loader import AnsibleLoader

    def test(data, secret, salt, vaultid, wrap_object, expected, check_for_none=False):
        vault = do_vault(data, secret, salt, vaultid, wrap_object)
        assert to_native(vault) == to_native(expected)

        decrypted_data = do_unvault(vault, secret, vaultid)
        assert to_native(data) == to_native(decrypted_data)

        # Check if we can decrypt vault in a different way
        vs = VaultSecret(secret)
        vl = VaultLib([(vaultid, vs)])

# Generated at 2022-06-22 11:57:14.512231
# Unit test for function do_unvault
def test_do_unvault():
    secret = 'MySecret'
    encrypted = '$ANSIBLE_VAULT;1.1;AES256\n3665353039346466653633663665646634613835663435653233346132396365376564626430653\n613736333035666366636332646635346563636465343737363033653837383761620a3635666565\ntest'
    decrypted = do_unvault(encrypted, secret)
    assert decrypted == 'test'


# Generated at 2022-06-22 11:57:26.592891
# Unit test for function do_unvault

# Generated at 2022-06-22 11:57:38.922594
# Unit test for function do_vault

# Generated at 2022-06-22 11:57:48.086434
# Unit test for function do_vault
def test_do_vault():
    test_string = 'test'
    test_secret = 'secret'

    expected_string = '$ANSIBLE_VAULT;1.1;AES256\n613566383563313562336665346363343165656436363561353537313636633137386438396266623\n3961306232316430393961616532666630363435653237626437353934336132306237613161336130\n3935373637363865653566613737346465333662346137326236656131666362383839373033353364\n'

    assert do_vault(test_string, test_secret) == expected_string



# Generated at 2022-06-22 11:58:00.268135
# Unit test for function do_vault
def test_do_vault():
    secret = VaultSecret('secret')
    secret_b64 = VaultSecret('c2VjcmV0')
    secret_bytes = VaultSecret(b'c2VjcmV0')
    secret_bytes_b64 = VaultSecret(b'c2VjcmV0')
    secret_unicode = VaultSecret(u'c2VjcmV0')
    secret_undefnd = VaultSecret(Undefined('N/A'))
    secret_unicode_undefnd = VaultSecret(Undefined(u'N/A'))
    secret_bytes_undefnd = VaultSecret(Undefined(b'c2VjcmV0'))
    secret_bytes_undefnd_unicode = VaultSecret(Undefined(u'c2VjcmV0'))
    secret_bytes_undefnd_b64

# Generated at 2022-06-22 11:58:08.279586
# Unit test for function do_unvault
def test_do_unvault():
    secret = "password"
    vault = "$ANSIBLE_VAULT;1.1;AES256"
    vault += "31323334353637383930313233343536373839303132333435363738393031323334353637383930313233343536373839"
    vault += "3031323334353637383930313233343536373839303132333435363738393031323334353637383930313233343536373839"
    vault += "3031323334353637383930313233343536373839303132333435363738393031323334353637383930313233343536373839"
    vault += "3031323334353637383930"

    t = do_

# Generated at 2022-06-22 11:58:20.336165
# Unit test for function do_unvault
def test_do_unvault():
    secret = 'AnsibleVaultIsAwesome'
    vault = '$ANSIBLE_VAULT;1.1;AES256;test\n353061306466633432373463623733393562396536353065313462323763303366653532666235\n643062396333623936643935626366626439646630353432613165323962306466326238636134\n313538356565646135396164393530663062313066653530666563313331343865313436636465\n333632303561303733343730353366353737663935646232346331653436326236396433326334\n'

# Generated at 2022-06-22 11:58:32.872597
# Unit test for function do_unvault

# Generated at 2022-06-22 11:58:44.752588
# Unit test for function do_vault
def test_do_vault():
  secret = "password"
  data = "secret"
  vault = do_vault(data, secret)

# Generated at 2022-06-22 11:58:55.973780
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('data', 'secret') == '$ANSIBLE_VAULT;1.1;AES256\n336535666266393338323865343338376261633730336336623363653135313731326237353162310a333064353765646531326135346537643365306435663964363365643536386335343766336a0a3462663263303431656132323661623732336230376261313437363865383536646530656436\n'
    assert do_vault('data', 'secret', wrap_object=True).data == do_vault('data', 'secret')

# Generated at 2022-06-22 11:59:07.396475
# Unit test for function do_unvault
def test_do_unvault():
    secret = 'secret123'
    vaultid = 'my_vault'

# Generated at 2022-06-22 11:59:14.425139
# Unit test for function do_vault
def test_do_vault():
    ''' test for vault filter '''
    secret = 'thisisasecret'
    data = 'I.AM.THE.DATA'
    vault = do_vault(data, secret)

    assert is_encrypted(vault), 'vault does not appear to be encrypted'
    assert secret != vault, 'vault is the same as the secret'
    assert data == do_unvault(vault, secret), 'unvault decrypted value is not the same as the original data'



# Generated at 2022-06-22 11:59:25.715347
# Unit test for function do_unvault
def test_do_unvault():
    secret = "password"
    plaintext = "hello world"
    encrypted = "!vault |\n$ANSIBLE_VAULT;1.1;AES256\n36363563303261633034393537313064663861346237316263323132356333616366396562386630\n35343964343863643065323462326439646534336532623930626530393830313836326265326462\n35653033643734656333656537386637656466306564386362356430323230643639386438663834\n303238366662306364376434353738636631633532653265316431393931386530\n"


# Generated at 2022-06-22 11:59:32.585669
# Unit test for function do_vault

# Generated at 2022-06-22 11:59:42.705691
# Unit test for function do_vault
def test_do_vault():

    # Test data
    test_data = 'Happy New Year 2020'
    test_secret = 'ZZZZZZZZZZZZZZZZ'

# Generated at 2022-06-22 11:59:53.203373
# Unit test for function do_vault
def test_do_vault():
    test = FilterModule()
    str = 'this is a secret'
    secret = 'secret'
    # salt = '12345'
    vaultid = 'filter_default'
    wrap_object = False

# Generated at 2022-06-22 12:00:00.649940
# Unit test for function do_vault
def test_do_vault():
    test_secret = '40e9d08c-2024-4de2-8f86-b4a0ffd4b4e4'
    test_data = 'secret'
    assert do_vault(test_data, test_secret) == '$ANSIBLE_VAULT;1.1;AES256;filter_default\n' \
                                               '313632326163326433613161346132393237653666323262626465373938326239383439616434\n' \
                                               '373365363731323462646536373637323066393761307d0a\n'



# Generated at 2022-06-22 12:00:16.339308
# Unit test for function do_vault
def test_do_vault():
    """
    This test validates the functionality of do_vault filter.
    """
    import pytest
    secret = "secret"
    data = "data"

    vaultencryption = do_vault(data, secret)
    vaultencryption1 = do_vault(data, secret, 'salt')
    vaultencryption2 = do_vault(data, secret, 'salt', wrap_object=True)

    data1 = "data1"
    with pytest.raises(TypeError):
        do_vault(data1, secret)

    secret1 = "secret1"
    with pytest.raises(TypeError):
        do_vault(data, secret1)

    # Test argument wrap_object
    assert(type(vaultencryption2) == AnsibleVaultEncryptedUnicode)
   

# Generated at 2022-06-22 12:00:26.731392
# Unit test for function do_unvault
def test_do_unvault():
    secret = 'test'
    vaultid = 'test_vaultid'
    vault = '$ANSIBLE_VAULT;1.1;AES256;test_vaultid\n' \
            '65336566363733323561626263376236666633663431373036316330396265373630663938356634\n' \
            '396535396365396361336132646533636562626366616339633036623739623631646566305a0a00\n' \
            '\n'
    data = b'PASSWORD'
    assert do_unvault(vault, secret, vaultid) == data

# Generated at 2022-06-22 12:00:34.721504
# Unit test for function do_unvault
def test_do_unvault():
    import string

    # Generate a secret via os.urandom()
    secret = ''.join([chr(ord(i) % 256) for i in secret])

    # Encrypt the test string
    input_string = 'The quick brown fox jumps over the lazy dog'
    encrypted_string = do_vault(input_string, secret)

    # Compare the original to the decrypted output
    decrypted_string = do_unvault(encrypted_string, secret)
    assert decrypted_string == input_string