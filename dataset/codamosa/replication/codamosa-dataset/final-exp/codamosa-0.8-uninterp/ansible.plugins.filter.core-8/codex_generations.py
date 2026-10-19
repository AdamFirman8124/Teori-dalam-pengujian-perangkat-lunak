

# Generated at 2022-06-22 11:40:43.940561
# Unit test for function do_groupby
def test_do_groupby():
    from ansible.template import JinjaEnvironment
    from collections import namedtuple
    class AnsibleHost(namedtuple('AnsibleHost', ['name', 'ip'])):
        '''a namedtuple to simulate a host'''
        pass

    h1 = AnsibleHost('host_1', '192.168.1.5')
    h2 = AnsibleHost('host_2', '192.168.1.5')
    h3 = AnsibleHost('host_3', '192.168.1.6')
    h4 = AnsibleHost('host_4', '192.168.1.7')
    hosts = [h1, h2, h3, h4]

    env = JinjaEnvironment()
    template = JinjaTemplateModule()
    env.filters['groupby'] = do_groupby
    sorted

# Generated at 2022-06-22 11:40:46.541278
# Unit test for function fileglob
def test_fileglob():
    assert ['/tmp/a.txt', '/tmp/b.txt'] == fileglob('/tmp/*.txt')
    assert [] == fileglob('/tmp/*.jpg')



# Generated at 2022-06-22 11:40:59.950465
# Unit test for function extract
def test_extract():

    ipv4_interface = {
        'name': 'eth0',
        'ipv4': {
            'address': [
                {
                    'ip': '192.168.1.1',
                    'prefix_length': 24,
                },
                {
                    'ip': '192.168.2.1',
                    'prefix_length': 24,
                },
            ],
        },
    }
    assert extract('name', ipv4_interface) == 'eth0'
    assert extract('ip', 'ipv4', 'address', ipv4_interface) == '192.168.1.1'
    assert extract('ip', 'ipv4', 'address', 1, ipv4_interface) == '192.168.2.1'

# Generated at 2022-06-22 11:41:03.692344
# Unit test for function fileglob
def test_fileglob():
    assert fileglob('/non/existing/path') == []
    assert fileglob('') == []
    assert fileglob('/etc/passwd') == ['/etc/passwd']



# Generated at 2022-06-22 11:41:10.813190
# Unit test for function extract
def test_extract():
    assert extract({"a": {"b": {"c": "d"}}}, "a", {"a": {"b": {"c": "d"}}}) == {"b": {"c": "d"}}
    assert extract({"a": {"b": {"c": "d"}}}, "a", {"a": {"b": {"c": "d"}}}, "b") == {"c": "d"}
    assert extract({"a": {"b": {"c": "d"}}}, "a", {"a": {"b": {"c": "d"}}}, ["b", "c"]) == "d"
    assert extract({"a": {"b": {"c": "d"}}}, "a", {"a": {"b": {"c": "d"}}}, morekeys=["b", "c"]) == "d"

# Generated at 2022-06-22 11:41:21.704801
# Unit test for function fileglob
def test_fileglob():
    # Test normal strings
    assert fileglob("foo") == ["foo"]
    assert fileglob("foo*") == []
    assert fileglob("*foo*") == []
    assert fileglob("/bin/ls") == ["/bin/ls"]

    # Test unicode strings
    assert fileglob(u"foo") == ["foo"]
    assert fileglob(u"foo*") == []
    assert fileglob(u"*foo*") == []
    assert fileglob(u"/bin/ls") == ["/bin/ls"]

    # Test string as a list of characters
    assert fileglob(list("foo")) == ["foo"]
    assert fileglob(list("foo*")) == []
    assert fileglob(list("*foo*")) == []

# Generated at 2022-06-22 11:41:24.785781
# Unit test for function fileglob
def test_fileglob():
    assert filter_loader.filters()["fileglob"]('/does/not/exist/*') == []
    assert filter_loader.filters()["fileglob"]('/bin/*') != []


# Generated at 2022-06-22 11:41:37.011117
# Unit test for function regex_replace
def test_regex_replace():
    res = regex_replace("foobar", "^foo", "food")
    assert res == "foodbar"
    res = regex_replace("foobarbaz", "baz$", "bonanza", ignorecase=True)
    assert res == "foobarbonanza"
    res = regex_replace("foo\nbar", ".", "X", multiline=True)
    assert res == "XXX\nXXX"
    res = regex_replace("foo\nbar", ".", "X", ignorecase=True, multiline=True)
    assert res == "XXX\nXXX"
    res = regex_replace("foobar", "^foo", "food")
    assert res == "foodbar"
    res = regex_replace("foobarbaz", "baz$", "bonanza", ignorecase=True)

# Generated at 2022-06-22 11:41:38.822728
# Unit test for function mandatory
def test_mandatory():
    assert mandatory('foo') == 'foo'
    assert mandatory(AnsibleUndefined(name='blah')) == 'blah'



# Generated at 2022-06-22 11:41:50.687247
# Unit test for function mandatory
def test_mandatory():
    # test passing in a defined var
    testvar = 'hi'
    assert mandatory(testvar) == 'hi'

    # test passing in an undefined var with a custom message
    testvar = None
    try:
        mandatory(testvar, msg="This is not defined")
    except AnsibleFilterError as e:
        assert "not defined" in to_text(e)
    else:
        assert False, "A failure should have been raised"

    # test passing in an undefined var without a custom message
    testvar = None
    try:
        mandatory(testvar)
    except AnsibleFilterError as e:
        assert "not defined" in to_text(e)
    else:
        assert False, "A failure should have been raised"

    # test passing in a jinja undefined var with a custom message
    testvar = None

# Generated at 2022-06-22 11:42:04.287598
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('abcdefg12345', '\\d+') == '12345'
    assert regex_search('abcdefg12345', '\\d+', '\\g<1>') == ['12345', '12345']
    assert regex_search('abcdefg12345', '\\d+', '\\g<0>') == ['12345', '12345']
    assert regex_search('abcdefg12345', '\\d+', '\\1') == ['12345', '12345']
    assert regex_search('abcdefg12345', '\\d+', '\\1', '\\1') == ['12345', '12345', '12345']

# Generated at 2022-06-22 11:42:05.660172
# Unit test for function fileglob
def test_fileglob():
    return file("/etc/passwd").read()



# Generated at 2022-06-22 11:42:06.216950
# Unit test for function get_hash
def test_get_hash():
    pass



# Generated at 2022-06-22 11:42:13.226090
# Unit test for function get_hash
def test_get_hash():
    d = {'foo': 'bar'}
    assert get_hash(d) == md5s(d)
    assert get_hash(d, hashtype='md5') == md5s(d)
    assert get_hash(d, hashtype='sha1') == checksum_s(d)
    assert get_hash(d, hashtype='sha256') == checksum_s(d, hashfunc='sha256')
    assert get_hash(d, hashtype='sha512') == checksum_s(d, hashfunc='sha512')
    assert get_hash(d, hashtype='none') == checksum_s(d, hashfunc='none')



# Generated at 2022-06-22 11:42:19.752546
# Unit test for function get_hash
def test_get_hash():
    assert get_hash("test string") == '734f05a68bfe7d8abae665fbbd7a1a3b2f3b1fd3'
    assert get_hash("test string", "md5") == '1f4d4c6e2cf6f3cc6d0d9b93e6b4c6e8'



# Generated at 2022-06-22 11:42:31.800794
# Unit test for function regex_search
def test_regex_search():
    #  default test, no named groups
    assert regex_search(
        'john.doe@example.com',
        r'(?P<local>[^@]+)@(?P<domain>[^@]+)',
        '\\g<local>',
        '\\g<domain>',
        ) == ['john.doe', 'example.com']

    #  one named group
    assert regex_search(
        'john.doe@example.com',
        r'(?P<local>[^@]+)@(?P<domain>[^@]+)',
        '\\g<local>',
        '\\2',
        ) == ['john.doe', 'example.com']

    #  some named groups

# Generated at 2022-06-22 11:42:42.520603
# Unit test for function do_groupby
def test_do_groupby():
    import jinja2
    environment = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
    environment.filters['groupby'] = do_groupby
    tmpl = environment.get_template('groupby.j2')
    input_data = {
        'a' : [
            {'group': 'one', 'value': 1},
            {'group': 'one', 'value': 2},
            {'group': 'two', 'value': 3},
        ]
    }
    expected_result = {
        'one': [ (1,'one'), (2,'one') ],
        'two': [ (3,'two') ],
    }
    result = tmpl.render(input_data)
    assert result == expected_result


# Generated at 2022-06-22 11:42:54.437979
# Unit test for function extract
def test_extract():
    try:
        from ansible.compat.tests import unittest
    except:
        import unittest
    from ansible.parsing.tests.test_yaml import YAMLTestData

    class ExtractTest(unittest.TestCase):
        def test_extract_with_dict(self):
            data = {'foo': {'bar': 'baz'}}
            with YAMLTestData('extract.yml', data) as test_data:
                self.assertDictEqual(extract('foo.bar', data), {'_ansible_item_result': True, '_ansible_no_log': False, 'changed': False, 'item': 'baz', 'skipped': False, 'failed': False, 'invocation': {'module_args': 'foo.bar'}})
               

# Generated at 2022-06-22 11:43:04.522573
# Unit test for function regex_search
def test_regex_search():
    assert regex_search("abcabcabcabcabcabcabcabcabc",'(\d+)') == None
    assert regex_search("abcabcabcabcabcabcabcabcabc1",'(\d+)') == '1'
    assert regex_search("abcabcabcabcabcabcabcabcabc1",'(\d+)', '\\1') == ['1']
    assert regex_search("abcabcabcabcabcabcabcabcabc1",'(\d+)', '\\g<1>') == ['1']
    assert regex_search("abcabcabcabcabcabcabcabcabc1",'(\d+)', '\\g<1>','\\1') == ['1','1']
    assert regex_search("abc123xyz",'(?P<digits>\d+)') == '123'

# Generated at 2022-06-22 11:43:11.033442
# Unit test for function subelements
def test_subelements():
    obj = {'x': [{'a': 1, 'b': 2, 'c': 3}, {'a': 4, 'b': 5, 'c': 6}]}

    assert subelements(obj, 'x.a') == [(obj['x'][0], 1), (obj['x'][1], 4)]
    assert subelements(obj, 'x.d', skip_missing=True) == []



# Generated at 2022-06-22 11:43:27.853641
# Unit test for function regex_search
def test_regex_search():
    assert regex_search(
        'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin vulputate tortor eget diam pellentesque  '
        'venenatis id nec nisl. Pellentesque accumsan varius ante, vitae vulputate arcu rhoncus in. ',
        '(vulputate){1,2}', '\\g<1>') == 'vulputate'

# Generated at 2022-06-22 11:43:30.401660
# Unit test for function strftime
def test_strftime():
    now = time.time()
    assert strftime('%Y') == strftime('%Y', now)
    assert strftime('%A') == strftime('%A', now)



# Generated at 2022-06-22 11:43:38.702016
# Unit test for function mandatory
def test_mandatory():
    # Testing Undefined variable
    try:
        ret = mandatory(AnsibleUndefined)
    except AnsibleFilterError:
        pass
    else:
        raise AssertionError(ret)

    # Testing Must fail with a defined variable
    try:
        ret = mandatory({})
    except AnsibleFilterError:
        raise AssertionError(ret)

    # Testing Defined variable
    try:
        ret = mandatory(False)
        assert ret is False
    except AnsibleFilterError:
        raise AssertionError(ret)



# Generated at 2022-06-22 11:43:45.577281
# Unit test for function do_groupby
def test_do_groupby():
    from ansible.compat.tests import unittest
    import itertools

    class TestDoGroupBy(unittest.TestCase):
        class FakeEnvironment(object):
            def getitem(self, value, attribute):
                '''Simple getitem function to simulate jinja2 getitem env'''
                if hasattr(value, '__getitem__') or isinstance(value, dict):
                    return value.__getitem__(attribute)

                raise TypeError('Attribute not found (%s).' % attribute)

        def setUp(self):
            self._getitem = do_groupby.environmentfilter.__globals__['getitem']
            self._dict = do_groupby.environmentfilter.__globals__['dict']
            self._groupby = itertools.groupby


# Generated at 2022-06-22 11:43:50.529652
# Unit test for function do_groupby
def test_do_groupby():
    from jinja2 import DictLoader, Environment
    env = Environment(loader=DictLoader({'template':
                       '{{ ["1a", "2b", "1c", "2a", "3a", "1b", "2c", "3c", "1d", "1e", "2d", "3b"]|sort|groupby(attribute="0") }}'}))
    template = env.get_template('template')
    value = safe_eval(template.render())
    assert value == [('1', ['1a', '1c', '1b', '1d', '1e']), ('2', ['2b', '2a', '2c', '2d']), ('3', ['3a', '3c', '3b'])]


# Generated at 2022-06-22 11:43:54.529594
# Unit test for function regex_escape
def test_regex_escape():
    assert '.' == regex_escape('.', "python")
    assert '\\.' == regex_escape('.', "posix_basic")
    assert '\\\\.' == regex_escape(r'\\.', "posix_basic")


# Generated at 2022-06-22 11:44:04.709116
# Unit test for function do_groupby
def test_do_groupby():
    from ansible import constants as C
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = {"group": Host("127.0.0.1")}
    variable_manager.set_inventory(inventory)
    inventory._variable_manager = variable_manager
    templar = Templar(loader, variables=variable_manager, fail_on_undefined=C.DEFAULT_UNDEFINED_VAR_BEHAVIOR)
    group = templar.do_groupby([1, 2, 3], 'divmod(item, one).0')
    # Test that the first item in the result is a tuple

# Generated at 2022-06-22 11:44:11.930091
# Unit test for function fileglob
def test_fileglob():
    assert fileglob("test/test_filter_plugins/fileglob/test_data/") == ['test/test_filter_plugins/fileglob/test_data/text1.txt', 'test/test_filter_plugins/fileglob/test_data/text2.txt']
    assert fileglob("/non/existing/path/") == []



# Generated at 2022-06-22 11:44:24.959839
# Unit test for function extract
def test_extract():
    # noinspection PyDictCreation
    env = DictEnvironment({}, variable_start_string='[', variable_end_string=']')
    results = extract(env, 'key', {'key': 'value'})
    assert results == 'value'

# Generated at 2022-06-22 11:44:33.552260
# Unit test for function regex_search
def test_regex_search():
    '''
    Test the regex_search filter in the jinja2 filters.
    '''

    # Imports
    import sys

    # Append path where the filter is located
    sys.path.append('/usr/lib/python2.7/site-packages/ansible/plugins/filter')

    # Import jinja2 filters
    from jinja2.filters import environmentfilter

    # Filter value

# Generated at 2022-06-22 11:44:51.655073
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('Ansible', r'^Ansible$') == 'Ansible'
    assert regex_search('Ansible', r'^Ansible$', '\\g<0>') == 'Ansible'
    assert regex_search('Ansible', r'^Ansible(.)', '\\1') == 'i'
    assert regex_search('Ansible', r'^Ansible(.)', '\\g<1>') == 'i'
    assert regex_search('Ansible', r'^Ansible(.)', '\\2') == None
    assert regex_search('Ansible-2.0', r'^Ansible-(?P<version>\d.\d)', '\\g<version>') == '2.0'

# Generated at 2022-06-22 11:45:03.155969
# Unit test for function regex_search
def test_regex_search():
    '''return True if regex_search works, false otherwise'''
    if regex_search("abcdef", "(bc)(de)(f)", '\g<2>\g<1>\g<3>') != 'debc':
        return False
    if regex_search("test", "^test$") != 'test':
        return False
    if regex_search("test", "^test$", "\\1") != 't':
        return False
    if regex_search("test", "^test$", "\\g<1>") != 't':
        return False
    if regex_search("test", "^(t)(e)(st)$", "\\2\\3\\1") != 'estt':
        return False

# Generated at 2022-06-22 11:45:05.394076
# Unit test for function regex_search
def test_regex_search():
    assert regex_search("abc", 'abc', '\\g<0>') == ['abc']


# Generated at 2022-06-22 11:45:13.115275
# Unit test for function regex_escape
def test_regex_escape():
    string = '''$()*+?[]^{|}'''
    assert regex_escape(string) == '\\$\\(\\)\\*\\+\\?\\[\\]\\^\\{\\|\\}'
    assert regex_escape(string, re_type='posix_basic') == '\\$\\(\\)\\*\\+\\?\\[\\]\\^\\{\\|\\}'
    # TODO: assert regex_escape(string, re_type='posix_extended') == ...



# Generated at 2022-06-22 11:45:19.245889
# Unit test for function regex_search
def test_regex_search():
    result = regex_search('cab', r'(a)(b)')
    assert result == 'ab'

    result = regex_search('cab', r'(a)(b)', '\\2\\1')
    assert result == 'ba'

    result = regex_search('cab', r'(a)(b)', '\\g<2>\\g<1>')
    assert result == 'ba'

    result = regex_search('cab', r'(a)(b)', '\\2\\1', '\\1\\2')
    assert result == ['ba', 'ab']



# Generated at 2022-06-22 11:45:26.321952
# Unit test for function randomize_list
def test_randomize_list():
    import numpy as np
    mylist = [1, 2, 3, 4, 5]
    shuffle_list = randomize_list(mylist)
    assert mylist != shuffle_list
    mylist = np.arange(5)
    shuffle_list = randomize_list(mylist)
    assert mylist.all != shuffle_list.all



# Generated at 2022-06-22 11:45:29.501764
# Unit test for function do_groupby
def test_do_groupby():
    assert tuple(do_groupby((1, 2, 3, 4, 5), 'odd')) == ((False, [2, 4]), (True, [1, 3, 5]))



# Generated at 2022-06-22 11:45:38.889228
# Unit test for function do_groupby
def test_do_groupby():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.template import Jinja2Environment
    # If a list of dicts is supplied and attribute is a string
    value = [{'a': 'b'}, {'a': 'b'}, {'a': 'c'}]
    attribute = 'a'
    expected_results = [(('b', [{'a': 'b'}, {'a': 'b'}]),), (('c', [{'a': 'c'}]),)]
    results = do_groupby(Jinja2Environment(), value, attribute)
    # Results should be a list of tuples, with each tuple containing two elements:
    # An AnsibleUnsafeText object containing the group value and a list of AnsibleUnsafeText objects
    # representing each of the dictionaries in the

# Generated at 2022-06-22 11:45:46.525489
# Unit test for function rand
def test_rand():
    from ansible.parsing.yaml.loader import AnsibleLoader
    env = AnsibleLoader('./randtest.yaml').get_single_data()
    assert rand(env,10,2,2) in [2,4,6,8,10]
    assert rand(env,10,2) in [2,3,4,5,6,7,8,9]
    assert rand(env,[10,20,30]) in [10,20,30]
    assert rand(env,[10,20,30], seed='test') in [10,20,30]



# Generated at 2022-06-22 11:45:58.878035
# Unit test for function rand
def test_rand():
    cases = [
        { 'end': 10, 'start': 0, 'step': 2 },
        { 'end': 10, 'start': 0, 'step': 5 },
        { 'end': 10, 'start': 2, 'step': 2 },
        { 'end': 10, 'start': 5, 'step': 5 },
        { 'end': 10, 'seed': 20 },
        { 'end': [1, 2, 3, 4, 5]},
        { 'end': [1, 2, 3, 4, 5], 'seed': 20 },
        { 'end': 'str' },
        { 'end': [] },
        { 'end': [], 'seed': 20 },
    ]
    func = rand

# Generated at 2022-06-22 11:46:26.629851
# Unit test for function regex_search
def test_regex_search():
    result = regex_search('foo', r'o')
    assert result == 'o'
    result = regex_search('foo', r'o', '\\1')
    assert result == ['o', 'o']
    result = regex_search('foo', r'(o)')
    assert result == 'o'
    result = regex_search('foo', r'(o)', '\\g<1>')
    assert result == ['o']
    result = regex_search('foo', r'(o)', '\\1', '\\g<1>')
    assert result == ['o', 'o']
    result = regex_search('a foo and a bar', r'foo', '\\1', '\\g<1>')
    assert result == [None, None]

# Generated at 2022-06-22 11:46:32.730907
# Unit test for function regex_escape
def test_regex_escape():
    assert regex_escape('foo.bar') == 'foo\\.bar'
    assert regex_escape('foo.bar', re_type='posix_basic') == 'foo\\.bar'
    assert regex_escape('foo[bar]') == 'foo\\[bar\\]'
    assert regex_escape('foo[bar]', re_type='posix_basic') == 'foo\\[bar\\]'
    assert regex_escape('foo[.]bar', re_type='posix_basic') == 'foo\\[\\.\\]bar'
    assert regex_escape('foo(bar)', re_type='posix_basic') == 'foo\\(bar\\)'
    assert regex_escape('foo\\(bar)', re_type='posix_basic') == 'foo\\\\\\(bar\\)'

# Generated at 2022-06-22 11:46:43.819138
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('This is a string', 'string', '\g<0>') == 'string'
    assert regex_search('This is a string', 'This', '\g<0>') == 'This'
    assert regex_search('foobar', 'foo', '\g<0>') == 'foo'
    assert regex_search('foobar', 'foobar', '\g<0>') == 'foobar'
    assert regex_search('foo', 'foo', '\g<0>') == 'foo'
    assert regex_search('foobar', 'foo', '\g<0>') == 'foo'
    assert regex_search('foo', 'foo', '\g<0>') == 'foo'

# Generated at 2022-06-22 11:46:51.602073
# Unit test for function do_groupby
def test_do_groupby():
    test_input = [{'name': 'bob', 'age': 20}, {'name': 'bill', 'age': 25}, {'name': 'bob', 'age': 30}]
    result = do_groupby(test_input, 'name')
    assert result == [('bob', [{'age': 20, 'name': 'bob'}, {'age': 30, 'name': 'bob'}]), ('bill', [{'age': 25, 'name': 'bill'}])]


# Generated at 2022-06-22 11:47:00.705725
# Unit test for function get_hash
def test_get_hash():
    assert get_hash('data', hashtype='md5') == '1bc29b36f623ba82aaf6724fd3b16718'
    assert get_hash('data', hashtype='sha1') == '03d69d99e0a4c186e12f4e4b06a0d3e409b5aff2'
    assert get_hash('data', hashtype='sha224') == '8d5573c2a9d9c58f0ae0f93b22498c206bfa2331d745a755a8fe0055'
    assert get_hash('data', hashtype='sha256') == '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5'

# Generated at 2022-06-22 11:47:12.701002
# Unit test for function do_groupby
def test_do_groupby():

    # Import the required modules
    import jinja2

    do_groupby = lambda *args: [tuple(t) for t in _do_groupby(*args)]
    environment = jinja2.Environment()

    value = []
    attribute = ""

    result = do_groupby(environment, value, attribute)
    assert result == []

    # Test 2
    value = [{}]
    attribute = ""
    result = do_groupby(environment, value, attribute)
    assert result == []

    # Test 3
    value = [{}, {}]
    attribute = ""
    result = do_groupby(environment, value, attribute)
    assert result == []

    # Test 4
    value = [{}, {'1': '2'}]
    attribute = "1"

# Generated at 2022-06-22 11:47:21.714186
# Unit test for function do_groupby
def test_do_groupby():
    env = Environment()
    data = [{'a': 1, 'b': 3}, {'a': 2, 'b': 4}, {'a': 1, 'b': 5}]
    grouped = do_groupby(env, data, 'a')
    assert isinstance(grouped, list)
    assert isinstance(grouped[0], tuple)
    assert isinstance(grouped[0][0], int)
    assert isinstance(grouped[0][1], list)


# ------------------------------------------------------------------------------
# Data manipulation filters
# ------------------------------------------------------------------------------



# Generated at 2022-06-22 11:47:32.588139
# Unit test for function to_bool
def test_to_bool():
    assert to_bool('true') == True
    assert to_bool('TRUE') == True
    assert to_bool('True') == True
    assert to_bool('yes') == True
    assert to_bool('YES') == True
    assert to_bool('Yes') == True
    assert to_bool('on') == True
    assert to_bool('ON') == True
    assert to_bool('On') == True
    assert to_bool('y') == True
    assert to_bool('Y') == True
    assert to_bool('1') == True
    assert to_bool('false') == False
    assert to_bool('FALSE') == False
    assert to_bool('False') == False
    assert to_bool('no') == False
    assert to_bool('NO') == False
    assert to_bool('No') == False

# Generated at 2022-06-22 11:47:38.052758
# Unit test for function do_groupby
def test_do_groupby():
    env = Environment()
    data = [{'value': 1}, {'value': 1}]
    res = do_groupby(env, data, 'value')
    if res != [tuple(t) for t in _do_groupby(env, data, 'value')]:
        raise AssertionError()



# Generated at 2022-06-22 11:47:50.651896
# Unit test for function do_groupby
def test_do_groupby():
    env = Environment()
    env.globals['dict2items'] = dict2items
    env.globals['groupby'] = do_groupby
    test_template = u"""
{%- set g = dict2items(d) | groupby('key') -%}
{%- for key, items in g %}
{{ key }}:
{%- for i in items %}
  {{ i.key }}:{{ i.value }}
{%- endfor %}
{%- endfor %}
"""

    test_input = {
        'foo': 'bar',
        'bar': 'baz',
        'qux': 'quux'
    }

    test_output = u"""
foo:
  foo:bar
bar:
  bar:baz
qux:
  qux:quux
"""
    assert test

# Generated at 2022-06-22 11:48:14.701388
# Unit test for function extract
def test_extract():
    assert extract(None, 'ansible', {'ansible': {'version': {'full': '2.2.0.0'}}, 'not': 'tested'}) == {'version': {'full': '2.2.0.0'}}
    assert extract(None, 'ansible', {'ansible': {'version': {'full': '2.2.0.0'}}, 'not': 'tested'}, 'version') == {'full': '2.2.0.0'}
    assert extract(None, 'ansible', {'ansible': {'version': {'full': '2.2.0.0'}}, 'not': 'tested'}, ['version', 'full']) == '2.2.0.0'



# Generated at 2022-06-22 11:48:20.288692
# Unit test for function do_groupby
def test_do_groupby():
    from test.support import EnvironmentVarGuard
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    env = Environment()
    env.loader = DictLoader({
        't.j2': '''{{ (1, 2, 3) | groupby('__getitem__') }}'''
    })
    template = env.get_template('t.j2')
    with EnvironmentVarGuard():
        os.environ['ANSIBLE_DISABLE_UNSAFE_TEMPLATE_VARS'] = 'true'
        assert template.render() == "[(1, (1, 2, 3)), (2, (1, 2, 3)), (3, (1, 2, 3))]"
        assert isinstance(template.render(), AnsibleUnsafeText)

# Generated at 2022-06-22 11:48:27.600097
# Unit test for function regex_search
def test_regex_search():
    sample_string = 'a0b1c2d3e4f5123'
    regex = '[0-9]+'
    assert regex_search(sample_string, regex) == '0'
    assert regex_search(sample_string, regex, '\\1') == '1'
    assert regex_search(sample_string, '(?P<one>[0-9]+)', '\\g<one>') == '0'
    assert regex_search(sample_string, '(?P<one>[0-9]+)(?P<two>[0-9]+)', '\\g<two>') == '1'



# Generated at 2022-06-22 11:48:34.662059
# Unit test for function randomize_list
def test_randomize_list():
    assert randomize_list(range(3)) == randomize_list(range(3), seed=0)
    assert randomize_list(range(8)) == randomize_list(range(8), seed=0)
    assert randomize_list([]) == randomize_list([], seed=0)
    assert randomize_list(('a', 'b', 'c')) == randomize_list(('a', 'b', 'c'), seed=0)



# Generated at 2022-06-22 11:48:44.202122
# Unit test for function get_hash
def test_get_hash():
    assert get_hash('data', 'md5') == '1a79a4d60de6718e8e5b326e338ae533'
    assert get_hash('data', 'sha1') == '86f7e437faa5a7fce15d1ddcb9eaeaea377667b8'
    assert get_hash('data', 'sha224') == '23097d223405d8228642a477bda255b32aadbce4bda0b3f7e36c9da7'
    assert get_hash('data', 'sha256') == '2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae'

# Generated at 2022-06-22 11:48:56.429170
# Unit test for function get_hash
def test_get_hash():
    assert get_hash('hello', hashtype='sha1') == 'aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d'
    assert get_hash('hello', hashtype='sha224') == '4575bb4ec129df6380cedde6d71217fe0536f8ffc4e18bca530a7a1a'
    assert get_hash('hello', hashtype='sha256') == '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'

# Generated at 2022-06-22 11:49:09.082503
# Unit test for function comment
def test_comment():

    plain_comment_text = '''
This is a plain text comment.
    '''

    plain_comment = comment(plain_comment_text)

    assert plain_comment == '''\
# This is a plain text comment.
'''

    plain_multiline_comment_text = '''
This is a plain text comment.
It is multiline.
    '''

    plain_multiline_comment = comment(plain_multiline_comment_text)

    assert plain_multiline_comment == '''\
# This is a plain text comment.
# It is multiline.
'''

    xml_comment_text = '''
This is an XML comment.
    '''

    xml_comment = comment(
        '''\
This is an XML comment.
''',
        'xml'
    )



# Generated at 2022-06-22 11:49:21.497812
# Unit test for function subelements
def test_subelements():
    data = [
        {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'},
        {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'},
        {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'},
        {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'},
    ]
    result = subelements(data, ['key2', 'key4'])
    assert len(result) == 16
    assert ('value1', 'value1') in result

# Generated at 2022-06-22 11:49:32.654946
# Unit test for function strftime
def test_strftime():
    assert strftime("%Y-%m-%d %H:%M:%S") == time.strftime("%Y-%m-%d %H:%M:%S")
    assert strftime("%Y-%m-%d %H:%M:%S", 1477661953.13) == time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(1477661953.13))
    assert strftime("%Y-%m-%d %H:%M:%S", "1477661953.13") == time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(1477661953.13))



# Generated at 2022-06-22 11:49:36.653887
# Unit test for function strftime
def test_strftime():
    assert strftime("%Y") == time.strftime("%Y")
    assert strftime("%Y", 0) == time.strftime("%Y", time.localtime(0))



# Generated at 2022-06-22 11:49:53.855486
# Unit test for function rand
def test_rand():
    assert rand([1,2,3], 1, seed=1) == 2
    assert rand([1,2,3], seed=1) in [1,2,3]
    assert rand(8, seed=1) in range(8)
    assert rand(8, 2, seed=1) in range(2,8,2)
    assert rand(3, 1, 2, seed=1) in range(1,3,2)
    assert rand(8) in range(8)
    assert rand(8, 2) in range(2,8,2)
    assert rand(3, 1, 2) in range(1,3,2)



# Generated at 2022-06-22 11:50:04.467631
# Unit test for function regex_search
def test_regex_search():
    assert ['foo'] == regex_search('bar foobar', r'.*(foo)', '\\1')
    assert 'foo' == regex_search('bar foobar', r'.*(foo)', '\\g<1>')
    assert 'foo' == regex_search('bar foobar', r'.*(foo)', '\\g<1>', ignorecase=True)
    assert 'bar' == regex_search('bar foobar', r'^(.*)', '\\g<1>')
    assert 'bar' == regex_search('bar foobar', r'^(.*)', '\\1')
    assert 'bar' == regex_search('bar foobar', r'^(.*)', '\\g<1>')