

# Generated at 2022-06-22 11:40:45.672917
# Unit test for function rand
def test_rand():
    # Get a deterministic set of random numbers
    # By seeding with 1, we can guarantee the same set
    # of random numbers on every run.
    r = Random(1)

    # Test for integers
    for i in range(10):
        assert rand(None, i, seed=r) == rand(None, i, seed=r)
        assert rand(None, i, seed=1) == rand(None, i, seed=1)
        assert rand(None, i, seed=1) != rand(None, i, seed=2)
        assert rand(None, 1, 10, seed=r) == rand(None, 1, 10, seed=r)
        assert rand(None, 1, 10, seed=1) == rand(None, 1, 10, seed=1)

# Generated at 2022-06-22 11:40:48.185801
# Unit test for function fileglob
def test_fileglob():
    test_list = ["hello.txt", "goodbye.txt", "testing.py"]
    path = "*txt"
    result = fileglob(path)
    assert result == test_list



# Generated at 2022-06-22 11:41:00.772448
# Unit test for function do_groupby
def test_do_groupby():
    from jinja2 import Environment
    from ansible.template.safe_eval import safe_eval
    import ansible.module_utils.six
    # checking for python 2.6 compatibility, since it is required by ansible

# Generated at 2022-06-22 11:41:12.859461
# Unit test for function to_bool
def test_to_bool():
    assert to_bool(True) is True
    assert to_bool(False) is False
    assert to_bool('on') is True
    assert to_bool('true') is True
    assert to_bool('yes') is True
    assert to_bool('1') is True
    assert to_bool('off') is False
    assert to_bool('false') is False
    assert to_bool('no') is False
    assert to_bool('0') is False
    assert to_bool(None) is None
    assert to_bool('') is False
    assert to_bool('foo') is False
    assert to_bool(1) is True
    assert to_bool(0) is False


# Generated at 2022-06-22 11:41:16.930594
# Unit test for function mandatory
def test_mandatory():
    from jinja2.runtime import Undefined
    try:
        mandatory(Undefined(name='a'))
    except AnsibleFilterError:
        pass
    else:
        raise Exception("Expected AnsibleFilterError")



# Generated at 2022-06-22 11:41:21.139366
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    a = {"list": ["one", "two", "three"]}
    b = to_nice_yaml(a)
    assert b == "list:\n" \
                " - one\n" \
                " - two\n" \
                " - three\n"


# Generated at 2022-06-22 11:41:26.245249
# Unit test for function regex_escape
def test_regex_escape():
    assert regex_escape(r'^https?://\S+\.com$', re_type='python') == r'\^https\?\://\\S\+\\.com\$'
    assert regex_escape(r'^https?://\S+\.com$', re_type='posix_basic') == r'\^https?://\S+\.com\$'


# Generated at 2022-06-22 11:41:35.276856
# Unit test for function get_hash
def test_get_hash():
    assert get_hash('value', 'sha1') == 'b7e23ec29af22b0b4e41da31e868d57226121c84'
    assert get_hash('value', 'sha256') == '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
    assert get_hash('value', 'sha512') == '9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2dff72519673ca72323c3d99ba5c11d7c7acc6e14b8c5da0c4663475c2e5c3adef46f73bcdec043'
    assert get_hash

# Generated at 2022-06-22 11:41:48.134476
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch, Mock

    from ansible.template import filters

    list_value = [10, 20, 20, 'yes', 'no']
    str_value = '{0}'
    unicode_value = u'{0}'

    # patch jinja2.filters.do_dictsort to test OrderedDict
    def fake_dictsort(value, case_sensitive=False, by='key'):
        return None

    with patch.object(filters, 'do_dictsort', fake_dictsort):
        assert(to_nice_yaml(list_value) == '[\n    10,\n    20,\n    20,\n    "yes",\n    "no"\n]')


# Generated at 2022-06-22 11:41:59.111618
# Unit test for function fileglob
def test_fileglob():
    # Test with empty pathname
    assert [] == fileglob(None)
    assert [] == fileglob('')
    # Test with a glob returns empty
    assert [] == fileglob('/path/to/non-exists-file')
    assert [] == fileglob('/path/to/non-exists-file.*')
    # Test with a glob returns one file
    assert ['/path/to/file1'] == fileglob('/path/to/file1')
    assert ['/path/to/file.2'] == fileglob('/path/to/file.2')
    assert ['/path/to/file1', '/path/to/file.2'] == sorted(fileglob('/path/to/file*'))
    # Test with a glob returns multiple files

# Generated at 2022-06-22 11:42:12.600404
# Unit test for function subelements
def test_subelements():
    from ansible.compat.tests import unittest

    class TestSubelements(unittest.TestCase):
        def test_subelements(self):
            sub_obj = dict(
                id='1',
                lists=[
                    dict(
                        id=1,
                        tuples=[(0, 1), (2, 3)],
                        text='text_list',
                    ),
                    dict(
                        id=2,
                        tuples=[(4, 5), (6, 7)],
                        text='text_list',
                    ),
                ],
                text='text',
            )
            sub_test = subelements(sub_obj, ['text', 'lists', 'tuples'])
            self.assertIsInstance(sub_test, list)
            self.assertEqual(len(sub_test), 4)


# Generated at 2022-06-22 11:42:18.713774
# Unit test for function regex_replace
def test_regex_replace():
    if sys.version_info[0] == 3:
        search_replace_test = u'replace\u0020me'
        if sys.version_info[1] == 6:
            # Python 3.6 returns this instead of \u0020
            search_replace_test = u'replace me'
        assert regex_replace(u'test\\ttest\nreplace\\u0020me', u'\\\\(t|u[0-9a-z]{4})', u'\\\\1') == u'test\\ttest\n' + search_replace_test



# Generated at 2022-06-22 11:42:30.040971
# Unit test for function to_yaml
def test_to_yaml():
    from ansible.utils.unsafe_proxy import wrap_var
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.template.templar import Templar
    import os
    import pytest

# Generated at 2022-06-22 11:42:37.295195
# Unit test for function fileglob
def test_fileglob():
    m = mock.mock_open()
    m.return_value.__iter__.return_value = ['/tmp/test1.log', '/tmp/test2.log']
    with mock.patch('ansible.module_utils.basic.open', m, create=True):
        assert {'files': ['/tmp/test1.log', '/tmp/test2.log']} == fileglob('/tmp/*.log')

# Generated at 2022-06-22 11:42:49.970986
# Unit test for function fileglob
def test_fileglob():
    assert fileglob('/bin/[') == ['/bin/[']
    assert fileglob('/bin/ls') == ['/bin/ls']
    assert fileglob('/bin/*') == ['/bin/' + x for x in os.listdir('/bin')]
    assert fileglob('/usr/bin/python*') == ['/usr/bin/python' + x for x in os.listdir('/usr/bin') if x.startswith('python')]
    assert fileglob('/bin/n*p*') == ['/bin/' + x for x in os.listdir('/bin') if x.startswith('n') and x.find('p') > -1]

# Generated at 2022-06-22 11:42:52.852557
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    assert(to_nice_yaml({"foo": "bar"}) == '---\n{foo: bar}\n')



# Generated at 2022-06-22 11:43:01.633777
# Unit test for function rand
def test_rand():
    assert rand(None, 10) in xrange(10)
    assert rand(None, [1,2,3,4]) in [1,2,3,4]
    assert rand(None, 10, seed=1) == 6
    assert rand(None, 10, seed=1) == 6
    assert rand(None, 10, seed=2) != 6
    assert rand(None, 10, seed=2) != 6
    assert rand(None, 10, seed='hello world') == 3
    assert rand(None, 10, seed='hello world') == 3
    assert rand(None, 10, seed='hello world') == 3
    assert rand(None, 10, seed='hello world') == 3
    assert rand(None, 10, seed='hello world') == 3
    assert rand(None, 10, seed='hello world') == 3

# Generated at 2022-06-22 11:43:13.052566
# Unit test for function mandatory
def test_mandatory():

    from jinja2.runtime import Undefined
    from ansible.vars import AnsibleUnicode, AnsibleUndefined

    # test non-recursive type check with none
    assert mandatory(None) is None

    # test non-recursive type check with defined
    assert mandatory(True) is True

    # test non-recursive type check with dict
    assert mandatory({}) == {}

    # test non-recursive type check with string
    assert mandatory('test') == 'test'

    # test non-recursive type check with var
    assert mandatory(AnsibleUnicode('test')) == 'test'

    # test non-recursive type check with AnsibleUndefined
    assert mandatory(AnsibleUndefined()) is None

    # test non-recursive type check with Jinja undefined
    # assert mandatory(Undefined()) == None

# Generated at 2022-06-22 11:43:24.246120
# Unit test for function do_groupby
def test_do_groupby():
    from jinja2 import Environment
    env = Environment()
    import six
    import collections
    if six.PY2:
        NamedTuple = collections.namedtuple('NamedTuple', ['a', 'b'])
    else:
        class NamedTuple(collections.namedtuple('NamedTuple', ['a', 'b'])):
            __slots__ = ()
            def __repr__(self):
                return 'NamedTuple(a=%r, b=%r)' % self
    value = [NamedTuple(a=1, b=2), NamedTuple(a=2, b=1), NamedTuple(a=1, b=1)]


# Generated at 2022-06-22 11:43:33.651029
# Unit test for function regex_escape
def test_regex_escape():
    # Also consider the test cases in filters/math.py
    assert regex_escape(r'foo+bar') == r'foo\+bar'
    assert regex_escape(r'foo.bar') == r'foo\.bar'
    assert regex_escape(r'foo[1]bar') == r'foo\[1\]bar'
    assert regex_escape(r'foo(bar)') == r'foo\(bar\)'
    assert regex_escape(r'foo^bar') == r'foo\^bar'
    assert regex_escape(r'foo{bar}') == r'foo\{bar\}'
    assert regex_escape(r'foo$bar') == r'foo\$bar'
    assert regex_escape(r'foo|bar') == r'foo\|bar'

# Generated at 2022-06-22 11:43:45.695388
# Unit test for function do_groupby
def test_do_groupby():
    from jinja2 import Environment

    env = Environment()
    env.filters['groupby'] = do_groupby

    # create a tuple with a namedtuple as the key
    test_tuple_list = [('test_a', 'value_a', 'test_a_a'), ('test_a', 'value_b', 'test_a_b'), ('test_b', 'value_c', 'test_b_c')]
    test_groupby_result = env.from_string('{{ mylist | groupby(0) | list }}').render(mylist=test_tuple_list)

# Generated at 2022-06-22 11:43:51.853009
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    # Generate a random object to test with
    rand = Random()
    v = { "value": rand.randint(0, 255) }
    # Ensure it is valid YAML (may fail if the random values generated a bad object)
    yaml_load(to_nice_yaml(v))
    assert type(yaml_load(to_nice_yaml(v))) == dict


# Generated at 2022-06-22 11:43:53.054122
# Unit test for function comment
def test_comment():
    """Function comment(text) has been tested in test_jinja2.py"""
    pass



# Generated at 2022-06-22 11:43:56.027525
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    assert to_nice_yaml(_to_nice_yaml_dummy_data) == _to_nice_yaml_reference



# Generated at 2022-06-22 11:44:03.052065
# Unit test for function randomize_list
def test_randomize_list():
    mylist = [1, 2, 3, 4]
    shuffled_list = randomize_list(mylist)
    assert len(shuffled_list) == 4
    assert set(shuffled_list) == set(mylist)
    shuffled_list = randomize_list(mylist, seed='myseed')
    assert len(shuffled_list) == 4
    assert set(shuffled_list) == set(mylist)

        

# Generated at 2022-06-22 11:44:15.181231
# Unit test for function get_hash
def test_get_hash():
    assert get_hash('hello', hashtype='sha1') == 'aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d'
    assert get_hash('hello', hashtype='sha224') == 'ea09ae9cc6768c50fcee903ed054556e5bfc8347907f12598aa24193'
    assert get_hash('hello', hashtype='sha256') == '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'

# Generated at 2022-06-22 11:44:24.903060
# Unit test for function do_groupby
def test_do_groupby():
    # pylint: disable=redefined-outer-name
    # we use jinja2._compat here, because it has the do_groupby function from jinja2
    # that we want to test against
    from jinja2 import _compat
    from collections import namedtuple

    TestItem = namedtuple('TestItem', ['foo', 'bar'])
    test_list = [TestItem('foo', 1), TestItem('bar', 1), TestItem('foo', 2)]
    env = None
    attribute = 'foo'
    # we are using the same function that jinja2 would use here, so make sure
    # this still works as expected, before we use our special function
    jinja_result = [tuple(t) for t in _compat.do_groupby(env, test_list, attribute)]

# Generated at 2022-06-22 11:44:33.528950
# Unit test for function subelements
def test_subelements():
    # Import here to avoid circular import dependency
    from units.mock.loader import DictDataLoader


# Generated at 2022-06-22 11:44:39.169174
# Unit test for function fileglob
def test_fileglob():
    assert fileglob('/etc/resolv.conf') == ['/etc/resolv.conf']
    assert fileglob('/etc/rc?.d') == []
    assert fileglob('/etc/rc*.d') == ['/etc/rc.d', '/etc/rc.local']


# Generated at 2022-06-22 11:44:50.422554
# Unit test for function comment
def test_comment():
    assert(comment("") == "# \n")
    assert(comment("", style='c') == "// \n")
    assert(comment("", style='erlang') == "% \n")
    assert(comment("", style='cblock') == "/*\n * \n */")
    assert(comment("", style='xml') == "<!--\n - \n-->")
    assert(comment("test\n") == "# test\n# \n")
    assert(comment("test\n", style='c') == "// test\n// \n")
    assert(comment("test\n", style='erlang') == "% test\n% \n")
    assert(comment("test\n", style='cblock') == "/*\n * test\n * \n */")

# Generated at 2022-06-22 11:45:05.876490
# Unit test for function do_groupby
def test_do_groupby():
    from jinja2._compat import iteritems, iterkeys

    result = do_groupby(value={}, attribute={})
    assert result == []
    result = do_groupby(value={'a': 'a', 'b': 'b'}, attribute={'a': 'a', 'b': 'b'})
    assert result == [({'a': 'a', 'b': 'b'}, ['a', 'b'])]
    result = do_groupby(value={'a': 'a', 'b': 'b', 'c': 'a2'}, attribute={'a': 'a', 'b': 'b', 'c': 'a2'})
    assert result == [({'a': 'a', 'b': 'b', 'c': 'a2'}, ['a', 'b', 'c'])]
    result = do

# Generated at 2022-06-22 11:45:16.315836
# Unit test for function strftime
def test_strftime():
    import time
    import pytest
    second = time.time()
    assert strftime('%Y-%m-%d', second) == time.strftime('%Y-%m-%d', time.localtime(second))
    assert strftime('%Y-%m-%d %H:%M:%S', second) == time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(second))
    with pytest.raises(AnsibleFilterError) as excinfo:
        strftime('%Y-%m-%d', 'invalidvalue')
    assert 'Invalid value for epoch value' in str(excinfo.value)



# Generated at 2022-06-22 11:45:26.484523
# Unit test for function to_yaml
def test_to_yaml():
    a = {
            "a": ["b", "c"],
            "d": {
                "e": "f",
                "g": 1,
                "h": True,
                "i": False,
                "j": None,
                },
            "k": [1, 2],
            "l": [3, 4],
            }
    yaml_a = '''\
a:
- b
- c
d:
  e: f
  g: 1
  h: true
  i: false
  j: null
k: [1, 2]
l:
- 3
- 4
'''
    assert to_yaml(a) == to_text(yaml_a)


# Generated at 2022-06-22 11:45:36.677561
# Unit test for function regex_search
def test_regex_search():
    # This function is a unit test for regex_search
    def test_regex_search(value, regex, *args, expected_result, **kwargs):
        # This function is a unit test for regex_search
        if regex_search(value=value, regex=regex, *args, **kwargs) != expected_result:
            raise AnsibleFilterError('Failed unit test for regex_search.')
    # End test_regex_search

    test_regex_search(
        value='test string',
        regex='t\w{2}',
        expected_result='test'
    )


# Generated at 2022-06-22 11:45:40.445830
# Unit test for function regex_escape
def test_regex_escape():
    assert regex_escape(r'$*.', re_type='posix_basic') == r'\$\*\.'
    assert regex_escape(r'$*.', re_type='python') == r'\$\*\.'



# Generated at 2022-06-22 11:45:51.276251
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    assert to_nice_yaml({u'a': u'b'}) == "a: b\n"
    assert to_nice_yaml({u'a': u'b\nc'}) == "a: |-\n    b\n    c\n"
    assert to_nice_yaml({u'a': {u'b': u'c'}}, indent=2) == "a:\n  b: c\n"
    assert to_nice_yaml({u'a': {u'b': u'c\nd'}}, indent=2) == "a:\n  b: |-\n    c\n    d\n"



# Generated at 2022-06-22 11:46:02.264028
# Unit test for function regex_search
def test_regex_search():
    assert regex_search(value="TEST", regex="[A-Z]+") == 'TEST'
    assert regex_search(value="TEST", regex="[A-Z]+", ignorecase=True) == 'TEST'
    assert regex_search(value="test", regex="[A-Z]+", ignorecase=True) == 'TEST'
    assert regex_search(value="TEST", regex="(\d+)") is None
    assert regex_search(value="TEST", regex="(\d+)") == None
    assert regex_search(value="TEST1", regex="(\d+)", ignorecase=True) == '1'
    assert regex_search(value="TEST1", regex="[A-Z]+", ignorecase=True) == 'TEST1'

# Generated at 2022-06-22 11:46:14.400237
# Unit test for function to_yaml
def test_to_yaml():
    output = to_yaml({'a': 1, 'b': 2}, default_flow_style=False)
    assert output == 'a: 1\nb: 2\n', "to_yaml with default_flow_style=False failed"
    output = to_yaml({'a': 1, 'b': 2})
    assert output == '{a: 1, b: 2}\n', "to_yaml with default_flow_style=True failed"
    output = to_yaml([1, 2, 3], default_flow_style=False)
    assert output == '- 1\n- 2\n- 3\n', "to_yaml with default_flow_style=False and array input failed"

# Generated at 2022-06-22 11:46:25.441409
# Unit test for function subelements
def test_subelements():
    obj = [{"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}]
    assert subelements(obj, 'groups') == [({'name': 'alice', 'groups': ['wheel'], 'authorized': ['/tmp/alice/onekey.pub']}, 'wheel')]

    obj = [{"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}]
    assert subelements(obj, 'user.groups') == []

    obj = [{"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}]

# Generated at 2022-06-22 11:46:35.441814
# Unit test for function get_hash
def test_get_hash():
    data = 'The quick brown fox jumped over the lazy dog.'
    assert get_hash(data) == get_hash(data, 'sha1') == '2fd4e1c67a2d28fced849ee1bb76e7391b93eb12'
    assert get_hash(data, 'md5') == '9e107d9d372bb6826bd81d3542a419d6'
    assert get_hash(data, 'sha256') == 'd7a8fbb307d7809469ca9abcb0082e4f8d5651e46d3cdb762d02d0bf37c9e592'
    print('get_hash() test successful.')


# Generated at 2022-06-22 11:46:46.595902
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('foo bar', '(foo) (bar)') == 'foo bar'
    assert regex_search('foo bar', '(foo) (bar)', '\\1') == ['foo']
    assert regex_search('foo bar', '(foo) (bar)', '\\1', '\\2') == ['foo', 'bar']
    assert regex_search('foo bar', '(foo) (bar)', '\\g<1>') == ['foo']
    assert regex_search('foo bar', '(foo) (bar)', '\\g<1>', '\\g<2>') == ['foo', 'bar']
    assert regex_search('foo bar', '(foo) (bar)', '\\g<2>', '\\g<1>') == ['bar', 'foo']

# Generated at 2022-06-22 11:46:54.153870
# Unit test for function mandatory
def test_mandatory():
    assert mandatory(None) == None
    assert mandatory(2) == 2
    assert mandatory(True) == True
    assert mandatory(False) == False
    assert mandatory(dict(a=1)) == dict(a=1)
    assert mandatory([1,2,3]) == [1,2,3]
    assert mandatory(set([1,2,3])) == set([1,2,3])
    assert mandatory('string') == 'string'
    assert mandatory(u'string') == u'string'

# Generated at 2022-06-22 11:47:04.324236
# Unit test for function combine
def test_combine():
    import ansible.utils.unsafe_proxy
    import jinja2.runtime

    # Configure the jinja enviroment
    env = jinja2.Environment(undefined=jinja2.runtime.Undefined)
    env.filters['combine'] = combine

    # Test actual function
    arg1 = {'var': True}
    arg2 = {'var': False, 'overridden': True}
    result = combine(arg1, arg2)

    assert result['var'] == False
    assert result['overridden'] == True

    # Test with undefined
    arg1 = ansible.utils.unsafe_proxy.UnsafeProxy({'var': True})
    arg2 = {'var': False, 'overridden': True}
    result = combine(arg1, arg2)

    assert result['var']

# Generated at 2022-06-22 11:47:14.781486
# Unit test for function get_hash
def test_get_hash():
    assert get_hash('test') == 'a94a8fe5ccb19ba61c4c0873d391e987982fbbd3'
    assert get_hash('test', hashtype='sha256') == '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08'
    try:
        get_hash('test', hashtype='invalid')
        raise AssertionError('get_hash() function did not fail with invalid hashtype')
    except AnsibleFilterError:
        pass



# Generated at 2022-06-22 11:47:21.109830
# Unit test for function subelements
def test_subelements():
    obj = [{"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}]
    assert obj == subelements(obj, 'name')
    assert obj[0]['name'] == subelements(obj, 'name')[0][1]
    assert obj[0]['groups'] == [x[1] for x in subelements(obj, 'groups')]
    assert obj[0]['authorized'] == [x[1] for x in subelements(obj, 'authorized')]
    assert subelements([obj[0]], 'groups')[0] == subelements(obj, 'groups')[0]


# Generated at 2022-06-22 11:47:32.078647
# Unit test for function do_groupby
def test_do_groupby():
    from ansible.compat.tests import unittest as ansible_unittest

    from jinja2 import DictLoader, Environment

    env = Environment(loader=DictLoader({
        'do_groupby.j2': '{% set items = [{ "a": "a", "b": "b" }, { "a": "a", "b": "c" }, { "a": "b", "b": "b" }] %}{{ items | groupby("a") }}'
    }))

    env.filters['groupby'] = do_groupby

    template_string = env.get_template('do_groupby.j2')
    output = template_string.render()
    assert 'a' in output  # This is the only test we can do with a non-hashed output



# Generated at 2022-06-22 11:47:42.559776
# Unit test for function do_groupby
def test_do_groupby():
    env = Environment()
    result = env.from_string('{{ thing | groupby("group") | list }}').render(dict(thing=[dict(group='g1', foo='bar'),
                                                                                         dict(group='g2', foo='meh'),
                                                                                         dict(group='g1', foo='baz')]))
    assert result == (
        "[('g1', [{'group': 'g1', 'foo': 'bar'}, {'group': 'g1', 'foo': 'baz'}]), ('g2', [{'group': 'g2', 'foo': 'meh'}])]"
    )



# Generated at 2022-06-22 11:47:48.230314
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    assert to_nice_yaml({'foo': 1, 'bar': 2}) == '''{foo: 1,
bar: 2}
'''
    assert to_nice_yaml({'foo': 1, 'bar': 2}, width=10, indent=3) == '''{   foo: 1,
   bar: 2}
'''



# Generated at 2022-06-22 11:47:58.724473
# Unit test for function flatten
def test_flatten():
    assert [] == flatten([])
    assert ['foo', 'bar'] == flatten(['foo', 'bar'])
    assert ['foo', 'bar', 'baz', 'qux'] == flatten(['foo', ['bar', 'baz'], 'qux'])
    assert ['foo', 'bar', 'baz', 'qux'] == flatten(['foo', ['bar', ['baz']], 'qux'])
    assert ['foo', 'bar', 'baz', 'qux', 'quux'] == flatten(['foo', ['bar', ['baz', 'qux']], 'quux'])

# Generated at 2022-06-22 11:48:06.070219
# Unit test for function regex_search
def test_regex_search():
    try:
        assert regex_search('abbc', 'abb') == 'abb'
        assert regex_search('abbc', 'abb', '\\g<1>') == ['abb', 'c']
        assert regex_search('abbc', 'abb', '\\1') == ['abb', 'c']
        assert regex_search('abbc', 'abb', '\\g<0>') == ['abb']
        assert regex_search('abbc', 'abb', '\\0') == ['abb']
    except Exception as e:
        raise AnsibleFilterError("Assertion failed: {}".format(repr(e)))



# Generated at 2022-06-22 11:48:12.628540
# Unit test for function get_hash
def test_get_hash():
    assert get_hash('test') == 'a94a8fe5ccb19ba61c4c0873d391e987982fbbd3'


# Generated at 2022-06-22 11:48:18.079090
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
  """Test the method filters of class FilterModule"""

  # Object instantiation
  j2filters = FilterModule()

  # Check the object's filter methods
  filter_methods = j2filters.filters()
  assert filter_methods['path_join'] is path_join
  assert filter_methods['random'] is rand
  assert filter_methods['bool'] is to_bool
  assert filter_methods['basename'] is os.path.basename
  assert filter_methods['exists'] is os.path.exists
  assert filter_methods['islink'] is os.path.islink
  assert filter_methods['isdir'] is os.path.isdir
  assert filter_methods['isfile'] is os.path.isfile
  assert filter_methods['to_datetime'] is to_

# Generated at 2022-06-22 11:48:21.846974
# Unit test for function randomize_list
def test_randomize_list():
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 2, 3, 4, 5]
    shuffle(list1)
    return list1 == randomize_list(list2)



# Generated at 2022-06-22 11:48:33.911718
# Unit test for function mandatory
def test_mandatory():
    from ansible.errors import AnsibleFilterError
    from jinja2.runtime import Undefined
    from ansible.module_utils.six import PY2

    # No value for mandatory
    if PY2:
        try:
            mandatory(Undefined, "No value for mandatory")
        except AnsibleFilterError as e:
            assert "No value for mandatory" in to_text(e)
    else:
        try:
            mandatory(Undefined, "No value for mandatory")
        except AnsibleFilterError as e:
            assert "No value for mandatory" in str(e)

    # Named variable missing
    if PY2:
        try:
            mandatory(Undefined(name="bacon"))
        except AnsibleFilterError as e:
            assert "'bacon' not defined." in to_text(e)

# Generated at 2022-06-22 11:48:39.159375
# Unit test for function mandatory
def test_mandatory():
    assert mandatory('foo') == 'foo'
    try:
        mandatory(AnsibleUndefined)
    except AnsibleFilterError as e:
        assert 'Mandatory' in str(e)
    assert mandatory(AnsibleUndefined, msg='foo') == 'foo'



# Generated at 2022-06-22 11:48:46.102087
# Unit test for function regex_search
def test_regex_search():
    value = '''
        url: http://www.example.org
        url: http://www.example2.org
        url: http://www.example3.org
    '''
    regex = r'http[s]?://([^/]+)/'

    matches = regex_search(value, regex, r'\g<1>')
    assert matches == ['www.example.org']

    matches = regex_search(value, regex, r'\g<0>')
    assert matches == ['http://www.example.org']

    matches = regex_search(value, regex, r'\0')
    assert matches == ['http://www.example.org']

    matches = regex_search(value, regex, r'\1')
    assert matches == ['www.example.org']


# Generated at 2022-06-22 11:48:56.892385
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('abcd', '^b', '\\g<0>', ignorecase=True) == 'b'
    assert regex_search('abcd', '^a', '\\g<0>', '\\g<0>', ignorecase=True) == ['a', 'a']
    assert regex_search('abcd', '^a', 0, ignorecase=True) == 'a'
    assert regex_search('abcd', '^a', 1, ignorecase=True) == 'b'
    # Multiline testing
    assert regex_search('abcd\nabcd', '^b', '\\g<0>', ignorecase=True, multiline=True) == 'b'

# Generated at 2022-06-22 11:49:03.229670
# Unit test for function mandatory
def test_mandatory():
    import jinja2
    env = jinja2.Environment()
    env.filters['mandatory'] = mandatory
    foo = env.from_string('{{ missing | mandatory }}')
    try:
        foo.render({})
        assert False
    except jinja2.exceptions.UndefinedError:
        pass
    except Exception as e:
        assert False, e



# Generated at 2022-06-22 11:49:15.835618
# Unit test for function extract
def test_extract():
    environment = Dict({})

    d = {'a': {'b': {'c': 42}}}
    assert extract(environment, 'c', d, ['b', 'a']) == 42
    assert extract(environment, 'c', d, 'b') == {'c': 42}
    assert extract(environment, 'b', d, 'a') == {'b': {'c': 42}}

    t = [{'b': {'c': 42}}]
    assert extract(environment, 0, t) == {'b': {'c': 42}}

    t = (1, 2, 3)
    assert extract(environment, 1, t) == 2

    s = 'abc'
    assert extract(environment, 1, s) == 'b'

    s = set([1, 2, 3])

# Generated at 2022-06-22 11:49:20.020987
# Unit test for function flatten
def test_flatten():
    mylist = [1, 2, 3, [1, 2, 3, {'a': [1, 2], 'b': [3, 4]}]]
    assert flatten(mylist) == [1, 2, 3, 1, 2, 3, {'a': [1, 2], 'b': [3, 4]}]
    assert flatten(mylist, levels=1) == [1, 2, 3, 1, 2, 3, {'a': [1, 2], 'b': [3, 4]}]
    assert flatten(mylist, levels=2) == [1, 2, 3, 1, 2, 3, {'a': [1, 2], 'b': [3, 4]}]

# Generated at 2022-06-22 11:49:38.519624
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('some string', r'\s') == ' '
    assert regex_search('some string', r'\s', '\\g<0>') == ' '
    assert regex_search('some string', r'\s', '\\g<1>') == None
    assert regex_search('some string', r'(?P<match>\w+)', '\\g<match>') == 'some'
    assert regex_search('some string', r'(\w+)', '\\g<1>') == 'some'
    assert regex_search('some string', r'(\w+)', '\\1') == 'some'
    assert regex_search('some string', r'(\w+)', '\\g<1>', '\\g<1>') == ['some', 'some']

# Generated at 2022-06-22 11:49:49.935935
# Unit test for function do_groupby
def test_do_groupby():
    ret = _do_groupby(None, [{'foo': 1}, {'foo': 2}], 'foo')
    assert(isinstance(ret, list))
    assert(len(ret) == 2)
    assert(all([isinstance(i, tuple) for i in ret]))
    assert(ret[0][0] == 1)
    assert(ret[1][0] == 2)

    from collections import namedtuple
    test_named_tp = namedtuple('test_named_tp', 'foo bar')
    ret = _do_groupby(None, [test_named_tp(foo=1, bar=2), test_named_tp(foo=2, bar=3)], 'foo')
    assert(isinstance(ret, list))
    assert(len(ret) == 2)

# Generated at 2022-06-22 11:50:00.874510
# Unit test for function do_groupby
def test_do_groupby():
    from jinja2 import Environment
    from jinja2.runtime import StrictUndefined
    env = Environment(extensions=['jinja2.ext.do'])
    t = env.from_string("""
    {{ data|groupby('a')|list }}
    """).render(data=[{'a': 1, 'b': 1}, {'a': 1, 'b': 2}])
    assert t == "[(1, [{'a': 1, 'b': 1}, {'a': 1, 'b': 2}])]"
    env = Environment(undefined=StrictUndefined)
    t = env.from_string("""
    {{ data|groupby('a')|list }}
    """).render(data=[{'a': 1, 'b': 1}, {'a': 1, 'b': 2}])

# Generated at 2022-06-22 11:50:08.545333
# Unit test for function extract
def test_extract():
    assert extract({}, "foo", {"foo": {"bar": "baz"}}) == {"bar": "baz"}
    assert extract({}, "foo", {"foo": "baz"}) == "baz"
    assert extract({}, "foo", {"foo": 'baz'}) == "baz"
    assert extract({}, "foo", {"foo": ["baz", "biz"]}) == ["baz", "biz"]
    assert extract({}, "foo", {"foo": 12}) == 12
    assert extract({}, "foo", {"foo": '12'}) == "12"
    assert extract({}, "foo", {"foo": -12}) == -12
    assert extract({}, "foo", {"foo": 12.0}) == 12.0
    assert extract({}, "foo", {"foo": -12.0}) == -12.0