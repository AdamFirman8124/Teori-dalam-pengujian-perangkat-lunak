

# Generated at 2022-06-14 05:49:13.637374
# Unit test for function load_env_file
def test_load_env_file():
    import pathlib

    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    os.environ["HOME"] = str(pathlib.Path.home())
    os.environ["PATH"] = os.path.pathsep.join(["/home/swaggins", "/home/swaggins/yeee", "/tmp/yeee"])
    changes = load_env_file(lines, write_environ=None)


# Generated at 2022-06-14 05:49:24.524108
# Unit test for function load_env_file
def test_load_env_file():
    def test(lines: typing.Iterable[str], expected):
        environment = load_env_file(lines)
        assert environment == expected

    test(
        lines=['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'],
        expected=collections.OrderedDict([
            ('TEST', os.path.expanduser('~/yeee')),
            ('THISIS', os.path.expanduser('~/a/test')),
            ('YOLO', os.path.expanduser('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'))
        ])
    )


# If

# Generated at 2022-06-14 05:49:36.359039
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    output = collections.OrderedDict(
        [('TEST', os.path.expanduser(os.path.expandvars('${HOME}/yeee-$PATH'))),
         ('THISIS', os.path.expanduser(os.path.expandvars('~/a/test'))),
         ('YOLO', os.path.expanduser(os.path.expandvars('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'))),
         ]
    )

# Generated at 2022-06-14 05:49:42.050199
# Unit test for function load_env_file
def test_load_env_file():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())


if __name__ == '__main__':
    print(load_env_file(['HOME=/home/olivier'], write_environ=dict()))
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 05:49:54.728850
# Unit test for function load_env_file
def test_load_env_file():
    import re
    import os

    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    env = load_env_file(lines)

    assert isinstance(env, collections.OrderedDict)

    for k in env:
        assert re.match(r'\A[A-Za-z_0-9]+\Z', k)

    # get the home from os.environ
    home = os.environ.get('HOME', '*~*')
    path = os.environ.get('PATH', '*PATH*')

    assert env['TEST'] == home + '/yeee'

    # This ${HOME} stuff is handled by os

# Generated at 2022-06-14 05:50:06.842071
# Unit test for function load_env_file
def test_load_env_file():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    environ = load_env_file(lines, write_environ=dict())
    assert environ['TEST'] == os.path.expandvars(os.path.expanduser('~/yeee-${PATH}'))
    assert environ['THISIS'] == os.path.expandvars(os.path.expanduser('~/a/test'))

# Generated at 2022-06-14 05:50:15.045267
# Unit test for function load_env_file
def test_load_env_file():
    """Test the load_env_file function"""
    import io
    import sys

    # Use an in memory file
    input = io.StringIO("TEST = ${HOME}/yeee\n")
    sys.stdin = input

    # Load env file
    environ = dict()
    result = load_env_file(lines=input.readlines(), write_environ=environ)

    # Check result
    assert len(result) == 1
    assert result["TEST"].endswith("/yeee")

    # Check environ
    assert len(environ) == 1
    assert environ["TEST"].endswith("/yeee")


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 05:50:18.542854
# Unit test for function load_env_file
def test_load_env_file():
    assert load_env_file(["A=B", "TEST=1"]) == collections.OrderedDict([('A', 'B'), ('TEST', '1')])



# Generated at 2022-06-14 05:50:27.966242
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    assert load_env_file(lines) == collections.OrderedDict([('TEST', os.path.join(os.path.expanduser('~'), 'yeee')),
                                                            ('THISIS', os.path.join(os.path.expanduser('~'), 'a/test')),
                                                            ('YOLO', os.path.join(os.path.expanduser('~'),
                                                                                  'swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'))])



# Generated at 2022-06-14 05:50:39.746749
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    expected = [('TEST', '.../yeee'), ('THISIS', '.../a/test'), ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]
    actual = list(parse_env_file_contents(lines))
    for i in range(len(expected)):
        assert actual[i][0] == expected[i][0]
        assert actual[i][1] == expected[i][1]



# Generated at 2022-06-14 05:50:48.602718
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    test_lines = [
        "FOO=BAR",
        "BAR=BAZ",
        "BAZ=QQQ",
        "FOO=BAT=$FOO",
    ]

    expected_outcome = [
        ("FOO", "BAR"),
        ("BAR", "BAZ"),
        ("BAZ", "QQQ"),
        ("FOO", "BAT=$FOO")
    ]

    assert list(parse_env_file_contents(test_lines)) == expected_outcome



# Generated at 2022-06-14 05:50:50.079725
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import doctest
    doctest.testmod(verbose=True)



# Generated at 2022-06-14 05:50:58.946799
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    unittest.TestCase().assertEqual(
        dict(parse_env_file_contents(["TEST=${HOME}/yeee", "THISIS=~/a/test", "YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"])),
        {'TEST': '.../yeee',
         'THISIS': '.../a/test',
         'YOLO': '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'})



# Generated at 2022-06-14 05:51:09.958325
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert load_env_file(lines, write_environ=dict()) == collections.OrderedDict([
        ('TEST', expand('${HOME}/yeee-$PATH')),
        ('THISIS', expand('~/a/test')),
        ('YOLO', expand('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'))
    ])



# Generated at 2022-06-14 05:51:20.975772
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    env_lines = """
TEST=${HOME}/yeee
THISIS=~/a/test
YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST
    """.splitlines()

    expected_tuples = """
TEST=${HOME}/yeee
THISIS=~/a/test
YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST
    """.splitlines()

    assert(list(parse_env_file_contents(env_lines)) == list(map(
        lambda t: tuple(t.split("=", 1)), expected_tuples)))


# Test load_env_file

# Generated at 2022-06-14 05:51:27.012680
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    pairs = load_env_file(lines)

    pairs = (
        ('TEST', '.../yeee'),
        ('THISIS', '.../a/test'),
        ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    )

    assert list(parse_env_file_contents(lines)) == pairs



# Generated at 2022-06-14 05:51:37.030384
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    lines = parse_env_file_contents(lines)
    assert next(lines) == ('TEST', '.../yeee')
    assert next(lines) == ('THISIS', '.../a/test')
    assert next(lines) == ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    with pytest.raises(StopIteration):
        next(lines)


# Generated at 2022-06-14 05:51:48.686138
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    got = parse_env_file_contents(lines)
    expect = [('TEST', '.../yeee'),
              ('THISIS', '.../a/test'),
              ('YOLO',
               '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]

    for i, (g, e) in enumerate(zip(got, expect)):
        assert g == e, 'Failed at test case %i; got %r, expect %r' % (i, g, e)



# Generated at 2022-06-14 05:51:57.311361
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    assert list(parse_env_file_contents(lines)) == [('TEST', '${HOME}/yeee-$PATH'),
                                                    ('THISIS', '~/a/test'),
                                                    ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'),
                                                    ]



# Generated at 2022-06-14 05:52:05.660384
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())


if __name__ == '__main__':
    # Unit test for function parse_env_file_contents
    test_parse_env_file_contents()

# Generated at 2022-06-14 05:52:17.224199
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    test = parse_env_file_contents(lines)


# Generated at 2022-06-14 05:52:25.719382
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    regex = re.compile('/home/user/Dropbox')

    lines = ['TEST=~/Dropbox/yeee-$PATH',
             'THISIS=~/test',
             'YOLO=~/Dropbox/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    results = list(parse_env_file_contents(lines))

    assert len(results) == 3
    assert results[0][0] == 'TEST'
    assert results[0][1] == '~/Dropbox/yeee-$PATH'
    assert results[1][0] == 'THISIS'
    assert results[1][1] == '~/test'
    assert results[2][0] == 'YOLO'

# Generated at 2022-06-14 05:52:35.725779
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    parsed = collections.OrderedDict(parse_env_file_contents(lines))

    assert parsed.keys() == collections.OrderedDict(parse_env_file_contents(lines)).keys()  # ordered dict is ordered dict
    assert parsed.keys() == collections.OrderedDict(parse_env_file_contents(lines)).keys()  # ordered dict is ordered dict
    assert parsed['YOLO'] == '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'  # no expansion

# Generated at 2022-06-14 05:52:47.832532
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import tempfile
    from io import StringIO

    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    # test original
    values = parse_env_file_contents(lines)

    values = [next(values) for _ in range(3)]
    assert values[0] == ('TEST', os.path.join(os.environ['HOME'], 'yeee-', os.environ['PATH']))
    assert values[1] == ('THISIS', os.path.expanduser('~/a/test'))

# Generated at 2022-06-14 05:52:54.628761
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    import pprint

    assert load_env_file(lines, write_environ=dict()) == collections.OrderedDict(
        [('TEST', '.../yeee'),
         ('THISIS', '.../a/test'),
         ('YOLO',
          '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])



# Generated at 2022-06-14 05:53:05.199547
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    result = load_env_file(lines, write_environ=dict())
    expected = collections.OrderedDict([('TEST', '.../yeee'),
                                        ('THISIS', '.../a/test'),
                                        ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])
    assert result == expected

# Generated at 2022-06-14 05:53:14.960419
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    buffer_string_lists = (
        ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'],

        ['TEST="$HOME/a/test"', "WHEE='$HOME/a/test'", 'YOLO="$HOME/a/test"']
    )

    for buffer_string_list in buffer_string_lists:

        for key, val in parse_env_file_contents(buffer_string_list):
            assert '"' not in val
            assert "'" not in val


# Generated at 2022-06-14 05:53:20.262072
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())

    assert True



# Generated at 2022-06-14 05:53:30.614763
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    line1 = 'TEST=${HOME}/yeee-$PATH'
    line2 = 'THISIS=~/a/test'
    line3 = 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'

    lines = (line1, line2, line3)

    import collections
    import os

    environ = collections.OrderedDict()
    environ['HOME'] = '...'
    environ['PATH'] = '...'
    environ['NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'] = '...'

    def expand(path):
        for k, v in environ.items():
            path = path.replace('$' + k, v)

# Generated at 2022-06-14 05:53:35.786388
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())



# Generated at 2022-06-14 05:53:49.834831
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    """
    We test the function parse_env_file_contents by supplying various inputs and comparing with the expected output.
    To make sure the function can handle all kinds of inputs, we provide six different kinds of inputs. One of the inputs
    is empty, a couple of inputs are valid but invalid key-value pairs, the last two inputs are the kind of input we would
    expect to get and want to work with.
    """
    parser = parse_env_file_contents

    assert parser(lines="") == []
    assert parser(lines="THIS IS NOT VALID") == []
    assert parser(lines="nor=is_this") == []
    assert parser(lines="KEY='value'") == []
    assert parser(lines="KEY=value") == [('KEY', 'value')]

# Generated at 2022-06-14 05:53:54.604754
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())
    assert True

# Generated at 2022-06-14 05:54:06.357683
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    res = list(parse_env_file_contents(lines))

    exp = [('TEST', '.../yeee'), ('THISIS', '.../a/test'), ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]
    assert len(res) == len(exp)
    for i in range(len(res)):
        assert res[i][0] == exp[i][0]
        assert res[i][1] in exp[i][1]



# Generated at 2022-06-14 05:54:07.655265
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import doctest
    doctest.testmod()



# Generated at 2022-06-14 05:54:16.938596
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert dict(parse_env_file_contents(lines)) == {
        'TEST': '${HOME}/yeee',
        'THISIS': '~/a/test',
        'YOLO': '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    }



# Generated at 2022-06-14 05:54:29.761021
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # Create and populate the file we're going to test
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    # Parse and check
    check_values = collections.OrderedDict((
        ('TEST', '.../.../yeee-...:...'),
        ('THISIS', '.../a/test'),
        ('YOLO',
         '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    ))


# Generated at 2022-06-14 05:54:42.809408
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import sys

    # This is used in an assertion below; is there a better way?
    yeee = expand('${HOME}/yeee')
    yeeepath = expand('${HOME}/yeee-$PATH')
    thisis = expand('~/a/test')
    yolo = expand('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')

    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert list(parse_env_file_contents(lines)) == [('TEST', yeee), ('THISIS', thisis), ('YOLO', yolo)]

   

# Generated at 2022-06-14 05:54:51.066413
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    parse_env_file_contents(lines)

    lines = ['THIS_IS_A_BAD_LINE']
    try:
        parse_env_file_contents(lines)
        assert False, 'Should not have gotten here'
    except ValueError:
        pass



# Generated at 2022-06-14 05:54:59.322347
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    d = parse_env_file_contents(lines)
    d = dict(d)  # type: ignore
    assert d['TEST'] == expand('${HOME}/yeee')
    assert d['THISIS'] == expand('~/a/test')
    assert d['YOLO'] == expand('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')



# Generated at 2022-06-14 05:55:12.523786
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # Test single equal form
    lines = ['TEST=${HOME}/yeee']
    assert next(parse_env_file_contents(lines)) == ('TEST', expand('${HOME}/yeee'))

    # Test single equal form with unexpanded variable
    lines = ['TEST=$PATH']
    assert next(parse_env_file_contents(lines)) == ('TEST', expand('$PATH'))

    # Test single equal form, quoted
    lines = ['TEST="${HOME}/yeee"']
    assert next(parse_env_file_contents(lines)) == ('TEST', expand(r'${HOME}/yeee'))

    # Test single equal form, quoted, with unexpanded variable
    lines = ['TEST="$PATH"']

# Generated at 2022-06-14 05:55:23.135033
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert list(
        parse_env_file_contents(lines=['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'])) == [
               ('TEST', '${HOME}/yeee'),
               ('THISIS', '~/a/test'),
               ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]



# Generated at 2022-06-14 05:55:32.591265
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():

    line_iterable = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    result = parse_env_file_contents(lines=line_iterable)

    # result is iterable, but we convert it to a list to keep it simple
    result = list(result)

    assert len(result) == len(line_iterable)

    assert result[0] == ('TEST', os.path.join(expand('${HOME}'), 'yeee'))
    assert result[1] == ('THISIS', os.path.join(expand('~'), 'a', 'test'))

# Generated at 2022-06-14 05:55:45.511518
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import os

    with open(".env", "w") as f:
        f.writelines([
            "TEST1=foo",
            "TEST2=bar",
            "TEST3='foo bar'",
            "TEST4=\"foo bar\"",
            "TEST5='foo\nbar'",
            "TEST6=\"foo\nbar\"",
            "TEST7='foo\\ bar'",
            "TEST8=\"foo\\ bar\"",
            "TEST9=${HOME}/foo",
            "TEST10=~/foo",
            "TEST11=$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST",
            "TEST12=${NONEXISTENT_VAR_THAT_DOES_NOT_EXIST}",
        ])


# Generated at 2022-06-14 05:55:56.221622
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert list(parse_env_file_contents(lines)) == [('TEST', '.../.../yeee-...:...'), ('THISIS', '.../a/test'), ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert load_env_

# Generated at 2022-06-14 05:56:07.317890
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    from unittest import mock

    def check_parse(lines: typing.Iterable[str] = None, expected: typing.Iterable[typing.Tuple[str, str]] = None):
        with mock.patch("builtins.print") as mp_builtins_print:
            actual = parse_env_file_contents(lines)
            assert list(actual) == expected
            assert mp_builtins_print.call_count == 0

    check_parse(lines=None, expected=[])
    check_parse(lines=[], expected=[])
    check_parse(lines=[""], expected=[])
    check_parse(lines=["# This is a comment"], expected=[])
    check_parse(lines=["   "], expected=[])
    check_parse(lines=["  blah blah blah  "], expected=[])
    check_

# Generated at 2022-06-14 05:56:18.171376
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import collections
    import unittest

    class TestParseEnvFileContents(unittest.TestCase):
        def test_parse_env_file_contents(self):
            lines = ['a=b\n', 'c=d\n', 'e=f\n']

            gen = parse_env_file_contents(lines)

            values = collections.OrderedDict()

            for k, v in gen:
                values[k] = v

            self.assertEqual(
                values,
                collections.OrderedDict([('a', 'b'), ('c', 'd'), ('e', 'f')])
            )

    unittest.main()


if __name__ == '__main__':
    test_parse_env_file_contents()

# Generated at 2022-06-14 05:56:23.965187
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())

# Generated at 2022-06-14 05:56:32.632911
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert load_env_file(lines, write_environ=dict()) == collections.OrderedDict(
        [('TEST', '.../yeee'),
         ('THISIS', '.../a/test'),
         ('YOLO',
          '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])



# Generated at 2022-06-14 05:56:41.821722
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



# Generated at 2022-06-14 05:56:51.453339
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert list(parse_env_file_contents(lines)) == [('TEST', '${HOME}/yeee'), ('THISIS', '~/a/test'), ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]



# Generated at 2022-06-14 05:57:04.651384
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = [
        "TEST=${HOME}/yeee",
        "THISIS=~/a/test",
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST',
    ]

    got = load_env_file(lines, write_environ=dict())

    want = collections.OrderedDict()
    want['TEST'] = expand("${HOME}/yeee")
    want['THISIS'] = expand("~/a/test")
    want['YOLO'] = expand("~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST")

    assert got == want, f"Got: {got}, want: {want}"

# Generated at 2022-06-14 05:57:06.467997
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import doctest

    doctest.testmod()



# Generated at 2022-06-14 05:57:13.283479
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())
    assert True



# Generated at 2022-06-14 05:57:23.013566
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    results = parse_env_file_contents(lines)
    assert list(results) == [('TEST', '${HOME}/yeee'), ('THISIS', '~/a/test'),
                             ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]



# Generated at 2022-06-14 05:57:35.726609
# Unit test for function parse_env_file_contents

# Generated at 2022-06-14 05:57:44.240057
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert list(parse_env_file_contents()) == []
    assert list(parse_env_file_contents([])) == []
    assert list(parse_env_file_contents(["abc=123"])) == [("abc", "123")]
    assert list(parse_env_file_contents(["abc=123", "def=456"])) == [("abc", "123"), ("def", "456")]
    assert list(parse_env_file_contents(["abc=123", "def=456", " \t "])) == [("abc", "123"), ("def", "456")]
    assert list(parse_env_file_contents(["abc=123", "def=456", "abc=789"])) == [("abc", "789"), ("def", "456")]

# Generated at 2022-06-14 05:57:50.649205
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert next(parse_env_file_contents(lines)) == ('TEST', '.../.../yeee')



# Generated at 2022-06-14 05:57:52.289287
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import doctest
    doctest.testmod()



# Generated at 2022-06-14 05:58:01.285297
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    parsed = parse_env_file_contents(
        ["TEST=${HOME}/yeee", "THISIS=~/a/test", "YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"]
    )

    assert isinstance(parsed, typing.Generator)
    assert tuple(parsed) == (
        ("TEST", "${HOME}/yeee"),
        ("THISIS", "~/a/test"),
        ("YOLO", "~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"),
    )


# Generated at 2022-06-14 05:58:11.740395
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = [
        'TEST=${HOME}/yeee',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST',
    ]
    assert list(parse_env_file_contents(lines)) == [
        ('TEST', '${HOME}/yeee'),
        ('THISIS', '~/a/test'),
        ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'),
    ]



# Generated at 2022-06-14 05:58:26.362304
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert list(parse_env_file_contents(lines)) == [('TEST', expand('${HOME}/yeee')),
                                                    ('THISIS', expand('~/a/test')),
                                                    ('YOLO', expand('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'))]

# Generated at 2022-06-14 05:58:29.246588
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())
    return None



# Generated at 2022-06-14 05:58:40.714250
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    values = parse_env_file_contents(lines=lines)
    changes = collections.OrderedDict(values)

    assert changes == collections.OrderedDict({
        "TEST": "${HOME}/yeee",
        "THISIS": "~/a/test",
        "YOLO": "~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"
    })



# Generated at 2022-06-14 05:58:50.448195
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    env_file_path = './test_env.env'
    with open(env_file_path) as f:
        lines = f.readlines()

    actual = dict(parse_env_file_contents(lines))
    assert isinstance(actual, dict)

    # Check to make sure the expected values exist
    assert actual['TEST'] == '${HOME}/yeee-$PATH'
    assert actual['THISIS'] == '~/a/test'
    assert actual['YOLO'] == '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'


if __name__ == '__main__':
    import doctest

    doctest.testmod()
    doctest.testfile('test_env.env')

# Generated at 2022-06-14 05:59:01.932899
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import io
    import itertools
    import unittest
