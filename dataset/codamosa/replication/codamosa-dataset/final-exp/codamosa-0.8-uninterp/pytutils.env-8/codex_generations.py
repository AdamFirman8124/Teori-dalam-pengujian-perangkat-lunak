

# Generated at 2022-06-14 05:49:18.602826
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    environ = load_env_file(lines, write_environ=dict())
    assert environ == collections.OrderedDict(
        TEST=os.path.join(os.environ['HOME'], 'yeee'),
        THISIS=os.path.join(os.environ['HOME'], 'a', 'test'),
        YOLO=os.path.join(os.environ['HOME'], 'swaggins', '$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'),
    )



# Generated at 2022-06-14 05:49:20.016734
# Unit test for function load_env_file
def test_load_env_file():
    import doctest
    doctest.testmod()



# Generated at 2022-06-14 05:49:22.146661
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import doctest

    doctest.testmod()



# Generated at 2022-06-14 05:49:28.118192
# Unit test for function parse_env_file_contents

# Generated at 2022-06-14 05:49:38.712406
# Unit test for function load_env_file
def test_load_env_file():
    test_lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    changes = load_env_file(test_lines)

    assert len(changes) == 3
    assert 'TEST' in changes and 'THISIS' in changes and 'YOLO' in changes
    assert changes['TEST'] == os.path.expanduser(os.path.expandvars('${HOME}/yeee-$PATH'))
    assert changes['THISIS'] == os.path.expanduser(os.path.expandvars('~/a/test'))

# Generated at 2022-06-14 05:49:50.853922
# Unit test for function load_env_file
def test_load_env_file():
    lines = ['TEST=${HOME}/yeee-${PATH}', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    environ = os.environ
    result = load_env_file(lines, environ)
    assert result['TEST'] == environ['HOME'] + '/yeee-' + environ['PATH']
    assert result['THISIS'] == environ['HOME'] + '/a/test'
    assert result['YOLO'] == environ['HOME'] + '/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'

    # same test but with no write
    environ = dict(os.environ)
    result = load_env_file

# Generated at 2022-06-14 05:49:56.154156
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    print(load_env_file(lines, write_environ=dict()))



# Generated at 2022-06-14 05:50:07.078985
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    test = """
    TEST=${HOME}/yeee
    THISIS=~/a/test
    YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST
    """
    lines = test.splitlines()
    output = parse_env_file_contents(lines)
    output2 = collections.OrderedDict(output)
    assert output2["TEST"] == "${HOME}/yeee"
    assert output2["THISIS"] == "~/a/test"
    assert output2["YOLO"] == "~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"

# Generated at 2022-06-14 05:50:10.316285
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test']

    assert list(parse_env_file_contents(lines)) == [('TEST', '.../yeee'), ('THISIS', '.../a/test')]
    assert list(parse_env_file_contents([''])) == []



# Generated at 2022-06-14 05:50:17.366277
# Unit test for function load_env_file
def test_load_env_file():
    source = [
        "VAR1=This is a test\n",
        "VAR2=$VAR1\n",
        "VAR3=This is not",
    ]

    result = load_env_file(source)
    assert result['VAR1'] == "This is a test"
    assert result['VAR2'] == result['VAR1']
    assert result['VAR3'] == "This is not"

# Generated at 2022-06-14 05:50:28.017064
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    expected = [('TEST', '${HOME}/yeee-$PATH'), ('THISIS', '~/a/test'), ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]

    res = list(parse_env_file_contents(lines))

    # On Windows tilde is not expanded.

# Generated at 2022-06-14 05:50:33.893314
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())

# Generated at 2022-06-14 05:50:43.570349
# Unit test for function load_env_file
def test_load_env_file():
    result = load_env_file(['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'])
    assert result['TEST'] == f'{os.environ["HOME"]}/yeee'
    assert result['THISIS'] == f'{os.environ["HOME"]}/a/test'
    assert result['YOLO'] == f'{os.environ["HOME"]}/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'



# Generated at 2022-06-14 05:50:46.862807
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['YOLO=%HOME%', 'TEST=${HOME}/yeee']
    values = parse_env_file_contents(lines)

    print(values)



# Generated at 2022-06-14 05:50:57.872079
# Unit test for function load_env_file
def test_load_env_file():
    import os
    from pkg_resources import resource_string

    src_path = os.path.dirname(__file__)
    src_path = os.path.abspath(src_path)

    with open(resource_string(__name__, 'test.env')) as f:
        text = f.read()

    test_env = load_env_file(text.splitlines())


# Generated at 2022-06-14 05:51:06.963632
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():  # type: ignore
    """
    Tests whether env files are properly parsed.
    """
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    res = parse_env_file_contents(lines)
    res = dict(res)

    assert res['TEST'].endswith('/yeee')
    assert res['THISIS'].endswith('/a/test')
    assert res['YOLO'].endswith('/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')

# Generated at 2022-06-14 05:51:11.635677
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    env_path = 'app/.env'
    with open(env_path) as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    print(lines)
    values = parse_env_file_contents(lines)
    changes = load_env_file(lines, write_environ=dict())
    for k, v in changes.items():
        print(k, '=', v)
    assert True


if __name__ == '__main__':
    test_parse_env_file_contents()

# Generated at 2022-06-14 05:51:23.340850
# Unit test for function load_env_file
def test_load_env_file():
    lines = ['TEST=${HOME}/yeee-$PATH',
             'THISIS=~/a/test',
             'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    results = load_env_file(lines=lines, write_environ=dict())

    assert results == collections.OrderedDict([('TEST', f'{os.path.expanduser("~")}/yeee-{os.environ["PATH"]}'), ('THISIS', f'{os.path.expanduser("~")}/a/test'), ('YOLO', f'{os.path.expanduser("~")}/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])

# Unit test

# Generated at 2022-06-14 05:51:30.163570
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import pytest

    test_cases = [
        ('TEST=${HOME}/yeee', {'TEST': os.path.expanduser('~/yeee')}),
        ('THISIS=~/a/test', {'THISIS': os.path.expanduser('~/a/test')}),
        ('YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST', {'YOLO': os.path.expanduser('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')}),
    ]

    for test, expect in test_cases:
        got = parse_env_file_contents([test])
        got = {k: v for k, v in got}


# Generated at 2022-06-14 05:51:42.888900
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # We need to store results into a list because we are tearing down the generator
    results = list(parse_env_file_contents(['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']))

    assert results == [
        ('TEST', '${HOME}/yeee'),
        ('THISIS', '~/a/test'),
        ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'),
    ]

    # Make sure we can iterate over it multiple times

# Generated at 2022-06-14 05:51:50.732749
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())

# Generated at 2022-06-14 05:51:58.674941
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    parsed = collections.OrderedDict(parse_env_file_contents(lines))
    expected = collections.OrderedDict([('TEST', '${HOME}/yeee'),
                                        ('THISIS', '~/a/test'),
                                        ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])
    assert parsed == expected



# Generated at 2022-06-14 05:52:03.397884
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    _ = load_env_file(lines, write_environ=dict())

# Generated at 2022-06-14 05:52:14.028567
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    from pprint import pprint

    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    result = list(parse_env_file_contents(lines))
    pprint(result)
    assert result == [('TEST', '.../yeee'),
                      ('THISIS', '.../a/test'),
                      ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]



# Generated at 2022-06-14 05:52:18.653679
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())



# Generated at 2022-06-14 05:52:31.317990
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert parse_env_file_contents(['']) == []
    assert list(parse_env_file_contents(['a', 'b'])) == []
    assert list(parse_env_file_contents(['a=1'])) == [('a', '1')]
    assert list(parse_env_file_contents(['a=1', 'b=2'])) == [('a', '1'), ('b', '2')]
    assert list(parse_env_file_contents(['a="\"This is a test\""'])) == [('a', '"This is a test"')]
    assert list(parse_env_file_contents(['a="This is a test"'])) == [('a', 'This is a test')]

# Generated at 2022-06-14 05:52:38.011165
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    string = '''
    TEST=${HOME}/yeee
    THISIS=~/a/test
    YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST
    '''
    expected_result = [
        ("TEST", "${HOME}/yeee"),
        ("THISIS", "~/a/test"),
        ("YOLO", "~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"),
    ]
    result = parse_env_file_contents(string.split("\n"))
    assert list(result) == expected_result



# Generated at 2022-06-14 05:52:51.529948
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    #         0                  1              2                                                                  3
    values = list(parse_env_file_contents(lines))
    assert len(values) == 3, "Didn't parse correct lines"
    assert values[0][0] == 'TEST', "Didn't get correct key"
    assert values[0][1] == '${HOME}/yeee-$PATH', "Didn't get correct val"
    assert values[1][0] == 'THISIS', "Didn't get correct key"

# Generated at 2022-06-14 05:52:59.107157
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    result = parse_env_file_contents(lines)

    for k, v in result:
        assert isinstance(k, str)
        assert isinstance(v, str)



# Generated at 2022-06-14 05:53:11.101585
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import io

    data = '''
    VAR1=test
    VAR2=~/test
    VAR3=${HOME}/test
    VAR4="test"

    VAR5='test-test'
    VAR6='test
    test'
    VAR7="test-test"
    VAR8="test
    test"
    VAR9=test\\test
    '''


# Generated at 2022-06-14 05:53:23.285599
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    values = parse_env_file_contents(lines)

    assert isinstance(values, typing.Generator)

    values = dict(values)

    assert isinstance(values, dict)

    assert values['TEST'].endswith('/yeee')
    assert values['THISIS'].endswith('/a/test')
    assert 'NONEXISTENT_VAR_THAT_DOES_NOT_EXIST' in values['YOLO']

# Generated at 2022-06-14 05:53:36.562507
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # these are weird because they are really intended for use with envsubst
    lines = [
        "FOO=$BAR",
        'SPAM="$SPAM SPAM"',
        "EGGS='$EGGS $EGGS'",
        "TEST=${HOME}/yeee",
        "THISIS=~/a/test",
        "YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST",
    ]

    d = collections.OrderedDict(parse_env_file_contents(lines))

    # TODO: make this test not OS dependent

# Generated at 2022-06-14 05:53:48.916573
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    d = parse_env_file_contents(lines)

    assert d.__next__() == ('TEST', expand('${HOME}/yeee'))
    assert d.__next__() == ('THISIS', expand('~/a/test'))
    assert d.__next__() == ('YOLO', expand('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'))

    with pytest.raises(StopIteration):
        d.__next__()



# Generated at 2022-06-14 05:53:54.116871
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())



# Generated at 2022-06-14 05:54:06.060132
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    yielded = parse_env_file_contents(lines)

    test_results = [
        (k, v)
        for k, v in yielded
    ]
    assert test_results[0][0] == 'TEST'
    assert test_results[1][0] == 'THISIS'
    assert test_results[2][0] == 'YOLO'

    assert test_results[0][1].startswith('${HOME}/yeee')
    assert test_results[1][1].startswith('${HOME}/a/test')

# Generated at 2022-06-14 05:54:07.707998
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import doctest
    doctest.testmod()


# Generated at 2022-06-14 05:54:17.795768
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())
    assert load_env_file(lines, write_environ=dict()) == OrderedDict([('TEST', '.../yeee'),
            ('THISIS', '.../a/test'),
            ('YOLO',
             '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])

# Generated at 2022-06-14 05:54:22.440312
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines)



# Generated at 2022-06-14 05:54:23.943070
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import doctest
    doctest.testmod(verbose=True)

# Generated at 2022-06-14 05:54:36.158287
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    """
    Test if the environment file is parsed correctly.
    """
    # Test case 1
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    environ = dict()
    load_env_file(lines, write_environ=environ)
    assert 'TEST' in environ
    assert 'THISIS' in environ
    assert 'YOLO' in environ
    assert 'HOME' in os.environ
    assert 'NONEXISTENT_VAR_THAT_DOES_NOT_EXIST' not in environ
    assert os.environ['HOME'] in environ['TEST']
    assert os.environ['PATH']

# Generated at 2022-06-14 05:54:49.256999
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    values = parse_env_file_contents(lines)
    assert next(values) == ('TEST', '.../yeee')
    assert next(values) == ('THISIS', '.../a/test')
    assert next(values) == ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')



# Generated at 2022-06-14 05:54:58.598173
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert load_env_file(lines, write_environ=dict()) == OrderedDict(
        [('TEST', '.../yeee'),
         ('THISIS', '.../a/test'),
         ('YOLO',
          '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])
    print("parse_env_file_contents: PASS")



# Generated at 2022-06-14 05:55:02.023898
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = [
        'TEST=${HOME}/yeee',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    ]
    changes = parse_env_file_contents(lines)

    print(changes)

# Generated at 2022-06-14 05:55:12.303913
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    print("Testing parse_env_file_contents")
    assert parse_env_file_contents(
        ["TEST=${HOME}/yeee", "THISIS=~/a/test", "YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"]) == [
               ("TEST", expand("${HOME}/yeee")),
               ("THISIS", expand("~/a/test")),
               ("YOLO", expand("~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"))]



# Generated at 2022-06-14 05:55:22.189929
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



# Generated at 2022-06-14 05:55:28.713173
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    for line, (k, v) in zip(lines, parse_env_file_contents(lines)):
        assert line == '{}={}'.format(k, v)



# Generated at 2022-06-14 05:55:41.495312
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = [
        'TEST=${HOME}/yeee-$PATH',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST',
        'DUDE="he said, \\"hey\\""'
    ]
    changes = parse_env_file_contents(lines)
    expected = [
        ('TEST', '.../.../yeee-...:...'),
        ('THISIS', '.../a/test'),
        ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'),
        ('DUDE', 'he said, "hey"')
    ]
    # assert changes == expected, 'Error: changes={

# Generated at 2022-06-14 05:55:47.900543
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${H}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())



# Generated at 2022-06-14 05:55:54.690382
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    os.environ['HOME'] = 'unittests_home'
    os.environ['PATH'] = 'unittests_path'
    for key, value in parse_env_file_contents(lines):
        print(key, value)



# Generated at 2022-06-14 05:55:57.662076
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert list(parse_env_file_contents(['TEST=one', 'bla=hey ho'])) == [('TEST', 'one'), ('bla', 'hey ho')]

# Generated at 2022-06-14 05:56:05.503002
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # Test for parsing the file at the root of this repo (i.e, where the tests are)
    with open(os.path.join(os.getcwd(), '..', '.env')) as env_file_handle:
        env_file_contents = list(parse_env_file_contents(env_file_handle))

    assert len(env_file_contents) == 2

    env_file_contents = dict(env_file_contents)

    assert 'CHARON_PASSWORD' in env_file_contents
    assert 'CHARON_USERNAME' in env_file_contents
    assert 'CHARON_DB_HOST' in env_file_contents
    assert 'CHARON_DB_PORT' in env_file_contents
    assert 'CHARON_DB_USERNAME' in env_

# Generated at 2022-06-14 05:56:15.155714
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



# Generated at 2022-06-14 05:56:23.304684
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = [
        'TEST=${HOME}/yeee',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    ]

    # Write values to new dict
    d = dict()
    load_env_file(lines, write_environ=d)

    # Compare values with dict
    values = parse_env_file_contents(lines)

    for k, v in values:
        assert v == d[k]



# Generated at 2022-06-14 05:56:31.608835
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    some_data = [
        'TEST=${HOME}/yeee',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST',
    ]
    for k, v in parse_env_file_contents(some_data):
        assert re.match(r'\A[A-Za-z_0-9]+\Z', k)
        assert re.match(r'\A[A-Za-z_/0-9~$]+\Z', v)



# Generated at 2022-06-14 05:56:41.767572
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    expected = collections.OrderedDict([
        ('TEST', expand('${HOME}/yeee')),
        ('THISIS', expand('~/a/test')),
        ('YOLO', expand('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')),
    ])
    actual = collections.OrderedDict(parse_env_file_contents(lines))
    assert actual == expected



# Generated at 2022-06-14 05:56:53.799821
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    parse_env_file_contents(lines)
    os.environ['TEST'] = os.path.expandvars('${HOME}/yeee-$PATH')
    os.environ['THISIS'] = os.path.expandvars('~/a/test')
    os.environ['YOLO'] = os.path.expandvars('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')



# Generated at 2022-06-14 05:56:59.057954
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines)



# Generated at 2022-06-14 05:57:10.398797
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    out = dict(parse_env_file_contents(lines))

    assert out['TEST'] == '{HOME}/yeee-{PATH}'.format(HOME=expand('${HOME}'), PATH=expand('${PATH}'))
    assert out['THISIS'] == expand('~/a/test')
    assert out['YOLO'] == expand('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')

# Generated at 2022-06-14 05:57:22.482815
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import tempfile

    with tempfile.NamedTemporaryFile('w') as f:
        f.write('TEST=${HOME}/yeee\n')
        f.write('THISIS=~/a/test\n')
        f.write('YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
        f.flush()

        with open(f.name) as fr:
            lines = fr.readlines()

            result = parse_env_file_contents(lines)
            result = collections.OrderedDict(result)

            expected = collections.OrderedDict()
            expected['TEST'] = os.path.join(os.environ['HOME'], 'yeee')

# Generated at 2022-06-14 05:57:35.053380
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    """
    Tests function parse_env_file_contents with the docstring examples

    """
    # First example with no comments
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    out = load_env_file(lines, write_environ=dict())
    #print(out)

# Generated at 2022-06-14 05:57:41.719809
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())



# Generated at 2022-06-14 05:57:48.434985
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    with open(os.path.join(os.path.dirname(__file__), 'test_file.env')) as f:
        values = parse_env_file_contents(f.readlines())

    changes = dict(values)

    for k, v in changes.items():
        assert os.path.exists(expand(v)), k



# Generated at 2022-06-14 05:57:59.573051
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    od = collections.OrderedDict(parse_env_file_contents(lines))

    assert od['TEST'] == os.path.join(os.environ['HOME'], 'yeee')
    assert od['THISIS'] == os.path.join(os.environ['HOME'], 'a', 'test')
    assert od['YOLO'] == os.path.join(os.environ['HOME'], 'swaggins', '$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')



# Generated at 2022-06-14 05:58:04.998658
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    value = parse_env_file_contents(lines)

    for val in value:
        k, v = val
        print(k, v)

# Generated at 2022-06-14 05:58:13.182199
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import os
    import tempfile

    with tempfile.NamedTemporaryFile(mode='w') as temp_file:
        temp_file.writelines(['TEST=${HOME}/yeee',
                              'THISIS=~/a/test',
                              'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'])
        temp_file.flush()

        values = parse_env_file_contents(open(temp_file.name, mode='r'))

        # Just a sanity check for now.
        assert next(values) == ('TEST', '{}/yeee'.format(os.getenv('HOME')))



# Generated at 2022-06-14 05:58:16.651523
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert list(parse_env_file_contents(['foo=bar', 'bar=baz'])) == [
        ('foo', 'bar'),
        ('bar', 'baz'),
    ]



# Generated at 2022-06-14 05:58:29.610369
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import unittest
    from unittest import TestCase
    from io import StringIO

    class Parse(TestCase):
        def setUp(self):
            self.lines = ['export TEST_VAR_1=test1', 'EXPORT TEST_VAR_2=test2', '#test3', '   TEST_VAR_3="test\n3"', 'TEST_VAR_4="test4"', 'TEST_VAR_5="test5\$test5"', '#test6', '   TEST_VAR_6=test6']


# Generated at 2022-06-14 05:58:42.290508
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import doctest

    env_file_content = [
        "WORLD='hello'",
        "HELLO='hello \\\"HELLO\\\"'",
        "UNQUOTED='hello \"HELLO\"'",
        "UNQUOTED_UNESCAPED='hello'",
    ]
    expected_env_file_contents = [
        ("WORLD", "hello"),
        ("HELLO", 'hello "HELLO"'),
        ("UNQUOTED", 'hello "HELLO"'),
        ("UNQUOTED_UNESCAPED", "hello"),
    ]
    results = list(parse_env_file_contents(env_file_content))
    assert results == expected_env_file_contents



# Generated at 2022-06-14 05:58:50.139420
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    result = load_env_file(lines, write_environ=dict())
    assert result == collections.OrderedDict(
        [('TEST', '.../yeee'), ('THISIS', '.../a/test'), ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])



# Generated at 2022-06-14 05:59:01.821251
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import io

    lines = [
        'TEST=$HOME/yeee-$PATH',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST',
    ]

    env_dict = dict()
    env_dict['HOME'] = '...'
    env_dict['PATH'] = '...:...'

    output = io.StringIO()
    with contextlib.redirect_stdout(output), mock.patch.dict(os.environ, env_dict):
        result = load_env_file(lines, write_environ=dict())
