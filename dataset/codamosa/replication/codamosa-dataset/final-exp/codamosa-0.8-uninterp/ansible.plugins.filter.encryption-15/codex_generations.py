

# Generated at 2022-06-22 11:50:51.197159
# Unit test for function do_unvault

# Generated at 2022-06-22 11:51:03.416161
# Unit test for function do_unvault
def test_do_unvault():
    data = '0123456789'

# Generated at 2022-06-22 11:51:15.510966
# Unit test for function do_unvault

# Generated at 2022-06-22 11:51:27.948891
# Unit test for function do_unvault

# Generated at 2022-06-22 11:51:37.785936
# Unit test for function do_vault

# Generated at 2022-06-22 11:51:51.015922
# Unit test for function do_vault
def test_do_vault():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    secret = 'thisisasecret'

    # Wrap_object is False
    data = 'This is the plain text string'
    res = do_vault(data, secret)
    assert res != data
    assert not isinstance(res, AnsibleVaultEncryptedUnicode)

    # Wrap_object is True
    res = do_vault(data, secret, wrap_object=True)
    assert res != data
    assert isinstance(res, AnsibleVaultEncryptedUnicode)
    assert str(res) == res.data

    data = 'this is another plain text string'
    res = do_vault(data, secret, wrap_object=True)
    assert res != data

# Generated at 2022-06-22 11:52:02.967852
# Unit test for function do_unvault
def test_do_unvault():
    VaultLib.global_vault_id = None
    # These tests require plaintext variables to work:
    # https://docs.ansible.com/ansible/devel/reference_appendices/faq.html#how-do-i-generate-crypted-passwords-for-the-user-module

# Generated at 2022-06-22 11:52:12.468646
# Unit test for function do_vault
def test_do_vault():
    # do_vault will generate a vault from the given data and return it
    # The vault generated is tested for its length to ensure it is
    # encrypted by the Ansible Vault.
    assert len(do_vault("ansible", "secret")) > 0
    assert len(do_vault("ansible", "secret".encode("utf-8"))) > 0
    assert len(do_vault("ansible".encode("utf-8"), "secret")) > 0
    assert len(do_vault("ansible".encode("utf-8"), "secret".encode("utf-8"))) > 0

# Generated at 2022-06-22 11:52:24.335754
# Unit test for function do_vault
def test_do_vault():
    # This unit test is created to check what happens when the data is empty.
    # We should just return empty data.
    # Fixing github issue #75069
    # https://github.com/ansible/ansible/issues/75069
    #
    # It should be noted that the vault filter that is called by the jinja2 template
    # system is different from the ansible vault cli. The vault cli can be called with
    # an empty file, but the vault filter cannot.
    # This is why we need to handle the empty data situation.
    #
    # Checks for the following things:
    #   - empty data, empty secret
    #   - empty data, secret
    #   - data, empty secret
    #   - data, secret

    data = ''
    secret = ''
    vault = ''
    expected_vault

# Generated at 2022-06-22 11:52:36.006390
# Unit test for function do_unvault

# Generated at 2022-06-22 11:52:51.281231
# Unit test for function do_unvault
def test_do_unvault():
    test_secret = "mysecret"

# Generated at 2022-06-22 11:53:01.186772
# Unit test for function do_vault
def test_do_vault():
    '''unit test for function do_vault'''
    assert do_vault('XXX', 'password') == '$ANSIBLE_VAULT;1.1;AES256\n3236383364363537643261613739303730363533363539396664623139663533\n393530386135336530313432386132366234383630343539393334356637316434\n39333232303538363433656231363139316364303962323263323864663536619\n0d0a'

# Generated at 2022-06-22 11:53:10.955684
# Unit test for function do_unvault

# Generated at 2022-06-22 11:53:15.081933
# Unit test for function do_unvault
def test_do_unvault():
    assert do_unvault('$ANSIBLE_VAULT;1.1;AES256\n373161653738316132323161313437343738666630353233623461666264323337393933313933660a',
                    'some_random_secret') == 'some string to be decrypted'



# Generated at 2022-06-22 11:53:26.301358
# Unit test for function do_unvault

# Generated at 2022-06-22 11:53:30.701090
# Unit test for function do_vault
def test_do_vault():
    secret = 'totally_secret'
    data = 'brand new data'
    salt = 'some salt'
    vaultid = 'test_vault'
    wrap_object = False
    assert '$ANSIBLE_VAULT' in do_vault(data, secret, salt, vaultid, wrap_object)


# Generated at 2022-06-22 11:53:40.973697
# Unit test for function do_unvault
def test_do_unvault():
    secret = "$ANSIBLE_VAULT;1.2;AES256;my_secret\n33313531353133383731323932323032373039663534363339653637373031383365303735633236\n65356633616137663331363566303162366339373936623735316631373837363562373439333566\n62376561663666356565666563626261313736333865376666353331303339333632623365396435\n3033383032323939\n"
    decrypted = do_unvault(secret, "my_secret")


# Generated at 2022-06-22 11:53:47.529516
# Unit test for function do_vault
def test_do_vault():

    # Test for do_vault for data and secret
    test_data = "hello"
    test_secret = "test"
    vault_result = do_vault(test_data, test_secret)

# Generated at 2022-06-22 11:53:59.760228
# Unit test for function do_unvault

# Generated at 2022-06-22 11:54:07.686953
# Unit test for function do_unvault
def test_do_unvault():
    assert do_unvault('$ANSIBLE_VAULT;1.1;AES256;ansible\r\n323931633763643835346534623966376265323932373066343665663965373536326663356434\r\n353964386635636462363034613365366666393163336335346565643332303163376432653732\r\n636664373561366133313663353737646662356333636636643963386339333638306531363031\r\n32386633\r\n', 'secret') == "some plain text"

# Generated at 2022-06-22 11:54:19.510126
# Unit test for function do_vault
def test_do_vault():
    result = do_vault('string', 'secret', salt='1234567890', vaultid='filter_default', wrap_object=False)

# Generated at 2022-06-22 11:54:30.584570
# Unit test for function do_unvault

# Generated at 2022-06-22 11:54:41.339317
# Unit test for function do_vault

# Generated at 2022-06-22 11:54:53.356375
# Unit test for function do_unvault

# Generated at 2022-06-22 11:54:58.343548
# Unit test for function do_vault
def test_do_vault():

    """Function to test do_vault method"""

    s = 'abc' # secret
    d = 'def' # data
    v = do_vault(d, s) # vault

    assert(is_encrypted(v))
    assert(do_unvault(v, s) == d)


# Generated at 2022-06-22 11:55:09.569821
# Unit test for function do_unvault
def test_do_unvault():
    """ Ansible vault jinja2 filter test cases """
    import tempfile

    # Create temporary file, write test cases to the file
    test_data = ['# vault_password_file = ~/.vault_pass.txt',
                 'vault_password_file = /dev/null',
                 'vault_password_file = /non/existent/file',
                 'vault_password = secret']
    tmp_file = tempfile.NamedTemporaryFile()
    for line in test_data:
        tmp_file.write((line + '\n').encode('utf-8'))
    tmp_file.flush()

    # Read the test cases from the file
    f = open(tmp_file.name, 'r')
    test_cases = f.read()

    import os

# Generated at 2022-06-22 11:55:20.019755
# Unit test for function do_vault
def test_do_vault():
    import os
    import jinja2
    import tempfile
    import ansible.constants as C
    from ansible.parsing.vault import VaultLib

    assert "ANSIBLE_VAULT" in os.environ

    if "ANSIBLE_VAULT_PASSWORD_FILE" in os.environ:
        with open(os.environ["ANSIBLE_VAULT_PASSWORD_FILE"], "r") as f:
            content = f.read()
        secret = content.strip()
    else:
        secret = os.environ["ANSIBLE_VAULT"]

    # the test text below is from https://github.com/ansible/ansible/issues/57422
    #
    # the literal_block elements of the text in the issue had not been indented (with spaces)
    # which caused a failure when

# Generated at 2022-06-22 11:55:29.490975
# Unit test for function do_vault

# Generated at 2022-06-22 11:55:33.773371
# Unit test for function do_vault
def test_do_vault():
    secret = 'foobar'
    data = 'password'
    vault = do_vault(data, secret)
    assert isinstance(vault, string_types)
    assert vault.startswith('$ANSIBLE_VAULT')


# Generated at 2022-06-22 11:55:43.346509
# Unit test for function do_unvault
def test_do_unvault():
    secret = "thisisnotagoodsecret"
    vaultid = "filter_default"
    # The encrypted string was generated using:
    # $ ansible-vault encrypt_string --name 'myvariable' 'this_is_the_unencrypted_data' --vault-id 'any-name' 'thisisnotagoodsecret'
    # The encrypted string will change everytime you run the above command.

# Generated at 2022-06-22 11:55:57.136523
# Unit test for function do_vault
def test_do_vault():
    secret = 'mysecret'
    data = 'this is the data'

    vault = '$ANSIBLE_VAULT;1.1;AES256;default\n39653532353436313033353232376261313436333738303465383666373730663531413364343435632d636563703d0a3099333265393134393238393336303536303938663363656137383964353330636434336433393035383038653531336661303d0a'

    assert do_vault(data, secret, vaultid='default') == vault


# Generated at 2022-06-22 11:56:08.205432
# Unit test for function do_unvault
def test_do_unvault():
    import os
    from subprocess import Popen, PIPE, STDOUT
    import sys
    import yaml

    here = os.path.abspath(os.path.dirname(__file__))
    playbook = os.path.join(here, "../playbook.yml")
    filter_file = os.path.join(here, "../filter_plugins/vault.py")

    with open(playbook) as data:
        yml = yaml.load(data)
    vault_string = yml['vars']['vault_string']
    secret_string = yml['vars']['secret_string']

    vault_string_bytes = vault_string.encode('utf-8')
    secret_string_bytes = secret_string.encode('utf-8')

    proc = Popen

# Generated at 2022-06-22 11:56:13.575044
# Unit test for function do_vault
def test_do_vault():
    secret = 'mysecret'
    data = 'mydata'

    result = do_vault(data, secret)
    assert result == '!vault |' + "\n" + '          $ANSIBLE_VAULT;1.1;AES256' + "\n" + '          63353637356634646266356164313662316433383339346630326566633836353165653135633530' + "\n" + '          61666336386166623363'


# Generated at 2022-06-22 11:56:25.068254
# Unit test for function do_vault

# Generated at 2022-06-22 11:56:36.573223
# Unit test for function do_vault

# Generated at 2022-06-22 11:56:45.004709
# Unit test for function do_unvault
def test_do_unvault():
    """Test that do_unvault() works correctly."""
    vault = b'$ANSIBLE_VAULT;1.1;AES256\n35646635366138366535356234616264303839396663363235626533643331326265363735666330\n39333166323462633664653937326666386438313337383337626331386138616664633835613037\necb80b9d620202b3c2a1f4a030c65c1d0b4e4a4a9d92e0a78\n'
    secret = b'foosecret'
    result = do_unvault(vault, secret)
    assert result == b'this is a test'

# Generated at 2022-06-22 11:56:56.546958
# Unit test for function do_vault
def test_do_vault():
    vault_data = do_vault("testing", "fake_secret")

# Generated at 2022-06-22 11:57:07.317196
# Unit test for function do_unvault
def test_do_unvault():
    import ansible.parsing.vault
    import hashlib


# Generated at 2022-06-22 11:57:17.082457
# Unit test for function do_vault
def test_do_vault():
    secret = 'password'
    vault = do_vault('mystring', secret)
    assert vault == '$ANSIBLE_VAULT;1.1;AES256\n62316553623936373363643662316336643765363766656133313732616661376564363561366461\n6530333639343133656234383031316233313231383162613235360a363533343464363866633666\n64303962323465393864303466353365643165323532346335313736316532623235643038656537\n6132333132623035346436313939\n'



# Generated at 2022-06-22 11:57:27.619608
# Unit test for function do_unvault

# Generated at 2022-06-22 11:57:40.822050
# Unit test for function do_unvault
def test_do_unvault():
    secret = '$ANSIBLE_VAULT;1.1;AES256'

# Generated at 2022-06-22 11:57:50.031407
# Unit test for function do_vault
def test_do_vault():
    from ansible.module_utils.six.moves import cStringIO as StringIO

    class TestVaultLib(VaultLib):
        def __init__(self):
            super(TestVaultLib, self).__init__([])

    # Can not generate the vault lib on the fly, so mock it
    def encrypt_method(data, key, id, salt=None):
        return '$ANSIBLE_VAULT;1.1;AES256\ntestRTA\n'

    TestVaultLib.encrypt = encrypt_method
    vault = do_vault('test', 'test', vaultid='test_vault', salt=None)
    assert vault == '$ANSIBLE_VAULT;1.1;AES256\ntestRTA\n'


# Generated at 2022-06-22 11:57:57.703164
# Unit test for function do_unvault
def test_do_unvault():
    secret = 'some_secret_string'
    vault = '$ANSIBLE_VAULT;1.2;AES256;test\n345353453534234534234523452345345\n34235342345342345345345345345345345\n3453453453534534534534345345345345345\n345345345345345345345345345345345345'
    data = do_unvault(vault, secret)
    assert data == ''

# Generated at 2022-06-22 11:58:05.536222
# Unit test for function do_unvault
def test_do_unvault():
    import yaml
    from textwrap import dedent
    from base64 import b64encode as b64
    assert do_unvault('!!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          393034356537333164363339636562383231616636643034383337343637343539323935373739\n          6461353038663936373566306437363464616665\n          373734316638653965636565303533316564346639303732333332643635663938626133316538\n          3535373332366532653166',
                      'ansible') == 'This is a secret\n'

# Generated at 2022-06-22 11:58:08.609957
# Unit test for function do_vault
def test_do_vault():
    secret = "mypassword"
    data = "secretdata"
    encrypted = do_vault(data, secret)
    assert is_encrypted(encrypted)


# Generated at 2022-06-22 11:58:18.583705
# Unit test for function do_vault
def test_do_vault():
    from ansible_collections.ansible.community.tests.unit.plugins.filter.test_vault import FilterModule
    filters = FilterModule().filters()
    test_value = 'foo'
    returned_value = filters['vault'](test_value, 'bar')
    assert(returned_value == '$ANSIBLE_VAULT;1.2;AES256;filter_default\n6466393664306633643332616431656639383466303435656133313231666436303665323761336\n66337633623233303466353734623134353736\n')


# Generated at 2022-06-22 11:58:30.265992
# Unit test for function do_vault

# Generated at 2022-06-22 11:58:35.082080
# Unit test for function do_unvault
def test_do_unvault():

    assert do_unvault('$ANSIBLE_VAULT;1.2;AES256;tiger123\n376436633066656538643337666162353432376337613661333139313162623365633431643766\n30363939383538336165343338313464613238353331303262643236303433656630', 'password') == 'foo'

# Generated at 2022-06-22 11:58:46.455489
# Unit test for function do_vault
def test_do_vault():
    assert do_vault("", "secret") == ""
    assert do_vault("", "secret", salt='abcd') == "$ANSIBLE_VAULT;1.2;AES256;abcd;abcd\n3137333536393434623963636661613031656263353536326564636638316264353531343830\n353830643336396435333064363038643865306435616234653539656433303365373763363566\n646638323536663037333937623530633134336435663134353663313666306637323066653437\n6539623333396262303533373863316536363537\n"

# Generated at 2022-06-22 11:58:57.244335
# Unit test for function do_unvault

# Generated at 2022-06-22 11:59:09.131322
# Unit test for function do_vault
def test_do_vault():
    result = do_vault("my_secret", "my_password", vaultid="test_vault", wrap_object=False)

# Generated at 2022-06-22 11:59:20.837038
# Unit test for function do_vault
def test_do_vault():
    #
    #  If a "invalid" secret is passed in, the vault lib should throw an exception.
    #
    secret = "invalid"
    try:
        do_vault('test_data', secret)
    except AnsibleFilterError as e:
        assert "Unable to encrypt: " in str(e), \
                "Expecting 'Unable to encrypt: ' in exception.  Got %s" % str(e)

    #
    #  If a valid secret and data is passed, then we should get back a
    #  vault string, and the string should be different than the original string.
    #
    secret = "validsecret"
    original_string = "test_data"
    vault = do_vault(original_string, secret)
    assert original_string != vault, "Expecting %s != %s"

# Generated at 2022-06-22 11:59:29.182372
# Unit test for function do_vault
def test_do_vault():
    data = "hello"
    secret = "secret"
    vault = do_vault(data, secret)
    assert vault == "$ANSIBLE_VAULT;1.1;AES256\n3637333932656566343764313338313730323165323165306466653865333430376630346431613363\n303366633262613231356230316139366431656137393434626336363033363137333334616563623833\n656564343665353866613038663832643563396237656636643939356466363464366265396433653064\n35646633326639\n"


# Generated at 2022-06-22 11:59:30.357996
# Unit test for function do_vault
def test_do_vault():
    data = do_vault('test', 's3cr3t')
    assert type(data) == str


# Generated at 2022-06-22 11:59:41.052203
# Unit test for function do_vault

# Generated at 2022-06-22 11:59:51.945072
# Unit test for function do_unvault
def test_do_unvault():
    # Test key definition
    key = "my_key"

    # Test simple text
    text = "Hello, World"

# Generated at 2022-06-22 11:59:54.338568
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('test', 'mysecret', salt='salt', vaultid='id', wrap_object=False) != 'test'


# Generated at 2022-06-22 11:59:55.708750
# Unit test for function do_vault
def test_do_vault():

    # TODO - Implement Unit tests here
    pass


# Generated at 2022-06-22 12:00:04.362532
# Unit test for function do_unvault
def test_do_unvault():

    vault_secret_file = "test_data/vaults/unvault_vault_secret.txt"
    with open(vault_secret_file, "r") as f:
        secret = f.readlines()[0]

    vault_file = "test_data/vaults/unvault_vault_file.txt"
    with open(vault_file, "r") as f:
        data = f.readlines()[0]

    output = do_unvault(data, secret)

    assert(output == 'this is a secret string')

# Generated at 2022-06-22 12:00:16.099490
# Unit test for function do_unvault
def test_do_unvault():
    secret = 'ansible'
    # Encrypted data using ansible-vault encrypt_string

# Generated at 2022-06-22 12:00:23.185548
# Unit test for function do_vault
def test_do_vault():
    test_data = "foobar"
    test_secret = "howtotrainyourdragon"

    encrypted_data = do_vault(test_data, test_secret, wrap_object=True)
    decrypted_data = do_unvault(encrypted_data, test_secret)

    assert decrypted_data == test_data


# Generated at 2022-06-22 12:00:32.146601
# Unit test for function do_vault
def test_do_vault():

    # Testing Invalid inputs
    try:
        __builtins__['__salt__'] = {}
        do_vault(1, 2, 3)
    except AnsibleFilterTypeError as e:
        assert "Secret passed is required to be a string" in str(e)

    try:
        do_vault('vaulted string', 2)
    except AnsibleFilterTypeError as e:
        assert "Secret passed is required to be a string" in str(e)

    try:
        do_vault(2, 'vaulted key')
    except AnsibleFilterTypeError as e:
        assert "Can only vault strings" in str(e)

    # Testing success case

# Generated at 2022-06-22 12:00:42.955254
# Unit test for function do_vault
def test_do_vault():

    text = "This is secret"
    vault = do_vault(text, "secret")
    assert vault == "$ANSIBLE_VAULT;1.1;AES256\n35316130366466396236646635623435373365363466316233326239323766313732323334373534\n323266653937663865383733633330346631313430663735\n"
    assert not is_encrypted(text)
    assert is_encrypted(vault)
    secret = do_unvault(vault, "secret")
    assert secret == "This is secret"

    # Test AnsibleVaultEncryptedUnicode Obj
    vault = do_vault(text, "secret", wrap_object=True)