

# Generated at 2022-06-14 05:49:16.635128
# Unit test for function load_env_file
def test_load_env_file():
    test_lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    test_output = load_env_file(test_lines)

# Generated at 2022-06-14 05:49:27.381535
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # In the following strings, \n should be in the end of each string.
    # This also implies that the function should work with lines ending with \n.
    # The following strings are actually lines from a .env file.
    s = "TEST=${HOME}/yeee\n"
    assert list(parse_env_file_contents([s]))[0] == ("TEST", "~/yeee")

    s = 'THISIS="~/a/test"\n'
    assert list(parse_env_file_contents([s]))[0] == ("THISIS", "~/a/test")

    s = "YOLO='~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'\n"

# Generated at 2022-06-14 05:49:32.895855
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())



# Generated at 2022-06-14 05:49:34.368403
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 05:49:40.121393
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

# Generated at 2022-06-14 05:49:53.464042
# Unit test for function load_env_file
def test_load_env_file():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    import os
    import tempfile

    writes = {}

    changes = load_env_file(lines, writes)

    assert writes == {'TEST': tempfile.gettempdir() + '/yeee-', 'THISIS': tempfile.gettempdir() + '/a/test',
                      'YOLO': tempfile.gettempdir() + '/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'}
    assert changes['TEST'].startswith(tempfile.gettempdir())

# Generated at 2022-06-14 05:50:03.621822
# Unit test for function load_env_file
def test_load_env_file():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    result = load_env_file(lines, write_environ=dict())

    assert result == collections.OrderedDict([('TEST', '.../.../yeee-...:...'),
                                              ('THISIS', '.../a/test'),
                                              ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])

# Generated at 2022-06-14 05:50:10.669267
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    with pytest.raises(ValueError):
        vals = [('NAME', os.environ['USER']), ('export', '1234'), ('HOST', os.uname()[1])]
        envvars = parse_env_file_contents(vals)
        for k, v in envvars:
            print(f'{k}: {v}')



# Generated at 2022-06-14 05:50:21.230593
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert dict(parse_env_file_contents(lines)) == {
        'TEST': '%s/yeee-%s' % (os.environ['HOME'], os.environ['PATH']),
        'THISIS': '%s/a/test' % (os.environ['HOME']),
        'YOLO': '%s/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST' % (os.environ['HOME'])
    }

# Generated at 2022-06-14 05:50:29.151385
# Unit test for function load_env_file
def test_load_env_file():
    import sys

    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    with open(__file__) as f:
        lines.append(f'SCRIPT_PATH={f.name}')

# Generated at 2022-06-14 05:50:40.656231
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert [item for item in parse_env_file_contents(['TEST=${HOME}/yeee'])] == [('TEST', '.../yeee')]

    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert [item for item in parse_env_file_contents(lines)] == [('TEST', '.../yeee'), ('THISIS', '.../a/test'), ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]



# Generated at 2022-06-14 05:50:47.179276
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ["TEST=$HOME/yeee-$PATH", "THISIS=~/a/test", "YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"]
    test_case = list(parse_env_file_contents(lines))
    if test_case[0] != ("TEST", "$HOME/yeee-$PATH"):
        print(test_case[0])
        raise ValueError()
    if test_case[1] != ("THISIS", "~/a/test"):
        raise ValueError()
    if test_case[2] != ("YOLO", "~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"):
        raise ValueError()
    return True

# Generated at 2022-06-14 05:50:58.411332
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    line1 =  "TEST=${HOME}/yeee"
    line2 =  "THISIS=~/a/test"
    line3 =  "YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"
    line4 = "FOO=BAR"
    line5 = "HOO=$HOME/foo"

    lines = [line1, line2, line3, line4, line5]
    values = parse_env_file_contents(lines)

    result = collections.OrderedDict()
    for k, v in values:
        result[k] = v

    assert result["TEST"] == os.path.abspath(os.path.join(os.path.expanduser("~"), "yeee"))

# Generated at 2022-06-14 05:51:11.364692
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = [
        'TEST=${HOME}/yeee-$PATH',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST',
        '',
        '# A comment',
        '#COMMENT=value',
        'COMMENT=value',
        ' # lots of whitespaces',
        '   # more whitespaces',
        ' \t#tabbin',
        '  \t\t #more tabbin',
    ]


# Generated at 2022-06-14 05:51:23.053265
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    env_lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    environ_changes = parse_env_file_contents(env_lines)

    # Check results
    assert len(environ_changes) == 3


# Generated at 2022-06-14 05:51:25.849829
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert parse_env_file_contents(['TEST=1', 'TEST2=2']) == \
        [('TEST', '1'), ('TEST2', '2')]



# Generated at 2022-06-14 05:51:33.573165
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())
    assert lines == ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']



# Generated at 2022-06-14 05:51:46.533144
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    import pprint
    pprint.pprint(load_env_file(lines, write_environ=dict()))
    pprint.pprint((dict(load_env_file(lines, write_environ=dict()))))

# Generated at 2022-06-14 05:51:52.887062
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    results = parse_env_file_contents(lines)

    for k, v in results:
        print(k, "=", v)


# Generated at 2022-06-14 05:52:03.520788
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = [
        "TEST=${HOME}/yeee-$PATH",
        "THISIS=~/a/test",
        "YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST",
    ]

    values = parse_env_file_contents(lines)

    assert next(values) == ("TEST", "{HOME}/yeee-{PATH}")
    assert next(values) == ("THISIS", "~/a/test")
    assert next(values) == ("YOLO", "~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST")



# Generated at 2022-06-14 05:52:11.179775
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=$HOME/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    assert dict(parse_env_file_contents(lines)) == dict(
        TEST='${HOME}/yeee',
        THISIS='~/a/test',
        YOLO='~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST',
    )



# Generated at 2022-06-14 05:52:22.194309
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # Arrange
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    # Act
    result = parse_env_file_contents(lines)

    # Assert
    assert isinstance(result, collections.Generator)
    assert next(result) == ('TEST', os.path.expanduser('~/yeee'))
    assert next(result) == ('THISIS', os.path.expanduser('~/a/test'))
    assert next(result) == ('YOLO', os.path.expanduser('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'))



# Generated at 2022-06-14 05:52:31.229415
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert list(parse_env_file_contents(['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'])) == [
        ('TEST', '~/yeee-$PATH'),
        ('THISIS', '~/a/test'),
        ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'),
    ]

# Generated at 2022-06-14 05:52:38.458071
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # Test 1
    test1_filename = 'test1.env'
    test1_lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    # Write test file
    with open(test1_filename, 'w') as test1_file:
        for test1_line in test1_lines:
            test1_file.write(test1_line + '\n')

    # Collect output
    test1_output = []

    # Call function
    with open(test1_filename, 'r') as test1_file:
        for test1_line in test1_file:
            test1_output.append(test1_line)

    # Ass

# Generated at 2022-06-14 05:52:42.883254
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # type: () -> None
    env = parse_env_file_contents(['TEST=123', 'HOME=/home/test'])
    assert list(env) == [('TEST', '123'), ('HOME', '/home/test')]



# Generated at 2022-06-14 05:52:52.825210
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert list(parse_env_file_contents(lines)) == [('TEST', os.path.expandvars('${HOME}/yeee')), ('THISIS', os.path.expanduser('~/a/test')), ('YOLO', os.path.expanduser('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'))]



# Generated at 2022-06-14 05:53:04.803424
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    """
    Unit test for function `parse_env_file_contents`.
    """
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    t = load_env_file(lines, write_environ=dict())

    assert t['TEST'].endswith('/yeee')
    assert t['THISIS'].endswith('/a/test')
    assert t['YOLO'].endswith('/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')

# Generated at 2022-06-14 05:53:12.411421
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    results = parse_env_file_contents(lines)
    assert results == {'TEST': '${HOME}/yeee', 'THISIS': '~/a/test', 'YOLO': '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'}

# Generated at 2022-06-14 05:53:21.214382
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    environ = collections.OrderedDict()

    for key, val in parse_env_file_contents(lines):
        environ[key] = val

    assert environ == collections.OrderedDict(
        [('TEST', expand(expand('${HOME}/yeee'))), ('THISIS', expand(expand('~/a/test'))), ('YOLO', expand(expand('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')))])



# Generated at 2022-06-14 05:53:27.680631
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import pprint
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    pprint.pprint(load_env_file(lines, write_environ=os.environ))


if __name__ == '__main__':
    test_parse_env_file_contents()

# Generated at 2022-06-14 05:53:39.994329
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



# Generated at 2022-06-14 05:53:49.833020
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert load_env_file(lines, write_environ=dict()) == collections.OrderedDict([('TEST', '.../yeee'),
                                                                                 ('THISIS', '.../a/test'),
                                                                                 ('YOLO',
                                                                                  '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])


# Unit tests for function read_env_file

# Generated at 2022-06-14 05:53:58.167832
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



# Generated at 2022-06-14 05:54:09.934327
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    data = {
        'TEST=${HOME}/yeee',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    }

    output = {
        'TEST': '${HOME}/yeee',
        'THISIS': '~/a/test',
        'YOLO': '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    }

    assert list(parse_env_file_contents(data)) == list(output.items())



# Generated at 2022-06-14 05:54:16.636849
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    loaded = load_env_file(lines, write_environ=dict())
    assert len(loaded) == 3
    assert not loaded['TEST'].startswith('${HOME}')



# Generated at 2022-06-14 05:54:29.521223
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import os

    # Parsing a simple env-file
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    result = load_env_file(lines, write_environ=None)
    assert isinstance(result, collections.OrderedDict)
    key_test, val_test = result['TEST']
    key_thisis, val_thisis = result['THISIS']
    key_yolo, val_yolo = result['YOLO']
    assert key_test == 'TEST'
    assert key_thisis == 'THISIS'
    assert key_yolo == 'YOLO'

# Generated at 2022-06-14 05:54:39.756807
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    parsed = tuple(parse_env_file_contents(lines))

    assert lines[0].startswith(parsed[0][0] + '=')
    assert lines[1].startswith(parsed[1][0] + '=')
    assert lines[2].startswith(parsed[2][0] + '=')

    assert parsed[0][1].endswith('yeee-')
    assert parsed[1][1].endswith('a/test')

# Generated at 2022-06-14 05:54:50.384635
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert [
        (k, expand(v))
        for k, v in parse_env_file_contents([
            'TEST=${HOME}/yeee',
            'THISIS=~/a/test',
            'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
        ])
    ] == [
        ('TEST', '.../yeee'),
        ('THISIS', '.../a/test'),
        ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    ]



# Generated at 2022-06-14 05:54:54.801815
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())



# Generated at 2022-06-14 05:55:00.852158
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # Arrange
    lines = [
        'TEST=${HOME}/yeee',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    ]

    # Act
    actual = parse_env_file_contents(lines)

    # Assert
    expected = [
        ('TEST', '${HOME}/yeee'),
        ('THISIS', '~/a/test'),
        ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    ]

    assert list(actual) == expected



# Generated at 2022-06-14 05:55:08.739997
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    values = parse_env_file_contents(lines)
    expected = [('TEST', '.../yeee'), ('THISIS', '.../a/test'), ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]
    for item, value in zip(values, expected):
        key, val = item
        assert key == value[0]
        assert val == value[1]



# Generated at 2022-06-14 05:55:20.835710
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    """
    Tests that parse_env_file_contents does what it is supposed to do.
    """
    # Create test contents for env file
    contents = [
        "SOME_PATH=/usr/bin/env\n",
        "SOME_OTHER_VAR=/home/\n",
        "THE_LAST_VAR=/usr/bin/env\n",
    ]

    lines = parse_env_file_contents(contents)
    collected_lines = []
    for line in lines:
        collected_lines.append(line)

    # Some asserts
    assert collected_lines[0][0] == "SOME_PATH"
    assert collected_lines[0][1] == "/usr/bin/env"

    assert collected_lines[1][0] == "SOME_OTHER_VAR"

# Generated at 2022-06-14 05:55:31.989624
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # Empty file
    lines = []
    assert list(parse_env_file_contents(lines)) == []

    # No assignments
    lines = ['nothing to see here']
    assert list(parse_env_file_contents(lines)) == []

    # Single assignment
    lines = ['TEST="HELLO THERE"']
    assert list(parse_env_file_contents(lines)) == [("TEST", '"HELLO THERE"')]

    # Multiple assignments
    lines = ['TEST="HELLO THERE"', 'YOLO="YO"', 'WHAT="WHAT"']
    assert list(parse_env_file_contents(lines)) == [("TEST", '"HELLO THERE"'), ("YOLO", '"YO"'), ("WHAT", '"WHAT"')]

    # Test case

# Generated at 2022-06-14 05:55:44.174928
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import sys
    import io

    actual = load_env_file(['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'])

    expected = collections.OrderedDict([
        ('TEST', '~/yeee-{}'.format(':'.join(sys.path))),
        ('THISIS', '~/a/test'),
        ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'),
    ])

    assert actual == expected, "Failed to parse env file contents"



# Generated at 2022-06-14 05:55:53.793726
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



# Generated at 2022-06-14 05:56:04.975922
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    """Check that the env file is loaded correctly."""

    assert parse_env_file_contents([]) == []
    assert parse_env_file_contents(["test=yeee"]) == [("test", "yeee")]
    assert parse_env_file_contents(["test=yeee-yeee"]) == [("test", "yeee-yeee")]
    assert parse_env_file_contents(["test='yeee'"]) == [("test", "yeee")]
    assert parse_env_file_contents(["test=\"yeee\""]) == [("test", "yeee")]

# Generated at 2022-06-14 05:56:14.602353
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    result = list(parse_env_file_contents(lines))

    assert result == [
        ('TEST', '${HOME}/yeee'),
        ('THISIS', '~/a/test'),
        ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'),
    ]



# Generated at 2022-06-14 05:56:18.352782
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # Given
    lines = []

    # When
    values = dict(parse_env_file_contents(lines))

    # Then
    assert len(values) == 0



# Generated at 2022-06-14 05:56:28.411695
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import sys
    import io

    env_file_str = """
    TEST=${HOME}/yeee-$PATH
    THISIS=~/a/test
    YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST
    """

    captured = io.StringIO()
    sys.stdout = captured

    assert list(parse_env_file_contents(env_file_str.split('\n'))) == list(
        [('TEST', '.../.../yeee-...:...'), ('THISIS', '.../a/test'), ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])



# Generated at 2022-06-14 05:56:40.944507
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    actual_result = parse_env_file_contents(lines)
    expected_result = [('TEST',
                        os.path.expanduser(os.path.expandvars('${HOME}/yeee'))),
                       ('THISIS', os.path.expanduser(os.path.expandvars('~/a/test'))),
                       ('YOLO',
                        os.path.expanduser(os.path.expandvars('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')))]


# Generated at 2022-06-14 05:56:55.922648
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert dict(parse_env_file_contents(lines)) == {
        "TEST": "${HOME}/yeee",
        "THISIS": "~/a/test",
        "YOLO": "~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST",
    }

    lines = ['TEST="${HOME}/yeee"', "THISIS='~/a/test'", 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert dict

# Generated at 2022-06-14 05:56:57.873973
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import doctest
    doctest.testmod()



# Generated at 2022-06-14 05:57:10.541319
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
        ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])



# Generated at 2022-06-14 05:57:20.830159
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import doctest
    import pprint

    env_lines = [
        'TEST=${HOME}/yeee',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST',
    ]

    environ = os.environ.copy()
    changes = load_env_file(env_lines, environ)

    pprint.pprint(changes)
    doctest.testmod()


if __name__ == '__main__':
    test_parse_env_file_contents()

# vim: fsl=python.vim tabstop=4 expandtab

# Generated at 2022-06-14 05:57:29.374197
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert load_env_file(lines, write_environ=dict()) == collections.OrderedDict(
        [
            ('TEST', '{}/yeee'.format(os.path.expanduser("~"))),
            ('THISIS', '{}/a/test'.format(os.path.expanduser("~"))),
            (
                'YOLO',
                '{}/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'.format(os.path.expanduser("~"))
            )
        ]
    )

# Generated at 2022-06-14 05:57:40.341539
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = [
        "TEST=${HOME}/yeee",
        "THISIS=~/a/test",
        "YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST",
    ]

    env = parse_env_file_contents(lines)

    assert next(env) == ("TEST", os.path.expanduser("~/yeee"))
    assert next(env) == ("THISIS", os.path.expanduser("~/a/test"))
    assert next(env) == ("YOLO", os.path.expanduser("~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"))

# Generated at 2022-06-14 05:57:53.344290
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['# this is a comment', 'TEST=${HOME}/yeee',
             'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    expected = [('TEST',
                 '~/yeee'),
                ('THISIS',
                 '~/a/test'),
                ('YOLO',
                 '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]
    assert (list(parse_env_file_contents(lines)) == expected)
    # assert (len(list(parse_env_file_contents(lines))) ==
    # expected)



# Generated at 2022-06-14 05:57:58.812312
# Unit test for function parse_env_file_contents

# Generated at 2022-06-14 05:58:04.282592
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    out = load_env_file(lines)

    assert isinstance(out, collections.OrderedDict)
    assert out



# Generated at 2022-06-14 05:58:16.596768
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import unittest

    class ParseEnvFileContentsTestCase(unittest.TestCase):

        def test_parse(self):

            output = parse_env_file_contents(['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'])

            output = list(output)

            self.assertEquals(len(output), 3)
            self.assertEquals(output[0], ('TEST', '${HOME}/yeee'))
            self.assertEquals(output[1], ('THISIS', '~/a/test'))

# Generated at 2022-06-14 05:58:27.912114
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import sys
    import os

    sys.path.append(os.path.dirname(__file__))

    import cumtest_env_parse as test
    import test_env_parse

    test_env_parse.test_parse_env_file_contents(test.parse_env_file_contents)



# Generated at 2022-06-14 05:58:42.116617
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # Unit test for function parse_env_file_contents
    assert list(parse_env_file_contents([
        'TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'])) == [
            ('TEST', '.../yeee'), ('THISIS', '.../a/test'), (
                'YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]


# Generated at 2022-06-14 05:58:47.033294
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())

# Generated at 2022-06-14 05:59:00.061598
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    f = io.StringIO('TEST=${HOME}/yeee-$PATH\nTHISIS=~/a/test\nYOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    lines = f.readlines()
    environ = load_env_file(lines, write_environ=dict())
    assert environ['TEST'] == os.path.expandvars('${HOME}/yeee-$PATH')
    assert environ['THISIS'] == os.path.expandvars('~/a/test')
    assert environ['YOLO'] == os.path.expandvars('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')



# Generated at 2022-06-14 05:59:05.343985
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    assert len(list(parse_env_file_contents(lines))) == 3

