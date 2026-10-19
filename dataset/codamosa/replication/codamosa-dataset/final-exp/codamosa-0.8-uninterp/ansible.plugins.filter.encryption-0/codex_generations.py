

# Generated at 2022-06-22 11:50:46.568864
# Unit test for function do_vault
def test_do_vault():
    secret = 'minions'
    data = 'are great'
    vault = do_vault(data, secret)
    assert vault == "$ANSIBLE_VAULT;1.1;AES256\n363732303934313037383332616535313338653137346231333665646634373331326538393462373\n6331396561333035656331356639323734363135303839343936663861633663302363613731303565\n3833323763663430376131613666613632316330326134313763306130\n"


# Generated at 2022-06-22 11:50:54.547468
# Unit test for function do_vault
def test_do_vault():
    secret = 'ilikeyummykittens'
    data = 'supersecretdata'
    salt = 'firstsalt'
    vaultid = 'filter_default'
    wrap_object = False
    # Test do_vault function
    vault = do_vault(data, secret, salt=salt, vaultid=vaultid, wrap_object=wrap_object)
    # Test that VaultString is in the output
    assert(vault.startswith("$ANSIBLE_VAULT;"))
    # Test that unvault function is reversible
    assert(data == do_unvault(vault, secret))


# Generated at 2022-06-22 11:51:01.823024
# Unit test for function do_vault
def test_do_vault():
    filter_module = FilterModule()
    vaulted_data = filter_module.filters()['vault'](b'abc', b'abc')
    assert isinstance(vaulted_data, str)
    assert vaulted_data.startswith('$ANSIBLE_VAULT') is True
    assert filter_module.filters()['vault']('abc', 'abc', wrap_object=True).__class__.__name__ == 'AnsibleVaultEncryptedUnicode'



# Generated at 2022-06-22 11:51:10.576817
# Unit test for function do_unvault
def test_do_unvault():
    # Test for same value for string
    value = "Ansible in a Nutshell"
    secret = "ansible"
    vaultid = "filter_default"
    encrypted_value = do_vault(value, secret, vaultid, wrap_object=False)
    decrypted_value = do_unvault(encrypted_value, secret, vaultid)
    assert value == decrypted_value
    # Test for unicode string
    value = u"Ansible in a Nutshell"
    secret = "ansible"
    vaultid = "filter_default"
    encrypted_value = do_vault(value, secret, vaultid, wrap_object=False)
    decrypted_value = do_unvault(encrypted_value, secret, vaultid)
    assert value == decrypted_value
    # Test for same value for

# Generated at 2022-06-22 11:51:19.242967
# Unit test for function do_unvault
def test_do_unvault():
    assert do_unvault("$ANSIBLE_VAULT;1.1;AES256;myhost\n306137633161333434643031386664333561396465396634353863643631383964653562333765\n643965386430636637303433393839663963636663316236633335613234333434376432663933\n663731333666330a31303635336135353733653432373139323965383736633664323638306562\n30", "abcde") == "abcde"


# Generated at 2022-06-22 11:51:31.726840
# Unit test for function do_unvault
def test_do_unvault():
    # Sample data
    secret = "the password"
    vault = "$ANSIBLE_VAULT;9.9;AES256;ansible\n633434306565386365353664616132333961333434313733343938303364613465393166663137\n613162663261383635333761353635633530633462626235643161656564316237396234396563\n35653362356331323132353963646461626431303866318a313930653739343637373630316535\n343337343936313164626338"
    true_data = "this is some data"

    # Test data
    assert secret == "the password"

# Generated at 2022-06-22 11:51:36.215776
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('test_data', 'test_password') == '$ANSIBLE_VAULT;1.1;AES256\n353762663334633936653639626561363330363861313766393566623432643966316336386636\n65653530313266656530376536666537613900\n'


# Generated at 2022-06-22 11:51:44.848802
# Unit test for function do_unvault
def test_do_unvault():
    print("Testing do_unvault...")
    import os
    TPATH = os.path.dirname(os.path.realpath(__file__))
    secret = open(TPATH+'/samples/secret', 'r').read()
    vault = open(TPATH+'/samples/vault', 'r').read()
    data = do_unvault(vault, secret)
    print(data)
    print("Testing passed")
    return


# Generated at 2022-06-22 11:51:55.037954
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('my-secret', 'my-secret') == '$ANSIBLE_VAULT;1.1;AES256\n35336362373633323337323532633338383238626661623338636131373366373332353261353633\n31653164383766316164616536666232393937333637356433653233653038653865306130393933\n66383636666332643562633063373033376434623934393536366264356363356132346339326263\n65663635636663643531313162393164643830633964336338616137653464353235666666353836\n3533643663383036346435373739'

# Generated at 2022-06-22 11:52:02.734038
# Unit test for function do_unvault
def test_do_unvault():
    try:
        assert(do_unvault('$ANSIBLE_VAULT;1.1;AES256;user001\n34623066613439396564376162623331353439656336396633366236656332666238373533653432\n62333862326262313633353934623236363436353366353964663865633731646561386530653432\n653466383632383365318300000', 'password') == '12345')
    except AssertionError:
        print('test_do_unvault failed, can not decrypt vault')


# Generated at 2022-06-22 11:52:15.819135
# Unit test for function do_vault

# Generated at 2022-06-22 11:52:26.147738
# Unit test for function do_vault
def test_do_vault():

    secret = "test_secret"
    data_1 = "Hello world"

# Generated at 2022-06-22 11:52:34.956344
# Unit test for function do_vault
def test_do_vault():
    # TODO: Figure out how to convert to pytest
    from ansible.parsing.vault import VaultSecret
    # Make sure we can encrypt and decrypt the string
    secret = 'password'
    vs = VaultSecret(secret)
    vl = VaultLib()
    data = "Hello"
    vault = do_vault(data, secret)
    assert do_unvault(vault, secret) == data

    # Now try to encrypt an Undefined variable
    data = Undefined()
    vault = do_vault(data, secret)
    assert vault == "VaultEncryptedUnicode"

    # Now try to encrypt an invalid type
    data = ['1', '2', '3']
    vault = do_vault(data, secret)
    assert vault == "VaultEncryptedUnicode"

    # Now

# Generated at 2022-06-22 11:52:47.570995
# Unit test for function do_unvault

# Generated at 2022-06-22 11:52:58.928473
# Unit test for function do_vault

# Generated at 2022-06-22 11:53:09.677770
# Unit test for function do_vault
def test_do_vault():
    do_vault_filter = FilterModule()
    secret = 'test'
    val = 'ansible'
    wrong_secret = 'wrong'

    data = AnsibleVaultEncryptedUnicode.load(do_vault(val, secret, salt='test'))
    assert data == val

    with pytest.raises(AnsibleFilterTypeError):
        do_vault(val, '', salt='test')

    with pytest.raises(AnsibleFilterTypeError):
        do_vault(val, '', salt='test')

    # Test the salt parameter
    salt = 'test'
    data_salt = AnsibleVaultEncryptedUnicode.load(do_vault(val, secret, salt=salt))
    assert data_salt != data

    # Test the vaultid parameter
   

# Generated at 2022-06-22 11:53:13.263092
# Unit test for function do_vault
def test_do_vault():
    secret = 'thesecret'
    data = 'thedata'
    vault = do_vault(data, secret)

    # Test if the vault is encrypted
    assert vault != 'thedata'

    # Test if the vault can be decrypted
    assert data == do_unvault(vault, secret)

# Generated at 2022-06-22 11:53:24.949730
# Unit test for function do_vault
def test_do_vault():
    vault = do_vault('mypassword', 'mysecret')
    assert type(vault) == str

# Generated at 2022-06-22 11:53:34.355244
# Unit test for function do_vault
def test_do_vault():
    secret = 'secret'
    data = 'data'
    salt = 'salt'

    vault = do_vault(data, secret, salt)

# Generated at 2022-06-22 11:53:44.011787
# Unit test for function do_unvault
def test_do_unvault():
    assert do_unvault("$ANSIBLE_VAULT;1.1;AES256\n333461623761343265326531316662356534313466666463356530356566366435653338653066623\n30643930336336323961666539376335353466643133666131613531330a616432343539383364393\n63666356643566646363366362626338623664633064373037643336623238623766643162653764\n3162336333306535396331356161386430\n") == "secret"

# Generated at 2022-06-22 11:53:55.094593
# Unit test for function do_unvault
def test_do_unvault():
    """
    Test do_unvault function
    """
    # test case 1
    # Create string to be vaulted
    data = "topsecretinformation"
    # Set secret to be used for vaulting
    secret="newpassword"
    # Vault the string
    vault = do_vault(data, secret)
    # Unvault the vaulted string
    unvaulted = do_unvault(vault, secret)
    # Verify
    assert unvaulted == data


# Generated at 2022-06-22 11:54:05.399621
# Unit test for function do_unvault
def test_do_unvault():
    print('Testing do_unvault')


# Generated at 2022-06-22 11:54:15.148142
# Unit test for function do_unvault
def test_do_unvault():
    from ansible.parsing.vault import VaultLib, VaultSecret
    from ansible.utils.vars import combine_vars
    from ansible.parsing.vault import is_encrypted
    from ansible.errors import AnsibleError

    vault_id = 'someid'
    passwd = 'mypass'
    data = 'mydata'

    vs = VaultSecret(passwd)
    vl = VaultLib([(vault_id, vs)])

    try:
        vault = vl.encrypt(data, vs, vault_id)
    except AnsibleError as e:
        raise AnsibleFilterError("Unable to encrypt: %s" % to_native(e), orig_exc=e)

    assert is_encrypted(vault)


# Generated at 2022-06-22 11:54:23.335168
# Unit test for function do_unvault
def test_do_unvault():
    import pytest
    from ansible.parsing.vault import VaultSecret

    secret = VaultSecret("my_secret")
    vault = VaultLib()
    encrypted_data = vault.encrypt("foo", secret)

    # test unvaulting with a single secret
    unvaulted_data = do_unvault(encrypted_data, secret)
    assert unvaulted_data == "foo"

    # test unvaulting with multiple secrets
    secret1 = VaultSecret("my_secret")
    secret2 = VaultSecret("my_secret2")
    secret3 = VaultSecret("my_secret3")
    vault = VaultLib()
    encrypted_data = vault.encrypt("foo", secret1)
    unvaulted_data = do_unvault(encrypted_data, (secret2, secret3))

# Generated at 2022-06-22 11:54:35.393528
# Unit test for function do_vault

# Generated at 2022-06-22 11:54:44.039123
# Unit test for function do_vault

# Generated at 2022-06-22 11:54:55.860487
# Unit test for function do_vault
def test_do_vault():

    assert do_vault(undefined, 'secret') is undefined

# Generated at 2022-06-22 11:55:05.119909
# Unit test for function do_vault
def test_do_vault():
    do_vault('my_secret_data', 'secret', 'salt', 'default', False)
    # TODO(roger.souza@redhat.com): How to test failure cases?
    # do_vault('my_secret_data', 'secret', 'salt', False)
    # do_vault('my_secret_data', 123, 'salt', False)
    # do_vault(123, 'secret', 'salt', False)
    # do_vault(Undefined())
    # do_vault('secret', Undefined())
    # do_vault('secret', 'salt', Undefined())


# Generated at 2022-06-22 11:55:09.208795
# Unit test for function do_vault
def test_do_vault():
    from ansible.parsing.vault import is_encrypted
    vault = do_vault(u'foobar', u'changeme', salt=None)
    assert is_encrypted(to_bytes(vault))


# Generated at 2022-06-22 11:55:19.611753
# Unit test for function do_unvault
def test_do_unvault():
    secret = 'thisisasecret'

# Generated at 2022-06-22 11:55:28.310414
# Unit test for function do_vault
def test_do_vault():
    data = "secret_data"
    secret = "secret_password"
    vault = do_vault(data, secret)
    assert vault == "AQAAABAAAAAg7wPfNq3/4d/ea4dl1X9ZF8VoL1VdFy6mvU6o="



# Generated at 2022-06-22 11:55:37.390166
# Unit test for function do_unvault
def test_do_unvault():
    actual = do_unvault("$ANSIBLE_VAULT;1.2;AES256;ansible_test\n39396536343836653335363730376236633634366261326266613033366232353665393631383934\n62343264393161333138663538306637353466353664326566666139303935633665336365343035\n3266356633","ansible_test")
    expect = "testing\n"
    assert actual == expect, "Should be equal"

# Generated at 2022-06-22 11:55:45.313189
# Unit test for function do_unvault
def test_do_unvault():
    if not __package__:
        import sys
        import os
        print("\n*******Test do_unvault*******")
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from filters import do_unvault

    secret = 'foo'
    vaultid = 'test_default'

    # Encrypt the 'bar' string with vaultid
    data = do_vault("bar", secret, vaultid=vaultid)

    # Decrypt the encrypted data to get the original string
    msg = do_unvault(data, secret, vaultid=vaultid)

    assert isinstance(msg, str)
    assert msg == 'bar'

    # Encrypt the 'bar' string with vaultid
    data = do_vault

# Generated at 2022-06-22 11:55:56.979492
# Unit test for function do_unvault
def test_do_unvault():
    import jinja2

    env = jinja2.Environment()
    env.filters['unvault'] = do_unvault

    myvar = 'mysecret'
    template = \
"""
This is a test: {{ myvar | unvault('toplevelsecret') }}
"""

    templateobj = env.from_string(template)

# Generated at 2022-06-22 11:56:08.058804
# Unit test for function do_vault

# Generated at 2022-06-22 11:56:14.220784
# Unit test for function do_vault
def test_do_vault():
    data = 'test_data'
    secret = 'filter_default'

    test_vault = do_vault(data, secret)
    assert test_vault == b"$ANSIBLE_VAULT;1.0;AES256\n35613631343231633263353035666634303232333962333762656633326337663963626638356165\n616635303932303837303439356131303738653537376364356534663034\n"
    assert isinstance(test_vault, binary_type)



# Generated at 2022-06-22 11:56:25.952692
# Unit test for function do_vault
def test_do_vault():
    secret = "password"
    data = "This is a test of the vault filter."
    vaultid = 'test_vault'
    vault = do_vault(data, secret, vaultid=vaultid)


# Generated at 2022-06-22 11:56:33.548953
# Unit test for function do_vault
def test_do_vault():
    # data = '(S(yb4zea4mj4v2qot4q3qun3pf))'
    data = 'my_secret_word'
    secret = 'password'
    salt = 'salt'
    vaultid = 'default'
    wrap_object = False
    a = do_vault(data, secret, salt, vaultid, wrap_object)
    print(a)
    return a


if __name__ == "__main__":
    test_do_vault()

# Generated at 2022-06-22 11:56:43.462414
# Unit test for function do_vault
def test_do_vault():
    import yaml

    # Test empty string, shouldn't encrypt
    data = ''
    secret = 'VaultSecret'
    result = do_vault(data, secret)
    assert result == data

    # Test undefined, shouldn't encrypt
    data = Undefined()
    secret = 'VaultSecret'
    result = do_vault(data, secret)
    assert result == data

    # Test invalid secret, should throw exception
    data = 'TestData'
    secret = False
    exception_raised = False
    try:
        result = do_vault(data, secret)
    except Exception:
        exception_raised = True
    assert exception_raised

    # Test invalid data, should throw exception
    data = True
    secret = 'VaultSecret'
    exception_raised = False

# Generated at 2022-06-22 11:56:50.738890
# Unit test for function do_unvault
def test_do_unvault():
    from ansible.parsing.yaml.objects import AnsibleUnicode

# Generated at 2022-06-22 11:57:00.844351
# Unit test for function do_vault

# Generated at 2022-06-22 11:57:09.685096
# Unit test for function do_unvault
def test_do_unvault():
    # Test do_unvault using the same tests as in
    # bin/ansible-vault.py
    # Copyright (c) 2013-2020 Michael DeHaan <michael.dehaan@gmail.com>,
    # Copyright (c) 2012-2017 Ansible Project
    # https://github.com/ansible/ansible/blob/devel/lib/ansible/parsing/vault/__init__.py
    import unittest

    class Test_AnsibleVault(unittest.TestCase):

        def test_basic(self):
            """
            ansible-vault encrypt_string --name 'value' --vault-password-file vault_pass
            """
            secret = 'password'

# Generated at 2022-06-22 11:57:17.400463
# Unit test for function do_unvault
def test_do_unvault():
    try:
        # case 1: vault parameter is None
        do_unvault(None, 'secret')
    except AnsibleFilterTypeError as e:
        assert "Vault should be in the form of a string" in str(e)

    try:
        # case 2: vault parameter is not a string
        do_unvault(123, 'secret')
    except AnsibleFilterTypeError as e:
        assert "Vault should be in the form of a string" in str(e)

    try:
        # case 3: vault parameter is a string but not encrypted
        do_unvault('test', 'secret')
    except AnsibleFilterTypeError as e:
        assert "Vault should be in the form of a string" in str(e)


# Generated at 2022-06-22 11:57:27.841868
# Unit test for function do_unvault
def test_do_unvault():
    vid = 'filter_default'

# Generated at 2022-06-22 11:57:39.596434
# Unit test for function do_vault

# Generated at 2022-06-22 11:57:42.983182
# Unit test for function do_unvault
def test_do_unvault():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    secret = "$ANSIBLE_VAULT;9.9;TESTING"
    decoded = "Hello Ansible"

# Generated at 2022-06-22 11:57:44.659040
# Unit test for function do_vault
def test_do_vault():

    # Test encryption
    sec = 'mysecret'
    data = 'mydata'

    encrypted = do_vault(data, sec)
    decrypted_data = do_unvault(encrypted, sec)

    assert decrypted_data == data, "Decrypted data didn't match original data"


# Generated at 2022-06-22 11:57:52.484428
# Unit test for function do_unvault
def test_do_unvault():
    context = {}
    secret_test = "vault_secret_test"

# Generated at 2022-06-22 11:58:03.422007
# Unit test for function do_vault
def test_do_vault():
    import os
    secret = os.urandom(32)
    data = os.urandom(64)

    # Test with strings
    secret1 = secret.decode('utf-8')
    data1 = data.decode('utf-8')
    expected1 = do_vault(data1, secret1)
    actual1 = do_vault(data1, secret1)
    assert expected1 == actual1

    # Test with bytes
    secret2 = secret
    data2 = data
    expected2 = do_vault(data2, secret2)
    actual2 = do_vault(data2, secret2)
    assert expected2 == actual2

    # Test with undefined
    expected3 = do_vault('', secret1)
    actual3 = do_vault(Undefined(), secret1)

# Generated at 2022-06-22 11:58:05.292681
# Unit test for function do_vault
def test_do_vault():
    import doctest
    doctest.testmod(verbose=False)



# Generated at 2022-06-22 11:58:16.017616
# Unit test for function do_unvault
def test_do_unvault():
    filtered_data = do_unvault(
        vault_data,
        secret_data,
    )
    assert(filtered_data == mock_data)

# Generated at 2022-06-22 11:58:22.301540
# Unit test for function do_unvault
def test_do_unvault():
    # Test string
    data = u"the quick brown fox jumped over the lazy dog"
    # Test password
    secret = u"password"
    # Test vault object

# Generated at 2022-06-22 11:58:32.912442
# Unit test for function do_unvault

# Generated at 2022-06-22 11:58:35.951318
# Unit test for function do_unvault
def test_do_unvault():
    data = 'this is a test'
    secret = 'mysecret'
    print(do_unvault(do_vault(data, secret), secret))

# Generated at 2022-06-22 11:58:47.926911
# Unit test for function do_unvault
def test_do_unvault():
    assert do_unvault("", None) == ""

# Generated at 2022-06-22 11:58:58.045122
# Unit test for function do_vault
def test_do_vault():
    secret = 'some_secret'
    secret_bytes = b'secret_bytes'
    secret_unicode = u'secret_unicode'

    assert isinstance(do_vault('foo', secret, wrap_object=False), str)
    assert isinstance(do_vault('foo', secret_bytes, wrap_object=False), str)
    assert isinstance(do_vault('foo', secret_unicode, wrap_object=False), str)
    assert isinstance(do_vault('foo', secret, wrap_object=True), AnsibleVaultEncryptedUnicode)
    assert isinstance(do_vault('foo', secret_bytes, wrap_object=True), AnsibleVaultEncryptedUnicode)

# Generated at 2022-06-22 11:59:08.343594
# Unit test for function do_unvault
def test_do_unvault():
    secret = "mysecret"
    vaultid = "ansible_vault_filter"

# Generated at 2022-06-22 11:59:15.303492
# Unit test for function do_vault
def test_do_vault():
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    data = u'hello world'
    secret = b'foo'

# Generated at 2022-06-22 11:59:26.337321
# Unit test for function do_unvault
def test_do_unvault():
    secret = 'blah'
    vaultid = 'filter_default'

# Generated at 2022-06-22 11:59:36.242858
# Unit test for function do_unvault
def test_do_unvault():
    tdata = FilterModule()

# Generated at 2022-06-22 11:59:55.301899
# Unit test for function do_unvault
def test_do_unvault():
    secret = "secret"
    vault = "(vault(%s))" % do_vault("secret", "secret")
    assert do_unvault(vault, secret) == secret


# Generated at 2022-06-22 12:00:06.788735
# Unit test for function do_vault

# Generated at 2022-06-22 12:00:18.412581
# Unit test for function do_vault
def test_do_vault():
    # example taken from the documentation.
    # DO NOT USE THIS FILE IN PRODUCTION!
    secret = '$ANSIBLE_VAULT;1.1;AES256'
    salt = '2855533069841050331235514582890199694216700665801'

# Generated at 2022-06-22 12:00:28.760787
# Unit test for function do_vault

# Generated at 2022-06-22 12:00:40.399168
# Unit test for function do_unvault