

# Generated at 2022-06-22 11:50:41.965345
# Unit test for function do_vault
def test_do_vault():
    secret = "this is secret"
    salt = "this is salt"
    vaultid = "this is vaultid"
    wrap_object = False
    display.display("do_vault: " + do_vault(secret, secret, salt, vaultid, wrap_object))


# Generated at 2022-06-22 11:50:44.232720
# Unit test for function do_unvault
def test_do_unvault():
    assert do_unvault(None, 'password') == ''


# Generated at 2022-06-22 11:50:52.239305
# Unit test for function do_vault
def test_do_vault():
    data = 'foo'
    secret = b'foobar'
    vault = do_vault(data, secret)

# Generated at 2022-06-22 11:51:02.298979
# Unit test for function do_unvault
def test_do_unvault():
    TEST_PASSWORD = 'ansible'
    TEST_VAULT = '$ANSIBLE_VAULT;1.2;AES256;ansible\n633862353264613561653138613532346264666336366163316364393734663661303365613231326\n3833666663333431623762643336643466633163373761346466653364303865343963373862663033\n3935346436663133326336356134396632373236633764353431323533303562316662366436396533\n393839326662346532386631623831323065326132626263653732306534373964396339326237\n'


# Generated at 2022-06-22 11:51:11.014086
# Unit test for function do_unvault
def test_do_unvault():
    import os
    import sys

    if sys.version_info[0] < 3:
        py3 = False
    else:
        py3 = True

    test_dir = os.path.dirname(__file__)
    test_vault_file = os.path.join(test_dir, "unittest_vault.yml")

    # Start with a locked file
    with open(test_vault_file, "rb") as fc:
        locked_vault = fc.read()

    # We need to make sure we can also handle strings that are unicode
    if not py3:
        locked_vault = locked_vault.decode('utf-8')

    # We should be able to handle a vaulted string with the correct key

# Generated at 2022-06-22 11:51:20.984058
# Unit test for function do_vault
def test_do_vault():
    secret = 'foo'
    invalid_secret = to_bytes('bar')
    invalid_secret2 = ['f', 'o', 'o']
    data = 'this is a secret'
    invalid_data = 10
    invalid_data2 = ['t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 's', 'e', 'c', 'r', 'e', 't']
    salt = 'salt'
    vaultid = 'salt'


# Generated at 2022-06-22 11:51:24.536557
# Unit test for function do_unvault
def test_do_unvault():
    # https://docs.python.org/2/library/unittest.html#basic-example
    assert ('1' == do_unvault(do_vault('1', 'test'), 'test'))

# Generated at 2022-06-22 11:51:31.157233
# Unit test for function do_unvault
def test_do_unvault():
    '''Unit test for function do_unvault'''
    password = 'password123'
    for text in ('this is a test', 'a' * 1000):
        vault = do_vault(text, password)
        assert do_unvault(vault, password) == text

if __name__ == "__main__":
    import sys

    test_do_unvault()
    sys.exit(0)

# Generated at 2022-06-22 11:51:39.281715
# Unit test for function do_unvault
def test_do_unvault():

    # Try data that is not encrypted
    data_not_encrypted = do_unvault("This is not encrypted", "This is a secret")
    assert data_not_encrypted == "This is not encrypted"

    # Try data that is encrypted with a different password
    data_encrypted_with_different_secret = do_unvault("!vault |\n          $ANSIBLE_VAULT;1.1;AES256;my_machine\n          3333306161623537656535393965633530346236613565373630393466363334620000", "This is a secret")
    assert data_encrypted_with_different_secret == "ANSIBLE_VAULT decrypting error: Can't decrypt data with provided secret"

    # Try data that is encrypted with the same password

# Generated at 2022-06-22 11:51:52.007970
# Unit test for function do_unvault
def test_do_unvault():
    # Should handle a salt=None
    assert do_unvault(do_vault('TestString', 'MySecret', salt=None), 'MySecret') == 'TestString'

    # Should raise an error for a wrong secret
    try:
        do_unvault(do_vault('TestString', 'MySecret', salt=None), 'MyWrongSecret')
    except AnsibleFilterError:
        pass
    else:
        assert False, "do_unvault should raise an error when an incorrect secret is supplied"

    # Should handle jinja2 undefined objects
    assert do_unvault(do_vault(Undefined(), 'MySecret', salt=None), 'MySecret') == 'UNDEFINED'
    assert do_unvault(do_vault('TestString', Undefined(), salt=None), 'MySecret')

# Generated at 2022-06-22 11:52:03.769564
# Unit test for function do_unvault

# Generated at 2022-06-22 11:52:13.545631
# Unit test for function do_unvault
def test_do_unvault():
    secret = 'secret'

# Generated at 2022-06-22 11:52:24.851770
# Unit test for function do_unvault
def test_do_unvault():
    secret = "secret"

# Generated at 2022-06-22 11:52:36.540768
# Unit test for function do_vault
def test_do_vault():
    ''' Test do_vault function '''
    secret = 'DUMMY_SECRET'

    assert do_vault('test_string', secret).startswith('$ANSIBLE_VAULT')
    assert do_vault('test_string', secret, True).data.startswith('$ANSIBLE_VAULT')
    assert do_vault('test_string', secret, '').startswith('$ANSIBLE_VAULT')
    assert do_vault('test_string', secret, '', True).data.startswith('$ANSIBLE_VAULT')
    assert do_vault('test_string', secret, 'test_salt').startswith('$ANSIBLE_VAULT')

# Generated at 2022-06-22 11:52:49.864688
# Unit test for function do_unvault
def test_do_unvault():
    vault_filter = FilterModule()

# Generated at 2022-06-22 11:52:58.349227
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('foo', 'bar') == b'$ANSIBLE_VAULT;1.2;AES256;ansible01\n39353366363031326132333831386436316437313337333064393434316631643538653262316634\n653336626363303039303239353133303634396262333266650a3566646139376637343366303538\n34623462336163396330373930353763636533623244383965333233366562613233646430393864\n633265363664373761620a'


# Generated at 2022-06-22 11:53:09.165926
# Unit test for function do_unvault
def test_do_unvault():
    secret = "ansible"

# Generated at 2022-06-22 11:53:16.432490
# Unit test for function do_vault
def test_do_vault():
    try:
        do_vault(1, 2)
    except AnsibleFilterTypeError as e:
        assert "Secret passed is required to be a string" in str(e), "Error message does not meet expectations"
    try:
        do_vault(1, '2')
    except AnsibleFilterTypeError as e:
        assert "Can only vault strings" in str(e), "Error message does not meet expectations"
    try:
        do_vault('1', '2')
    except AnsibleFilterError as e:
        assert "Unable to encrypt" in str(e), "Error message does not meet expectations"


# Generated at 2022-06-22 11:53:22.241217
# Unit test for function do_unvault
def test_do_unvault():

    secret = 'testpassword'
    salt = 'test_salt'
    vaultid = 'test'

    data = 'test_data'
    vaulted = do_vault(data=data, secret=secret, salt=salt, vaultid=vaultid)

    assert do_unvault(vaulted, secret=secret, vaultid=vaultid) == data

# Generated at 2022-06-22 11:53:33.099084
# Unit test for function do_unvault
def test_do_unvault():
    vault_string = '$ANSIBLE_VAULT;1.1;AES256;genesis\n36363035333934393237356232333266326232373035646338653335346665376262636632336330\n31386535613231326261383538653939336466303664663935306361303834383731666466333431\n35383232303966663436653133666135383066333161353436356566386438396661356232396463\n6430663734643164333334316333616334343662333438663030345a\n'
    secret = "gBBEF1cE"
    unvaulted = do_unvault(vault_string, secret)

# Generated at 2022-06-22 11:53:45.612784
# Unit test for function do_vault
def test_do_vault():
    import os
    import tempfile
    import subprocess
    import base64

    def _invoke_ansible_vault(data_file, password_file, action, vault_id='filter_default'):
        cmd = [
            'ansible-vault', action,
            '--vault-id',
            '@%s' % password_file,
            '--vault-id-type', 'prompt',
            '--vault-id-prompt', 'filter_default',
            data_file
        ]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = proc.communicate()
        if proc.returncode != 0:
            raise Exception((to_native(out), to_native(err)))
       

# Generated at 2022-06-22 11:53:57.751604
# Unit test for function do_unvault
def test_do_unvault():
    # Tests with all valid params
    assert do_unvault('gAAAAABdjJVrKZhk-tLvdmZmKw3Dq3Q2hNOyJGn_nRx9XCg-kqqYGdO-OwH2CvROiTTRBgC_unyW1e8rv55Mk1Za_pZ0l0Brw==', 'secret', 'filter_default') == 'this is a secret'


# Generated at 2022-06-22 11:54:09.550092
# Unit test for function do_vault

# Generated at 2022-06-22 11:54:19.401180
# Unit test for function do_vault
def test_do_vault():
    ansibleVaultEncryptedUnicode = u"$ANSIBLE_VAULT;1.2;AES256;test\n343432432dfffffef5e5f5f5e5e5e5e5ef5f5f5e5e5e5e5ef5f5e5e5e5e5e5e5e5ef5f5e5e5e5e5e5e5ef5f5e5e5\n"

    # Test bad secrets
    try:
        do_vault(None, None)
        assert(False)
    except AnsibleFilterTypeError as e:
        pass

    try:
        do_vault(None, 1)
        assert(False)
    except AnsibleFilterTypeError as e:
        pass


# Generated at 2022-06-22 11:54:30.491830
# Unit test for function do_vault
def test_do_vault():
    ''' do_vault unit test '''

# Generated at 2022-06-22 11:54:41.375870
# Unit test for function do_vault
def test_do_vault():
    from jinja2 import Template
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import hashes, hmac
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from binascii import hexlify

    data = b'hello world'

    salt_data = b'9e7b5f5dee10300a'
    salt = hexlify(salt_data).decode()
    iterations = 147000

# Generated at 2022-06-22 11:54:48.603154
# Unit test for function do_vault
def test_do_vault():
    vault = '$ANSIBLE_VAULT;1.1;AES256;filter_default\n333934373533303161636237616139363334353336353639383338386365303362643039333632633265\n646139633434363365653264f3b3d3e3e3238'
    secret = 'mysecret'
    assert vault == do_vault('test', secret)

# Generated at 2022-06-22 11:55:00.070798
# Unit test for function do_unvault
def test_do_unvault():
    # unvault will decrypt and return decrypted string
    assert do_unvault('$ANSIBLE_VAULT;1.1;AES256;test_default',"test") == "test"

    # unvault will return decrypted string

# Generated at 2022-06-22 11:55:03.565161
# Unit test for function do_unvault
def test_do_unvault():
    secret = "foo"
    vault_secret = VaultSecret(to_bytes(secret))
    vault = vault_secret.encrypt("bar")
    assert do_unvault(vault, secret) == "bar"

# Generated at 2022-06-22 11:55:06.268478
# Unit test for function do_unvault
def test_do_unvault():
    unvault = do_unvault(do_vault('secret-password', 'secret-password'), 'secret-password')
    assert unvault == "secret-password"

# Generated at 2022-06-22 11:55:19.307477
# Unit test for function do_unvault

# Generated at 2022-06-22 11:55:29.009973
# Unit test for function do_vault
def test_do_vault():
    secret_str = "secret"
    salt_str = "salt"
    vaultid_str = "filter_default"
    data_str = "data"
    vault_obj = do_vault("data", "secret", "salt", "filter_default", True)
    assert vault_obj.vaultid == "filter_default"

    # Make sure we fail for other data_type
    try:
        do_vault(42, secret_str, salt_str, vaultid_str)
        assert False
    except AnsibleFilterTypeError as e:
        assert e.message == "Can only vault strings, instead we got: <class 'int'>"

    # Make sure we fail for other secret_type

# Generated at 2022-06-22 11:55:40.416711
# Unit test for function do_vault

# Generated at 2022-06-22 11:55:52.534646
# Unit test for function do_vault

# Generated at 2022-06-22 11:55:58.500691
# Unit test for function do_vault
def test_do_vault():
    display.verbosity = 0
    try:
        do_vault('test', 'secret')
    except AnsibleFilterError as e:
        assert 'encrypted text' in to_native(e), "Unit test for 'test_do_vault' failed"
    else:
        assert False, "Unit test for 'test_do_vault' failed"


# Generated at 2022-06-22 11:56:09.105268
# Unit test for function do_vault
def test_do_vault():
    # Test the case of an empty vault.
    assert None == do_vault('', '')

    # Test the case of an empty secret and a valid vault.
    # This is a strange case but should be valid.

# Generated at 2022-06-22 11:56:20.666671
# Unit test for function do_unvault
def test_do_unvault():
    """ Test do_unvault filter """
    from . import do_unvault
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    # Try with a non-encrypted string
    assert do_unvault('https://docs.ansible.com', 'something') == 'https://docs.ansible.com'

    # Try with an encrypted string
    vault_value = do_vault('https://docs.ansible.com', 'something', vaultid='id1')
    assert do_unvault(vault_value, 'something', vaultid='id1') == u'https://docs.ansible.com'

    # Try with an AnsibleVaultEncryptedUnicode

# Generated at 2022-06-22 11:56:30.095701
# Unit test for function do_unvault
def test_do_unvault():
    import sys
    import ansible.constants as C

    if not C.DEFAULT_VAULT_IDENTITY_LIST:
        for path in ["~/.vault_pass.txt", "~/.vault_pass"]:
            vault_secret_file = os.path.abspath(os.path.expanduser(path))
            if os.path.exists(vault_secret_file):
                C.DEFAULT_VAULT_IDENTITY_LIST = [vault_secret_file]
                break

    if not C.DEFAULT_VAULT_IDENTITY_LIST:
        print("Unable to find any vault secrets to use")
        sys.exit(1)


# Generated at 2022-06-22 11:56:40.324160
# Unit test for function do_vault
def test_do_vault():
    import pytest
    from ansible.module_utils.six import PY3

    def _do_vault(data, secret, salt=None, vaultid='filter_default', wrap_object=False):
        from ansible.parsing.vault import is_encrypted, VaultSecret, VaultLib

        vault = ''
        vs = VaultSecret(secret.encode('utf-8'))
        vl = VaultLib()
        try:
            vault = vl.encrypt(data.encode('utf-8'), vs, vaultid, salt)
        except Exception as e:
            raise AnsibleFilterError("Unable to encrypt: %s" % to_native(e), orig_exc=e)

        if wrap_object:
            vault = AnsibleVaultEncryptedUnicode(vault)

# Generated at 2022-06-22 11:56:52.054412
# Unit test for function do_vault
def test_do_vault():
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six import u
    from ansible.utils.unsafe_proxy import wrap_var

    # Test unicode inputs
    secret = u('mysecret')
    data = u('mydata')
    vault_unicode = do_vault(data, secret)
    assert isinstance(vault_unicode, str)
    assert is_encrypted(vault_unicode)
    assert data == do_unvault(vault_unicode, secret)

    # Test string inputs
    secret = 'mysecret'
    data = 'mydata'
    vault_str = do_vault(data, secret)
    assert isinstance(vault_str, str)
    assert is_encrypted(vault_str)
    assert data == do_

# Generated at 2022-06-22 11:57:05.292059
# Unit test for function do_vault
def test_do_vault():
    secret = 'ansiBle1'
    salt = '12345678'
    vaultid = 'base64'


# Generated at 2022-06-22 11:57:16.116468
# Unit test for function do_vault
def test_do_vault():
    from ansible.plugins.filter.vault import FilterModule
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    filter_vault = FilterModule()
    filters = filter_vault.filters()

    # unencrypted string
    unencrypted_string = 'Some unencrypted string'
    # encrypted string
    # $ echo -n 'Some unencrypted string' | ansible-vault encrypt_string --vault-id 'filter_default' --name 'filters_vault_test' --stdin-name 'filters_vault_unencrypted'
    # ansible-vault encrypt_string --vault-id 'filter_default' --name 'filters_vault_test' --stdin-name 'filters_vault_unencrypted'
    # New Vault password:
    #

# Generated at 2022-06-22 11:57:22.837019
# Unit test for function do_vault
def test_do_vault():
    from ansible.module_utils.parsing.convert_bool import boolean
    assert do_vault("a", "secret") == "!vault |" + boolean(is_encrypted("!vault |"), True) + "| CSLKjV7/S6vxU6P3qzmbDD50OWDZovwvj0W3q8rhu5c="


if __name__ == '__main__':
    test_do_vault()

# Generated at 2022-06-22 11:57:32.750771
# Unit test for function do_unvault
def test_do_unvault():
    secret = "AES256_KEY"
    vault_text = b"$ANSIBLE_VAULT;1.1;AES256;f4b4aa4e9ff9d2f0a9468aca2cc8f6b78f1d543ac2072922a60836af884e3cdd\n3431373236363639646336616265396665353331656266343238626365656330343531326633\n36653936320a3231383339363062396265353338353864626135313165393138393033653333\n6365636135656264386236636236373331393162633630386532306539386438343564653362\n326464380a66643431"

# Generated at 2022-06-22 11:57:42.046209
# Unit test for function do_unvault

# Generated at 2022-06-22 11:57:51.053399
# Unit test for function do_vault
def test_do_vault():
    from ansible.utils.hashing import secure_hash
    from ansible.plugins.loader import filter_loader
    from ansible.errors import AnsibleFilterError

    plain = 'secret'
    vault = '$ANSIBLE_VAULT;1.1;AES256;{0}'

    # Generate a wrapped object
    secret = secure_hash(plain)
    filtered = filter_loader.filters().get('vault')(plain, secret, wrap_object=True)
    assert isinstance(filtered, AnsibleVaultEncryptedUnicode)
    assert is_encrypted(filtered)
    assert filtered == vault.format(secret)
    assert filtered.data == plain

    # Generate a string
    secret = secure_hash(plain)

# Generated at 2022-06-22 11:57:59.142468
# Unit test for function do_vault
def test_do_vault():
    from ansible.parsing.vault import preprocess_vaulted
    data="asdfasdf"
    secret="asdf"
    vaultid = "filter_default"
    vault = do_vault(data, secret, salt=None, vaultid=vaultid)
    assert preprocess_vaulted("$ANSIBLE_VAULT;1.1;AES256;asdfasdfasdf\n" + vault + "\n", secret_file=None) == data


# Generated at 2022-06-22 11:58:05.571936
# Unit test for function do_unvault
def test_do_unvault():
    assert do_unvault(u'$ANSIBLE_VAULT;1.1;AES256;test;2116171812783365666130333537653839353361333861662d35336132313861303235382d3137363863666165342d32323963396433363762356231612d3438393033366465653464313363206466386564343938376435373363393466636365303636633737333363230393664663738313466323064653330626330363734623133352e',
          'test') == u'jinja2 filters'


# Generated at 2022-06-22 11:58:17.207908
# Unit test for function do_unvault
def test_do_unvault():
    """
    Unit test for function do_unvault
    """

# Generated at 2022-06-22 11:58:29.350122
# Unit test for function do_vault
def test_do_vault():
    import pytest
    from ansible.parsing.vault import is_encrypted

    def run_test(data, secret, salt, vaultid, wrap_object, expected):
        result = do_vault(data, secret, salt, vaultid, wrap_object)
        assert is_encrypted(result)
        assert result == expected

    with pytest.raises(AnsibleFilterTypeError) as e:
        do_vault(123, "foo")
    assert "Can only vault strings, instead we got: <type 'int'>" in str(e)

    with pytest.raises(AnsibleFilterTypeError) as e:
        do_vault("foo", 123)
    assert "Secret passed is required to be as string, instead we got: <type 'int'>" in str(e)


# Generated at 2022-06-22 11:58:44.141106
# Unit test for function do_vault
def test_do_vault():

    secret = AnsibleFilterTypeError
    with pytest.raises(secret) as ex:
        do_vault('a', 1)
        assert "'Secret passed is required to be a string, instead we got: <class 'int'>" in ex.value

    data = AnsibleFilterTypeError
    with pytest.raises(data) as ex:
        do_vault(1, 'abc')
        assert "Can only vault strings, instead we got: <class 'int'>" in ex.value

    err = AnsibleFilterError
    with pytest.raises(err) as ex:
        do_vault('a', 'abc')
        assert 'Unable to encrypt: ' in ex.value

    assert isinstance(do_vault('a', 'abc', wrap_object=True), AnsibleVaultEncryptedUnicode)


# Generated at 2022-06-22 11:58:49.942169
# Unit test for function do_vault
def test_do_vault():
    secret = 'mysecret'
    data = 'mydata'

    vault = do_vault(data, secret)
    assert vault.startswith('$ANSIBLE_VAULT;')
    vault_decrypt_data = do_unvault(vault, secret)
    assert vault_decrypt_data == data


# Generated at 2022-06-22 11:58:59.537940
# Unit test for function do_unvault
def test_do_unvault():
    secret = 'hello_world'

# Generated at 2022-06-22 11:59:10.445138
# Unit test for function do_unvault

# Generated at 2022-06-22 11:59:12.962316
# Unit test for function do_vault
def test_do_vault():
    data = '123456'
    secret = 'password'
    vault = do_vault(data, secret)
    assert data != vault



# Generated at 2022-06-22 11:59:20.736584
# Unit test for function do_unvault
def test_do_unvault():

    vault = """$ANSIBLE_VAULT;1.2;AES256;filter_default
3338653835346665656239633166656137653333303436363835346630653136653639346161316437
6232376237633330353734666437653366313730363336386339353839376461306564396637643565
643366
"""
    secret = "secret"
    do_unvault(vault, secret)

# Generated at 2022-06-22 11:59:29.679790
# Unit test for function do_vault

# Generated at 2022-06-22 11:59:38.658916
# Unit test for function do_unvault
def test_do_unvault():
    import unittest
    class TestDoUnvault(unittest.TestCase):
        def test_do_unvault(self):
            # Encrypt a string
            vault = do_vault('test-data', 'secret-password')
            # Decrypt and verify string
            data = do_unvault(vault, 'secret-password')
            self.assertEqual(data, 'test-data')
            # Verify bytes
            self.assertTrue(isinstance(data, string_types))
    unittest.main()


if __name__ == '__main__':
    test_do_unvault()

# Generated at 2022-06-22 11:59:48.317956
# Unit test for function do_vault
def test_do_vault():
    ret = do_vault("secret", "password")
    assert ret == "$ANSIBLE_VAULT;1.1;AES256\n363938303734313162653335376230326632633132313163623934373539363637636637396634\n616430316531353266666339613365373635393462646535366130626538623265303730323239\n653066343832666165373834636361613637343764323530356233386364646630656466373064\n3464666534363761\n"


# Generated at 2022-06-22 11:59:58.287723
# Unit test for function do_vault
def test_do_vault():
    import os
    import tempfile

    # create temporary file to hold vault id list
    (fd1, vidfile) = tempfile.mkstemp(prefix='ansible-vault-ids')
    f1 = os.fdopen(fd1, 'w+')

# Generated at 2022-06-22 12:00:13.086453
# Unit test for function do_vault
def test_do_vault():
    secret = '12345678'
    plaintext = 'Hello World'
    salt = None
    encrypt_str = do_vault(plaintext, secret, salt, 'test_do_vault', wrap_object=False)
    encrypt_obj = do_vault(plaintext, secret, salt, 'test_do_vault', wrap_object=True)
    decode_str = do_unvault(encrypt_str, secret, 'test_do_vault')
    decode_obj = do_unvault(encrypt_obj, secret, 'test_do_vault')

    if plaintext != decode_str:
        print('test_do_vault: failed on string')
    elif plaintext != decode_obj:
        print('test_do_vault: failed on obj')

# Generated at 2022-06-22 12:00:23.483727
# Unit test for function do_vault
def test_do_vault():
    data = do_vault('hello world', 'secret', vaultid='filter_default', wrap_object=True)
    assert data == AnsibleVaultEncryptedUnicode(b'$ANSIBLE_VAULT;1.1;AES256;filter_default\n32363132613336636465636163373536663933386362626362656537323337653666386463313236\n66387265336639336335346535313235343835323062373837386662386435376130313261333935\n62336236616535333366343831326132333561363631653338346539623161326164656636353765\n313562376362626230393834646533356331386133353339\n')

# Generated at 2022-06-22 12:00:28.004404
# Unit test for function do_vault
def test_do_vault():
    secret = 'secret'
    data = 'The quick brown fox jumps over the lazy dog'
    expected_vault = '$ANSIBLE_VAULT;1.2;AES256;filter_default;3nq3q3J86VCjMyGh1nq3q3A=='
    vault = do_vault(data, secret)
    assert vault == expected_vault



# Generated at 2022-06-22 12:00:39.894347
# Unit test for function do_vault