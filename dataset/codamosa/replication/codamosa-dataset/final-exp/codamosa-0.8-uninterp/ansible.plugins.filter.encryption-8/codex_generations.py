

# Generated at 2022-06-22 11:50:48.192938
# Unit test for function do_vault
def test_do_vault():
    secret = "mysecret"
    not_secret = "mysecret2"
    data = "some data that needs to be encrypted"
    salt = "abcdefghijklmnopqrstuvwxyz"

    vault = do_vault(data, secret, salt=salt)
    do_vault(data, not_secret, salt=salt)

# Generated at 2022-06-22 11:50:55.003310
# Unit test for function do_unvault
def test_do_unvault():
    assert do_unvault('$ANSIBLE_VAULT;1.1;AES256;ansible-vault-filter-default\n35326541324232353931393033353333346538346662363564333065633233633936656665626\n36562333963613734376663383039643061396166323834653537303736656664353637346536\n3433313136333239393361326238633764356365616465663336\n', 'secret', 'filter_default') == 'data'

# Generated at 2022-06-22 11:51:03.523527
# Unit test for function do_unvault
def test_do_unvault():
    secret = 'testsecret'
    vault = '$ANSIBLE_VAULT;1.1;AES256;foo\n' \
            '31623036316536643161326336313761643635616462376337636566393832666339323961363166613\n' \
            '3264313538663630633335336162333261646362303034383538396439\n'
    result = do_unvault(vault, secret, vaultid='vault_id')
    assert result == 'value'


# Generated at 2022-06-22 11:51:15.185599
# Unit test for function do_vault
def test_do_vault():
    secret = 'example'
    wrap_object = False
    vault = do_vault('test', secret, wrap_object=wrap_object)
    assert vault == '$ANSIBLE_VAULT;1.2;AES256;example\n34663564333263376131656337636533643666303232633362363532393964656563386466383565\n3237316665653632623235643465346163646131636361320a356564663739306336333637366363\n38393764663132653730373061316238613563353134663835323532626662316666333639383065\n633262633335346564\n'


# Generated at 2022-06-22 11:51:22.779507
# Unit test for function do_unvault
def test_do_unvault():
    secret = '$ANSIBLE_VAULT;1.1;AES256;ansible\n633266623761366361643938656238636236363065663933333131323862383533393761386266620a61396361633164353630383232613534393830363265663139656631313639666533646632623030\n39643634373033353636393731316233656461613238393965633562376339346436323937643061'
    vaultid = 'filter_default'
    result = 'this is a test' 
    assert do_unvault(secret, 'test', vaultid) == result
    assert do_unvault(secret, 'test') == result

# Generated at 2022-06-22 11:51:27.948949
# Unit test for function do_vault
def test_do_vault():
    secret = "test"
    data = "data"
    vault = do_vault(data, secret)
    print(vault)
    secret = "test"
    data = "data"
    vault = do_vault(data, secret,salt="13")
    print(vault)



# Generated at 2022-06-22 11:51:37.786391
# Unit test for function do_vault
def test_do_vault():
    import os
    import tempfile

    def make_temp_vault_secret(secret):
        f = tempfile.NamedTemporaryFile(delete=False)
        f.write(to_bytes(secret))
        f.close()
        return f.name

    def cleanup_temp_vault_secret(filename):
        try:
            os.unlink(filename)
        except:
            pass

    secret_file = make_temp_vault_secret('test')

# Generated at 2022-06-22 11:51:51.016023
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('SECRET', 'password') == b'$ANSIBLE_VAULT;1.1;AES256\n37336536373435653265663130393735666266633266373265383934643730373635336664363061\n376665363133646437656664303232306339616138613162390a6664393733643535633564363264\n39313366326166623139623764386532323336633664396364616239356366643438636435333535\n346437356331313837306334660a3438303736666537376635363966333162666334633134616664\n'

# Generated at 2022-06-22 11:52:02.967419
# Unit test for function do_unvault
def test_do_unvault():
    vault_secret='$ANSIBLE_VAULT;1.1;AES256'
    vault_data='6334353665353639383231333331336539616462366632333466303334666430356130656535333631'
    vault_id='test_do_unvault'
    vault_string='%s;%s' % (vault_secret, vault_data)
    unvault_string='hola'
    display.debug(unvault_string)
    assert do_unvault(vault_string, unvault_string, vault_id) == 'hola'

    vault_string=AnsibleVaultEncryptedUnicode(vault_string)
    display.debug(unvault_string)

# Generated at 2022-06-22 11:52:12.937497
# Unit test for function do_vault

# Generated at 2022-06-22 11:52:25.651108
# Unit test for function do_vault

# Generated at 2022-06-22 11:52:36.847439
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('test', 'test') == '$ANSIBLE_VAULT;1.2;AES256;foo\n3537656431393363306239336132306633643139393362373237643234393330633338613364636\n306666636635613063373561633462383839396631343165663061323333656164373135346231\n363638343836356336373737313530626134383038346635383563376361623035343132626335\n35653836633533383332376132666266356466303762336363376233356443633323362623530\n3361323332356638'


# Generated at 2022-06-22 11:52:50.197785
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('my_secret', 'my_password') == '$ANSIBLE_VAULT;1.1;AES256\n36353336346661623165336166326439663763396265343331366266303939313935303730393334\n37353765663332316431336234313333616165303531643735313661626434343238336461343563\n62363330636264653632656533363731366132316466323165326531653234623138356431613861\n6132326631383833396635396133633464', 'vault_result'

# Generated at 2022-06-22 11:52:54.370382
# Unit test for function do_vault
def test_do_vault():
    print('testing do_vault')
    secret = 'mypass'
    data = 'supersecretdata'
    vault = do_vault(data, secret)
    assert vault is not None
    assert vault != ''
    assert data != vault
    assert type(vault) == str


# Generated at 2022-06-22 11:53:03.266861
# Unit test for function do_vault
def test_do_vault():
    vault = do_vault("foo", "mysecret", salt="my salt")
    assert vault == "$ANSIBLE_VAULT;1.1;AES256;my salt\n63343337373464616532626265323339383465373836343166333933313737366136616239616233330a\n3765313563356636306336333034666136316332656134313335656636353966356534653336363435\n"



# Generated at 2022-06-22 11:53:14.803482
# Unit test for function do_vault
def test_do_vault():
    exc_msg = "can't be encrypted unaltered"
    with display.override_role_scope():
        assert do_vault(None, 'somesecret') == '$ANSIBLE_VAULT;1.1;AES256\n31363338353433316236316437306434353864376133313662393938623233346261626336636666\n623232363731386264333365366565616632333139646336333231666200\n\n'

# Generated at 2022-06-22 11:53:26.827337
# Unit test for function do_unvault
def test_do_unvault():
    import unittest

    class TestVaultLib(unittest.TestCase):
        vaultid = 'test'
        secret = 'mysecret'

        def setUp(self):
            self.vl = VaultLib([(self.vaultid, VaultSecret(self.secret))])

        def test_unvault_encryption(self):
            expected_output = 'welcome to ansible world'
            encrypted_data = self.vl.encrypt(to_bytes(expected_output))
            unvaulted_data = do_unvault(encrypted_data, self.secret)
            self.assertEqual(expected_output, unvaulted_data)

        def test_unvault_encryption_with_encrypted_object(self):
            expected_output = 'welcome to ansible world'

# Generated at 2022-06-22 11:53:38.510763
# Unit test for function do_vault
def test_do_vault():
    from ansible.plugins.filter.vault import do_vault
    v = do_vault("hello", "1234", "abcd")
    assert v == '$ANSIBLE_VAULT;1.1;AES256;abcd\n3439336230616665346639623562373864613761373236626334373934316563386236413637\n38380a6637303666356539643630376665363335393833626162663062343939336363356264\n6539373037383263613531323335356437376665663265323034386331306566326233616666\n666539343736343763336235393263326262300a'


# Generated at 2022-06-22 11:53:46.540351
# Unit test for function do_unvault
def test_do_unvault():
    import os
    import collections
    import pdb
    import pytest

    # load existing vault
    vault_path = os.path.join(os.path.dirname(__file__), "fixtures", "vault.yaml")
    with open(vault_path) as f:
        vault_data = f.read()

    display.display('')
    display.display('---------------------------------------------')

    vault_plain_text = do_unvault(vault_data, 'hunter2')
    display.display('Plain text: %s' % vault_plain_text)

    decrypted_vault_data = do_unvault(vault_data, 'hunter2')
    display.display(decrypted_vault_data)

    assert decrypted_vault_data == vault_plain_text

# Unit

# Generated at 2022-06-22 11:53:51.708402
# Unit test for function do_vault
def test_do_vault():
    # Test that vaulting a string returns a string that is not the same as the input
    data = 'test string'
    secret = 'testsecret'
    vault = do_vault(data, secret)
    assert isinstance(str(vault), str)
    assert data != vault


# Generated at 2022-06-22 11:54:04.079589
# Unit test for function do_vault

# Generated at 2022-06-22 11:54:14.367888
# Unit test for function do_vault
def test_do_vault():
    secret = 'test_secret'
    data = 'Test Data'
    vault = do_vault(data, secret)
    assert not is_encrypted(data)
    assert is_encrypted(vault)

# Generated at 2022-06-22 11:54:26.242828
# Unit test for function do_vault

# Generated at 2022-06-22 11:54:35.393510
# Unit test for function do_vault
def test_do_vault():

    data = 'some secret text'
    secret = 'a password'
    salt = 'salt data'
    vaultid = 'test_vault'

    vault = do_vault(data, secret, salt=salt, vaultid=vaultid)
    assert vault != ''
    assert vault.startswith('$ANSIBLE_VAULT')

    # test the unvault function
    new_data = do_unvault(vault, secret, vaultid=vaultid)
    assert new_data == data

# Generated at 2022-06-22 11:54:44.039220
# Unit test for function do_unvault

# Generated at 2022-06-22 11:54:55.860272
# Unit test for function do_vault
def test_do_vault():
    try:
        from hashlib import sha256
    except ImportError:
        from sha import new as sha256

    import base64
    import os

    secret = 'some secret'
    data = "some data"
    salt = base64.b64encode(os.urandom(32)).decode('utf-8')

    h1 = sha256()
    h1.update(bytes(secret, 'utf-8'))
    h1.update(bytes(salt, 'utf-8'))
    h1.update(bytes(data, 'utf-8'))


# Generated at 2022-06-22 11:55:06.898349
# Unit test for function do_vault
def test_do_vault():
    secret = 'secret'
    data = 'test'
    salt = None
    vaultid = 'filter_default'
    wrap_object = False

# Generated at 2022-06-22 11:55:17.951141
# Unit test for function do_vault
def test_do_vault():
    data_str = "test_str"
    secret = "secret"
    vaultid = "filter_default"
    wrap_object = False


# Generated at 2022-06-22 11:55:24.473449
# Unit test for function do_vault
def test_do_vault():
    secret = 'secret'
    salt = 'salt'
    vaultid = 'test_vault'
    data = 'test data'
    wrap_object = True
    vaulted = do_vault(data, secret, salt, vaultid, wrap_object)
    assert isinstance(vaulted, AnsibleVaultEncryptedUnicode)
    assert data == do_unvault(vaulted, secret, vaultid)
    assert data == vaulted

# Generated at 2022-06-22 11:55:32.225500
# Unit test for function do_vault
def test_do_vault():
    # If a password is not provided, the function should return a vaulted string
    assert type(do_vault('abcdefg')) == str
    # If a password is provided, the function should return a vaulted string
    assert type(do_vault('abcdefg', 'wow')) == str
    # If the data is not a string, the function should return an error
    try:
        assert type(do_vault(1234)) == str
    except AnsibleFilterTypeError:
        return True
    # If the secret is not a string, the function should return an error
    try:
        assert type(do_vault('abcdefg', 1234)) == str
    except AnsibleFilterTypeError:
        return True
    # If the data is already vaulted, the function should return it
    vaulted_data = do_v

# Generated at 2022-06-22 11:55:44.950180
# Unit test for function do_vault

# Generated at 2022-06-22 11:55:56.624171
# Unit test for function do_unvault
def test_do_unvault():

    import re

    # test with a known secret
    secret = "123"
    # we want to decrypt these

# Generated at 2022-06-22 11:56:07.010544
# Unit test for function do_unvault
def test_do_unvault():
    import os, tempfile
    from ansible.parsing.vault import VaultLib, VaultSecret

    # test unvault with a known data value, then compare the results
    # of 'unvault' to the original
    original = "test_unvault"
    tmpfile = tempfile.NamedTemporaryFile(delete=False)
    tmpfile.close()
    passphrase = "test_passphrase"
    VaultLib().encrypt_file(tmpfile.name, passphrase, original)
    vs = VaultSecret(to_bytes(passphrase))
    vl = VaultLib([('filter_default', vs)])
    result = do_unvault(open(tmpfile.name, "r").read(), passphrase)
    assert result == original

# Generated at 2022-06-22 11:56:14.873963
# Unit test for function do_unvault
def test_do_unvault():
    assert do_unvault('$ANSIBLE_VAULT;1.1;AES256;ansible\n393064303065643633313564656538633539353037333437646535376339656363656432303664\n623366303637623961633164393961613661323136656165393830353366653965616365363865\n353633613039663432613236396330633937616462393431333263393139363461616434376234\n363130376635306130313562313839623066343532303236316339616237343764343733313037\n35666238636230\n', 'password') == 'text'


# Generated at 2022-06-22 11:56:24.495229
# Unit test for function do_vault
def test_do_vault():
    vault = do_vault('this is a secret', 'test')
    unvault = do_unvault(vault, 'test')
    assert unvault == 'this is a secret'

    vault = do_vault('this is a secret', None)
    unvault = do_unvault(vault, None)
    assert unvault == 'this is a secret'

    vault = do_vault('this is a secret', 'test')
    unvault = do_unvault(vault, 'test')
    assert unvault == 'this is a secret'

    vault = do_vault('this is a secret', 'test')
    unvault = do_unvault(vault, 'test')
    assert unvault == 'this is a secret'

    # Test with a string
    vault

# Generated at 2022-06-22 11:56:36.152920
# Unit test for function do_vault
def test_do_vault():
    # Set the secret for the test
    secret = 'My Secret'

    # Set the salt for the test
    salt = '6d2e6b79aae5d7c1'

    # Set the vault id for the test
    vaultid = 'custom_vault'

    # Set the string data for the test
    data = 'This is a string'

    # Set the vault id for the test

# Generated at 2022-06-22 11:56:44.766203
# Unit test for function do_vault
def test_do_vault():
    secret = 'ansible'
    data = 'This is a test'
    vault = do_vault(data, secret)

# Generated at 2022-06-22 11:56:53.552523
# Unit test for function do_vault
def test_do_vault():
    secret_value = "password123"
    data_to_vault = "This is data"
    vaulted_data = b"$ANSIBLE_VAULT;1.1;AES256\n3539356437336635333739363432646336306139656164363731346637333466393233393266\n3135373265356330386462656535633433346363666306536663865656639\n"
    vault_test = do_vault(data_to_vault, secret_value)
    assert vault_test == vaulted_data


# Generated at 2022-06-22 11:57:04.798625
# Unit test for function do_vault
def test_do_vault():
    secret = 'test1234'
    data = 'This vault will be encrypted'
    vault = do_vault(data, secret)
    assert type(vault) == str

# Generated at 2022-06-22 11:57:09.094545
# Unit test for function do_vault
def test_do_vault():
    FilterClass = FilterModule()

# Generated at 2022-06-22 11:57:15.739633
# Unit test for function do_vault
def test_do_vault():
    data = 'test_data'
    secret = 'test_secret'
    vault = do_vault(data, secret)
    assert vault is not None, 'Failed to create vault'


# Generated at 2022-06-22 11:57:22.252631
# Unit test for function do_vault
def test_do_vault():
    try:
        assert do_vault("secret", "1234")
    except AssertionError:
        assert False
    try:
        assert do_vault("secret is a secret", "1234")
    except AssertionError:
        assert False
    try:
        assert do_vault("secret is a secret", "1234", wrap_object=True)
    except AssertionError:
        assert False


# Generated at 2022-06-22 11:57:32.343314
# Unit test for function do_unvault
def test_do_unvault():
    print("Testing function do_unvault")
    secret = b'password'
    vaulted_data = '$ANSIBLE_VAULT;1.1;AES256\n36343830326630643635333965653038373062343763386139373466396365313536346466313463\n65306133326165623235643833313730643362393961343466353636666230393835383832663362\n35313462373364346338356438333866313835643237303766393935633561623231626363323932\n37363764652\n'
    data = 'test'
    assert(do_unvault(vaulted_data, secret) == data)


# Generated at 2022-06-22 11:57:41.821270
# Unit test for function do_vault
def test_do_vault():
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import is_encrypted
    from ansible_collections.ansible.community.plugins.filter.vault import do_vault

    assert is_encrypted(do_vault('xyz', 'pass', None, 'test'))

    assert not is_encrypted(do_vault('xyz', 'pass', None, 'test', wrap_object=False))

    vault = do_vault('xyz', 'pass', None, 'test', wrap_object=True)
    assert isinstance(vault, AnsibleVaultEncryptedUnicode)

    assert do_vault('xyz', 'pass', None, 'test') == do_vault('xyz', 'pass', None, 'test')

# Generated at 2022-06-22 11:57:50.912622
# Unit test for function do_vault
def test_do_vault():
    res = do_vault('foo_bar_baz', 'secret')

# Generated at 2022-06-22 11:58:02.604582
# Unit test for function do_vault
def test_do_vault():
    assert do_vault("test", "password", wrap_object=True) == AnsibleVaultEncryptedUnicode(b'$ANSIBLE_VAULT;1.1;AES256\n31383539663133373634396439636237623965616332396338646130333237646563313762366132636663865\n3464656639356566323239633233376365653135616566356234626831686561786939333630356561343931\n3435373337323066306330346665356662613264616361386533353730786f3d3d\n')

# Generated at 2022-06-22 11:58:05.767152
# Unit test for function do_vault
def test_do_vault():
    secret = 'secret'
    data = 'data'
    vault = do_vault(data, secret)
    assert isinstance(vault, string_types)


# Generated at 2022-06-22 11:58:08.372084
# Unit test for function do_vault
def test_do_vault():
    secret = "password"
    assert "password" == do_vault("password", secret, salt="salt")


# Generated at 2022-06-22 11:58:20.398679
# Unit test for function do_vault

# Generated at 2022-06-22 11:58:31.623911
# Unit test for function do_vault
def test_do_vault():
    secret = 'password'
    value = "my password is 'password'"
    enc_data = do_vault(value, secret)

# Generated at 2022-06-22 11:58:48.376440
# Unit test for function do_vault
def test_do_vault():
    crypt = do_vault('foo', 'bar')

# Generated at 2022-06-22 11:58:56.627990
# Unit test for function do_unvault
def test_do_unvault():
    assert do_unvault("$ANSIBLE_VAULT;1.1;AES256\n61313337323736663830336466346535326339326666326434666333666431366538620a64616136636264643666356430663332326339396264316238633038636631640a3338653436383832646432663864323033643034376631316236633938353239\n", 'password', 'filter_default') == "username: password\npassword: password123\n"

# Generated at 2022-06-22 11:59:05.794420
# Unit test for function do_vault
def test_do_vault():
    v = do_vault("password", "secretpassword", "somesalt", "filter_default", False)
    assert to_native(v) == "$ANSIBLE_VAULT;1.1;AES256;somesalt;somesalt;16339864338295811136;d5b5a9a5e54c03a5e5d1a86f5d15a716;bcee07d55bfe0e49fd0ffb4a4f4e13f77cb17d2adc2f2ddbd2a8d9d95920a1e1"
    assert isinstance(v, string_types)



# Generated at 2022-06-22 11:59:13.014717
# Unit test for function do_vault
def test_do_vault():
    assert do_vault(None, None) == ''
    assert do_vault(None, '') == ''

# Generated at 2022-06-22 11:59:24.258247
# Unit test for function do_vault
def test_do_vault():
    secret = "ansible"
    data = "my_secret_data"


# Generated at 2022-06-22 11:59:30.159972
# Unit test for function do_vault
def test_do_vault():
    vault_secret = "vault_secret"
    data = "data"
    vault = do_vault(data, vault_secret)
    assert vault.startswith(b"$ANSIBLE_VAULT;")
    # with salt
    vault = do_vault(data, vault_secret, salt="123")
    assert vault.startswith(b"$ANSIBLE_VAULT;")
    # with id
    vault = do_vault(data, vault_secret, vaultid="vault_id")
    assert vault.startswith(b"$ANSIBLE_VAULT;")



# Generated at 2022-06-22 11:59:37.764956
# Unit test for function do_vault
def test_do_vault():
    result = do_vault("foobar", "password")
    assert result == "$ANSIBLE_VAULT;1.1;AES256\r\n35313631653766306434623932623335396164633233373866356437393933646532343436366130\r\n6638653066313339643933376132356533326262343835653233323961\r\n"



# Generated at 2022-06-22 11:59:47.022192
# Unit test for function do_vault
def test_do_vault():
    test_data = "Test string to be vaulted"
    test_secret = "test_secret"
    test_vaultid = "test_vaultid"
    test_wrap_object = True

    result = do_vault(test_data, test_secret, vaultid=test_vaultid, wrap_object=test_wrap_object)
    assert result['version'] == 1
    assert result['cipher'] == "aes256"
    assert result['unwrapped_checksum'] == '8920088f848b7cc6f2c6d2a6ee9f5cc5e5ce5d5b'



# Generated at 2022-06-22 11:59:51.532100
# Unit test for function do_vault
def test_do_vault():
    from jinja2 import Environment, FileSystemLoader

    env = Environment(loader=FileSystemLoader('./tests/filter_plugins'))

    template = env.get_template('test_vault.j2')
    data = template.render(secret='test123')

    assert data.startswith('$ANSIBLE_VAULT;1.1;')



# Generated at 2022-06-22 12:00:00.857439
# Unit test for function do_unvault
def test_do_unvault():
    secret = 'secretpassword'
    vault_string = '$ANSIBLE_VAULT;1.1;AES256\n636233313262656536623632373965643532393336653039656662306438306130313238623165626\n6265353939356430663635633038346336656333333537366532316534353638353330663337353333\n38646665353666306562636538356331393135616265356433336306231666333373932333139306536\n6665383732323832396539613139373230\n'.encode()
    decrypted = do_unvault(vault_string, secret)
    assert decrypted == 'qwerty'

# Generated at 2022-06-22 12:00:14.180904
# Unit test for function do_vault
def test_do_vault():
    my_secret = 'hello'
    my_data = 'world'
    my_vault = do_vault(my_data, my_secret)

    assert(True)


# Generated at 2022-06-22 12:00:18.786723
# Unit test for function do_vault
def test_do_vault():
    secret = 'secret'
    assert type(do_vault(data='value', secret=secret)) == str
    assert type(do_vault(data='value', secret=secret, wrap_object=True)) == AnsibleVaultEncryptedUnicode


# Generated at 2022-06-22 12:00:25.537259
# Unit test for function do_vault
def test_do_vault():
    secret = "foo"
    data = "bar"
    vaultid = "filter_default"
    wrap_object = False
    res = do_vault(data, secret, salt=None, vaultid=vaultid, wrap_object=wrap_object)
    print("test_do_vault: res=",res)
    assert isinstance(res,str)


# Generated at 2022-06-22 12:00:37.599024
# Unit test for function do_vault
def test_do_vault():
    ''' Tests for ansible vault jinja2 filters.'''

    from ansible.module_utils._text import to_native
    from ansible.module_utils.six import string_types
    from ansible.utils.display import Display
    display = Display()
