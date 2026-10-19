

# Generated at 2022-06-13 07:28:13.793794
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    import yaml
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.module_utils._text import to_text

    text = to_text('''
---
a_string: A string
another_string: "Another string"
''')

    data = yaml.load(text, Loader=AnsibleConstructor)
    assert isinstance(data['a_string'], AnsibleUnicode)
    assert isinstance(data['another_string'], AnsibleUnicode)

# Generated at 2022-06-13 07:28:25.215753
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import VaultedUnicode
    from ansible.utils.unsafe_proxy import wrap_var
    from ansible.utils.vault import VaultLibException
    import json

    secret1 = VaultSecret(r'$ANSIBLE_VAULT;1.1;AES256', '387830393330386639626166656333343337632333739353632383162646164656466373935343064623862613337363865626237313232663964616364363037')

# Generated at 2022-06-13 07:28:26.481423
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    # FIXME: Test AnsibleConstructor.construct_mapping()
    pass

# Generated at 2022-06-13 07:28:29.902362
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():

    doctest_str = (
        u'key:\n'
        u'- value1\n'
        u'- value2\n')

    test_obj = AnsibleConstructor()
    test_obj.construct_yaml_seq(doctest_str)

# Generated at 2022-06-13 07:28:37.300161
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():

    vault_text = u'$ANSIBLE_VAULT;1.1;AES256\n63303636383730386665323266343936336635656564623239333761373430383438313132343261376234\n390a6633393566396438323233353235303663323063643533623231373831613162346366633239646632\n37373331653661643762363962306338636537386134613861623463316363306639\n'

    from io import StringIO
    from yaml import load, YAMLError


# Generated at 2022-06-13 07:28:40.238049
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    data = b"""
- foo: bar
- baz: quux
- quux: corge
"""

    yaml = YAML(typ="safe")
    yaml.Constructor = AnsibleConstructor
    yaml.constructor.load(data)

# Generated at 2022-06-13 07:28:54.369018
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor

# Generated at 2022-06-13 07:29:01.216745
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    # pylint: disable=redefined-outer-name,protected-access
    yaml_str = '''
        key1: value1
        key2: value2
        '''
    node = yaml.compose(yaml_str)
    AnnotationConstructor = AnsibleConstructor()
    result = AnnotationConstructor._AnsibleConstructor__construct_yaml_map(node)
    print(result)


# Generated at 2022-06-13 07:29:10.633969
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    c = AnsibleConstructor()
    # Test for non-node object
    ret = list(c.construct_yaml_seq('seq'))
    assert ret == []

    # Test for empty node
    ret = list(c.construct_yaml_seq(MappingNode(tag=u'tag:yaml.org,2002:map', value=[], start_mark=None, end_mark=None)))
    assert ret == []

    # Test for dict node
    val = MappingNode(tag=u'tag:yaml.org,2002:map', value=[('a', 'b'), ('c', 'd')], start_mark=None, end_mark=None)
    ret = list(c.construct_yaml_seq(val))
    assert ret == [{'a':'b', 'c':'d'}]

# Generated at 2022-06-13 07:29:19.041889
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    # Simple test, just to check if the method is executed without any runtime error
    from yaml.nodes import MappingNode
    from yaml.nodes import ScalarNode

    node = MappingNode(tag='tag:yaml.org,2002:map', value=[],
                       start_mark=None, end_mark=None, flow_style=None)
    node.value.append((
        ScalarNode(tag='tag:yaml.org,2002:str', value='key1',
                   start_mark=None, end_mark=None, style=None),
        ScalarNode(tag='tag:yaml.org,2002:str', value='value1',
                   start_mark=None, end_mark=None, style=None)
    ))

# Generated at 2022-06-13 07:29:31.525380
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    from yaml import nodes

    # Test for dict
    node = nodes.MappingNode(None, None, True, None, None)
    ret = AnsibleConstructor().construct_yaml_map(node)
    assert isinstance(ret, AnsibleMapping)

    # Test for list
    node = nodes.SequenceNode(None, None, True, None, None)
    ret = AnsibleConstructor().construct_yaml_seq(node)
    assert isinstance(ret, AnsibleSequence)


# Generated at 2022-06-13 07:29:42.117966
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    # Testing case when value is not a str
    node = u'tag:yaml.org,2002:str'
    assert AnsibleConstructor.construct_vault_encrypted_unicode(node) == u'tag:yaml.org,2002:str'

    # Testing case when value is a str and self.vault_secrets is None
    node = u'$ANSIBLE_VAULT;1.1;AES256\n3062323265616663386336664633561623363353435366231316265363335376365366430653438\n613665323436663763373566303438656530353936313532346165316566313261306663343432\n36393233346438352d643361\n'

# Generated at 2022-06-13 07:29:46.034037
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    data = """
foo:
    key1: value1
    key2: value2
    key1: value3
"""

    # Parse without errors
    construct = AnsibleConstructor(vault_secrets=['foo'])
    construct.constructor.construct_mapping(construct.loader.compose_node(data, 0, 0))

# Generated at 2022-06-13 07:29:51.770775
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    value = '''---
a: 1
'''
    constructor = AnsibleConstructor()
    yaml_obj = yaml.load(value, Loader=AnsibleConstructor)
    assert yaml_obj['a'] == 1
    assert yaml_obj.ansible_pos == ('<string>', 1, 0)


# Generated at 2022-06-13 07:30:02.650955
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    # TODO: remove when legacy vault format is no longer supported
    vault = VaultLib(secrets=[b'vault_password'])
    vault.update(b'$ANSIBLE_VAULT;1.1;AES256\n39393939393939393939393939393939393939393939393939393939393939393939393939\n39393939393939393939393939393939393939393939393939393939393939393939393939\n393939393939393939393939393939393939393939393', b'a')

# Generated at 2022-06-13 07:30:11.780561
# Unit test for method construct_yaml_str of class AnsibleConstructor

# Generated at 2022-06-13 07:30:19.349794
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    """
    Test the _node_position_info method of a AnsibleConstructor.
    :return: None
    """
    data = """
    a: 1
    b: 2
    c: 3
    """
    string_data = to_bytes(data)
    for line in data.split('\n'):
        string_data += b'\n'

    string_data += b'\n'

    yaml_data = yaml.load(string_data, Loader=AnsibleConstructor)

    assert yaml_data['a'].ansible_pos == ('<string>', 1, 0)
    assert yaml_data['b'].ansible_pos == ('<string>', 2, 0)
    assert yaml_data['c'].ansible_pos == ('<string>', 3, 0)

# Generated at 2022-06-13 07:30:28.222352
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    data = '''
    a: 1
    b: 2
    '''

    class TestAnsibleConstructor(AnsibleConstructor):
        def _node_position_info(self, node):
            return ('<string>', 0, 0)

    yaml = YAML(typ='safe', pure=True)
    yaml.default_flow_style = False
    yaml.Constructor = TestAnsibleConstructor
    yaml.width = 4096


# Generated at 2022-06-13 07:30:39.535202
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():

    # Verify that a dict with a duplicate key will raise an error
    # when DUPLICATE_YAML_DICT_KEY is 'error'
    yaml_str = r'''
    ---
      test:
      - name: foo
        foo: bar
        foo: baz
    '''
    try:
        AnsibleConstructor(file_name='<string>').get_single_data(yaml_str)
    except ConstructorError as e:
        assert to_native(e) == u'while constructing a mapping\n  in "<string>", line 5, column 9\nfound a duplicate dict key (foo). Using last defined value only.'

    # Verify that a dict with a duplicate key will warn users
    # when DUPLICATE_YAML_DICT_KEY is 'warn'
    C.DUPLICATE_

# Generated at 2022-06-13 07:30:49.402352
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    from io import StringIO
    from ansible.parsing.yaml.objects import AnsibleMapping

    AnsibleConstructor.add_constructor(
        u'tag:yaml.org,2002:str',
        AnsibleConstructor.construct_yaml_str)

    test_yaml_str = """
        a: "text1"
        b: "text2"
    """

    constructor = AnsibleConstructor()
    data = constructor.construct_yaml(StringIO(test_yaml_str))

    map_a = AnsibleMapping()
    map_a['a'] = 'text1'
    map_b = AnsibleMapping()
    map_b['b'] = 'text2'

    assert data == map_a

# Generated at 2022-06-13 07:31:07.009329
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import yaml
    from ansible.parsing.vault import VaultLib
    class VaultLib():
        def __init__(self, secrets=None):
            self.secrets = secrets
        def decrypt(self, ciphertext):
            return 'decrypted_content'
    
    class Fake_node():
        start_mark = None
        
    node = Fake_node()
    vault = VaultLib(secrets=['secret'])
    # test with valid secret
    constructor = AnsibleConstructor(file_name=None,vault_secrets=['secret'])
    constructor._vaults = {'default':vault}
    value = '$ANSIBLE_VAULT;1.1;AES256;test_test\ndecrypted_content'
    ret = constructor.construct_vault_encrypted_unicode(node)

# Generated at 2022-06-13 07:31:18.499745
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():   # pylint: disable=too-many-return-statements
    import yaml
    from ansible.parsing.yaml.objects import AnsibleUnsafeText
    debugger = AnsibleConstructor()
    input_value = {'abc': '!unsafe 123'}
    expected_value = {'abc': AnsibleUnsafeText('123')}
    for value in yaml.load_all(yaml.dump(input_value), Loader=AnsibleConstructor):
        assert value == expected_value
    input_value = {'abc': '!unsafe 123'}
    expected_value = {'abc': AnsibleUnsafeText('123')}
    for value in yaml.load_all(yaml.dump(input_value), Loader=debugger):
        assert value == expected_value
    input_value

# Generated at 2022-06-13 07:31:29.549820
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    vault_text = u"$ANSIBLE_VAULT;1.2;AES256;forrest"
    vault_text_b = vault_text.encode('utf-8')
    vault_md5digest = u"e13c82cc81408f2857e1893c309075b1"
    vault_md5digest_b = vault_md5digest.encode('utf-8')
    vault_ciphertext = u"AES256$forrest$1$89e67e6b9d78dcbb$d3b3eba79279de2f6abccd6ca359c897beb664a9fc7b7d3572c65f59ce8ea1e6"

# Generated at 2022-06-13 07:31:37.715415
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    constructor = AnsibleConstructor()
    memory_file  = '''\
        first_level_key1:
            second_level_key1: 2nd_level_value1

        first_level_key2:
            - item1
    '''
    node = yaml.compose(memory_file)
    data = constructor.construct_yaml_map(node)
    assert data.keys() == [u'first_level_key1', u'first_level_key2']
    assert data.values()[0].keys() == [u'second_level_key1']
    assert data.values()[0].values()[0] == u'2nd_level_value1'
    assert data.values()[1] == [u'item1']


# Generated at 2022-06-13 07:31:43.433912
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import yaml
    encrypted_text = u'$ANSIBLE_VAULT;1.1;AES256\n33326235643035376336323465323964343338643433666533383233623536316466623439353338\n34303962333139613235633131626233366339376361666637316438623230383734303331353734\n613537356537323031643531343636656434613038653932366239303433\n'
    yamlstring = u'---\n' + encrypted_text
    yamltree = yaml.load(yamlstring, AnsibleConstructor)
    encryption_backend = yamltree.vault
    assert isinstance(encryption_backend, VaultLib)

# Generated at 2022-06-13 07:31:51.820979
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    # Create an instance of AnsibleConstructor
    ansible_constructor = AnsibleConstructor()

    # Create a sample node for encrypting

# Generated at 2022-06-13 07:32:01.999854
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    import sys
    import _collections_abc

    if not hasattr(sys, 'pypy_version_info'):
        import types

    class _Sized(object):

        def __init__(self, size):
            self.size = size

        @property
        def __sizeof__(self):
            return self.size

        def __repr__(self):
            return '<_Sized {0}>'.format(self.size)

    class _Iterable(_Sized, _collections_abc.Iterable):

        def __iter__(self):
            return iter(['foo'])

    class _Iterator(_Iterable, _collections_abc.Iterator):

        def __next__(self):
            return 'foo'


# Generated at 2022-06-13 07:32:08.786231
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    yaml_data = '''
    a: 1 - 2
    b:
        k1: 1
        k2: 2
        k3: 3
    c:
        - foo
        - bar
        - baz
    d: [ 'A', 'B', 'C' ]
    e:
        - a: b
          c: d
        - e: f
          g: h
    f: { a: b, c: d, e: f }
    '''

    import yaml
    from ansible.parsing.yaml.dumper import AnsibleDumper
    yaml_obj = yaml.load(yaml_data, AnsibleConstructor)
    print(yaml.dump(yaml_obj, Dumper=AnsibleDumper, default_flow_style=False))

# Unit test

# Generated at 2022-06-13 07:32:18.540697
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import os
    import tempfile
    import yaml


# Generated at 2022-06-13 07:32:28.117896
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    const = AnsibleConstructor()

    node = None
    assert const.construct_yaml_str(node) is None

    # Test the default.
    node = u'Hello World!'
    const = AnsibleConstructor()
    result = const.construct_yaml_str(node)

    assert isinstance(result, AnsibleUnicode)
    assert result == u'Hello World!'

    # Test that unicode-objects have positions.
    node = u'Hello World!'
    const = AnsibleConstructor()
    result = const.construct_yaml_str(node)

    assert isinstance(result, AnsibleUnicode)
    assert result.ansible_pos == (None, None, None)



# Generated at 2022-06-13 07:32:48.132739
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    '''
    This is not a proper unit test and will be moved to testing/utils/yaml.py
    when we can generate the data at test time without the use of the import
    statements below. For the time being this is tested by the integration
    test test/integration/targets/unsafe_vars.yml
    '''
    from ansible.parsing.yaml import load
    from ansible.parsing.vault import _get_vault_secrets_from_file

    vault_secrets = _get_vault_secrets_from_file(C.DEFAULT_VAULT_PASSWORD_FILE)
    ac = AnsibleConstructor(vault_secrets=vault_secrets)


# Generated at 2022-06-13 07:32:50.266579
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from ansible.module_utils.parsing.convert_bool import boolean

    ac = AnsibleConstructor()

# Generated at 2022-06-13 07:32:59.363712
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    def _get_fake_secret():
        return "password"

    def _get_fake_secrets():
        return [_get_fake_secret()]

    def _fake_vault_decrypt(self, data):
        return "decrypted"

    class FakeVault:
        def __init__(self, secrets):
            self.secrets = secrets

        decrypt = _fake_vault_decrypt

    class FakeVaultLib:
        def __init__(self, secrets):
            self._vaults = {}
            self._vaults['default'] = FakeVault(secrets)

        def get_vault(self, vault_id):
            return self._vaults[vault_id]

    # test successful decryption
    ac = AnsibleConstructor()
    ac.vault_secrets = _get_

# Generated at 2022-06-13 07:33:08.678420
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    """Ensure that construct_yaml_unsafe is idempotent on plain strings"""
    c = AnsibleConstructor()

    # Empty string
    assert isinstance(c.construct_yaml_unsafe(''), AnsibleUnicode)
    assert c.construct_yaml_unsafe('') == AnsibleUnicode('')

    # Plain string
    assert isinstance(c.construct_yaml_unsafe('plain string'), AnsibleUnicode)
    assert c.construct_yaml_unsafe('plain string') == AnsibleUnicode('plain string')

    # Unicode string
    assert isinstance(c.construct_yaml_unsafe(u'Iñtërnâtiônàlizætiøn'), AnsibleUnicode)

# Generated at 2022-06-13 07:33:23.073373
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    construct_mapping = AnsibleConstructor.construct_mapping

    node = MappingNode(tag='tag:yaml.org,2002:map', value=[])
    value = construct_mapping(node)
    assert isinstance(value, AnsibleMapping)

    # Ensure construct_mapping raises an exception if given an argument of the wrong type.
    node = MappingNode(tag='tag:yaml.org,2002:int', value=[])
    try:
        construct_mapping(node)
    except ConstructorError:
        pass

    # Ensure construct_mapping raises an exception if given an argument of the wrong type.
    node = u'tag:yaml.org,2002:int'
    try:
        construct_mapping(node)
    except ConstructorError:
        pass

# Generated at 2022-06-13 07:33:33.040518
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    from io import StringIO
    from yaml import YAMLObject
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    class FooBar(YAMLObject):
        yaml_tag = u'!foobar'
        # we need to define a constructor since the default value of data is a AnsibleMapping.
        # __new__ is not available in Python3.
        # def __new__(cls, data):
        #     return super(YAMLObject, cls).__new__(cls)

        def __init__(self, data):
            self.data = data

    foo_bar_loader = AnsibleConstructor(None, ['foo', 'bar'])

# Generated at 2022-06-13 07:33:40.180481
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    test_case_1 = u'$ANSIBLE_VAULT;1.1;AES256 3435363234613564363935643461643439653835643934376238626463616239666131643166643034 3435363236633565363335643234346439653835643934376238626463326539666638326431633939 '
    context_mark = u'<string>'
    problem_mark = u'<string>'
    source_code = to_bytes(test_case_1)
    node = yaml.nodes.ScalarNode(u'tag:yaml.org,2002:str', source_code, start_mark=None, end_mark=None)
    ac = AnsibleConstructor()
    ret = ac.construct_v

# Generated at 2022-06-13 07:33:40.810517
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    pass

# Generated at 2022-06-13 07:33:50.781365
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.yaml.loader import AnsibleLoader
    import os
    import sys

    loader = DataLoader()
    file = os.path.join('test', 'data', 'construct_mapping.yml')
    file = loader.path_dwim_relative(loader._basedir, './', '', file)

    with open(file, 'rb') as test_file:
        all_data = test_file.read()
        data = AnsibleLoader(all_data, file, vault_secrets=[], vault_password_file=None)
        # pyyaml's dump method converts unicode strings to strings

# Generated at 2022-06-13 07:33:59.527881
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    from ansible.parsing.yaml import objects
    mapping = AnsibleConstructor.construct_mapping(
        None, {'__ansible_pos': (None, 1, 2), 'k1': 'v1', 'k2': 'v2', 'k3': 'v3'})
    assert isinstance(mapping, objects.AnsibleMapping)
    assert mapping.ansible_pos == (None, 1, 2)
    assert mapping['k1'] == 'v1'
    assert mapping['k2'] == 'v2'
    assert mapping['k3'] == 'v3'
    assert len(mapping) == 3



# Generated at 2022-06-13 07:34:26.124361
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():

    class TestAnsibleConstructor(AnsibleConstructor):
        def __init__(self):
            self.flattened_map = None
            self.construct_mapping_called = 0

        def flatten_mapping(self, node):
            self.flattened_map = node

        def construct_mapping(self, node, deep=False):
            self.construct_mapping_called += 1
            return {'construct_mapping_called': self.construct_mapping_called}

    test_constructor = TestAnsibleConstructor()
    result = test_constructor.construct_yaml_map(
        yaml.nodes.MappingNode(tag=u'tag:yaml.org,2002:map', value=[]))

    assert isinstance(result, AnsibleMapping)
    assert hasattr

# Generated at 2022-06-13 07:34:32.593863
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    document = """
        a: 1
        b: 2
        c: 3
        """

    # the document is loaded as a python object
    doc_obj = yaml.load(document, Loader=AnsibleConstructor)

    assert isinstance(doc_obj, dict)

    assert sorted(doc_obj.keys()) == ['a', 'b', 'c']

    assert doc_obj['a'] == 1
    assert doc_obj['b'] == 2
    assert doc_obj['c'] == 3



# Generated at 2022-06-13 07:34:40.013143
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.loader import AnsibleLoader
    import yaml


# Generated at 2022-06-13 07:34:49.177351
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    import os
    import sys
    import json
    from ansible.parsing.yaml.loader import AnsibleLoader

    ansible_constructor = AnsibleConstructor()

    d = {'foo':'bar', 'baz':'goober'}

    # pass it through YAML back to python
    s = AnsibleLoader(d, file_name=os.path.basename(__file__)).get_single_data()

    # check if the ansible_pos attributes were set
    s = json.loads(json.dumps(s, default=lambda o: o.__dict__))
    assert s['ansible_pos'] == (os.path.basename(__file__), 0, 0)

# Generated at 2022-06-13 07:34:58.480204
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from ansible.vars.unsafe_proxy import wrap_var
    import yaml
    from types import GeneratorType

    # Empty sequence, no aliases.
    test_data = "\n-\n-\n"
    result = yaml.load(test_data, Loader=AnsibleConstructor)
    assert isinstance(result, list)
    assert len(result) == 0

    # Empty sequence with aliases.
    test_data = "\n- &a\n- *a\n"
    result = yaml.load(test_data, Loader=AnsibleConstructor)
    assert isinstance(result, list)
    assert len(result) == 0

    # Ordinary sequence, no aliases.
    test_data = "\n- foo\n- bar\n"

# Generated at 2022-06-13 07:35:09.766008
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleUnsafeText

    tests = [
        # !unsafe
        (u'!unsafe', dict(tag="tag:yaml.org,2002:str", value=u'!unsafe')),
        (u'!unsafe null', dict(tag="tag:yaml.org,2002:null", value=None)),
        (u'!unsafe true', dict(tag="tag:yaml.org,2002:bool", value=True)),
        (u'!unsafe false', dict(tag="tag:yaml.org,2002:bool", value=False)),
    ]


# Generated at 2022-06-13 07:35:21.066396
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from ansible.parsing.yaml.objects import AnsibleUnsafe

    # Add two constructors to the class AnsibleConstructor: one for a
    # !yaml/dict tag, and the other for a !yaml/python/dict tag.  Use
    # the constructor we're testing (construct_yaml_unsafe) as the
    # construction function.  This lets us make sure the result of the
    # function under test is correct.
    AnsibleConstructor.add_constructor(
        u'!yaml/dict',
        AnsibleConstructor.construct_yaml_unsafe)

    AnsibleConstructor.add_constructor(
        u'!yaml/python/dict',
        AnsibleConstructor.construct_yaml_unsafe)

    # Create an instance of our yaml parser
    constructor = Ansible

# Generated at 2022-06-13 07:35:32.510191
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.dataloader import DataLoader

    data = """
foo: bar
fuz: baz
"""
    loader = AnsibleLoader(data, file_name='/tmp/foo.yml')
    a = loader.get_single_data()

    assert isinstance(a, dict)
    assert isinstance(a['foo'], AnsibleUnicode)
    assert isinstance(a['fuz'], AnsibleUnicode)

    assert a['foo'] == 'bar'
    assert a['fuz'] == 'baz'



# Generated at 2022-06-13 07:35:38.778120
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    # This is a way to test private class methods
    import types
    import sys
    import io
    import yaml
    sys.modules['yaml'].SafeLoader.add_multi_constructor(u'!unsafe', AnsibleConstructor.construct_yaml_unsafe)

    test_yaml = u'''
a: !unsafe 1
b: !unsafe 1
c: !unsafe
  - 1
  - 2
'''

    test_yaml_obj = yaml.load(test_yaml, Loader=yaml.SafeLoader)

    assert test_yaml_obj['a'].data == 1

# Generated at 2022-06-13 07:35:50.738749
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    # initialize vault
    vault = VaultLib(secrets=['secret'])
    # initialize class
    ansible_constructor = AnsibleConstructor(vault_secrets=['secret'])
    # encrypt plaintext
    ciphertext_data = vault.encrypt(b'foo')
    # create node
    node = MappingNode(tag=u'tag:yaml.org,2002:str', value=ciphertext_data, start_mark=None, end_mark=None, flow_style=False)
    # call method
    ansible_vault_encrypted_unicode = ansible_constructor.construct_vault_encrypted_unicode(node)
    # assert
    assert ansible_vault_encrypted_unicode.ciphertext_data == ciphertext_data
    assert ansible_vault_encrypted_unicode

# Generated at 2022-06-13 07:36:29.155554
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import sys
    import collections
    import base64

    from yaml.nodes import ScalarNode
    from yaml.constructor import ConstructorError
    
    from ansible.vars.unsafe_proxy import wrap_var
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    if sys.version_info < (2, 7):
        import unittest2 as unittest
    else:
        import unittest

    class TestAnsibleConstructor_construct_vault_encrypted_unicode(unittest.TestCase):

        def setUp(self):
            self.ac = AnsibleConstructor()
            self.ac._vaults['default'] = VaultLib({"password": "pass"})

            # set to vault format version 2

# Generated at 2022-06-13 07:36:37.703124
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    import sys
    import os
    import tempfile
    import yaml

    if os.name == 'nt':
        # os.chmod is not available on Windows
        sys.exit(0)

    base_dir = tempfile.mkdtemp()
    base_dir_old_mode=0o700
    base_dir_new_mode=0o600
    module_dir_old_mode=0o700

    tmp_dir= os.path.join(base_dir, 'some_tmp_dir')
    yml_file_name= os.path.join(tmp_dir, 'file.yml')

    os.mkdir(tmp_dir, base_dir_old_mode)
    os.chmod(base_dir, base_dir_old_mode)

# Generated at 2022-06-13 07:36:48.404029
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():

    yaml_str = u"{a: {b: c, d: e}, f: g}\n"

    try:
        data = yaml.load(yaml_str, Loader=AnsibleConstructor)
    except Exception as e:
        assert False, e

    assert isinstance(data, AnsibleMapping)
    assert data == {u'a': {u'b': u'c', u'd': u'e'}, u'f': u'g'}

    # test duplicate dict values by changing the yaml string
    yaml_str = u"{a: {b: c, d: e, f: g}, f: g}\n"

    try:
        data = yaml.load(yaml_str, Loader=AnsibleConstructor)
    except Exception as e:
        assert False, e

# Generated at 2022-06-13 07:36:51.801117
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from ansible.parsing.yaml.dumper import AnsibleDumper

    s = "{foo: {bar: [1,2]}}"
    node = yaml.compose(s)
    p = yaml.nodes.MappingNode(u'tag:yaml.org,2002:python/dict', [])
    ac = AnsibleConstructor()
    ac.construct_yaml_unsafe(node)

# Generated at 2022-06-13 07:36:57.440780
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    # constructor = AnsibleConstructor(node_class=AnsibleConstructor)
    # print(constructor)
    print(AnsibleConstructor)

if __name__ == '__main__':
    test_AnsibleConstructor_construct_yaml_seq()

# Generated at 2022-06-13 07:37:10.501206
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from ansible.parsing.yaml.loader import AnsibleLoader

    loader = AnsibleLoader(None, None)
    constructor = AnsibleConstructor()

    # normal list
    test_list1 = loader.construct_yaml_seq(yaml.nodes.SequenceNode(
        tag='tag:yaml.org,2002:seq',
        value=[yaml.nodes.ScalarNode(tag=u'tag:yaml.org,2002:str', value='foo'), yaml.nodes.ScalarNode(tag=u'tag:yaml.org,2002:str', value='bar'), yaml.nodes.ScalarNode(tag=u'tag:yaml.org,2002:str', value='baz')],
        flow_style=True))

# Generated at 2022-06-13 07:37:16.360318
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    ansibleconstructor = AnsibleConstructor()

    vault = VaultLib()
    vault_encrypted_unicode = vault.encrypt(b"test")

    node = AnsibleVaultEncryptedUnicode(vault_encrypted_unicode.encode('utf-8'))
    result = ansibleconstructor.construct_vault_encrypted_unicode(node)

    assert(vault_encrypted_unicode == result)

# Generated at 2022-06-13 07:37:22.222632
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.module_utils._text import to_text, to_bytes

    yaml = YAML(typ='safe')
    yaml.constructor.add_constructor('!unsafe',
                                     yaml.constructor.construct_yaml_unsafe)
    yaml.constructor.add_constructor(
        u'!vault',
        yaml.constructor.construct_vault_encrypted_unicode)
    yaml.constructor.add_constructor(u'!vault-encrypted',
                                     yaml.constructor.construct_vault_encrypted_unicode)


# Generated at 2022-06-13 07:37:33.056912
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    constructor = AnsibleConstructor()
    mapping_node = MappingNode()
    mapping_node.value = []
    mapping_node.start_mark.line = 1
    mapping_node.start_mark.column = 1
    mapping_node.start_mark.name = 'foo.yaml'
    result = constructor.construct_yaml_map(mapping_node)
    assert hasattr(result, 'ansible_pos')
    assert result.ansible_pos[0] == 'foo.yaml'
    # line number where the previous token has ended (plus empty lines)
    assert result.ansible_pos[1] == 1
    # Add one so that the first line is line 1 rather than line 0
    assert result.ansible_pos[2] == 2


# Generated at 2022-06-13 07:37:37.209539
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    import sys
    import unittest
    import yaml

    class TestAnsibleConstructor(unittest.TestCase):

        def test_construct_yaml_str(self):
            if sys.version_info[0] == 2:
                self.assertEqual(
                    type(yaml.load(u"foo: bar", Loader=AnsibleConstructor)),
                    dict)
                self.assertEqual(
                    type(yaml.load(u"foo: bar", Loader=AnsibleConstructor)["foo"]),
                    AnsibleUnicode)
                self.assertEqual(
                    type(yaml.load(u"foo: 42", Loader=AnsibleConstructor)["foo"]),
                    AnsibleUnicode)