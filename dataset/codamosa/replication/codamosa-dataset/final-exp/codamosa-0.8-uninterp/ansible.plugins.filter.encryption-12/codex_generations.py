

# Generated at 2022-06-22 11:50:48.798282
# Unit test for function do_unvault

# Generated at 2022-06-22 11:50:57.782232
# Unit test for function do_unvault
def test_do_unvault():
    from ansible.parsing.vault import VaultSecret
    import base64
    #        name: !vault |
    #            $ANSIBLE_VAULT;1.1;AES256
    #            62626662643633663632653738656532303637656335613763633961633233653865386531323931
    #            31353135666661396161326562353135356430373331353633356437663764356236356433306536
    #            66303962373563393338323534646234653834393962612d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d
    #            2d2d2d2d2d2d2d

# Generated at 2022-06-22 11:51:07.762737
# Unit test for function do_unvault
def test_do_unvault():
    # Test for non-encrypted string
    input_string = "test"
    assert do_unvault(input_string, "test") == input_string
    assert do_unvault(input_string, "test") != "test"

    # Test for encrypted string

# Generated at 2022-06-22 11:51:18.906080
# Unit test for function do_vault
def test_do_vault():

    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    import pytest

    # test of do_vault function with a string
    secret = "password"
    data = "ansible"
    vault = do_vault(data, secret)
    assert isinstance(vault, str)
    assert vault != data

    # test of do_vault function with an encrypted string
    secret = "password"

# Generated at 2022-06-22 11:51:28.453806
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('foo', 'bar') == '$ANSIBLE_VAULT;1.1;AES256\n3634663762346133633365643038636433633230323138653366636639303537326139326534\n3637373633653734313262393161376663353762643533393830356532613638373932343166\n3961646665393839623932623030653763326533613939666535396136316563636434306638\n3162647d\n'


# Generated at 2022-06-22 11:51:29.793397
# Unit test for function do_unvault
def test_do_unvault():
    # TODO: Add unit tests
    return

# Generated at 2022-06-22 11:51:38.650080
# Unit test for function do_vault
def test_do_vault():
    import pytest

    # import the method to test
    from ansible_collections.ansible.community.plugins.filter.vault import do_vault

    # Test 1
    # Input: hello, secret and salt
    # Output: vault object
    def test_1():
        vault = do_vault('hello', 'secret', 'salt')
        assert vault.startswith('$ANSIBLE_VAULT;1.1;AES256')

    # Test 2
    # Input: wrapped vault object
    # Output: vault object
    def test_2():
        vault = do_vault('hello', 'secret', 'salt', wrap_object=True)
        assert vault.startswith('$ANSIBLE_VAULT;1.1;AES256')

    # Test 3
    # Input: wrapped vault object when vaultid

# Generated at 2022-06-22 11:51:46.687294
# Unit test for function do_vault
def test_do_vault():
    secret = 'password'
    data = 'secret data'
    salt = 'salt'
    vaultid = 'test'
    test_vault = do_vault(data, secret, salt, vaultid, wrap_object=True)
    assert isinstance(test_vault, AnsibleVaultEncryptedUnicode)
    assert test_vault.vaultid == vaultid
    assert test_vault.salt == salt


# Generated at 2022-06-22 11:51:56.605784
# Unit test for function do_vault
def test_do_vault():
  data = "password2"
  secret = "password1"
  vault = do_vault(data, secret)


# Generated at 2022-06-22 11:52:08.696074
# Unit test for function do_vault

# Generated at 2022-06-22 11:52:23.426090
# Unit test for function do_vault
def test_do_vault():
    data = 'this is plaintext'
    secret = 'P@ssword'
    salt = 'salt'
    vaultid = 'test_vault'
    wrap_object = True

    assert isinstance(do_vault(data, secret, salt, vaultid, wrap_object), AnsibleVaultEncryptedUnicode)
    assert isinstance(do_vault(data, secret), string_types)
    assert isinstance(do_vault(data, secret, wrap_object=True), AnsibleVaultEncryptedUnicode)
    assert do_vault(data, secret) == do_vault(data, secret, salt, vaultid, False)
    assert do_vault(data, secret, salt, vaultid, wrap_object) != do_vault(data, secret, salt, vaultid, False)

#

# Generated at 2022-06-22 11:52:26.943037
# Unit test for function do_unvault
def test_do_unvault():
    from ansible.parsing.vault import VaultSecret, VaultLib

    secret = VaultSecret('password')
    vault = VaultLib([('test', secret)])
    vaultstr = vault.encrypt('password')

    try:
        assert_equal(do_unvault(vaultstr, 'password'), 'password')
    except Exception:
        assert False

# Generated at 2022-06-22 11:52:35.622809
# Unit test for function do_unvault

# Generated at 2022-06-22 11:52:48.670529
# Unit test for function do_vault
def test_do_vault():
    import sys
    import os
    import inspect
    import unittest

    try:
        from unittest.mock import patch, mock_open
    except ImportError:
        from mock import patch, mock_open

    from ansible.module_utils.six import PY3
    from ansible.module_utils._text import to_bytes, to_native
    from ansible.parsing.yaml import objects
    from ansible.parsing.vault import VaultSecret, VaultLib

    # Get the current test name
    test_name = inspect.stack()[0][3]

    # Get our vars ready
    v_secret = 'This is my secret'
    v_salt   = 'This is my salt'
    v_data   = 'This is my data'

# Generated at 2022-06-22 11:53:00.469128
# Unit test for function do_vault
def test_do_vault():
    """ Ansible vault jinja2 function simulate test """
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils._text import to_native, to_bytes
    from ansible.module_utils.six import binary_type

    vl = VaultLib()
    vs = VaultSecret(to_bytes("ansible"))
    data = to_bytes("ansible")

    print("\n")
    print("==============================")
    print("   UnitTest for do_vault")
    print("==============================")

    print("\n")
    print("data: ansible")
    print("password: ansible")
    print("vault:")
    print(vl.encrypt(data, vs))
    print("\n")

# Generated at 2022-06-22 11:53:11.648344
# Unit test for function do_vault
def test_do_vault():
    _vault = do_vault("test", "secret", "salt", "id")

# Generated at 2022-06-22 11:53:19.025696
# Unit test for function do_unvault
def test_do_unvault():
    assert do_unvault("$ANSIBLE_VAULT;1.2;AES256;test_value\n614352646365513033623635333064343536373539306438623333616561316538333231353432\n393534373731353033373533343739343830623139643461316464333635353262656166633463\n33633633066353436626163613064316364336130376338386663326263343a7a3933303333376\n63663336366230343433363039376161356231346662353262636664336132", "password") == "test_value"

# Generated at 2022-06-22 11:53:25.622946
# Unit test for function do_vault
def test_do_vault():
    encrypted_string = do_vault('data', 'secret')
    assert encrypted_string.startswith(u'$ANSIBLE_VAULT;')

    encrypted_obj = do_vault('data', 'secret', wrap_object=True)
    assert isinstance(encrypted_obj, AnsibleVaultEncryptedUnicode)
    assert encrypted_obj.startswith(u'$ANSIBLE_VAULT;')



# Generated at 2022-06-22 11:53:35.326088
# Unit test for function do_unvault
def test_do_unvault():
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.vault import VaultSecret

    data = 'test'
    secret = 'test'
    vaultid = 'filter_default'

    vs = VaultSecret(secret.encode('utf-8'))
    vl = VaultLib([(vaultid, vs)])

    vault = vl.encrypt(data.encode('utf-8'), vs, vaultid)
    vault = AnsibleUnsafeText(vault)

    result = do_unvault(vault, secret, vaultid)
    assert(data == result)

# Generated at 2022-06-22 11:53:44.224541
# Unit test for function do_vault
def test_do_vault():
    secret1 = "supersecret"
    mydict = {
        "name": "joe",
        "password": "supersecret"
    }
    result = do_vault(str(mydict), secret1, salt="abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabca", vaultid="vaultid", wrap_object=True)
    assert result is not None
    


# Generated at 2022-06-22 11:53:58.395889
# Unit test for function do_unvault

# Generated at 2022-06-22 11:54:10.061275
# Unit test for function do_vault
def test_do_vault():
    import json
    import os
    import hashlib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    vault_password = os.environ.get('ANSIBLE_VAULT_PASSWORD', None)
    if vault_password is None:
        print("ANSIBLE_VAULT_PASSWORD enviroment variable is not defined. The tests will fail.")
    _data = {
        'id': 'test@test.com',
        'password': 'test@test.com',
        'salt': 'salt',
        'data': 'test',
        'data_unicode': 'test',
        'data_list': ['test', 'test'],
        'data_dict': {'test': 'test'}
    }

# Generated at 2022-06-22 11:54:19.591006
# Unit test for function do_unvault

# Generated at 2022-06-22 11:54:30.673970
# Unit test for function do_vault
def test_do_vault():
    from ansible.parsing.yaml.constructor import DuplicateKeyError
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    # lowercase secret
    assert(do_vault("data", "secret") == "!.vault.ANSIBLE_VAULT!include:#0nAv6CFkz6U=:include:")

    # uppercase secret
    assert(do_vault("data", "SECRET") == "!.vault.ANSIBLE_VAULT!include:pZ9XnmIOKD0=:include:")

    # Unsupported salt

# Generated at 2022-06-22 11:54:41.339474
# Unit test for function do_vault
def test_do_vault():
    import os
    import textwrap
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    import ansible.constants as C

    def _mock_vault_lib(encrypt=True):
        class VaultLib:
            def encrypt(self, data, vault_secret, id=None, salt=None):
                raise AnsibleFilterError('do_vault test exception')
            def decrypt(self, data):
                raise AnsibleFilterError('do_unvault test exception')

        return VaultLib()

    def _mock_vault_secret(secret):
        class VaultSecret:
            def __init__(self, secret=None):
                self.secret = hashlib.sha256(secret.encode()).hexdigest()
                self.salt = '0123456789'

# Generated at 2022-06-22 11:54:53.410735
# Unit test for function do_unvault
def test_do_unvault():
    vaulted = AnsibleVaultEncryptedUnicode("$ANSIBLE_VAULT;1.1;AES256\n31393733383538373964633633643537386465336235623633663536386638306566353439\n30666331323139326565323935636637333464333933663730396231643962386363323364\n33323863393262626335313730356561323431376631333932626562393062373233353363\n3866623364353637323134313337353036623633646537663733393762393034\n")
    secret = "password"
    result = do_unvault(vaulted, secret)

# Generated at 2022-06-22 11:55:05.075487
# Unit test for function do_unvault
def test_do_unvault():
    # Tests passed
    # data unencrypted
    data = "some_data"
    vaultid = "filter_default"
    secret = "password"

    # data unencrypted - vaultid given
    data = "some_data"
    vaultid = "new_vaultid"
    secret = "password"

    # data encrypted - vaultid given

# Generated at 2022-06-22 11:55:13.052823
# Unit test for function do_vault
def test_do_vault():
    assert do_vault(None, None) == ''
    assert do_vault(15, 'password') == ''
    assert do_vault('string', 12) == ''


# Generated at 2022-06-22 11:55:24.263370
# Unit test for function do_unvault
def test_do_unvault():
    test_secret = b'$ANSIBLE_VAULT;1.1;AES256\n;vault_id                  vault_id_a\n;The key to vault your secrets\n65613339643262336339663765643835396465653564343165313739373330343836386431643430\033\n'
    test_data = b'$ANSIBLE_VAULT;1.1;AES256\n39323066623665636133313161393265613231393530363339623365363361306262633131393630\033\n'


# Generated at 2022-06-22 11:55:36.340363
# Unit test for function do_unvault
def test_do_unvault():
    # do_unvault should raise an error if args is not a string
    args = 1
    expected_msg = "Vault should be in the form of a string, instead we got: <type 'int'>"
    try:
        do_unvault(args)
        assert False
    except AnsibleFilterTypeError as e:
        assert to_native(e) == expected_msg

    # do_unvault should return the input if it is not encrypted
    args = 'text'
    expected = 'text'
    actual = do_unvault(args)
    assert expected == actual

    # do_unvault should return an error if input is encrypted and secret is not provided

# Generated at 2022-06-22 11:55:44.650100
# Unit test for function do_unvault
def test_do_unvault():
    secret = "test"
    data = "test"

    # Test with valid encoding of data
    vault = do_vault(data, secret)
    display.display(vault)
    assert do_unvault(vault, secret) == data

    # Test with invalid encoding of data
    data = "test"
    vault = "{$ANSIBLE_VAULT;1.1;AES256;ansible}test"
    display.display(vault)
    assert do_unvault(vault, secret) == data

    # Test with plaintext data
    data = "test"
    vault = data
    assert do_unvault(vault, secret) == data

# Generated at 2022-06-22 11:55:56.141538
# Unit test for function do_vault
def test_do_vault():
    import pytest
    # test for success case
    vault = do_vault('testpass', 'mysecret', wrap_object=True)
    assert vault.vault is not None
    assert vault.data == 'testpass'
    assert do_vault('testpass', 'mysecret', wrap_object=False) == '$ANSIBLE_VAULT;1.1;AES256'
    # test for failure cases
    with pytest.raises(AnsibleFilterTypeError):
        do_vault(None, 'mysecret')
    with pytest.raises(AnsibleFilterTypeError):
        do_vault(None, None)
    with pytest.raises(AnsibleFilterTypeError):
        do_vault('testpass', None)

# Generated at 2022-06-22 11:56:05.639500
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('foo', 'passwO0rd') == '$ANSIBLE_VAULT;1.2;AES256;filter_default\n3934653665363839663765326435673365653232616535336535316232303864383131656263663b0a\n'
    try:
        do_vault(1, 'passwO0rd')
        assert False, 'Expected an AnsibleFilterTypeError to be raised'
    except AnsibleFilterTypeError as e:
        assert e.message == 'Can only vault strings, instead we got: <class \'int\'>'



# Generated at 2022-06-22 11:56:14.073838
# Unit test for function do_vault
def test_do_vault():
    import pytest

    with pytest.raises(AnsibleFilterTypeError):
        do_vault({"test": "data"}, "secret")

    with pytest.raises(AnsibleFilterTypeError):
        do_vault("data", {"test": "secret"})


# Generated at 2022-06-22 11:56:21.498117
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('some-clear-text', 'some-secret') == u'$ANSIBLE_VAULT;1.2;AES256;filter_default;\naW5zZXJ0IHlvdXIga2V5LCBpZiB5b3Ugc2F5IG5vIGkga25vdyB5b3UgcmVtYWluc2lvbgoxNTQ0Mzg0NTU4Cg==\n'


# Generated at 2022-06-22 11:56:33.494994
# Unit test for function do_unvault
def test_do_unvault():
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import VaultLib
    import os
    import tempfile
    import shutil
    import yaml
    import pickle
    import json

    # Generic vault_secret to use for all tests.
    vault_secret = VaultSecret('secretpassword')

    # Set up temporary directory
    temp_dir = tempfile.mkdtemp()

    # Test cases

# Generated at 2022-06-22 11:56:44.059868
# Unit test for function do_vault
def test_do_vault():
    secret = 'secret'
    data = 'data'
    vault = do_vault(data, secret)

# Generated at 2022-06-22 11:56:54.414378
# Unit test for function do_unvault
def test_do_unvault():
    assert do_unvault(None, None) is None
    assert do_unvault(True, None) is True
    assert do_unvault(False, None) is False
    assert do_unvault(1, None) == 1
    assert do_unvault(0, None) == 0
    assert do_unvault(1.0, None) == 1.0
    assert do_unvault(0.0, None) == 0.0
    assert do_unvault([], None) == []
    assert do_unvault({}, None) == {}
    assert do_unvault({'foo': 'bar'}, None) == {'foo': 'bar'}



# Generated at 2022-06-22 11:57:00.386163
# Unit test for function do_vault
def test_do_vault():
    import jinja2
    template = '{{ "W8Zv1UiCkKj6A+M6Qg8n0Q==" | vault("test string", "test salt", "testvaultid") }}'
    env = jinja2.Environment()
    env.filters['vault'] = do_vault
    tmpl = env.from_string(template)
    tmpl.render()


# Generated at 2022-06-22 11:57:09.469247
# Unit test for function do_unvault

# Generated at 2022-06-22 11:57:17.578779
# Unit test for function do_vault
def test_do_vault():
    secret = 'secret'
    input_data = '123456789'
    original_data = '123456789'
    vault = do_vault(input_data, secret)
    assert vault != original_data
    assert do_unvault(vault, secret) == original_data


# Generated at 2022-06-22 11:57:29.339769
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('d1', 's1') == '$ANSIBLE_VAULT;1.2;AES256;ansible_vault_filter_default\n35313366626266326132333537623962353431646136663834383536333937623831646239616\n362620a3833383431386231343430366466363361303263383366653836646132333236393937\n6231316132313431333639386638623932396539623231303235663934653266\n'
    assert do_vault("{{ foo }}", secret="{{ bar }}") == "{{ foo }}"

# Generated at 2022-06-22 11:57:40.698718
# Unit test for function do_vault
def test_do_vault():
    assert do_vault("test_string", "my_secret") == "AQAAAAIAAAADZgAAABAAAAAQC+wGgKjNKBQbS/h1Sfq3/abn/9XZAAAAEAAAABAAAAAQAAAAQAAABWTgAAAAQAAAAJAAAAAAAAAAAAAAABAAAABPjxmU6f9pKjCYcYHvLPwRLoOu+L8yaWKbHl+2QAAAAQag1Og2hubV7e1ZjqL3qnhL5rPV5jdus5GxTE7bFhXdYM8joMgONkb7zwHklsghD7m8i10bMEAAAAB"


# Generated at 2022-06-22 11:57:51.141878
# Unit test for function do_vault
def test_do_vault():
    secret = "secret"
    data = "test"
    salt = None
    vaultid = 'filter_default'
    wrap_object = False

# Generated at 2022-06-22 11:58:02.735442
# Unit test for function do_unvault

# Generated at 2022-06-22 11:58:07.385453
# Unit test for function do_vault
def test_do_vault():
    vault = '$ANSIBLE_VAULT;1.1;AES256'
    secret = 'password'
    input_string = 'test string'

    result = do_vault(input_string, secret)
    assert result[0:len(vault)] == vault


# Generated at 2022-06-22 11:58:19.189181
# Unit test for function do_vault
def test_do_vault():
    # create a filter object
    filter = FilterModule()

    # get the filters from the object
    filters = filter.filters()
    vault = filters.get('vault')

    # test the do_vault function

# Generated at 2022-06-22 11:58:30.740601
# Unit test for function do_vault

# Generated at 2022-06-22 11:58:38.909241
# Unit test for function do_unvault
def test_do_unvault():
    data_unencrypted = "foobar"
    data_encrypted = "$ANSIBLE_VAULT;1.1;AES256\n30666430633962626536356430653138399f5b30d970baccd3b3c60d5ea0593e0a\n633231366430383237643730366437656664323066336537666439303764306330\n343563353065356432656163633033653937653466303437653938"

    assert do_unvault(data_encrypted, "secret") == data_unencrypted
    assert do_unvault(data_unencrypted, "secret") == data_unencrypted


# Generated at 2022-06-22 11:58:50.735742
# Unit test for function do_vault
def test_do_vault():
    secret = 'mysecret'
    data = 'mydata'
    salt = 'mysalt'
    vaultid = 'filter_default'
    wrap_object = False
    result = do_vault(data, secret, salt, vaultid, wrap_object)

    assert isinstance(result, string_types)

    vault = AnsibleVaultEncryptedUnicode(result)
    assert isinstance(vault, AnsibleVaultEncryptedUnicode)

    data = vault.data
    assert isinstance(data, string_types)

    wrap_object = True
    result = do_vault(data, secret, salt, vaultid, wrap_object)

    assert isinstance(result, AnsibleVaultEncryptedUnicode)
    assert isinstance(result.data, string_types)

    secret = 123

# Generated at 2022-06-22 11:59:05.513333
# Unit test for function do_vault
def test_do_vault():
    import copy

    my_secret = 'my_secret'
    my_string = 'my_string'
    my_string_vault = '$ANSIBLE_VAULT;1.1;AES256;filter_default\nvLHp/5X0Eg+ZKDWAHNQDPQ==\n'
    v = do_vault(my_string, my_secret, wrap_object=False)
    assert v == my_string_vault, "vaulted string is as expected"

    v = do_vault(my_string, my_secret, wrap_object=True)
    assert v.data == my_string, "vaulted string is as expected"

    secret1 = 'secret1'
    secret2 = 'secret2'


# Generated at 2022-06-22 11:59:16.607529
# Unit test for function do_unvault
def test_do_unvault():
    assert do_unvault(None, None) == ''
    assert do_unvault('', None) == ''
    assert do_unvault('This is a test string', 'test_secret') == 'This is a test string'

# Generated at 2022-06-22 11:59:27.292000
# Unit test for function do_unvault
def test_do_unvault():
    data = "Jinja2 and Ansible filters"
    secret = "changeme"
    vaultid = "filter_default"

    vault_obj = AnsibleVaultEncryptedUnicode(do_vault(data, secret, wrap_object=True))

    # Test using default vaultid
    assert do_unvault(vault_obj, secret) == data

    # Test using a function-specific vaultid
    assert do_unvault(vault_obj, secret, vaultid) == data

    # Test using string as a vault
    vault_str = do_vault(data, secret)
    assert do_unvault(vault_str, secret) == data

    # Test using wrong vaultid
    vaultid_err = "this_is_a_wrong_vaultid"

# Generated at 2022-06-22 11:59:34.043021
# Unit test for function do_vault
def test_do_vault():
    vault = do_vault("this is a secret", "password")
    assert vault.startswith("$ANSIBLE_VAULT;")
    assert not vault.endswith("\n")

    vault = do_vault("this is a secret\nwith more lines", "password")
    assert vault.startswith("$ANSIBLE_VAULT;")
    assert not vault.endswith("\n")



# Generated at 2022-06-22 11:59:36.986231
# Unit test for function do_vault
def test_do_vault():
    vault = do_vault("Data to be encrypted", "secretkey", "salt", "filter_default", True)
    assert isinstance(vault, AnsibleVaultEncryptedUnicode)



# Generated at 2022-06-22 11:59:44.462631
# Unit test for function do_unvault
def test_do_unvault():

    secret = 'secret'
    vaultid = 'filter_default'
    data = 'hello'
    vault = '$ANSIBLE_VAULT;1.2;AES256;foo\n12345678901234567890123456789012'

    test_vars = dict(
        secret = secret,
        vaultid = vaultid,
        data = data
    )

    filter_result = do_unvault(vault, secret, vaultid)
    assert filter_result == data

# Generated at 2022-06-22 11:59:48.437535
# Unit test for function do_vault
def test_do_vault():
    secret_key = 'secr3t'
    test_string = 'this is a secret string.'
    vault = do_vault(test_string, secret_key)

    assert(vault != '')



# Generated at 2022-06-22 11:59:54.854375
# Unit test for function do_vault
def test_do_vault():
    a = do_vault('md5hash', 'abcdefgh')
    assert a == '$ANSIBLE_VAULT;1.1;AES256\n3862306664386139666430303263303836363962316431336131633338653162323331303931326433\n66316463666365613665353037363834623664666233613434313f\n', 'do_vault failed'


# Generated at 2022-06-22 11:59:59.266936
# Unit test for function do_vault
def test_do_vault():
    password = "test"
    salt = "test"
    text = u"test"

    encrypted_text = do_vault(text, password, salt, "test")
    assert isinstance(encrypted_text, AnsibleVaultEncryptedUnicode)
    assert to_native(do_unvault(encrypted_text, password, "test")) == text



# Generated at 2022-06-22 12:00:10.438738
# Unit test for function do_vault
def test_do_vault():
    from ansible.module_utils.six import PY3

    # test vault bytes
    assert do_vault(b'foo', secret=b'bar') == b'$ANSIBLE_VAULT;1.1;AES256\n313364653461323134613138363866313062323036343766303165336334623939383565343065\n363539653039616366313265396335623162666335316662343137613339310a34333331323538\n303334663239316166326265326437366630326534303737333532336536373964373335386534\n623339626264326466616634636635386235363330613035383934310a'

   

# Generated at 2022-06-22 12:00:27.949952
# Unit test for function do_vault
def test_do_vault():
    secret = 'abc123'
    plaintext = 'foo'

# Generated at 2022-06-22 12:00:34.345317
# Unit test for function do_unvault
def test_do_unvault():
    # Arrange
    secret = 'password'
    vault = ''
    expected = 'string to unvault'
    vs = VaultSecret(to_bytes(secret))
    vl = VaultLib()
    data = 'string to unvault'
    vault = vl.encrypt(to_bytes(data), vs, 'key', None)

    # Act
    retval = do_unvault(vault, secret)

    # Assert
    assert retval == expected
