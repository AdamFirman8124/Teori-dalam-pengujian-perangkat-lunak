

# Generated at 2022-06-22 11:50:46.127541
# Unit test for function do_unvault
def test_do_unvault():
    actual = do_unvault("$ANSIBLE_VAULT;1.1;AES256;my;33511665611736306536303361356533373763306138633163646637356530333635383637393935613536633035373766393134626535306166613862330a6465666163696c696f6e3d6263636b636f6465206664316136636537653162336166663264383962643436306438626362613231333234303730343830643232620a", "verysecret", "verysecret")

# Generated at 2022-06-22 11:50:55.298875
# Unit test for function do_unvault
def test_do_unvault():
    from ansible.parsing.vault import is_encrypted
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from cryptography.fernet import InvalidToken

    secret = "password"
    vaultid = "filter_default"
    vault = do_vault('my super secret data', secret, vaultid)
    assert isinstance(vault, str)
    assert is_encrypted(vault)
    assert isinstance(AnsibleVaultEncryptedUnicode(vault), AnsibleVaultEncryptedUnicode)

    # test un-vaulting with a valid secret
    unvault = do_unvault(vault, secret, vaultid)
    assert unvault == 'my super secret data'

    # test un-vaulting with a invalid secret

# Generated at 2022-06-22 11:51:06.708375
# Unit test for function do_unvault
def test_do_unvault():
    import base64

    # Test with AnsibleVaultEncryptedUnicode
    unvault = AnsibleVaultEncryptedUnicode(base64.b64decode("$ANSIBLE_VAULT;8.0;AES256;filter_default;e6912af4358a4c4d4b4afe4c4a4a46e8e78d9e2b2a48e2b2b8c90e080a3a3e3f\nW8SvHDXl1mHfC/mGuwQ8iA=="))
    secret = "the_secret"
    unvault.vault = VaultLib([("filter_default", VaultSecret("the_secret"))])

    assert(do_unvault(unvault, secret) == "test")

    # Test with not encrypted string


# Generated at 2022-06-22 11:51:18.276311
# Unit test for function do_unvault

# Generated at 2022-06-22 11:51:30.992506
# Unit test for function do_unvault

# Generated at 2022-06-22 11:51:40.918926
# Unit test for function do_unvault
def test_do_unvault():
    class args:
        vault = '$ANSIBLE_VAULT;1.2;AES256;youridhere\n703765066331323834363733333263626338626465656430363764633036623263656466363539\n323961636164366363313965386664363334643564613762626661613236396438346664303938\n353031663038363365346130303838623333306230336539663135323661633435656565623732\n376431633436306637353238626161306633303263\n'
        secret = 'yoursecret'
        vaultid = 'youridhere'

    answer = 'this is my super secret text'
    assert do_un

# Generated at 2022-06-22 11:51:53.188558
# Unit test for function do_vault
def test_do_vault():
    from collections import Mapping
    f = FilterModule()
    data = "secret-data"
    secret = "secret-key"
    vaultid = "example_password"
    f.filters()["vault"](data, secret, vaultid=vaultid)
    f.filters()["vault"](data, secret)
    assert f.filters()["vault"](data, secret, vaultid=vaultid) == f.filters()["vault"](data, secret)
    assert len(f.filters()["vault"](data, secret, vaultid=vaultid)) == len(f.filters()["unvault"](f.filters()["vault"](data, secret, vaultid=vaultid), secret, vaultid))

# Generated at 2022-06-22 11:52:02.319995
# Unit test for function do_unvault
def test_do_unvault():
    secret = 'secret'

# Generated at 2022-06-22 11:52:09.491865
# Unit test for function do_unvault
def test_do_unvault():
    try:
        val = do_unvault("data", "my_secret")
        assert val == "data"
    except AnsibleFilterTypeError:
        pass
    try:
        val = do_unvault("", 123)
        assert False
    except AnsibleFilterTypeError:
        assert True
    try:
        val = do_unvault("", [])
        assert False
    except AnsibleFilterTypeError:
        assert True


# Generated at 2022-06-22 11:52:13.484866
# Unit test for function do_unvault
def test_do_unvault():
    assert do_unvault("!vault |\n $ANSIBLE_VAULT;1.1;AES256\ntest\n", "test") == "test"
    assert do_unvault("!vault |\n $ANSIBLE_VAULT;1.1;AES256\ntest\n") == "test"
    assert do_unvault("test") == "test"


# Generated at 2022-06-22 11:52:19.721609
# Unit test for function do_vault
def test_do_vault():
    secret = 'mysecret'
    data = 'mydata'
    vault = do_vault(data, secret)
    assert type(vault) is str, "Vault should be a string"


# Generated at 2022-06-22 11:52:30.815505
# Unit test for function do_unvault
def test_do_unvault():
    vault = '!vault |\n          $ANSIBLE_VAULT;1.2;AES256;test1\n          39656233653937323064383538343338323965343861643665333737393536343530353865383939\n          66646166656662646634346338376536636231373332333037646630653530646339653239343335\n          3566613036663336326263626163313638303537336435633965333561\n          '

    result = do_unvault(vault, 'test_secret')

    assert result == "test_value"

# Generated at 2022-06-22 11:52:36.228947
# Unit test for function do_vault
def test_do_vault():
    assert (do_vault("topsecret", "ansible") == "!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          373635393736356265666535653037336163343465666634353939323230343039353033373266360a\n          3437616663643431666334633165646565393530313936393338653465623431633463656136333864\n          306537336130346564376132333161370a") is True


# Generated at 2022-06-22 11:52:42.395176
# Unit test for function do_vault
def test_do_vault():
    data = 'Hello World!'
    secret = 'hello'

    vault = do_vault(data, secret, salt='a salt')

    # Confirm returned value is a string
    assert isinstance(vault, str)

    # Confirm returned string is encrypted
    assert is_encrypted(vault)



# Generated at 2022-06-22 11:52:51.745460
# Unit test for function do_vault
def test_do_vault():
    v = do_vault(data="foobar", secret="ansible", salt="ansible", vaultid="ansible", wrap_object=True)
    assert v == "$ANSIBLE_VAULT;1.1;AES256\n32663135636630336261623463620a303462356164383939316266616562366337363934646163633362386\n2363036306162333962656432303239373937620a3963396231366336643537363064616130643537346463\n3238626230646532396432343864313535656537333036\n"


# Generated at 2022-06-22 11:53:01.201408
# Unit test for function do_vault
def test_do_vault():
    secret = 'secret'
    clear = 'clear text'
    cipher = '$ANSIBLE_VAULT;1.1;AES256\n6262393264626663656662373463336234313938636637333934373765313431626537306437393566\n3639333167613738363830363465353362616139393266343538633763303438313266616638633662\n343532373936347d0a\n'

    assert do_vault(clear, secret) == cipher



# Generated at 2022-06-22 11:53:10.955399
# Unit test for function do_unvault

# Generated at 2022-06-22 11:53:14.777321
# Unit test for function do_vault
def test_do_vault():
    fake_secret = "not a secret"
    fake_vault = "$ANSIBLE_VAULT;1.1;"
    result_vault = do_vault("hello world", fake_secret, "filter_default")
    assert(result_vault.startswith(fake_vault))


# Generated at 2022-06-22 11:53:26.827397
# Unit test for function do_vault
def test_do_vault():

    # Test with string
    assert do_vault('foo', 'secret') == '$ANSIBLE_VAULT;1.1;AES256\n363965313237616332643761623533653934643261376139636236656334316339343866306365\n343763306139636664373931383133316666323431373761363364353666643935666439613362\n336238623932363932633063323539623233373431326635616662663533666437\n'

    # Test with bytes

# Generated at 2022-06-22 11:53:38.510699
# Unit test for function do_vault
def test_do_vault():

    test_secret = VaultSecret('Q2Fyb2W8QFjRTiRzepH')
    vl = VaultLib()
    # do_vault with no extra arguments
    assert(vl.encrypt(b'foo', test_secret, salt=None) == do_vault('foo', 'Q2Fyb2W8QFjRTiRzepH'))

    # do_vault with salt
    salt = 'AUz7A8xCxu1kQDjpJiiu'
    assert(vl.encrypt(b'foo', test_secret, salt=salt) == do_vault('foo', 'Q2Fyb2W8QFjRTiRzepH', salt))

    # do_vault with vaultid
    vaultid = 'vaultid'
   

# Generated at 2022-06-22 11:53:47.455618
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('foo', 'secret', salt='salt') == '!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          633262633237353435656533666338306436626638333965303634343134643664616232366531\n          3563313163656465353438613566336439663864366665643831363166353931\n          346133333131373230353562393638646266616234623737376466326665353937616137\n          64316238633164646630622a\n'

# Generated at 2022-06-22 11:53:59.652048
# Unit test for function do_unvault
def test_do_unvault():
    import pytest
    from ansible_collections.test_collection.not_real.plugins.filters.vault import FilterModule

    filter_module = FilterModule()

# Generated at 2022-06-22 11:54:05.723849
# Unit test for function do_vault
def test_do_vault():

    data = 'this is a test'
    secret = 'secret'
    salt = '12345'
    vault_id = 'filter_default'
    wrap_object = False
    result = do_vault(data, secret, salt, vault_id, wrap_object)

    assert isinstance(result, (string_types, binary_type))



# Generated at 2022-06-22 11:54:16.242339
# Unit test for function do_vault
def test_do_vault():
    import jinja2
    from ansible.compat.tests.mock import patch
    from ansible.compat.tests.mock import MagicMock

    with patch("ansible.parsing.vault.VaultSecret") as mock_vault_secret:
        with patch("ansible.parsing.vault.VaultLib") as mock_vault_lib:
            mock_vs = MagicMock()
            mock_vs.__str__.return_value = 'mock_vault_secret'
            mock_vault_secret.return_value = mock_vs

            mock_vl = MagicMock()
            mock_vl.encrypt.return_value = b'mock_vault_data'
            mock_vault_lib.return_value = mock_vl

            t = jinja2.Template

# Generated at 2022-06-22 11:54:27.840229
# Unit test for function do_unvault
def test_do_unvault():
    import ansible.constants as C
    from ansible.parsing.vault import VaultEditor
    from ansible.parsing.dataloader import DataLoader
    dl = DataLoader()

    test_vault = """$ANSIBLE_VAULT;1.1;AES256
34633234366437333731326362356635343733393565643038396435616433643539646339623265
65363865356136623035656634393638630a36643762626462363437643665623139356330643831
643533666432613666316235326362626462643336392d2d0a"""

    result = do_unvault(test_vault, "abcdefghijklmnop")



# Generated at 2022-06-22 11:54:33.260726
# Unit test for function do_vault
def test_do_vault():
    secret = 'thisisnotverysecret'
    salt = 'aaaa'
    vid = 'test_case'
    wrap = True
    data = 'thisisthesecret'
    vault = do_vault(data, secret, salt, vid)
    output = do_unvault(vault, secret, vid)

    assert output == 'thisisthesecret'


# Generated at 2022-06-22 11:54:38.972674
# Unit test for function do_vault
def test_do_vault():
    try:
        do_vault('test', 'secret', 'salt', 'filter_default')
    except AnsibleFilterError as e:
        assert "Unable to encrypt: " in to_native(e)
    assert isinstance(do_vault('test', 'secret', 'salt', 'filter_default', wrap_object=True),
                      AnsibleVaultEncryptedUnicode)


# Generated at 2022-06-22 11:54:49.501813
# Unit test for function do_unvault
def test_do_unvault():
    """
    test the do_unvault function
    """

    # use the custom module_utils.common.do_unvault function
    options = dict(
        vault_password_file = None,
        vault_password = 'test',
        no_log = True,
        vars = [],
    )

    secret = VaultSecret('test')
    vault_id = 'filter_default'
    vault_lib = VaultLib([(vault_id, secret)])

    # Test valid encrypted string

# Generated at 2022-06-22 11:55:00.828222
# Unit test for function do_unvault
def test_do_unvault():
    # Set up test data
    str_sec = "supersecret"
    str_data = "unencrypted test data"

# Generated at 2022-06-22 11:55:08.612775
# Unit test for function do_vault
def test_do_vault():
    filter_object = FilterModule()
    secret = b'ansible'
    test_cases = [
        ('b3BlbnNhZ2FyZGV2', 'opensahardev'),
        ('c3VwZXJsaW5n', 'superling'),
        ('c3R1ZmZmb29iYXI=', 'stufffoobar'),
    ]
    for expected_output, input_data in test_cases:
        assert filter_object.filters()['vault'](input_data, secret) == expected_output


# Generated at 2022-06-22 11:55:22.203218
# Unit test for function do_vault
def test_do_vault():
    my_data = 'TEST'
    my_secret = 'TEST_SECRET'
    my_salt = 'TEST_SALT'
    return_val = b'$ANSIBLE_VAULT;1.1;AES256\n37383664353666643937666434333764333332336438373064323031633763303534313039636133373\n3934356536633662353739303532333237623239626330653866313032360a6431346130333961653236\nea340ba7bc25c4bb4f7fb4c4b2fe271d8cad9b9a0c27f3d3a8bce5b5c7f5d5b0\n'
    assert do_v

# Generated at 2022-06-22 11:55:34.460795
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('hello world', 'sample_secret') == '$ANSIBLE_VAULT;1.1;AES256\n326663323262616562343831373233633539636436623037313736613161396332376238663330\n346539623865363736373939656433366330396561653465343163373336316232396361623565\n343635633165323531376635303263303765383335613937646338623962363866383332623731\n61316339356633386262626236\n'

# Generated at 2022-06-22 11:55:40.291225
# Unit test for function do_vault
def test_do_vault():
    data = "test_string"
    secret = "mysecret"
    vaultid = "filter_default"
    salt = None
    wrap_object = False

    vault = do_vault(data, secret, salt, vaultid, wrap_object)
    assert vault.startswith("$ANSIBLE_VAULT;")
    assert vault.find("\n") > 0


# Generated at 2022-06-22 11:55:43.734528
# Unit test for function do_vault
def test_do_vault():
    #ret = do_vault('abcdefhijklmnopqrstuvwxyz', 'changeMe', 'text', False)
    #print(ret)
    pass


# Generated at 2022-06-22 11:55:48.496528
# Unit test for function do_vault
def test_do_vault():
    data = 'helloworld'
    secret_password = 'secret'
    vault_data = do_vault(data, secret_password)
    vault_data_decrypted = do_unvault(vault_data, secret_password)
    assert vault_data_decrypted == data


# Generated at 2022-06-22 11:56:00.229905
# Unit test for function do_vault

# Generated at 2022-06-22 11:56:10.000786
# Unit test for function do_vault
def test_do_vault():
    from ansible.compat.tests.mock import patch
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    """
    mock the VaultSecret object and call do_vault
    """

    mock_secret = b'123'
    mock_data = b'secretstuff'
    mock_vault = b'$ANSIBLE_VAULT;1.1;AES256;mock\r\mockvalue'

    with patch('ansible.parsing.vault.VaultLib') as mock_vault_lib:
        with patch('ansible.parsing.vault.VaultSecret') as mock_vault_secret:
            instance = mock_vault_secret.return_value
            instance.load.return_value = mock_secret

            instance = mock_

# Generated at 2022-06-22 11:56:21.858574
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('mydata', 'mysecret', vaultid='vault_1') == '$ANSIBLE_VAULT;1.1;AES256\n30353833313561316132643265336665653966353139373938326131623333643730336231640a303132323035303130323431616338613938343061623363316331373830386438653565640a34356537663836333936396165356437363637303439333531326764343361376563353032633739353436336630643666'

# Generated at 2022-06-22 11:56:28.508247
# Unit test for function do_vault
def test_do_vault():
    secret = "secret-value"
    salt = "salt-value"
    data = "plain-text"
    assert do_vault(data, secret, salt) == "AQAAAAEAAC4dG6QIy+fB4qYmZl+xJn0n+F9SZmS4B4DUoQ6U4yek4wf3pMZ1DHx0xggBZCtSfS6GLk5SLucOiABaDFIy5w5Y5g=="


# Generated at 2022-06-22 11:56:34.223119
# Unit test for function do_vault
def test_do_vault():
    assert do_vault("test_string", "secret") is not None
    assert do_vault("test_string", None) is None
    assert do_vault(None, None) is None
    assert do_vault(None, "secret") is None
    assert do_vault("test_string", "secret", salt="abc", vaultid="debug") is not None



# Generated at 2022-06-22 11:56:44.797992
# Unit test for function do_vault
def test_do_vault():

    import os
    import tempfile
    import filecmp
    import yaml
    from ansible.parsing.vault import VaultEditor

    test_secret = "mysecret"
    test_data = "mydata"
    test_vault_id = "test_vault_id"

    test_data_yaml = """\
---
- test_vault:
    - test_key: "{{ '%s' | vault(template_vault_secret, vaultid=template_vault_id) }}"
""" % test_data


# Generated at 2022-06-22 11:56:53.598971
# Unit test for function do_unvault
def test_do_unvault():

    # vaulted
    assert do_unvault('$ANSIBLE_VAULT;1.1;AES256;test523656949478\n363161366665623536383165363835613633316562626164636163353831326433356161393962\n35366465326233313334313038653962626334663439376532653035313036343565373634\n', 'test') == 'test1234'

    # already unvaulted
    assert do_unvault('test1234', 'test') == 'test1234'


# Generated at 2022-06-22 11:57:04.847607
# Unit test for function do_vault

# Generated at 2022-06-22 11:57:09.423690
# Unit test for function do_vault
def test_do_vault():
    secret = "abcdefghjklmopqrstuvwxyz1234567890"
    data = "0123456789"
    res = do_vault(data, secret)
    assert isinstance(res, string_types)
    assert is_encrypted(res)



# Generated at 2022-06-22 11:57:17.223190
# Unit test for function do_unvault

# Generated at 2022-06-22 11:57:27.716180
# Unit test for function do_unvault

# Generated at 2022-06-22 11:57:39.472270
# Unit test for function do_vault
def test_do_vault():
    # test 1
    try:
        test_filter = do_vault(123, "secret", salt="abc")
        assert False
    except:
        assert True

    # test 2
    try:
        test_filter = do_vault("123", 123, salt="abc")
        assert False
    except:
        assert True

    # test 3
    try:
        test_filter = do_vault("123", "secret", salt=123)
        assert False
    except:
        assert True

    # test 4

# Generated at 2022-06-22 11:57:49.833070
# Unit test for function do_vault
def test_do_vault():
    import pytest
    from ansible.parsing.vault import VaultLib

    # VaultLib.__init__ does not correctly handle the list inputs
    # for vault_secrets, pass each item of the list instead
    # The list of encrypted data is set to None, as it is a meaningless
    # input for this test
    # The salt and vaultid should be passed to the format method
    # of the encrypted string
    vl = VaultLib([('test_filter_do_vault', VaultSecret('test_filter_do_vault_secret'))])
    test_str = 'test_filter_do_vault_str'

# Generated at 2022-06-22 11:57:55.629928
# Unit test for function do_unvault
def test_do_unvault():

    vault = to_native(VaultSecret('password').encrypt('hello world'))
    # Ensure that plain text is not encrypted
    assert do_unvault('hello world', 'password') == 'hello world'
    # Ensure that an encrypted string is decrypted
    assert do_unvault(vault, 'password') == 'hello world'

# Generated at 2022-06-22 11:58:03.753058
# Unit test for function do_vault

# Generated at 2022-06-22 11:58:17.521018
# Unit test for function do_vault
def test_do_vault():

    vault_filter = FilterModule()

# Generated at 2022-06-22 11:58:25.990781
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('secret_data', 'test_data') == b'$ANSIBLE_VAULT;1.1;AES256\n35623130643735306439333862623935656466376536366530646638336434363064356231663338\n393366626262313964316439316136636630623665636263376330366635623336343065\n'
    display.display("vault filter test passed")


# Generated at 2022-06-22 11:58:33.781220
# Unit test for function do_vault
def test_do_vault():
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.vars.clean import module_args_parser

    from ansible.v2.playbook import Playbook
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host, Group
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.callback.default import CallbackModule

    # Create the dataloader to parse the data
    loader = DataLoader()

    # Create the inventory and pass to var manager
    mock_host = Host(name="mocked")
    mock_host.vars

# Generated at 2022-06-22 11:58:38.787539
# Unit test for function do_vault
def test_do_vault():
    from ansible.parsing.vault import VaultLib
    vl = VaultLib()
    test_string = 'test_string'
    secret = 'secret'
    vault = do_vault(test_string, secret)
    data = do_unvault(vault, secret)
    assert test_string == data

# Generated at 2022-06-22 11:58:42.594071
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('data', 'secret').startswith('$ANSIBLE_VAULT')
    assert len(do_vault('data', 'secret')) > len(do_vault('data', 'secret', 'salt'))



# Generated at 2022-06-22 11:58:54.020131
# Unit test for function do_vault
def test_do_vault():
    # Successful test of encrypted vault
    assert do_vault('hello world', 'secret') == '$ANSIBLE_VAULT;1.1;AES256\n633539643165393530633239616262303330343664656665353636383138356463383233356539\n323138653838613835353664393035646635396134663037623364323736610a30333839633739\n653135643736313761643033316361336237613431313465393262316233376136656437313131\n64653836643965613961386332366265656431326331663835380a'

    # Successful test of encrypted vault with wrap_object=True

# Generated at 2022-06-22 11:59:00.112983
# Unit test for function do_vault
def test_do_vault():
    secret = "This is a secret"
    salt = "foo"
    vaultid = "bar"
    wrap_object = True
    string = "This is a test string"
    count = 1
    for i in range(count):
        enc_string = do_vault(string, secret, salt, vaultid, wrap_object)
        ret = do_unvault(enc_string, secret, vaultid)
        assert ret == string, "do_vault tests failed"
    print("do_vault %d passed" % count)



# Generated at 2022-06-22 11:59:07.860018
# Unit test for function do_unvault
def test_do_unvault():
    data = b'f0vxiGALZlzUmZp8GoLWnDEvCQm9XcXi'
    secret = b'$ANSIBLE_VAULT;1.2;AES256;filter_default;UvtD6UgRfFVhWUJvH3FzOwE0FFB2WlZO'
    vaultid = 'filter_default'
    result = do_unvault(data, secret, vaultid)
    assert result == 'this is a test'

# Generated at 2022-06-22 11:59:19.460937
# Unit test for function do_vault

# Generated at 2022-06-22 11:59:28.847149
# Unit test for function do_unvault
def test_do_unvault():
    assert do_unvault(None, None) == None
    assert do_unvault(None, 'ansible') == None
    assert do_unvault('ansible', 'ansible') == 'ansible'

# Generated at 2022-06-22 11:59:41.654714
# Unit test for function do_unvault

# Generated at 2022-06-22 11:59:52.468869
# Unit test for function do_vault
def test_do_vault():
    test = 'test'
    password = 'test'

# Generated at 2022-06-22 12:00:01.199457
# Unit test for function do_vault

# Generated at 2022-06-22 12:00:13.138284
# Unit test for function do_vault
def test_do_vault():
    secret = 'super_secret'
    salt = 'just_a_salt'
    data = 'secret_data'
    vaultid = 'sample_vaultid'
    wrap_object = True

# Generated at 2022-06-22 12:00:25.965194
# Unit test for function do_vault
def test_do_vault():
    secret = 'super_secret'
    data   = 'hunter2'
    test_vault = do_vault(data, secret, salt=None, vaultid='filter_default', wrap_object=False)

# Generated at 2022-06-22 12:00:38.046975
# Unit test for function do_unvault