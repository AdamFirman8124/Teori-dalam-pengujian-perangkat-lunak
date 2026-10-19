

# Generated at 2022-06-14 05:49:09.476696
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    val = parse_env_file_contents(['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'])  # noqa

    assert val is not None



# Generated at 2022-06-14 05:49:18.444749
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    vals = parse_env_file_contents(lines)
    assert vals == [('TEST', '${HOME}/yeee'), ('THISIS', '~/a/test'), ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]



# Generated at 2022-06-14 05:49:27.538267
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    envs = list(parse_env_file_contents(lines))

    expected = [('TEST', '${HOME}/yeee'), ('THISIS', '~/a/test'), ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]

    assert len(envs) == len(expected)
    for env, expected_env in zip(envs, expected):
        assert env == expected_env

# Generated at 2022-06-14 05:49:37.774150
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import io

    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    result = collections.OrderedDict(parse_env_file_contents(lines))

    assert result == {
        'TEST': '$HOME/yeee',
        'THISIS': '~/a/test',
        'YOLO': '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST',
    }



# Generated at 2022-06-14 05:49:49.961544
# Unit test for function load_env_file
def test_load_env_file():
    lines = ['TEST=$HOME/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    changes = load_env_file(lines, write_environ=dict())

    assert changes['TEST'].startswith('.../.../yeee-...:')
    assert changes['TEST'].endswith('...:...:...:...:.../swaggin')

    assert changes['THISIS'].startswith('.../a/test')

    assert changes['YOLO'] == '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'



# Generated at 2022-06-14 05:49:57.684494
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert list(parse_env_file_contents(lines)) == [('TEST', '${HOME}/yeee'),
                                                    ('THISIS', '~/a/test'),
                                                    ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]
    lines = ['TEST=Yeee space', '# It\'s just a comment', '', 'THISIS=~/a/test']

# Generated at 2022-06-14 05:50:09.036278
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    some = parse_env_file_contents(lines)
    assert some.__next__() == ('TEST', '{}/yeee'.format(os.environ['HOME']))
    assert some.__next__() == ('THISIS', '{}/a/test'.format(os.environ['HOME']))
    assert some.__next__() == ('YOLO', '{}/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'.format(os.environ['HOME']))



# Generated at 2022-06-14 05:50:21.417443
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    test_parse_env_file_contents = parse_env_file_contents(lines)
    ans = [('TEST', '{HOME}/yeee'), ('THISIS', '~/a/test'), ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]
    i = 0
    for elem in test_parse_env_file_contents:
        print("elem:", elem)
        assert ans[i] == elem
        i += 1


# Generated at 2022-06-14 05:50:28.143627
# Unit test for function load_env_file
def test_load_env_file():
    lines = [
        'TEST=${HOME}/yeee-$PATH',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST',
    ]

    result = load_env_file(lines, write_environ=dict())
    print(result)


if __name__ == '__main__':
    test_load_env_file()
    print("Done")

# Generated at 2022-06-14 05:50:38.054486
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    expected_output = [
        ('TEST', '${HOME}/yeee'),
        ('THISIS', '~/a/test'),
        ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    ]

    actual_output = parse_env_file_contents(['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'])

    assert list(actual_output) == expected_output



# Generated at 2022-06-14 05:50:46.708922
# Unit test for function load_env_file
def test_load_env_file():
    """
    >>> load_env_file(['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'], write_environ=dict())
    OrderedDict([('TEST', '.../.../yeee-...:...'),
                 ('THISIS', '.../a/test'),
                 ('YOLO',
                  '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])
    """
    pass



# Generated at 2022-06-14 05:50:57.782009
# Unit test for function load_env_file
def test_load_env_file():
    import os

    path = os.path.expanduser('~/.ssh')

    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    changes = load_env_file(lines, os.environ)

    test_val = os.environ['TEST']
    assert test_val == os.path.expanduser('~/yeee-%s' % path)

    test_val2 = os.environ['THISIS']
    assert test_val2 == os.path.expanduser('~/a/test')

    test_val3 = os.environ['YOLO']

# Generated at 2022-06-14 05:51:07.514955
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines, expected = (
        [
            'TEST=${HOME}/yeee',
            'THISIS=~/a/test',
            'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST',
        ],
        [
            ('TEST', os.path.expanduser('${HOME}/yeee')),
            ('THISIS', os.path.expanduser('~/a/test')),
            ('YOLO', os.path.expanduser('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')),
        ],
    )
    assert dict(parse_env_file_contents(lines)) == dict(expected)

# Generated at 2022-06-14 05:51:15.555747
# Unit test for function load_env_file
def test_load_env_file():
    load_env_file(['TEST=${HOME}/yeee-$PATH', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'], write_environ=os.environ)

    assert os.environ['TEST'] == os.path.join(os.environ['HOME'], 'yeee-') + os.pathsep + os.environ['PATH']
    assert os.environ['YOLO'] == os.path.join(os.environ['HOME'], 'swaggins', '$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')


# Generated at 2022-06-14 05:51:26.664574
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    values = parse_env_file_contents(lines)
    assert next(values) == ('TEST', os.path.join(os.path.expanduser("~"), "yeee"))
    assert next(values) == ('THISIS', os.path.join(os.path.expanduser("~"), "a", "test"))
    assert next(values) == ('YOLO', os.path.join(os.path.expanduser("~"), "swaggins", "$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"))

# Generated at 2022-06-14 05:51:32.410246
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test',
             'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    ret = parse_env_file_contents(lines)
    for k, v in ret:
        assert not v == '${HOME}/yeee'



# Generated at 2022-06-14 05:51:45.550964
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    environ = os.environ.copy()

    changes = parse_env_file_contents(lines)
    changes = list(changes)

    environ_expect = environ.copy()

    environ_expect['TEST'] = expand('${HOME}/yeee-$PATH')
    environ_expect['THISIS'] = expand('~/a/test')
    environ_expect['YOLO'] = expand('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')

    # Test for changes
    assert len

# Generated at 2022-06-14 05:51:57.053073
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    for lines in [['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']]:
        parsed = parse_env_file_contents(lines)

        assert isinstance(parsed, typing.Iterator)

        assert next(parsed) == ('TEST', '${HOME}/yeee')
        assert next(parsed) == ('THISIS', '~/a/test')
        assert next(parsed) == ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')



# Generated at 2022-06-14 05:52:09.080842
# Unit test for function load_env_file
def test_load_env_file():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', "YOLO='~/swag\\'gins/'"]
    lines.append('YEE=${HOME}')

    expected = {'TEST': '.../yeee', 'THISIS': '.../a/test',
                "YOLO": "~/swag'gins/", 'YEE': '...'}

    write_environ = dict()

    output = load_env_file(lines, write_environ)

    assert output == expected

    for k, v in expected.items():
        assert v == write_environ[k]


if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)

    import doctest
    doctest

# Generated at 2022-06-14 05:52:15.784315
# Unit test for function load_env_file
def test_load_env_file():
    # Test data
    data = [
        'TEST=${HOME}/yeee-$PATH',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    ]

    # Test
    load_env_file(data, write_environ=dict())



# Generated at 2022-06-14 05:52:25.078189
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    expected = {'TEST': '.../yeee', 'THISIS': '.../a/test', 'YOLO': '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'}

    results = dict(parse_env_file_contents(lines))

    assert results.keys() == expected.keys()
    assert all(expand(results[k]).endswith(expand(v)) for k, v in expected.items())



# Generated at 2022-06-14 05:52:35.378661
# Unit test for function load_env_file
def test_load_env_file():
    import io
    import json

    test_cases = [
        ('TEST=${HOME}/yeee-$PATH', 'TEST', os.environ['HOME'] + '/yeee-' + os.environ['PATH']),
        ('THISIS=~/a/test', 'THISIS', os.environ['HOME'] + '/a/test'),
        ('YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST', 'YOLO', os.environ['HOME'] + '/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'),
    ]

    for test_case in test_cases:
        expected_key, expected_value = test_case[1:]

# Generated at 2022-06-14 05:52:47.645948
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    res = parse_env_file_contents(lines)
    res_expected = [
        ('TEST', os.path.join(os.environ['HOME'], 'yeee')),
        ('THISIS', os.path.join(os.environ['HOME'], 'a/test')),
        ('YOLO', os.path.join(os.environ['HOME'], 'swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')),
    ]


# Generated at 2022-06-14 05:52:48.947271
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 05:52:53.790935
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())

# Generated at 2022-06-14 05:53:07.516071
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = [
        '# This is a comment',
        'TEST=${HOME}/yeee',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST',
        '# This is another comment',
        'EMPTY=',
        'SINGLE_QUOTED=\'hi there\'',
        'DOUBLE_QUOTED_WITH_SPACES="hello  $PATH"',
        'DOUBLE_QUOTED_WITH_SINGLE_QUOTES="hello \'$USER\'"',
        'DOUBLE_QUOTED_WITH_DOUBLE_QUOTES="hello \\"$VAR\\""',
    ]


# Generated at 2022-06-14 05:53:15.957937
# Unit test for function load_env_file
def test_load_env_file():
    import io

    test_lines = [
        'VALUE1=1',
        'VALUE2=2',
        'VALUE3=',
        'VALUE4=4',
        'VALUE5="    "',
        'VALUE6=""',
        "VALUE7='    '",
        "VALUE8=''",
        'VALUE9=abc',
        'VALUE10="abc"',
        "VALUE11='abc'",
        'VALUE12=1"2"3',
        "VALUE13=1'2'3",
        'VALUE14="1\'2"',
        "VALUE15='1\"2'",
    ]

    sio = io.StringIO('\n'.join(test_lines))
    load_env_file(sio, write_environ=dict())


# Generated at 2022-06-14 05:53:24.912815
# Unit test for function load_env_file
def test_load_env_file():
    lines = [
        "TEST=${HOME}/yeee-$PATH",
        "THIS=${EXISTING_ENV_VAR_THAT_WILL_NOT_BE_EXPANDED}",
        "THISIS=~/a/test",
        "YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"
    ]

# Generated at 2022-06-14 05:53:30.984276
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    changes = parse_env_file_contents(lines)
    assert list(changes) == [('TEST', '.../yeee'), ('THISIS', '.../a/test'), ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]

# Generated at 2022-06-14 05:53:36.701799
# Unit test for function load_env_file
def test_load_env_file():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    result = load_env_file(lines, write_environ=dict())

    assert 'TEST' in result
    assert 'THISIS' in result
    assert 'YOLO' in result

# Generated at 2022-06-14 05:53:50.731673
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    env_str = """
# This is a comment
TEST=${HOME}/yeee-$PATH
THISIS=~/a/test
YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST
"""
    lines = [line.strip() for line in env_str.splitlines()]
    res = parse_env_file_contents(lines)
    assert res == [
        ("TEST", "${HOME}/yeee-$PATH"),
        ("THISIS", "~/a/test"),
        ("YOLO", "~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST")
    ]


# Generated at 2022-06-14 05:53:57.849320
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH',
             'THISIS=~/a/test',
             'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    result = load_env_file(lines, write_environ=dict())


# Generated at 2022-06-14 05:54:10.506832
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    expected = {'TEST': '.../yeee', 'THISIS': '.../a/test',
                'YOLO': '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'}
    m = load_env_file(lines)

    # assertDictEqual is py3 only
    assert len(expected) == len(m)
    assert expected.keys() == m.keys()
    assert expected.values() == m.values()

# Generated at 2022-06-14 05:54:18.713651
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert tuple(parse_env_file_contents(lines)) == (
        ('TEST', '.../yeee'),
        ('THISIS', '.../a/test'),
        ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    )



# Generated at 2022-06-14 05:54:29.903221
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    results = load_env_file(['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'],
                            write_environ=dict())

    # TODO: check for HOME directory?
    assert results == collections.OrderedDict(
        [('TEST', '.../yeee'),
         ('THISIS', '.../a/test'),
         ('YOLO',
          '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])

    # TODO: more tests?



# Generated at 2022-06-14 05:54:42.519450
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = [
        'TEST=${HOME}/yeee',
        'THISIS=~/a/test',
        "YOLO='~/swaggins/'",
        'YOLO2="~/swaggins/"',
        'YOLO3="$HOME/swaggins/\\"',
    ]
    parsed = list(parse_env_file_contents(lines))
    assert parsed == [
        ('TEST', '${HOME}/yeee'),
        ('THISIS', '~/a/test'),
        ("YOLO", '~/swaggins/'),
        ('YOLO2', '~/swaggins/'),
        ('YOLO3', '$HOME/swaggins/"'),
    ], parsed



# Generated at 2022-06-14 05:54:51.344277
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # Parse env file contents
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())
    assert lines == ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']



# Generated at 2022-06-14 05:54:54.801791
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert 1 == 1

# Generated at 2022-06-14 05:54:58.764706
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())

# Generated at 2022-06-14 05:55:04.692771
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # Test a basic env var
    assert list(parse_env_file_contents([
        'PATH=${HOME}/bin:${HOME}/.local/bin:${PATH}'
    ])) == [('PATH', '${HOME}/bin:${HOME}/.local/bin:${PATH}')]
    assert list(parse_env_file_contents([
        '$PATH=${HOME}/bin:${HOME}/.local/bin:${PATH}'
    ])) == []
    assert list(parse_env_file_contents([
        '$PATH:=${HOME}/bin:${HOME}/.local/bin:${PATH}'
    ])) == []