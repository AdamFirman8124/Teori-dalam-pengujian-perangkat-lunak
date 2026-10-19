

# Generated at 2022-06-13 07:28:14.097477
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    import yaml
    from ansible.parsing.yaml.objects import AnsibleMapping

    yaml_snippet = '''
stuff:
  a: 1
  b: 2
  a: 3
'''

    exp_ansible_pos = ('<string>', 3, 3)
    exp_data = {'a': 3, 'b': 2}

    ans_cons = AnsibleConstructor(file_name=exp_ansible_pos[0])
    tmp_loader = yaml.Loader(yaml_snippet)
    tmp_loader.anchors = {}
    tmp_loader.version = (1, 2)
    tmp_loader.compat_loader = True
    tmp_loader.constructor = AnsibleConstructor


# Generated at 2022-06-13 07:28:25.562581
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.yaml.data import DataLoader
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    data = u'{"first": 1, "second": "second"}'
    dl = DataLoader()

    loader = AnsibleConstructor(file_name=None)
    obj = loader.get_single_data(data)
    assert isinstance(obj, AnsibleMapping), obj
    assert obj[u'first'] == 1, obj
    assert obj[u'second'] == u'second', obj

    if six.PY2:
        data = u'{"first": 1, "second": "second"}'.encode('utf-16-le')

# Generated at 2022-06-13 07:28:32.040199
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    yaml_str = to_bytes(u"\x00\u1234\u5678\u9abc\ud800\udc00\U0010ffff")
    yaml_str_constructor = AnsibleConstructor()
    assert yaml_str_constructor.construct_yaml_str(MappingNode('tag:yaml.org,2002:str', yaml_str, None, None, yaml_str)) == u"\x00\u1234\u5678\u9abc\udb80\udc00\U0010ffff"



# Generated at 2022-06-13 07:28:37.330674
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    import io
    import yaml

    a = io.StringIO("""
    ansible_str_var: '{"name": "foo", "key": "value", "bool": true}'
    """)

    constructor = AnsibleConstructor()
    y = yaml.load(a, Loader=yaml.Loader)
    assert y['ansible_str_var'] == '{"name": "foo", "key": "value", "bool": true}'


# Generated at 2022-06-13 07:28:50.349734
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    arg_node = u'$ANSIBLE_VAULT;1.1;AES256'
    test_vault_secrets = [u'p@$$w0rd']
    vault = VaultLib(secrets=test_vault_secrets)
    exp_ret = AnsibleVaultEncryptedUnicode(to_bytes(u'$ANSIBLE_VAULT;1.1;AES256'))
    exp_ret.vault = vault
    exp_ret.ansible_pos = (None, 1, 1)
    ac = AnsibleConstructor()
    ret = ac._AnsibleConstructor__construct_vault_encrypted_unicode(arg_node)
    assert exp_ret == ret, u'AnsibleConstructor not constructing AnsibleVaultEncryptedUnicode properly'

# Generated at 2022-06-13 07:28:57.712845
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    import yaml

    yaml.SafeLoader.add_constructor(u'!unsafe', AnsibleConstructor.construct_yaml_unsafe)
    yaml_doc = u'''
    test_unsafe_hosts: !unsafe ['a','b','c','d','e','f','g','h','i','j','k','l','m','n']
    '''
    v = yaml.load(yaml_doc)
    assert v['test_unsafe_hosts'] == wrap_var(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'])

# Generated at 2022-06-13 07:29:11.610239
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import base64
    from ansible.parsing.vault import VaultLib
    from ansible.errors import AnsibleError
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.yaml.loader import AnsibleLoader

    # dummy vault secret
    vault_secrets = ['12345']
    vault = VaultLib(secrets=vault_secrets)

    # mock values for unit test
    ciphertext_data = base64.b64encode(b'$ANSIBLE_VAULT$1.1$' + b'sha256$' + vault.encrypt(b'bar'))

# Generated at 2022-06-13 07:29:19.386488
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from ansible.parsing.yaml.loader import AnsibleLoader
    # Test for empty sequence
    data = u'''
    ---
    -
    '''
    data = AnsibleLoader(data).get_single_data()
    assert isinstance(data, AnsibleSequence)
    assert data.ansible_pos == ('<unicode string>', 1, 1)
    assert data == []

    # Test for non empty sequence
    data = u'''
    ---
    - one
    - two
    - three
    '''
    data = AnsibleLoader(data).get_single_data()
    assert isinstance(data, AnsibleSequence)
    assert data.ansible_pos == ('<unicode string>', 1, 1)
    assert data == ['one', 'two', 'three']

# Generated at 2022-06-13 07:29:25.452714
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    # Tests if a simple mapping node is correctly converted to a AnsibleMapping object.
    mapping_node = MappingNode('tag:yaml.org,2002:map',[],None,None,None,
                               start_mark=(None, 1, 0),end_mark=(None, 1, 0))
    ansible_constructor = AnsibleConstructor()
    ansible_map = ansible_constructor.construct_yaml_map(mapping_node)
    assert isinstance(ansible_map, AnsibleMapping)
    assert len(ansible_map) == 0
    assert ansible_map.ansible_pos == (None, 1, 0)

# Generated at 2022-06-13 07:29:31.609603
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():

    C = AnsibleConstructor()
    import yaml
    node = yaml.nodes.SequenceNode(tag=u'tag:yaml.org,2002:seq',
           value=[],
           flow_style=False)
    C.construct_yaml_seq(node)

    # This is the import line for test_AnsibleConstructor_construct_yaml_seq
    print("AnsibleConstructor_construct_yaml_seq import pass")

# Generated at 2022-06-13 07:29:52.507455
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    import yaml
    import yaml.resolver

    # We must use the yaml library that Ansible uses.
    # For this reason it is necessary to use as yaml_loader yaml.CLoader instead of yaml.SafeLoader
    my_loader = yaml.CLoader
    my_loader.add_constructor(u'tag:yaml.org,2002:seq', AnsibleConstructor.construct_yaml_seq)

    string = """
---
- [1, 2, 3]
- ["one", "two"]
    """

    data = yaml.load(string, Loader=my_loader)

    assert type(data) is list, "Returned data is a list"
    assert len(data) == 2, "Returned data has 2 elements"


# Generated at 2022-06-13 07:30:03.639940
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():

    class MyAnsibleConstructor(AnsibleConstructor):
        def __init__(self, file_name=None):
            super(MyAnsibleConstructor, self).__init__(file_name)

        def _node_position_info(self, node):
            return node.start_mark.index, node.start_mark.line, node.start_mark.column

    m = MyAnsibleConstructor('test.yml')
    src = '''
        foo:
            bar: baz
    '''

    import yaml
    node = yaml.parse(src)
    data = m.construct_yaml_map(node.children[0])

    assert dict(data) == dict(foo={'bar': 'baz'})

# Generated at 2022-06-13 07:30:12.652172
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    def _check_position(data, source, line, column):
        pos = getattr(data, 'ansible_pos', None)
        if pos is None:
            assert False, "Data has no ansible_pos attribute"
        else:
            assert pos[0] == source
            assert pos[1] == line
            assert pos[2] == column

    import yaml
    yaml_data = """
    - test1:
        - first
        - second
      key: value
    - test2: hello
      test3: world
    """

    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence
    data = yaml.load(yaml_data, Loader=AnsibleConstructor)
    assert isinstance(data, AnsibleSequence)
    _check_position

# Generated at 2022-06-13 07:30:19.934599
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from ansible.parsing.yaml.loader import AnsibleLoader

    assert_data = {
        'a': [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}],
        'b': [{'a': 5, 'b': 6, 'c': 7}, {'a': 8, 'b': 9, 'c': 10}],
    }

    yaml_data = '''
a:
  - a: 1
    b: 2
  - {a: 3, b: 4}
b:
  - {a: 5, b: 6, c: 7}
  - {a: 8, b: 9, c: 10}
'''

    assert AnsibleLoader(yaml_data).get_single_data() == assert_data



# Generated at 2022-06-13 07:30:28.533343
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    ansi_con = AnsibleConstructor()

    # Example of a mapping that produces the error
    data = ['a: b', 'a: c']
    first = ansi_con.construct_yaml_map(data[0])
    mapping = ansi_con.construct_mapping(first, deep=True)
    second = ansi_con.construct_yaml_map(data[1])
    ansi_con.construct_mapping(second, deep=True)

    # Actual test
    # Positive test - tests for key collision and warns user
    result = [ansi_con.construct_yaml_map(x) for x in data]
    mapping = ansi_con.construct_mapping(result[0], deep=True)

    exception = False

# Generated at 2022-06-13 07:30:39.823886
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import unittest
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    class TestAnsibleConstructor(unittest.TestCase):

        def setUp(self):
            vault_password_file = '/tmp/mypasswordfile'
            with open(vault_password_file, 'wb') as f:
                f.write(b'$ANSIBLE_VAULT;1.1;AES256\n3333333333333333333333333333333333333333333333333333333333333333\n'
                        b'333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333'
                        b'33333333333333333333333333333333333333333333333333333333\n')
            self.vault_secrets = [vault_password_file]

       

# Generated at 2022-06-13 07:30:49.557914
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.dataloader import DataLoader

    node = AnsibleLoader(dict(), DataLoader()).get_single_data("{1: 'b'}")
    assert node.value[0][0].value == '1'
    assert node.value[0][1].value == 'b'

    assert AnsibleConstructor().construct_mapping(node)[1] == 'b'

    node = AnsibleLoader(dict(), DataLoader()).get_single_data("{1: 'b', 1: 'c'}")
    assert node.value[0][0].value == '1'
    assert node.value[0][1].value == 'b'
    assert node.value[1][0].value == '1'

# Generated at 2022-06-13 07:30:52.015609
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    print('Test constructor to construct yaml map')
    ansible_constructor = AnsibleConstructor()
    assert ansible_constructor.construct_yaml_map is not None



# Generated at 2022-06-13 07:30:57.624403
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    import yaml

    m = '''
a: 1
b: 2
c:
 - 3
 - 4
'''

    d = yaml.load(m, Loader=AnsibleConstructor)
    assert isinstance(d, AnsibleMapping)
    assert d['a'].ansible_pos == ('<string>', 2, 0)

# Generated at 2022-06-13 07:31:06.034821
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    class MockAnsibleConstructor(AnsibleConstructor, object):
        def __init__(self):
            self.vault_secrets = []
            super(MockAnsibleConstructor, self).__init__(vault_secrets=self.vault_secrets)

        def construct_scalar(self, node):
            return u"abcdef"

    vault_lib_class = VaultLib

# Generated at 2022-06-13 07:31:17.509118
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    test_input = {"user1": AnsibleUnicode("password1"), "user2": AnsibleUnicode("password2")}
    test_output = AnsibleConstructor().construct_mapping(test_input)

    assert test_output == test_input

# Generated at 2022-06-13 07:31:24.145070
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from yaml.nodes import ScalarNode

    vault_id = '00000000000000000000000000000000'
    vault_secrets = ['vault-password']
    ac = AnsibleConstructor(vault_secrets=vault_secrets)


# Generated at 2022-06-13 07:31:34.242794
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    # Testing for method `construct_mapping`

    # Test case 1:
    # Test when `node` is a `MappingNode` and `node.value` is an empty list.
    node = MappingNode(tag=u'tag:yaml.org,2002:map', value=[], start_mark=None, end_mark=None)
    test_constructor = AnsibleConstructor()
    mapping = test_constructor.construct_mapping(node)
    assert isinstance(mapping, AnsibleMapping)

    # Test case 2:
    # Test when `node` is not a `MappingNode`.
    node = u'tag:yaml.org,2002:map'
    test_constructor = AnsibleConstructor()

# Generated at 2022-06-13 07:31:40.363675
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    data = "[1, 2, 3]"
    # FIXME: Is this supposed to be an empty string?
    # FIXME: What should it be instead?
    # FIXME: I don't believe it can be an empty string,
    # because then AnsibleConstructor() will call the
    # constructor for yaml.loader, which will initialize
    # the filename to None. Later, when the filename is
    # accessed in _node_position_info(), it will raise
    # an exception because the filename is None.
    filename = ""
    result = AnsibleConstructor(filename).get_single_data(data)
    assert type(result) == list
    assert result == [1, 2, 3]

# Generated at 2022-06-13 07:31:44.860790
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    yaml_str = """
    # example
    name: Rental car reservation
    confirm:
      booking: "Booking confirmation #12345"
      cost: ${{ 200 * 2 }}
    """

    ansible_constructor = AnsibleConstructor("")
    new_obj = ansible_constructor.construct_yaml_map(ansible_constructor.compose_node(yaml_str))
    assert isinstance(new_obj, AnsibleMapping) is True
    assert new_obj == {'name': 'Rental car reservation',
                       'confirm': {'booking': 'Booking confirmation #12345',
                                   'cost': '${ 200 * 2 }'}}


# Generated at 2022-06-13 07:31:52.592779
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    ans_constructor = AnsibleConstructor()
    print(ans_constructor.__dict__)
    print(ans_constructor.__class__.__dict__)

# Generated at 2022-06-13 07:32:06.508104
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    constructor = AnsibleConstructor()

    # Test case #1:
    # keys are not valid Python identifiers.
    # This should result in a ConstructorError being raised.
    #
    # For details, see:
    # https://github.com/ansible/ansible/issues/32575
    res1 = {}
    try:
        constructor.construct_yaml_map(MappingNode(u'tag:yaml.org,2002:map', [(("test__var", u'123'), None),
                                                                             (("test-var", u'abc'), None)]))
    except ConstructorError as err:
        res1 = dict(text=err, result=False)
    except Exception as err:  # pylint: disable=broad-except
        res1 = dict(text=err, result=False)

# Generated at 2022-06-13 07:32:11.345728
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from io import BytesIO

    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib

    fake_secrets = ['ansible']

# Generated at 2022-06-13 07:32:15.248253
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    yaml_str = '''
- 1
- 2
- 3
'''
    yaml_object = yaml.load(yaml_str, Loader=AnsibleConstructor)
    assert yaml_object == dict(
        val=AnsibleSequence([1, 2, 3])
    )

# Generated at 2022-06-13 07:32:18.835816
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    ac = AnsibleConstructor()
    node = MappingNode(tag='tag:yaml.org,2002:map', value=['node'], start_mark=None, end_mark=None, flow_style=None)
    assert 'node' == ac.construct_mapping(node)

# Generated at 2022-06-13 07:32:46.928409
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    ansible_constructor = AnsibleConstructor()
    test_node = {u'tag': u'!vault-encrypted', u'value': u'$ANSIBLE_VAULT;1.1;AES256\n35663639336233663463383338633632663430373439333738393036373537663134313661616639\n'}
    value = ansible_constructor.construct_scalar(test_node)
    b_ciphertext_data = to_bytes(value)
    # could pass in a key id here to choose the vault to associate with
    # TODO/FIXME: plugin vault selector
    vault = ansible_constructor._vaults['default']

# Generated at 2022-06-13 07:32:51.329647
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    # Testing to maken sure that the ansible_pos attribute is added to the
    # created ansible mapping
    constructor = AnsibleConstructor()
    mapping = constructor.construct_yaml_map(None)
    assert mapping.ansible_pos is not None
    mapping_object = next(mapping)
    assert mapping_object == mapping
    assert mapping_object.ansible_pos is not None

# Generated at 2022-06-13 07:33:00.052622
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from ansible.parsing.yaml.loader import AnsibleLoader
    class TestAnsibleConstructor(AnsibleConstructor):
        def construct_yaml_unsafe(self, node):
            return self.construct_scalar(node) + '_modified'

    test_loader = AnsibleLoader(None, None)

    # Test method overridden
    assert(isinstance(test_loader._constructor, TestAnsibleConstructor))

    # Test !unsafe method

# Generated at 2022-06-13 07:33:09.448556
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.vault import VaultLib

    # Create the constructors
    yaml_constructor = AnsibleConstructor()
    yaml_loader = yaml.Loader(yaml_constructor)

    # Load the data
    try:
        data = yaml_loader.get_single_data()
    except AttributeError:
        # PyYaml < 5
        data = yaml_loader.get_data()

    # Check the data
    assert isinstance(data, AnsibleMapping)
    assert len(data) == 4
    assert data['key1'] == 'value1'
    assert data['key2'] == 'value2'
    assert data['key3'] == 'value3'

# Generated at 2022-06-13 07:33:21.519905
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    import yaml

    data = [
        {
            u'a': u'b',
            u'c': u'd'
        },
        {
            u'e': u'f',
            u'g': u'h'
        },
    ]

    yaml_representation = yaml.dump(data, Dumper=AnsibleDumper)
    ansible_constructor = AnsibleConstructor()
    loaded = yaml.load(yaml_representation, Loader=yaml.Loader)

    assert len(loaded) == 2

# Generated at 2022-06-13 07:33:29.192207
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    from ansible.parsing.yaml.loader import AnsibleLoader
    loader = AnsibleLoader(None, None)
    data = AnsibleUnicode('{"pkg:role:foo":"bar"}')
    data.ansible_pos = ('file.yml', 2, 4)
    assert loader.construct_yaml_str(data) == '{"pkg:role:foo":"bar"}'
    assert loader.construct_yaml_str(data) is not data

# Generated at 2022-06-13 07:33:30.099852
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    pass


# Generated at 2022-06-13 07:33:37.932240
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import yaml
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.vault import VaultLib
    secrets = ['fake_secret']
    vault = VaultLib(secrets)
    vault.encrypt('plaintext')
    loader = AnsibleLoader(stream=None, file_name=None, vault_secrets=['fake_secret'])
    loader.vaults['default'] = vault
    plaintext = 'plaintext'
    ciphertext_data = vault._backend.encrypt('plaintext')
    yaml_string = '!vault |\n  $ANSIBLE_VAULT;1.1;AES256\n  {2}'.format(ciphertext_data)
    plain = yaml.load(yaml_string, Loader=loader)

# Generated at 2022-06-13 07:33:44.108785
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    import yaml
    from yaml.composer import Composer
    from yaml.constructor import BaseConstructor
    import ansible.parsing.yaml.loader as yaml_loader

    unicode_repr = 'unicode-repr'
    def construct_yaml_str(self, node):
        return unicode_repr

    class MockConstructor(BaseConstructor):
        def construct_yaml_str(self, node):
            return construct_yaml_str(self, node)

    class MyLoader(yaml_loader.AnsibleLoader):
        def __init__(self, stream, file_name=None, vault_secrets=None):
            self._composer = Composer(stream, Loader=self)

# Generated at 2022-06-13 07:33:49.525151
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    a = AnsibleConstructor()

    # test empty seq
    seq = a.construct_yaml_seq([])
    assert isinstance(seq, list)
    assert len(seq) == 0

    # test seq
    seq = a.construct_yaml_seq([1,2,3])
    assert isinstance(seq, list)
    assert len(seq) == 3

    # test seq by iterator
    seq = a.construct_yaml_seq(iter([1,2,3]))
    assert isinstance(seq, list)
    assert len(seq) == 3

    # test with ansible node position
    seq = a.construct_yaml_seq([1,2,3])
    assert isinstance(seq, list)
    assert len(seq) == 3

# Generated at 2022-06-13 07:34:21.695685
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from ansible.parsing.vault import VaultLib

    vault_secret = VaultLib.create_vault_secret(b'1234')

    c = AnsibleConstructor()


# Generated at 2022-06-13 07:34:26.343132
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.vault import VaultLib
    test_str = '192.168.0.1'
    test_str_unicode = u'\u4f60\u597d'
    loader = AnsibleLoader(None, None)
    result = loader.construct_yaml_str(AnsibleConstructor.construct_yaml_str(loader, test_str))
    assert isinstance(result, AnsibleUnicode)
    assert result == test_str
    result = loader.construct_yaml_str(AnsibleConstructor.construct_yaml_str(loader, test_str_unicode))
    assert isinstance(result, AnsibleUnicode)
    assert result == test_str_unicode
    test_data

# Generated at 2022-06-13 07:34:35.790631
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.dumper import AnsibleDumper

    yaml_text_1 = 'foo: 1\nbar: 2\nbaz: 3'
    yaml_text_2 = 'foo: 4\nbar: 2\nbaz: 3'
    yaml_text_3 = 'foo: 1\nbar: 2\nbaz: 3\nbaz: 3'
    yaml_text_4 = 'foo: 1\nbar: 2\nbaz: 3\nbaz: 4'

    # test yaml_text_1
    data = AnsibleLoader(yaml_text_1).get_single_data()

# Generated at 2022-06-13 07:34:38.902168
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    cons = AnsibleConstructor()
    data = cons.construct_mapping(dict(a=1, b=2), "test")
    assert data == dict(a=1, b=2)

# Generated at 2022-06-13 07:34:48.638036
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from ansible.parsing.yaml.loader import AnsibleLoader


# Generated at 2022-06-13 07:34:58.388529
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    # AnsibleConstructor is a subclass of SafeConstructor,
    # so there are 2 ways to call SafeConstructor.construct_yaml_str
    # directly to test AnsibleConstructor.construct_yaml_str
    from yaml.constructor import SafeConstructor
    from yaml.nodes import ScalarNode

    # 1. directly call SafeConstructor.construct_yaml_str
    class MySafeConstructor(SafeConstructor):
        pass

    # WARNING: unsafe by default
    my_safe_constructor = MySafeConstructor()
    node = ScalarNode(u'tag:yaml.org,2002:str', u'Hello world!')
    ret = my_safe_constructor.construct_yaml_str(node)

    assert(ret.__class__.__name__ == u'unicode')

# Generated at 2022-06-13 07:35:07.186235
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import yaml
    ciphertext = u"$ANSIBLE_VAULT;1.1;AES256"
    decrypted_text = u"Hello World"
    yaml_document = u"%s\n%s\n" % (ciphertext, decrypted_text)
    obj = yaml.load(yaml_document, Loader=AnsibleConstructor)
    # Ensure that the encrypted string is being decrypted
    assert obj == decrypted_text
    # Ensure that the encrypted string is being decrypted and is a unicode string
    assert type(obj) is unicode

# Generated at 2022-06-13 07:35:10.881019
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    AnsibleConstructor = globals()["AnsibleConstructor"]
    assert(AnsibleConstructor is not None)
    try:
        AnsibleConstructor.construct_mapping()
        assert False, "construct_mapping does not require argument 'node'."
    except TypeError as te:
        pass

# Generated at 2022-06-13 07:35:13.686341
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    node = MappingNode(u'tag:yaml.org,2002:map', [])
    Constructor = AnsibleConstructor()
    Constructor.construct_mapping(node)
    assert True

# Generated at 2022-06-13 07:35:20.604504
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    ac = AnsibleConstructor()
    # test that various unicode encodings work in python2
    from ansible.vars.unsafe_proxy import wrap_var
    # test that various unicode encodings work in python2 / python 3
    assert (u'\uc790\uc790' == ac.construct_yaml_str(ac.construct_yaml_str.__wrapped__(ac, None, '\uc790\uc790')))
    assert (u'\U0001f1fa\U0001f1f8' == ac.construct_yaml_str(ac.construct_yaml_str.__wrapped__(ac, None,
                                                                                              '\U0001f1fa\U0001f1f8')))

# Generated at 2022-06-13 07:36:02.241798
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import base64

    vault_data = base64.b64decode("AQD1TUgV6UJ1hR+Vyb/Un6XbhV7hQJvHEUh1Zmq3qd75I+QdfwDi22zKo5kj5q5+DpY=")
    vault_data = to_bytes("!vault |\n" + vault_data.decode("utf-8"))

    vault_secrets = [b'password']

    ansible_constructor = AnsibleConstructor(vault_secrets=vault_secrets)
    ans_obj = ansible_constructor.construct_yaml_unsafe(ansible_constructor.compose_document(vault_data))

    assert ans_obj == u'password'

# Generated at 2022-06-13 07:36:14.357382
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import yaml
    from ansible.vars.unsafe_proxy import wrap_var
    
    c = AnsibleConstructor()
    value_node = yaml.nodes.ScalarNode(u'tag:yaml.org,2002:str','!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          62316462373934306566326237363735653263333666336663643037366435356564373537633235\n          38373366363635323337383265613237622d2a46\n          ')
    value = c.construct_vault_encrypted_unicode(value_node)
    
    assert(isinstance(value, wrap_var))

# Generated at 2022-06-13 07:36:21.570407
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    import os
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.loader import AnsibleLoader
    # create a file with content
    filename = os.getcwd() + '/test_hosts.yml'
    test_str = '[ubuntu, centos]'
    f = open(filename, 'w')
    f.write(test_str)
    f.close()
    # now test the case
    stream = open(filename, 'r')
    d = AnsibleLoader(stream, file_name=filename).get_single_data()
    assert d == [u'ubuntu', u'centos']
    stream.close()

# Generated at 2022-06-13 07:36:28.346171
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from io import StringIO
    import sys
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.vars.unsafe_proxy import wrap_var

    class PatchedAnsibleConstructor(AnsibleConstructor):
        def __init__(self):
            super(PatchedAnsibleConstructor, self).__init__()
            self._vaults['default'] = VaultLib(secrets=['Secret123'])

    class PatchedAnsibleLoader(AnsibleLoader):
        def __init__(self, stream):
            super(PatchedAnsibleLoader, self).__init__(stream)

# Generated at 2022-06-13 07:36:37.441990
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import cStringIO
    from ansible.parsing.yaml.loader import AnsibleLoader

    test_string = u"""
    test_vault_string: !vault |
          $ANSIBLE_VAULT;1.2;AES256;foo
          3132333435363738393031323334353637383930313233343536373839303132
          3334353637383930313233343536373839303132333435363738393031323334
    """
    test_file = cStringIO.StringIO(to_bytes(test_string))
    load = AnsibleLoader(test_file, vault_secrets=['foo']).get_single_data()


# Generated at 2022-06-13 07:36:48.336852
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    ansible_constructor = AnsibleConstructor()
    node = object()
    node.start_mark = object()
    node.start_mark.line = 0
    node.start_mark.column = 56
    ansible_constructor._ansible_file_name = 'filename'
    ansible_constructor._vaults = {}
    ansible_constructor._vaults['default'] = VaultLib(secrets=['ansible'])
    ansible_constructor.construct_scalar = lambda n: '$ANSIBLE_VAULT_ARGS;$ANSIBLE_VAULT_PASSWORD'
    vault_encrypted_unicode = ansible_constructor.construct_vault_encrypted_unicode(node)
    assert vault_encrypted_unicode.ansible_pos == ('filename', 1, 57)

# Generated at 2022-06-13 07:36:52.966841
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    import yaml
    ac = AnsibleConstructor()
    # If a 7 digit integer is passed, its type should not be changed
    assert ac.construct_yaml_unsafe(yaml.nodes.ScalarNode('tag:yaml.org,2002:int', '1234567')) == 1234567
    # If a number with more than 7 digits is passed, its type should be changed to float
    assert ac.construct_yaml_unsafe(yaml.nodes.ScalarNode('tag:yaml.org,2002:int', '12345678')) == 12345678.0
    # If a double quoted string is passed, its type should be changed to str

# Generated at 2022-06-13 07:36:55.809728
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    mapping = """
    a: b
    c: d
    e: f
    """
    data = yaml.load(mapping, Loader=AnsibleConstructor)
    assert isinstance(data, AnsibleMapping)
    assert 'b' == data['a']
    assert 'f' == data['e']
    assert data.ansible_pos == ('<string>', 1, 1)



# Generated at 2022-06-13 07:37:09.771786
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    import ansible.errors
    from ansible.parsing.yaml.objects import AnsibleUnsafeText

    test_yaml = '''
    - shell: /usr/bin/foo
      args: echo "{{service_password}}"
    '''
    ac = AnsibleConstructor()
    try:
        result = ac.construct_yaml(test_yaml)
    except ansible.errors.AnsibleParserError as e:
        if e.message == u"found an undefined variable, 'service_password'":
            raise AssertionError('Expect no error but got ' + e.message)

    if not isinstance(result[0]['args'], AnsibleUnsafeText):
        raise AssertionError('Expect AnsibleUnsafeText but got %s' % type(result[0]['args']))

# Generated at 2022-06-13 07:37:10.564263
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    pass