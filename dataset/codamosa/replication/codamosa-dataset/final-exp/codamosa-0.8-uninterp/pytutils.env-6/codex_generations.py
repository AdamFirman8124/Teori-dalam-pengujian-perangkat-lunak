

# Generated at 2022-06-14 05:49:04.730486
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import doctest

    doctest.testmod()



# Generated at 2022-06-14 05:49:14.360482
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    actual = parse_env_file_contents(lines)
    assert len(actual) == 3
    assert next(actual) == ('TEST', '.../yeee')
    assert next(actual) == ('THISIS', '.../a/test')
    assert next(actual) == ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')



# Generated at 2022-06-14 05:49:26.128375
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    env_file_contents = '''
    TEST=${HOME}/yeee-${PATH}
    THISIS=~/a/test
    YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST
    '''

    expected = collections.OrderedDict([
        ("TEST", os.path.join(os.path.expanduser("~"), "yeee-") + os.environ['PATH']),
        ("THISIS", os.path.join(os.path.expanduser("~"), "a/test")),
        ("YOLO", os.path.join(os.path.expanduser("~"), "swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST")),
    ])

    keys

# Generated at 2022-06-14 05:49:35.195106
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'environ.env')
    with open(path) as f:
        lines = f.read().splitlines()
    actual = parse_env_file_contents(lines)
    expected = [
        ('TEST', '${HOME}/yeee-$PATH'),
        ('THISIS', '~/a/test'),
        ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    ]
    assert tuple(actual) == tuple(expected)



# Generated at 2022-06-14 05:49:44.515793
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    result = load_env_file(lines, write_environ=dict())

    r = list(result.items())
    print(r)
    assert m1_re.match(r[0][0])
    assert m2_re.match(r[1][1])
    assert r[2][0] == "YOLO"
    assert r[2][1] == expand("~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST")



# Generated at 2022-06-14 05:49:49.728278
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test']
    d = load_env_file(lines, write_environ=None)

    assert d == {
        'TEST': '.../yeee',
        'THISIS': '.../a/test'
    }

# Generated at 2022-06-14 05:49:58.295973
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    values = parse_env_file_contents(lines)

    first = next(values)
    assert first == ('TEST', '.../yeee')

    second = next(values)
    assert second == ('THISIS', '.../a/test')

    third = next(values)
    assert third == ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')



# Generated at 2022-06-14 05:50:09.297853
# Unit test for function load_env_file
def test_load_env_file():
    import io

    lines = """
TEST=${HOME}/yeee-$PATH
THISIS=~/a/test
YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST
""".splitlines()

    env = load_env_file(lines)

    assert env["TEST"].startswith(os.getenv("HOME"))
    assert str(env["TEST"]).endswith(os.pathsep + os.getenv("PATH"))
    assert env["THISIS"].startswith(os.getenv("HOME"))
    assert env["YOLO"].startswith(os.getenv("HOME"))


if __name__ == "__main__":
    import sys

    load_env_file(sys.stdin)

# Generated at 2022-06-14 05:50:16.398218
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    text = """
    # This is a comment in the env file
    ASDF=123
    # This is another comment in the env file
    JKL=abc
    """
    results = parse_env_file_contents(text.split("\n"))

    assert collections.OrderedDict(results) == collections.OrderedDict([("ASDF", "123"), ("JKL", "abc")])



# Generated at 2022-06-14 05:50:27.024706
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    _write_environ = dict()
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    changes = load_env_file(lines, write_environ=_write_environ)
    assert changes == collections.OrderedDict(
        [('TEST', os.path.expanduser('${HOME}/yeee')),
         ('THISIS', os.path.expanduser('~/a/test')),
         ('YOLO', os.path.expanduser('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'))])



# Generated at 2022-06-14 05:50:39.346289
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import tempfile
    import textwrap
    import unittest

    class Tests(unittest.TestCase):
        def test_load_env_file_double_quoted(self):
            text = textwrap.dedent("""
            TEST='${HOME}/yeee'
            """)

            with tempfile.NamedTemporaryFile('w') as f:
                f.write(text)
                f.flush()

                with open(f.name, 'r') as f:
                    data = list(parse_env_file_contents(f))

            self.assertEqual(data, [('TEST', '${HOME}/yeee')])



# Generated at 2022-06-14 05:50:43.815331
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # TODO: Add assertions
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    list(parse_env_file_contents(lines))



# Generated at 2022-06-14 05:50:53.956295
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert list(parse_env_file_contents(lines)) == [('TEST', '${HOME}/yeee'), ('THISIS', '~/a/test'), ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]



# Generated at 2022-06-14 05:51:00.067507
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    from pprint import pprint
    from io import StringIO
    lines = [
        '# This is a comment',
        'TEST="This is a test with a quote: \\""',  # Test quote expansion
        "TEST='This is a test with a quote: \\\"\\n'",  # Test quote expansion
        'TEST=${HOME}/yeee',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST',
    ]
    fileobj = StringIO("\n".join(lines))
    results = parse_env_file_contents(fileobj)
    pprint(list(results))
    return list(results)



# Generated at 2022-06-14 05:51:11.058600
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    result = load_env_file(lines, write_environ=dict())
    assert result.get('TEST') == os.path.expanduser('~') + '/yeee'
    assert result.get('THISIS') == os.path.expanduser('~') + '/a/test'
    assert result.get('YOLO').startswith(os.path.expanduser('~') + '/swaggins/')

# Generated at 2022-06-14 05:51:22.764381
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ["TEST=${HOME}/yeee-$PATH", "THISIS=~/a/test",
             "YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"]
    values = parse_env_file_contents(lines)
    for k, v in values:
        if k == "TEST":
            assert v == os.path.dirname(__file__) + "/../yeee-" + \
                os.getenv("PATH")
        elif k == "THISIS":
            assert v == os.path.expanduser("~/a/test")

# Generated at 2022-06-14 05:51:29.751127
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    from furl.furl import furl

    _input = """THISIS=~/a/test
HOME=${HOME}
"""
    expected = [("THISIS", furl("~/a/test").url), ("HOME", furl("${HOME}").url)]

    contents = parse_env_file_contents(_input.split("\n"))
    actual = [x for x in contents]
    assert expected == actual



# Generated at 2022-06-14 05:51:35.937630
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = (
        'DATABASE_URL=${DB_HOST}/postgres?user=${DB_USER}',
    )
    dic = parse_env_file_contents(lines)
    assert dic == {
        'DATABASE_URL': '${DB_HOST}/postgres?user=${DB_USER}',
    }



# Generated at 2022-06-14 05:51:46.883743
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = [
        "TEST=${HOME}/yeee",
        "THISIS=~/a/test",
        "YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST",
    ]

    # Replace following function with `load_env_file` to test for this function
    # load_env_file(lines)
    result = parse_env_file_contents(lines)

    assert OrderedDict(result) == OrderedDict(
        [
            ("TEST", "..."),
            ("THISIS", "..."),
            ("YOLO", "..."),
        ]
    )

# Generated at 2022-06-14 05:52:00.016712
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    """
    Tests for function parse_env_file_contents.
    """
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    records = parse_env_file_contents(lines)
    records2 = parse_env_file_contents(lines)

    records = list(records)

    assert records[0][0] == 'TEST'
    assert records[0][1] == '${HOME}/yeee'

    assert records[1][0] == 'THISIS'
    assert records[1][1] == '~/a/test'

    assert records[2][0] == 'YOLO'

# Generated at 2022-06-14 05:52:08.166948
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())



# Generated at 2022-06-14 05:52:19.776667
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert list(parse_env_file_contents(['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'])) == [
        ('TEST', os.path.expanduser(os.path.expandvars('${HOME}/yeee-${PATH}'))),
        ('THISIS', os.path.expanduser(os.path.expandvars('~/a/test'))),
        ('YOLO', os.path.expanduser(os.path.expandvars('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')))
    ]

# Generated at 2022-06-14 05:52:31.263021
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    from io import StringIO
    from pprint import pprint

    lines = StringIO("""
    TEST=${HOME}/yeee
    THISIS=~/a/test
    YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST
    """)

    pprint(list(parse_env_file_contents(lines)))

    assert parse_env_file_contents(lines) == \
           [('test', '~/yeee'),
            ('thisis', '~/a/test'),
            ('yolo', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]



# Generated at 2022-06-14 05:52:37.611744
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    result = tuple(parse_env_file_contents(lines))
    expected = (('TEST', '.../yeee'), ('THISIS', '.../a/test'), ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'))
    assert result == expected, 'Got: {}'.format(result)



# Generated at 2022-06-14 05:52:51.298354
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    result = load_env_file(lines, write_environ=dict())

# Generated at 2022-06-14 05:53:04.690280
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    """
    This tests the function parse_env_file_contents.

    >>> lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    >>> load_env_file(lines, write_environ=dict())
    OrderedDict([('TEST', '.../yeee'),
             ('THISIS', '.../a/test'),
             ('YOLO',
              '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])
    """

# Generated at 2022-06-14 05:53:14.661019
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = [
        'TEST=${HOME}/yeee-$PATH',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST',
    ]

    changes = collections.OrderedDict(parse_env_file_contents(lines))

    assert len(changes) == 3

    assert changes.popitem()[1] == os.path.expanduser(
        '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    )

    assert changes.popitem()[1] == os.path.expanduser('~/a/test')

    key, val = changes.popitem()


# Generated at 2022-06-14 05:53:23.733367
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    loaded = load_env_file(lines, write_environ=None)
    assert loaded == {
        'TEST': expand('${HOME}/yeee'),
        'THISIS': expand('~/a/test'),
        'YOLO': expand('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'),
    }



# Generated at 2022-06-14 05:53:33.846824
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    values = parse_env_file_contents(['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'])

    assert values == [
        ('TEST', '.../yeee'),
        ('THISIS', '.../a/test'),
        ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    ]



# Generated at 2022-06-14 05:53:37.259238
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    contents = ["TEST=${HOME}/yeee",
                "THISIS=~/a/test",
                "YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"]

    assert tuple(parse_env_file_contents(contents)) == (
        ("TEST", "${HOME}/yeee"), ("THISIS", "~/a/test"),
        ("YOLO", "~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"))



# Generated at 2022-06-14 05:53:49.226154
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    changes = parse_env_file_contents(lines)

    assert changes == collections.OrderedDict([('TEST', '{HOME}/yeee-{PATH}'), ('THISIS', '~/a/test'), ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]), "env file parsing is broken"

# Generated at 2022-06-14 05:53:58.017572
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    result = dict(parse_env_file_contents(lines))
    assert result == {'YOLO': '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST',
                      'THISIS': '~/a/test',
                      'TEST': '${HOME}/yeee'}


# Generated at 2022-06-14 05:54:11.626760
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert list(parse_env_file_contents([])) == []


# Generated at 2022-06-14 05:54:12.803282
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 05:54:22.824557
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert parse_env_file_contents(['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']) == [
        ('TEST', '${HOME}/yeee-$PATH'),
        ('THISIS', '~/a/test'),
        ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    ]



# Generated at 2022-06-14 05:54:35.794510
# Unit test for function parse_env_file_contents

# Generated at 2022-06-14 05:54:44.958754
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    expected_result = {'TEST': '.../yeee', 'THISIS': '.../a/test', 'YOLO': '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'}

    result = parse_env_file_contents(lines)
    for key, value in result:
        assert value == expected_result[key]



# Generated at 2022-06-14 05:54:50.084540
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    load_env_file(lines, write_environ=dict())

    assert True

# Generated at 2022-06-14 05:55:00.051773
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import textwrap

    def parse_and_verify(source, result):
        lines = [line for line in textwrap.dedent(source).strip().splitlines()]
        if list(parse_env_file_contents(lines)) != result:
            raise Exception('Expected %r but got %r' % (result, list(parse_env_file_contents(lines))))

    parse_and_verify('', [])
    parse_and_verify('test=test', [('test', 'test')])
    parse_and_verify('test=\n', [('test', '')])
    parse_and_verify('test=test\n', [('test', 'test')])
    parse_and_verify('test = test', [('test', 'test')])

# Generated at 2022-06-14 05:55:08.728875
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    load_env_file(lines, write_environ=dict())
    assert 'TEST' in os.environ
    assert 'THISIS' in os.environ
    assert 'YOLO' in os.environ



# Generated at 2022-06-14 05:55:22.628685
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    expected = {'TEST': expand('${HOME}/yeee'), 'THISIS': expand('~/a/test'), 'YOLO': expand('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')}

    assert list(parse_env_file_contents(lines)) == list(expected.items())



# Generated at 2022-06-14 05:55:31.198518
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    kv = [x for x in parse_env_file_contents(['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'])]
    assert kv == [('TEST', '.../.../yeee-...:...'), ('THISIS', '.../a/test'), ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]



# Generated at 2022-06-14 05:55:40.566327
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    f = open('tests/fixtures/sample_env_file')
    data = parse_env_file_contents(f)

    assert next(data) == ('TEST', '${HOME}/yeee')
    assert next(data) == ('THISIS', '~/a/test')
    assert next(data) == ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    assert next(data) == ('TWO', 'TWO')



# Generated at 2022-06-14 05:55:45.157078
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ["TEST=${HOME}/yeee", "THISIS=~/a/test", "YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"]

    expected = {"TEST": "hello", "THISIS": "hello", "YOLO": "hello"}

    results = {}

    for k, v in parse_env_file_contents(lines):
        results[k] = v

    assert expected == results
    assert load_env_file(lines) == results



# Generated at 2022-06-14 05:55:55.493787
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    test_dict = dict(parse_env_file_contents(lines))
    assert test_dict['TEST'] == os.environ['HOME'] + '/yeee'
    assert test_dict['THISIS'] == os.environ['HOME'] + '/a/test'
    assert test_dict['YOLO'] == os.environ['HOME'] + '/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'



# Generated at 2022-06-14 05:56:03.153199
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert list(parse_env_file_contents(lines)) == [('TEST', '${HOME}/yeee'), ('THISIS', '~/a/test'),
                                                    ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]



# Generated at 2022-06-14 05:56:11.356899
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert list(parse_env_file_contents(lines=[])) == []

    assert list(parse_env_file_contents(lines=['ABC=123'])) == [('ABC', '123')]

    assert list(parse_env_file_contents(lines=['ABC="hej"'])) == [('ABC', 'hej')]
    assert list(parse_env_file_contents(lines=['ABC="hej med dig"'])) == [('ABC', 'hej med dig')]
    assert list(parse_env_file_contents(lines=['ABC="hej med dig og\n dig og"'])) == [('ABC', 'hej med dig og\n dig og')]

# Generated at 2022-06-14 05:56:20.460562
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    contents = '''
    # comment line
    TEST=${HOME}/yeee
    THISIS=~/a/test
    YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST
    '''

    lines = parse_env_file_contents(contents.splitlines())

    expected = [
        'TEST',
        'THISIS',
        'YOLO',
    ]

    actual = [k for k, v in lines]

    assert actual == expected

# Generated at 2022-06-14 05:56:31.296197
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # Test data from honcho
    from io import StringIO

    lines = StringIO("""TEST=${HOME}/yeee
THISIS=${NOTHING}/a/test
YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST""")

    parsed = parse_env_file_contents(lines.readlines())

    # Check each line
    assert ('TEST', expand('${HOME}/yeee')) == next(parsed)
    assert ('THISIS', expand('${NOTHING}/a/test')) == next(parsed)
    assert ('YOLO', expand('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')) == next(parsed)

    #

# Generated at 2022-06-14 05:56:42.229268
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    dict_values = []
    write_environ = dict()

    for k, v in parse_env_file_contents(lines):
        dict_values.append((k, v))
        write_environ[k] = v

    dict_values = dict(dict_values)


# Generated at 2022-06-14 05:56:56.032155
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = [
        'TEST=${HOME}/yeee',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    ]
    assert dict(parse_env_file_contents(lines)) == {
        'TEST': '${HOME}/yeee',
        'THISIS': '~/a/test',
        'YOLO': '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    }



# Generated at 2022-06-14 05:56:57.564050
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 05:57:07.898084
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    result = load_env_file(lines, write_environ=dict())
    assert result == collections.OrderedDict([('TEST', '.../yeee'), ('THISIS', '.../a/test'), ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])



# Generated at 2022-06-14 05:57:18.599848
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    values = dict(parse_env_file_contents(lines))

    assert values['TEST'] == f"{os.environ['HOME']}/yeee"
    assert values['THISIS'] == f"{os.environ['HOME']}/a/test"
    assert values['YOLO'] == f"{os.environ['HOME']}/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"



# Generated at 2022-06-14 05:57:28.365594
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert parse_env_file_contents(["TEST=${HOME}/yeee", "THISIS=~/a/test", "YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"]) == [("TEST", os.path.expanduser("~/yeee")), ("THISIS", os.path.expanduser("~/a/test")), ("YOLO", os.path.expanduser("~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"))]

# Generated at 2022-06-14 05:57:40.912134
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert tuple(parse_env_file_contents(iter(['TEST=${HOME}/yeee']))) == (('TEST', expand('${HOME}/yeee')),)
    assert tuple(parse_env_file_contents(iter(['TEST=${HOME}/yeee']))) == (('TEST', expand('${HOME}/yeee')),)
    assert tuple(parse_env_file_contents(iter(['TEST=~/yeee']))) == (('TEST', expand('~/yeee')),)
    assert tuple(parse_env_file_contents(iter(['TEST=$PATH']))) == (('TEST', expand('$PATH')),)

# Generated at 2022-06-14 05:57:53.291526
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert list(parse_env_file_contents(['A=B', 'C=D'])) == [('A', 'B'), ('C', 'D')]
    assert list(parse_env_file_contents(['A="B C"', 'C=D'])) == [('A', 'B C'), ('C', 'D')]
    assert list(parse_env_file_contents(['A="B\\"C"', 'C=D'])) == [('A', 'B"C'), ('C', 'D')]
    assert list(parse_env_file_contents(['A=\'B\\\'C\'', 'C=D'])) == [('A', 'B\'C'), ('C', 'D')]

# Generated at 2022-06-14 05:58:04.591901
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # Check for invalid files.
    for lines in (['TEST']), (['FOO=BAR', 'BAR$=FOO']), (['FOO=BAR', 'BAR=FOO=']):
        with pytest.raises(AssertionError):
            list(parse_env_file_contents(lines))

    # Check for valid files.
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

# Generated at 2022-06-14 05:58:12.159002
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    """
    >>> lines = ['TEST=${HOME}', 'THISIS=~/a/test']
    >>> parse_env_file_contents(lines)
    <generator object parse_env_file_contents at 0x7f6e1f44acd0>
    >>>
    >>> env_vars = parse_env_file_contents(lines)
    >>> for key, value in env_vars: print(f'{key}: {value}')
    ...
    TEST: /home/user
    THISIS: /home/user/a/test
    """
    pass



# Generated at 2022-06-14 05:58:24.734203
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import io
    import unittest

    class TestEnvFile(unittest.TestCase):
        def test_parse(self):
            lines = ('TEST=$HOME/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
            result = dict(parse_env_file_contents(lines))

            self.assertEqual(result['TEST'], '$HOME/yeee')
            self.assertEqual(result['THISIS'], '~/a/test')
            self.assertEqual(result['YOLO'], '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
