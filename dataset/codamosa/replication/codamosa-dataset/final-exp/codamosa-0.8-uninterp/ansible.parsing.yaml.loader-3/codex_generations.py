

# Generated at 2022-06-13 07:38:35.606747
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    import os

    # get resources directory
    resource_dir = os.path.join(os.path.dirname(__file__), 'resources')

    # get test yaml file
    test_file = os.path.join(resource_dir, 'good.yml')

    # create the loader
    stream = open(test_file, 'r')
    loader = AnsibleLoader(stream)

    # check that loader works
    assert loader

    # cleanup
    stream.close()

# Generated at 2022-06-13 07:38:37.747978
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert issubclass(AnsibleLoader, Resolver)
    assert issubclass(AnsibleLoader, AnsibleConstructor)

# Generated at 2022-06-13 07:38:46.673425
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.yaml.objects import AnsibleSequence


    # test simple list
    sample_yaml_data = '''
    - 1
    - 2
    - 3
    '''

    yaml_obj = AnsibleLoader(sample_yaml_data).get_single_data()
    assert isinstance(yaml_obj, AnsibleSequence)
    assert len(yaml_obj) == 3

    # test simple dict
    sample_yaml_data = '''
    a: 1
    b: 2
    c: 3
    '''

    yaml_obj = AnsibleLoader(sample_yaml_data).get_single_data()
    assert isinstance(yaml_obj, AnsibleMapping)

# Generated at 2022-06-13 07:38:56.161953
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    def get_yaml_config(config):

        config = """\
---
%s
""" % config

        loader = AnsibleLoader(config)
        return loader.get_single_data()

    # Test the load of a config with a dynamic hash
    config = """\
log:
  name: [first, second]
  level: debug
"""
    data = get_yaml_config(config)
    assert len(data['log']) == 2
    assert data['log'][0]['name'] == 'first'
    assert data['log'][0]['level'] == 'debug'
    assert data['log'][1]['name'] == 'second'
    assert data['log'][1]['level'] == 'debug'

    # Test the load of a config with a dynamic hash

# Generated at 2022-06-13 07:38:56.799542
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    pass

# Generated at 2022-06-13 07:39:06.178770
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    data = """
    - hosts: all
      tasks:
      - name: test
        command: /bin/something
        register: result
        changed_when: "result.rc != 0"
    """

    loader = AnsibleLoader(None)
    loader.compose_document(data)
    assert loader.get_single_data() == dict(
        hosts='all',
        tasks=[dict(
            name='test',
            command='/bin/something',
            changed_when='result.rc != 0',
            register='result'
        )]
    )

# Generated at 2022-06-13 07:39:06.933468
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader

# Generated at 2022-06-13 07:39:09.310519
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    stream = '''
        this is a string
        this is another string
        '''

    AnsibleLoader(stream)

# Generated at 2022-06-13 07:39:10.683503
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    AnsibleLoader(stream=None)

# Generated at 2022-06-13 07:39:21.192362
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import io
    stream = io.BytesIO(b"""
        - hosts: 127.0.0.1
          roles:
            - common
        - hosts: 127.0.0.2
          roles:
            - webserver
        """)
    loader = AnsibleLoader(stream)
    data = list(loader)
    assert data, "Empty data"
    assert data == [{'hosts': '127.0.0.1', 'roles': ['common']}, {'hosts': '127.0.0.2', 'roles': ['webserver']}], "Incorrect data"

# Generated at 2022-06-13 07:39:38.363666
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # No vault_secrets
    loader = AnsibleLoader(None)
    result = loader.get_single_data()
    assert result is None

    # vault_secrets is list of dictionaries
    vault_secrets = [{'my_key': 'my_value'}]
    loader = AnsibleLoader(None, vault_secrets=vault_secrets)
    result = loader.get_single_data()
    assert result == {'my_key': 'my_value'}

    # vault_secrets is a unicode string
    vault_secrets = u'{my_key: my_value}'
    loader = AnsibleLoader(None, vault_secrets=vault_secrets)
    result = loader.get_single_data()
    assert result == {'my_key': 'my_value'}

# Generated at 2022-06-13 07:39:39.886663
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    loader = AnsibleLoader(sys.stdin)
    assert loader

# Generated at 2022-06-13 07:39:42.356135
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    stream = """
---
:var: val
"""
    loader = AnsibleLoader(stream)
    loader.get_data()

# Generated at 2022-06-13 07:39:42.826244
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    pass

# Generated at 2022-06-13 07:39:43.736561
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    a = AnsibleLoader(None)
    assert a is not None



# Generated at 2022-06-13 07:39:46.143122
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader(): # pylint: disable=missing-docstring
    ansible_loader = AnsibleLoader("")
    assert(hasattr(ansible_loader, '_compose_node'))

# Generated at 2022-06-13 07:39:46.697757
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    pass

# Generated at 2022-06-13 07:39:47.757797
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    pass


# Generated at 2022-06-13 07:39:58.883152
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.constructor import (_load_unsafely_without_spec,
                                                  _load_yaml_guess_indent)

    # unmarshal correctly
    yaml = '''
---
foo: bar
baz: [1, 2]
'''
    assert AnsibleLoader(yaml).get_single_data() == \
           _load_yaml_guess_indent(yaml) == \
           _load_unsafely_without_spec(yaml) == \
           {'foo': 'bar', 'baz': [1, 2]}

    # no parsing issue
    yaml = '''
---
foo: bar
  baz:
    quux: 1
'''

# Generated at 2022-06-13 07:40:01.357891
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert hasattr(AnsibleLoader, "add_constructor")
    assert hasattr(AnsibleLoader, "add_multi_constructor")


# Generated at 2022-06-13 07:40:11.387376
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    TEST_DATA = b"""
list:
 - foo
 - 1
 - [baz, qux]
 - {a: 1, b: 2}
 - [bar, {a: 1, b: 2}, [baz, qux]]
"""
    import io

    ansible_loader = AnsibleLoader(io.BytesIO(TEST_DATA))
    ansible_loader_type = type(ansible_loader)
    assert issubclass(ansible_loader_type, Resolver), 'failed to find Resolver class'
    assert issubclass(ansible_loader_type, AnsibleConstructor), 'failed to find AnsibleConstructor class'

    ansible_loader.get_single_data()

if __name__ == '__main__':
    test_AnsibleLoader()

# Generated at 2022-06-13 07:40:19.744626
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import io
    import sys

    input_str = '''
    ---
    - hosts: localhost
      gather_facts: no
      tasks:
      - name: install xfsprogs
        yum:
          name: xfsprogs
          state: latest
    '''

    file_name = 'default'

    if sys.version_info[0] >= 3:
        stream = io.StringIO(input_str)
    else:
        stream = io.BytesIO(input_str)

    AnsibleLoader(stream, file_name)

# Generated at 2022-06-13 07:40:21.786088
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    def test_Class():
        assert AnsibleLoader
    test_Class()


__all__ = ['AnsibleLoader']

# Generated at 2022-06-13 07:40:26.944530
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from collections import namedtuple
    AnsibleLoader.add_constructor('!test',
            lambda loader, node: namedtuple('Test', loader.construct_scalar(node))('test'))

    data = AnsibleLoader('''---
        !test
    ''').get_single_data()
    assert data.test == 'test'

# Generated at 2022-06-13 07:40:38.522882
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    test_string = """
    - hosts: localhost
      gather_facts: False
      tasks:
      - name: time sync test
        block:
        - name: using service module
          service: name=ntp state=started enabled=yes
        - name: using command module
          command: ntpdate 0.asia.pool.ntp.org
          register: ntp_check
          ignore_errors: yes
        - debug: msg="The time was not synchronized"
          when: ntp_check.rc != 0
    """
    #import pdb; pdb.set_trace()
    loader = AnsibleLoader(test_string)
    data = loader.get_single_data()
    assert data['tasks'][0]['block'][1]['ignore_errors'] is True

# Generated at 2022-06-13 07:40:43.941550
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    '''
    This test case is used to check if AnsibleLoader can be created and if the
    Resolver of the class is as expected
    '''
    # create an AnsibleLoader object and then test it
    Aloader = AnsibleLoader(stream='test_stream')
    # check if the Resolver of the AnsibleLoader is as expected
    assert hasattr(Aloader, 'Resolver') and Aloader.Resolver == Resolver

# Generated at 2022-06-13 07:40:48.620328
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    """
    # Create instance of class AnsibleLoader
    """
    ansible_loader = AnsibleLoader(stream=None)

    assert ansible_loader is not None

# Generated at 2022-06-13 07:40:58.481156
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import ssl
    if getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context # pylint: disable=protected-access
    import urllib2
    loader_file = open('library/ANSIBLE_MODULE_ARGS', 'r')
    loader_file_str = loader_file.read()
    loader_file.close()
    response = urllib2.urlopen('https://raw.github.com/ansible/ansible/devel/lib/ansible/module_utils/basic.py')
    loader_stream = response.read()
    loader = AnsibleLoader(loader_stream)
    data = loader.get_single_data()
    assert("check_args" in data)

# Generated at 2022-06-13 07:41:09.885523
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import textwrap

    src = '''
    # A simple playbook with one play and some variables
    - hosts: all
      user: root
      vars:
        http_port: 80
        max_clients: 200
      tasks:
      - name: ensure apache is at the latest version
        yum: name=httpd state=latest
      - name: write the apache config file
        template: src=/srv/httpd.j2 dest=/etc/httpd.conf
        notify:
        - restart apache
        - restart memcached
    '''


# Generated at 2022-06-13 07:41:10.772887
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    ld = AnsibleLoader(None)
    assert ld != None

# Generated at 2022-06-13 07:41:30.409434
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import os
    import sys

    # creating a minimal yaml file
    if os.path.exists('/tmp/test.yml'):
        os.remove('/tmp/test.yml')
    with open('/tmp/test.yml', 'w') as f:
        f.write('''---
- hosts: all
  gather_facts: False
  tasks:
    - name: "test"
      ping:
''')
        f.close()

    # loading file using AnsibleLoader
    loader = AnsibleLoader(open('/tmp/test.yml'), 'test.yml')
    yaml_data = loader.get_single_data()

    # checking output
    if sys.version_info.major >= 3:
        if yaml_data['hosts'] != 'all':
            raise Exception

# Generated at 2022-06-13 07:41:34.585336
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader('')
    assert loader.stream == ''
    assert loader.file_name is None
    assert loader.vault_secrets is None
    assert loader.file_name is None
    assert loader.file_name is None
    assert loader.vault_secrets is None

# Generated at 2022-06-13 07:41:35.744462
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader  # silence pyflakes

# Generated at 2022-06-13 07:41:37.928124
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # type: () -> None
    # If constructor for class "AnsibleLoader" fails,
    # the object does not have attribute "construct_yaml_map"
    AnsibleLoader(None)
    assert hasattr(AnsibleLoader, "construct_yaml_map")

# Generated at 2022-06-13 07:41:38.782927
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    l = AnsibleLoader('foo')
    assert(l.stream == 'foo')

# Generated at 2022-06-13 07:41:39.317015
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    pass

# Generated at 2022-06-13 07:41:42.513944
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None)
    assert hasattr(loader, 'vault_secrets')
    assert hasattr(loader, '_vault_secrets_names')

# Generated at 2022-06-13 07:41:47.105636
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    yaml_str = '''
    hello:
      - world
      - from
      - ansible
    '''
    loader = AnsibleLoader(yaml_str)
    assert loader.get_single_data() == {'hello': ['world', 'from', 'ansible']}

# Generated at 2022-06-13 07:41:55.136306
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from ansible.module_utils.common.yaml import HAS_LIBYAML, Parser
    from io import StringIO
    # Create a fake stream
    stream = StringIO()
    stream.write("---\n")
    stream.write("- hosts: localhost\n")
    stream.write("  connection: local\n")
    stream.write("  tasks:\n")
    stream.write("  - name: hello world\n")
    stream.write("    debug:\n")
    stream.write("      msg: \"hello world\"\n")
    stream.seek(0)

    if HAS_LIBYAML:
        loader = AnsibleLoader(stream=stream)
    else:
        from yaml.composer import Compos

# Generated at 2022-06-13 07:42:01.139243
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    valid = '''
        - hosts: all
          gather_facts: False
          vars:
            favorite:
            - apples
            - oranges
    '''
    loader = AnsibleLoader(valid)
    result = loader.get_single_data()
    assert isinstance(result, list)
    assert len(result) == 1
    assert isinstance(result[0], dict)
    assert result[0].get('hosts') == 'all'
    assert result[0].get('gather_facts') == False
    assert result[0].get('vars') == dict(favorite=['apples', 'oranges'])

    invalid = '''
        - hosts: all
          user: "{{ foo }}"
    '''
    loader = AnsibleLoader(invalid)
    result = loader.get_single_data()


# Generated at 2022-06-13 07:42:32.322167
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    valid_yaml_snippet = "\n- hosts: localhost\n" \
                         "  gather_facts: no\n" \
                         "  connection: local\n" \
                         "  tasks:\n" \
                         "    - name: debug\n" \
                         "      debug:\n" \
                         "        msg: '{{ ansible_os_family }}'"
    ansible_loader = AnsibleLoader(valid_yaml_snippet)
    assert len(list(ansible_loader.get_data())) == 1  # pylint: disable=no-member

# Generated at 2022-06-13 07:42:42.762775
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import yaml
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.data import AnsibleMapping
    from yaml.resolver import Resolver
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from ansible.module_utils.common.yaml import Parser
    a = Parser('[1,2,3]')
    assert(list(a) == [1,2,3])
    b = AnsibleConstructor(None)
    c = Resolver()
    if HAS_LIBYAML:
        assert(AnsibleLoader.__bases__ == (Parser, AnsibleConstructor, Resolver))
    d = AnsibleLoader('string: hello')

# Generated at 2022-06-13 07:42:45.037889
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    """
    Tests if AnsibleLoader instantiates properly
    """

    loader = AnsibleLoader(None, os.devnull)

# Generated at 2022-06-13 07:42:55.147758
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    """
    >>> from ansible import constants as C
    >>> from ansible.utils.vars import combine_vars
    >>> from ansible.vars import VariableManager
    >>> from ansible.parsing.vault import VaultLib
    >>> from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    >>> from ansible.parsing.dataloader import DataLoader
    >>> from io import StringIO
    >>> my_data = StringIO("""

# Generated at 2022-06-13 07:42:58.633040
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    module = AnsibleConstructor()
    assert isinstance(module, AnsibleConstructor)

# Generated at 2022-06-13 07:43:04.073101
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    data = '''
    - hosts: all
      tasks:
        - name: testing123
          command: whoami
    '''
    loader = AnsibleLoader(data)
    assert loader.compose_document() == {"hosts": "all", "tasks": [{"name": "testing123", "command": "whoami"}]}

# Generated at 2022-06-13 07:43:04.687534
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader

# Generated at 2022-06-13 07:43:10.332399
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    data = '''
- hosts: localhost
  tasks:
  - name: silly echo example
    shell: echo {{ item }}
    with_items:
       - dog
       - cat
       - chinchilla
- hosts: remote
  tasks:
  - name: silly echo example
    shell: echo {{ item }}
    with_items:
       - dog
       - cat
       - chinchilla
'''
    loader = AnsibleLoader(data)
    for x in loader:
        pass

# Generated at 2022-06-13 07:43:25.355679
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode, AnsibleMapping
    from ansible.vars.unsafe_proxy import wrap_var

    test_string = u'foo: bar\n'

    # test basic constructor
    loader = DataLoader()
    data = loader.load(test_string)
    assert data == dict(foo='bar')

    # test with an empty vault secret
    loader = DataLoader(vault_secrets=(None,))
    data = loader.load(test_string)
    assert data == dict(foo='bar')

    # test with a vault secret
    data = test_string.encode('utf-8')
    ansible_vault_encrypted_unicode = wrap_var

# Generated at 2022-06-13 07:43:32.422114
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    yaml_str = '''
---
- hosts: localhost
  connection: local
  tasks:
  - name: subscribe the "changed" event.
    debug:
      msg: "event has been fired."
    register: event_result
    tags: test
    listen: "ansible_module_test"
  - name: fire the event.
    debug:
      msg: "this is from task."
    tags: test
    fire_event:
      event: "ansible_module_test"'''
    AnsibleLoader(yaml_str)

# Generated at 2022-06-13 07:44:20.781669
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    data = '''
    a: "{{ var }}"
    b: "{% if a == '1' %}{{ foo }}{% else %}{{ bar }}{% endif %}"
    c: "a{% foo %}b"
    d: "{% if a == '1' %}x{% else %}y{% endif %}"
    '''

    class OptionsModule(object):
        def __init__(self, check=False):
            self.check = check
            self.tags = []

    class HostVarsVaultSecretModule(object):
        def __init__(self):
            self.hostvars = {
                'other_host': dict(
                    ansible_ssh_pass='secret_pass',
                ),
            }
            self.vault_password = 'vault_pass'

    loader

# Generated at 2022-06-13 07:44:29.905571
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleSequence, AnsibleMapping
    from ansible.module_utils.common.yaml import HAS_LIBYAML

    stream = u'''
    one: two
    three: four
    five:
      six: seven
    eight:
      - nine
      - ten
    eleven: "{{ 'one' if True else 'zero'}}"
    '''

    if HAS_LIBYAML:
        my_loader = AnsibleLoader(stream)
    else:
        my_loader = AnsibleLoader(stream.encode('utf8'))

    my_data = my_loader.get_single_data()

    assert isinstance(my_data, AnsibleMapping)
    assert isinstance(my_data.get('five'), AnsibleMapping)


# Generated at 2022-06-13 07:44:41.092068
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    test_data = '''
---
# No.1
- name: test
- name: test
- name: test

# No.2
- include: test.yml
- include: test.yml

# No.3
- include_vars:
  - test.yml
  - test.yml

# No.4
- include_tasks: test.yml
- include_tasks: test.yml
'''
    data = AnsibleLoader(test_data)

# Generated at 2022-06-13 07:44:41.695773
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    pass

# Generated at 2022-06-13 07:44:49.745262
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import json
    import os
    import tempfile

    from ansible.parsing.vault import VaultSecret

    test_string = '{"a": 1, "b": 2, "c": {"d": 4}}'
    fd, json_file = tempfile.mkstemp()
    try:
        os.write(fd, test_string.encode('utf-8'))
        loader = AnsibleLoader(open(json_file, 'rb'), vault_secrets=[VaultSecret('abcd1234')])
        data = loader.get_single_data()
        assert data == json.loads(test_string)
    finally:
        os.close(fd)
        os.unlink(json_file)

# Generated at 2022-06-13 07:44:58.013034
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    try:
        dummy_stream = open('dummy_file_name', 'w')
    except Exception as e:
        assert False, "Failed to create dummy_stream: %s" % to_native(e)

    try:
        loader = AnsibleLoader(dummy_stream)
    except Exception as e:
        assert False, "Failed to create instance of AnsibleLoader: %s" % to_native(e)

    try:
        dummy_stream.close()
    except Exception as e:
        assert False, "Failed to close dummy_stream: %s" % to_native(e)

# Generated at 2022-06-13 07:45:04.982107
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml import load
    from io import StringIO

    loader = AnsibleLoader(StringIO(''), file_name='<string>')
    assert(isinstance(loader, (Parser, Reader, Scanner, Composer, AnsibleConstructor, Resolver)))
    data = load('', Loader=AnsibleLoader)
    assert(isinstance(data, list))

# Generated at 2022-06-13 07:45:08.419130
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    data = '''
        foo: 1
        bar:
          baz: 1
          foo: 2
        baz: 3
    '''

    loader = AnsibleLoader(data)
    for i in loader:
        print(i)

# Generated at 2022-06-13 07:45:20.515783
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.errors import AnsibleParserError
    from io import BytesIO

    obj = AnsibleLoader(BytesIO(u'test: &id001\n  foo: bar\n  foo: baz\n\nobj: *id001\n')).get_single_data()
    assert isinstance(obj, dict)
    assert obj == {'test': {'foo': 'baz'}, 'obj': {'foo': 'baz'}}


# Generated at 2022-06-13 07:45:23.248546
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.module_utils.common.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleUnicode
    loader = AnsibleLoader(b'hello: world\n', file_name='string')
    data = loader.get_single_data()
    assert isinstance(data['hello'], AnsibleUnicode)
    assert data['hello'] == u'world'

# Generated at 2022-06-13 07:47:01.972833
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.errors import AnsibleParserError


# Generated at 2022-06-13 07:47:10.533994
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import os
    import re
    import tempfile

    from ansible import constants as C

    # Create a temporary YAML file.
    (fd, yaml_file) = tempfile.mkstemp()
    os.close(fd)
    contents = None

# Generated at 2022-06-13 07:47:12.513159
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # The AnsibleLoader class is constructed by a base class.
    # Constructing it here to will throw an error
    pass

# Generated at 2022-06-13 07:47:14.934881
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(file_name="blah")
    assert loader.file_name == "blah"
    assert loader.vault_secrets == None

# Generated at 2022-06-13 07:47:25.434342
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # Create AnsibleLoader object and test it
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret


# Generated at 2022-06-13 07:47:36.968851
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.parsing.vault import VaultLib  # pylint: disable=unused-import

    test_data = '''
a: 1
b:
  - 2
  - 3
c:
  k1: v1
  k2: v2
'''
    loader = AnsibleLoader(test_data)
    data = loader.get_single_data()
    assert isinstance(data, AnsibleMapping)
    assert data.get('a') == 1
    assert isinstance(data.get('b'), AnsibleSequence)
    assert data.get('b')[0] == 2

# Generated at 2022-06-13 07:47:40.582138
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    class __fake_stream(object):
        def read(*args, **kwargs):
            return 'foo: 1\nbar: [2, 3]'
    assert AnsibleLoader(__fake_stream()).get_single_data() == {'foo': 1, 'bar': [2, 3]}

# Generated at 2022-06-13 07:47:46.593570
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import yaml

    with open("test/unit/yaml/default_ansible_loader/test.yaml") as f:
        data = yaml.load(f, Loader=AnsibleLoader)
        assert isinstance(data, dict)
        assert data['a'] == 1
        assert data['b'] == 2
        assert data['c'] == 3
        assert len(data) == 3

# Generated at 2022-06-13 07:47:56.639890
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    '''
    >>> print(AnsibleLoader.__bases__)
    (<class 'ansible.module_utils.common.yaml.reader.Reader'>, <class 'ansible.module_utils.common.yaml.scanner.Scanner'>, <class 'ansible.module_utils.common.yaml.parser.Parser'>, <class 'ansible.module_utils.common.yaml.composer.Composer'>, <class 'ansible.parsing.yaml.constructor.AnsibleConstructor'>, <class 'ansible.module_utils.common.yaml.resolver.Resolver'>)
    '''

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 07:47:57.588929
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader
