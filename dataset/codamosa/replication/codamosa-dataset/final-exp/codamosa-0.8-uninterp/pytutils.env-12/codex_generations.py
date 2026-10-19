

# Generated at 2022-06-14 05:49:16.881864
# Unit test for function load_env_file
def test_load_env_file():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    environ = dict()

    result = load_env_file(lines, write_environ=environ)

    assert result['TEST'] == os.path.join(os.environ['HOME'], 'yeee-', os.environ['PATH'])
    assert result['THISIS'] == os.path.join(os.environ['HOME'], 'a', 'test')

# Generated at 2022-06-14 05:49:25.591271
# Unit test for function load_env_file
def test_load_env_file():
    assert load_env_file(
        lines=[
            "HOME=/home/test",
            "PATH=/usr:/bin:$PATH",
        ],
        write_environ=dict(),
    ) == collections.OrderedDict([
        ("HOME", "/home/test"),
        ("PATH", "/usr:/bin:$PATH"),
    ])

    assert load_env_file(
        lines=[
            "HOME=/home/test",
            "PATH=/usr:/bin:$PATH",
        ],
        write_environ=dict(
            PATH="/path/to/bin",
        ),
    ) == collections.OrderedDict([
        ("HOME", "/home/test"),
        ("PATH", "/usr:/bin:/path/to/bin"),
    ])

# Generated at 2022-06-14 05:49:30.750660
# Unit test for function load_env_file
def test_load_env_file():
    import doctest

    doctest.testmod()


if __name__ == '__main__':
    test_load_env_file()

# Generated at 2022-06-14 05:49:41.260708
# Unit test for function load_env_file
def test_load_env_file():
    import tempfile

    data = [
        "TEST=${HOME}/yeee-$PATH",
        "THISIS=~/a/test",
        "YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST",
        "SPACES=$ENV_WITH_SPACES"
    ]

    os.environ["ENV_WITH_SPACES"] = "hello world"

    with tempfile.TemporaryDirectory() as tmp:
        with open(os.path.join(tmp, "env"), "w+") as tmp_env:
            tmp_env.write("\n".join(data))
            tmp_env.flush()

            values = load_env_file(tmp_env, write_environ=None)


# Generated at 2022-06-14 05:49:54.193282
# Unit test for function load_env_file
def test_load_env_file():
    data = [
        ('TEST=${HOME}/yeee-$PATH', 'TEST', '.../.../yeee-...:...'),
        ('THISIS=~/a/test', 'THISIS', '.../a/test'),
        ('YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST', 'YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    ]

    loaded = load_env_file(data, write_environ=None)

    assert isinstance(loaded, collections.OrderedDict)

    for k, v in data:
        assert k.split('=')[0] in loaded
        assert loaded[k.split('=')[0]] == v

# Generated at 2022-06-14 05:50:04.728849
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = [
        'TEST=${HOME}/yeee',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    ]
    assert list(parse_env_file_contents(lines)) == [
        ('TEST', '${HOME}/yeee'),
        ('THISIS', '~/a/test'),
        ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    ]



# Generated at 2022-06-14 05:50:13.369911
# Unit test for function load_env_file
def test_load_env_file():
    filename = os.path.abspath(os.path.join(os.path.dirname(__file__), 'fixtures', 'env_file'))
    write_environ = os.environ

    changes = load_env_file(filename, write_environ)
    assert changes['TEST'] == '.../.../yeee-...:...'
    assert changes['THISIS'] == '.../a/test'
    assert changes['YOLO'] == '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'



# Generated at 2022-06-14 05:50:23.618113
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    values = load_env_file(lines, write_environ=dict())
    # Create list containing the expected results
    expected = []
    expected.append(['TEST', os.path.expanduser('~/yeee')])
    expected.append(['THISIS', os.path.expanduser('~/a/test')])
    expected.append(['YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'])
    assert values == collections.OrderedDict(expected)

# Generated at 2022-06-14 05:50:29.972561
# Unit test for function load_env_file
def test_load_env_file():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    results = load_env_file(lines, write_environ=dict())
    print(results)


if __name__ == '__main__':
    test_load_env_file()

# Generated at 2022-06-14 05:50:40.837664
# Unit test for function load_env_file
def test_load_env_file():
    import io

    # Test for file with one variable
    data = io.StringIO('TEST=${HOME}/yeee\n')
    assert load_env_file(data, write_environ=dict()) == collections.OrderedDict([('TEST', './yeee')])

    # Test for file with three variables
    data = io.StringIO('TEST=${HOME}/yeee-$PATH\nTHISIS=~/a/test\nYOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')

# Generated at 2022-06-14 05:50:52.153046
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    changes = load_env_file(lines, write_environ=dict())

    print(changes['TEST'])
    assert isinstance(changes, collections.OrderedDict)
    assert changes['TEST'] == expand('${HOME}/yeee')
    assert changes['THISIS'] == expand('~/a/test')
    assert changes['YOLO'] == expand('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')

    print(changes)



# Generated at 2022-06-14 05:50:58.096895
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    results = load_env_file(lines, write_environ=dict())
    assert isinstance(results, collections.OrderedDict)
    assert len(results) == 3



# Generated at 2022-06-14 05:51:05.492137
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    env = load_env_file(lines, write_environ=dict())
    assert isinstance(env, collections.OrderedDict)
    assert 'TEST' in env
    assert '${HOME}' not in env['TEST']
    assert '~' not in env['THISIS'] and '~' in env['YOLO']



# Generated at 2022-06-14 05:51:12.115323
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = [
        'TEST=${HOME}/yeee',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST',
        'NOW_WE_TEST_ESCAPE_CHARS=\'"\\\a\b\f\n\r\t\v',
    ]


# Generated at 2022-06-14 05:51:20.976752
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert list(parse_env_file_contents(lines=
    ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'],)) == \
           [('TEST', '.../yeee'),
            ('THISIS', '.../a/test'),
            ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]



# Generated at 2022-06-14 05:51:28.475906
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    """
    Tests for function parse_env_file_contents
    """
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    expected = [
        ('TEST', '${HOME}/yeee-$PATH'),
        ('THISIS', '~/a/test'),
        ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'),
    ]
    results = list(parse_env_file_contents(lines))
    assert results == expected



# Generated at 2022-06-14 05:51:37.938898
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    test_vals = dict(
        test_basic='test=test_val',
        test_complex='test2=${HOME}/yeee-$PATH',
        test_quoted1='test="quoted_val"',
        test_quoted2='test2="${HOME}/foo-$VAL"',
        test_quoted3="test3='quoted_val'",
        test_quoted4="test4='${HOME}/foo-$VAL'",
    )

    for k, v in test_vals.items():
        values = parse_env_file_contents((v,))

        assert tuple(values)[0] == ('test', 'test_val')
        assert tuple(values)[0] == ('test2', '${HOME}/yeee-$PATH')

# Generated at 2022-06-14 05:51:49.180435
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    content = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert parse_env_file_contents(lines=content) == [
        ('TEST', os.environ['HOME'] + '/yeee-' + os.environ['PATH']),
        ('THISIS', os.environ['HOME'] + '/a/test'),
        ('YOLO', os.environ['HOME'] + '/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]

    # Unit test for function load_env_file

# Generated at 2022-06-14 05:51:58.965015
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import pytest

    assert parse_env_file_contents(["TEST=123"]) == [("TEST", "123")]
    assert parse_env_file_contents(["TEST=123", "TEST2=456"]) == [("TEST", "123"), ("TEST2", "456")]
    assert parse_env_file_contents(["TEST=123", "# Hello", "# There", "TEST2=456"]) == [("TEST", "123"), ("TEST2", "456")]
    assert parse_env_file_contents(["# Hello", "# There", "TEST=123", "TEST2=456"]) == [("TEST", "123"), ("TEST2", "456")]

    with pytest.raises(ValueError):
        parse_env_file_cont

# Generated at 2022-06-14 05:52:09.979598
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    values = parse_env_file_contents(lines)

    assert isinstance(values, collections.abc.Generator) is True
    assert isinstance(list(values), list) is True
    assert len(list(values)) == 3
    assert list(values) == [('TEST', '.../yeee'), ('THISIS', '.../a/test'),
                            ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]


# Generated at 2022-06-14 05:52:23.118330
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    """
    Tests parsing of env file content.

    >>> lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    >>> load_env_file(lines, write_environ=dict())
    OrderedDict([('TEST', '.../yeee'),
             ('THISIS', '.../a/test'),
             ('YOLO',
              '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])
    """

# Generated at 2022-06-14 05:52:32.773539
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    expected = [('TEST', '.../yeee'),
                ('THISIS', '.../a/test'),
                ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]

    assert parse_env_file_contents(lines) == expected



# Generated at 2022-06-14 05:52:38.966072
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    data = list(parse_env_file_contents(lines))

    if isinstance(data[0], tuple):
        pass
    else:
        raise ValueError("Expected tuple, got {}".format(data[0]))

    if len(data[0]) == 2:
        pass
    else:
        raise ValueError("Expected tuple of length 2, got {}".format(data[0]))

    if data[0][0] == 'TEST':
        pass

# Generated at 2022-06-14 05:52:48.679792
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    """
    The function parse_env_file_contents parses an env file (content) and returns the result as a generator.

    >>> lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    >>> load_env_file(lines)
    OrderedDict([('TEST', '.../yeee'),
             ('THISIS', '.../a/test'),
             ('YOLO',
              '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])
    """



# Generated at 2022-06-14 05:53:01.971514
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert list(parse_env_file_contents(lines)) == [
        ('TEST', os.path.expanduser(os.path.expandvars('${HOME}/yeee'))),
        ('THISIS', os.path.expanduser(os.path.expandvars('~/a/test'))),
        ('YOLO', os.path.expanduser(os.path.expandvars('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')))]

# Generated at 2022-06-14 05:53:13.122094
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # Test: Parse env file content with HOME variable
    def test_env_file_contents_with_home_variable():
        lines = [
            'TEST=${HOME}/yeee',
            'THISIS=~/a/test',
            'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
        ]

        load_env_file(lines)

    # Test: Parse env file content with PATH variable

# Generated at 2022-06-14 05:53:21.107879
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    expected = collections.OrderedDict([
        ('TEST', '${HOME}/yeee'),
        ('THISIS', '~/a/test'),
        ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    ])

    values = parse_env_file_contents(lines)
    changes = collections.OrderedDict(values)

    assert changes == expected



# Generated at 2022-06-14 05:53:26.492349
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    from unittest import TestCase

    lines = ["TEST='this is a test'", "TEST2='this is a second test'"]

    env = parse_env_file_contents(lines)

    assert list(env) == [('TEST', 'this is a test'), ('TEST2', 'this is a second test')]

# Generated at 2022-06-14 05:53:33.126978
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    out = load_env_file(lines, write_environ=dict())
    assert "TEST=/Users/mattman/Documents/Lighthouse/solar/yeee-/usr/bin:/bin:/usr/sbin:/sbin" in out.values()
    assert "THISIS=/Users/mattman/a/test" in out.values()
    assert "YOLO=/Users/mattman/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST" in out.values()



# Generated at 2022-06-14 05:53:37.800542
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())



# Generated at 2022-06-14 05:53:51.589612
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert load_env_file(lines, write_environ=dict()) == collections.OrderedDict(
        [('TEST', os.path.expandvars(os.path.expanduser('${HOME}/yeee'))),
         ('THISIS', os.path.expandvars(os.path.expanduser('~/a/test'))),
         ('YOLO', os.path.expandvars(os.path.expanduser('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')))])

# Generated at 2022-06-14 05:53:59.113558
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    contents = list(parse_env_file_contents(lines))

    # Check that the number of items is correct
    assert len(contents) == len(lines)

    # Check the content of the first item
    first_key, first_val = contents[0]
    assert first_key == 'TEST'
    assert first_val == os.path.expanduser('~') + '/yeee'

    # Check the content of the second item
    second_key, second_val = contents[1]
    assert second_key == 'THISIS'

# Generated at 2022-06-14 05:54:12.059944
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import unittest
    from itertools import islice
    from unittest.mock import patch

    class Test_parse_env_file_contents(unittest.TestCase):
        def setUp(self):
            self.lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']


# Generated at 2022-06-14 05:54:24.580034
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert load_env_file(lines, write_environ=dict()) == collections.OrderedDict(
        [('TEST', '.../yeee'),
         ('THISIS', '.../a/test'),
         ('YOLO',
          '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])


if __name__ == "__main__":
    test_parse_env_file_contents()

# Generated at 2022-06-14 05:54:36.678146
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    values = parse_env_file_contents(lines)
    changes = collections.OrderedDict()

    for k, v in values:
        v = expand(v)

        changes[k] = v

    assert changes == collections.OrderedDict([
        ('TEST', '.../.../yeee-...:...'),
        ('THISIS', '.../a/test'),
        ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'),
    ])



# Generated at 2022-06-14 05:54:42.884182
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

# Generated at 2022-06-14 05:54:48.727207
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    for line in parse_env_file_contents(lines):
        key, value = line
        print(f'{key}={value}')



# Generated at 2022-06-14 05:54:59.244478
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    env_text = """
    # Comment
    TEST=${HOME}/yeee-$PATH
    STUFF=this is $PATH
    THINGS=this is "another $PATH"
    SINGLE="single quotes"
    DOUBLE='double quotes'
    EMPTY= 
    """
    e = parse_env_file_contents(env_text.splitlines())

    assert (next(e) == ("TEST", os.path.join(os.environ["HOME"], "yeee-", os.environ["PATH"])))
    assert (next(e) == ("STUFF", "this is " + os.environ["PATH"]))
    assert (next(e) == ("THINGS", "this is another " + os.environ["PATH"]))

# Generated at 2022-06-14 05:55:12.468928
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # Test with varying line endings
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    for seperator in (os.linesep, "\n", "\r\n"):
        assert dict(parse_env_file_contents(seperator.join(lines))) == dict(parse_env_file_contents(lines))

    # Test single lined strings

# Generated at 2022-06-14 05:55:21.347526
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # Execute the function under test
    result = list(parse_env_file_contents(lines=["TEST=${HOME}/yeee", "THISIS=~/a/test", "YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"]))

    # Assert the result
    assert result == [("TEST", "~/yeee"), ("THISIS", "~/a/test"), ("YOLO", "~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST")]



# Generated at 2022-06-14 05:55:31.712134
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    """
    >>> lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    >>> load_env_file(lines, write_environ=dict())
    OrderedDict([('TEST', '.../yeee'),
             ('THISIS', '.../a/test'),
             ('YOLO',
              '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])
    """
    pass



# Generated at 2022-06-14 05:55:38.034091
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = [
        "TEST=$HOME/yeee",
        "THISIS=~/a/test",
        "YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST",
        "",
        "# This is a comment.",
        "",
        "ANOTHER=$TEST",
    ]



# Generated at 2022-06-14 05:55:45.909471
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import pprint

    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    TEST_VALUES = dict()
    for k, v in parse_env_file_contents(lines):
        TEST_VALUES[k] = v

    pprint.pprint(TEST_VALUES)



# Generated at 2022-06-14 05:55:56.022709
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    """
    Tests the parse_env_file_contents function

    >>> from io import StringIO
    >>> with StringIO('TEST=${HOME}/yeee\nTHISIS=~/a/test\nYOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST') as f:
    ...     for k, v in parse_env_file_contents(f):
    ...         print('{}={}'.format(k, v))
    TEST=.../yeee
    THISIS=.../a/test
    YOLO=.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST
    """



# Generated at 2022-06-14 05:56:07.222262
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = [
        "# comment",
        "TEST=\"${HOME}/yeee\"",
        "THISIS=~/a/test",
        "YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST",
        "YOLO_2=value",
    ]

    # NOTE: --parallel does not work with doctests.

# Generated at 2022-06-14 05:56:13.268912
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 05:56:24.438806
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    os.environ['PATH'] = '...'

    assert load_env_file(lines, write_environ=dict()) == {
        'TEST': os.path.expanduser('~') + '/yeee',
        'THISIS': os.path.expanduser('~') + '/a/test',
        'YOLO': os.path.expanduser('~') + '/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    }


# Generated at 2022-06-14 05:56:30.987999
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    envfile_contents = '''TEST=${HOME}/yeee
    THISIS=~/a/test
    YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'''
    parse_env_file_contents(envfile_contents.splitlines())


if __name__ == '__main__':
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 05:56:42.130521
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    filename = "tests/test_env_file"
    with open(filename) as f:
        lines = parse_env_file_contents(f)
        d = load_env_file(lines)

        assert len(d) == 26
        assert d["TEST_1"] == "test_1"
        assert d["TEST_2"] == "test_2"
        assert d["TEST_3"] == ""
        assert d["TEST_4"] == "test_4"
        assert d["TEST_5"] == "test_5"
        assert d["TEST_6"] == "test_6"
        assert d["TEST_8"] == "test_8"
        assert d["TEST_9"] == "test_9"
        assert d["TEST_10"] == "test_10"


# Generated at 2022-06-14 05:56:55.097588
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    answer = collections.OrderedDict(parse_env_file_contents(lines))
    expected = collections.OrderedDict([('TEST', '.../yeee'),
                                        ('THISIS', '.../a/test'),
                                        ('YOLO',
                                         '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])

    for k, v in expected.items():
        try:
            assert answer[k] == v
        except AssertionError:
            assert answer[k] is v



# Generated at 2022-06-14 05:57:10.311435
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    res = load_env_file(lines, write_environ=dict())
    correct_res = collections.OrderedDict([('TEST', '.../yeee'),
                                           ('THISIS', '.../a/test'),
                                           ('YOLO',
                                            '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])
    assert res == correct_res



# Generated at 2022-06-14 05:57:22.453761
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    """
    Parses env file content.

    >>> lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    >>> load_env_file(lines, write_environ=dict())
    OrderedDict([('TEST', '.../yeee'),
             ('THISIS', '.../a/test'),
             ('YOLO',
              '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])
    """

# Generated at 2022-06-14 05:57:31.853507
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert list(parse_env_file_contents(lines)) == [('TEST', '${HOME}/yeee'),
                                                    ('THISIS', '~/a/test'),
                                                    ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]



# Generated at 2022-06-14 05:57:40.448583
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert list(parse_env_file_contents(lines)) == [('TEST', '${HOME}/yeee'), ('THISIS', '~/a/test'), ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]



# Generated at 2022-06-14 05:57:48.272785
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    """
    Tests the function parse_env_file_contents.
    """
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())



# Generated at 2022-06-14 05:57:59.919752
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = """TEST=${HOME}/yeee-$PATH
    THISIS=~/a/test
    YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST""".strip().split("\n")

    parsed = list(parse_env_file_contents(lines))

    expected = [("TEST", "{HOME}/yeee-$PATH"),
                ("THISIS", "~/a/test"),
                ("YOLO", "~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST")]

    print("Expected:")
    print("\n".join("%s %s" % (key, repr(val)) for (key, val) in expected))

    print("Actual:")

# Generated at 2022-06-14 05:58:13.052087
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    mapping = load_env_file(lines, write_environ=dict())
    assert mapping == {'TEST': os.path.join(os.getenv('HOME'), 'yeee'),
                       'THISIS': os.path.join(os.getenv('HOME'), 'a', 'test'),
                       'YOLO': os.path.join(os.getenv('HOME'), 'swaggins', '$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
                       }

# Generated at 2022-06-14 05:58:25.907741
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # Test a single entry
    lines = ['TEST=${HOME}/yeee']
    values = [(key, val) for key, val in parse_env_file_contents(lines)]
    assert len(values) == 1
    key, val = values[0]
    assert key == 'TEST'
    assert val == '${HOME}/yeee'

    # Test two entries
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test']
    values = [(key, val) for key, val in parse_env_file_contents(lines)]
    assert len(values) == 2
    key, val = values[0]
    assert key == 'TEST'
    assert val == '${HOME}/yeee'

    key, val = values[1]
   

# Generated at 2022-06-14 05:58:32.613497
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    parse_env_file_contents(lines)


if __name__ == '__main__':
    test_parse_env_file_contents()

# Generated at 2022-06-14 05:58:44.966768
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    try:
        _a = os.environ['TEST']
    except:
        _a = os.getenv('TEST')
    try:
        _b = os.environ['THISIS']
    except:
        _b = os.getenv('THISIS')
    try:
        _c = os.environ['YOLO']
    except:
        _c = os.getenv('YOLO')
    test_vals = {
        'TEST': _a,
        'THISIS': _b,
        'YOLO': _c,
    }
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    test

# Generated at 2022-06-14 05:59:05.458410
# Unit test for function parse_env_file_contents