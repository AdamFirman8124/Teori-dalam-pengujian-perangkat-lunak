

# Generated at 2022-06-14 05:49:07.420064
# Unit test for function load_env_file
def test_load_env_file():
    try:
        from contextlib import redirect_stdout

        with open(os.devnull, "w") as f, redirect_stdout(f):
            import doctest
            doctest.testmod()

    except ImportError:
        import doctest
        doctest.testmod()


if __name__ == "__main__":
    test_load_env_file()

# Generated at 2022-06-14 05:49:09.176820
# Unit test for function load_env_file
def test_load_env_file():
    if __name__ == "__main__":
        import doctest
        doctest.testmod()

# Generated at 2022-06-14 05:49:21.152557
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    """

    """
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    r = load_env_file(lines, write_environ=dict())

    assert 'TEST' in r
    assert r['TEST'] == '{}/yeee'.format(os.environ.get('HOME'))

    assert 'THISIS' in r
    assert r['THISIS'] == '{}/a/test'.format(os.environ.get('HOME'))

    assert 'YOLO' in r

# Generated at 2022-06-14 05:49:27.818869
# Unit test for function load_env_file
def test_load_env_file():
    # Successfully load the file
    with tempfile.NamedTemporaryFile(mode="wt", delete=False) as f:
        f.write("TEST=${HOME}/yeee-$PATH\n")
        f.write("THISIS=~/a/test\n")
        f.write("YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST\n")

    environ = load_env_file([f.name])
    assert len(environ) == 3
    assert environ["TEST"] == (Path.home() / "yeee-" / os.environ["PATH"])
    assert environ["THISIS"] == (Path.home() / "a" / "test")

# Generated at 2022-06-14 05:49:39.128917
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    contents = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    results = parse_env_file_contents(contents)
    assert results.__next__() == ('TEST', '${HOME}/yeee')
    assert results.__next__() == ('THISIS', '~/a/test')
    assert results.__next__() == ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')


if __name__ == '__main__':
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 05:49:51.035918
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    """
    Tests function parse_env_file_contents.
    """
    lines = [
        'TEST=${HOME}/yeee',
        'THISIS=~/a/test',
        'YOLO=',
        'WOHOO="$HOME/something"',
        'YOLOL="$HOME/nothing"',
        'NOW=',
        'WITHOUTSPACES="$HOME/something else"',
        'WITHOUTQUOTES=${HOME}/something',
    ]

    result = parse_env_file_contents(lines)


# Generated at 2022-06-14 05:50:00.077278
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert dict(parse_env_file_contents(lines=[
        "TEST=${HOME}/yeee",
        "THISIS=~/a/test",
        "YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"
    ])) == {
        "TEST": os.path.expanduser("~/yeee"),
        "THISIS": os.path.expanduser("~/a/test"),
        "YOLO": os.path.expanduser("~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST")
    }



# Generated at 2022-06-14 05:50:04.728883
# Unit test for function load_env_file
def test_load_env_file():
    load_env_file(lines=["TEST=${HOME}/yeee", "THISIS=~/a/test", "YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"], write_environ=dict())

# Generated at 2022-06-14 05:50:09.909114
# Unit test for function load_env_file
def test_load_env_file():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines)



# Generated at 2022-06-14 05:50:12.190272
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # TODO: implement
    assert 0



# Generated at 2022-06-14 05:50:21.983849
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert list(parse_env_file_contents(['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'])) == [('TEST', '${HOME}/yeee'),
                                                                                                                                                   ('THISIS', '~/a/test'),
                                                                                                                                                   ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]



# Generated at 2022-06-14 05:50:27.315223
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    with open(__file__, 'r', encoding='utf8') as f:
        lines = f.readlines()
        env = parse_env_file_contents(lines)
        env_dict = dict(env)

    assert 'test_parse_env_file_contents' in env_dict
    assert 'lines' in env_dict
    assert 'env' in env_dict
    assert 'env_dict' in env_dict

# Generated at 2022-06-14 05:50:38.730557
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import io
    import inspect

    env = load_env_file(io.StringIO('TEST=${HOME}/yeee'), write_environ=None)

    assert env['TEST'] == inspect.getfile(inspect.currentframe()).replace('.py', '/yeee')


if __name__ == '__main__':
    print(inspect.getfile(inspect.currentframe()))
    print(os.path.expandvars('$HOME'))
    print(os.path.expanduser('~/test'))
    print(load_env_file(['TEST=$HOME/yeee']))

    test_parse_env_file_contents()

# Generated at 2022-06-14 05:50:45.157389
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert list(
        parse_env_file_contents([
            "TEST=yeee",
            "THISIS=~/a/test",
            "YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"
        ])
    ) == [
        ("TEST", "yeee"),
        ("THISIS", "~/a/test"),
        ("YOLO", "~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST")
    ]



# Generated at 2022-06-14 05:50:53.519684
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # Empty
    input_ = []
    expected_output = []

    assert parse_env_file_contents(input_) == expected_output

    # One line
    input_ = ['TEST=1']
    expected_output = [('TEST', '1')]

    assert parse_env_file_contents(input_) == expected_output

    # Two lines
    input_ = ['TEST=1', 'TEST2=$TEST']
    expected_output = [('TEST', '1'), ('TEST2', '$TEST')]

    assert parse_env_file_contents(input_) == expected_output



# Generated at 2022-06-14 05:51:03.812847
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert list(parse_env_file_contents()) == []
    assert list(parse_env_file_contents([])) == []
    assert list(parse_env_file_contents(())) == []

    assert list(parse_env_file_contents(['TEST=${HOME}/yeee'])) == [('TEST', '.../yeee')]
    assert list(parse_env_file_contents(['TEST=${HOME}/yeee'])) == [('TEST', '.../yeee')]
    assert list(parse_env_file_contents(['TEST=$HOME/yeee'])) == [('TEST', '.../yeee')]

# Generated at 2022-06-14 05:51:11.379715
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    sample_env_file_contents = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    sample_env_file_contents = parse_env_file_contents(sample_env_file_contents)
    result = list(sample_env_file_contents)
    expected = list()
    expected.append(('TEST', '${HOME}/yeee'))
    expected.append(('THISIS', '~/a/test'))
    expected.append(('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'))
    assert result == expected


# Unit test

# Generated at 2022-06-14 05:51:23.097566
# Unit test for function parse_env_file_contents

# Generated at 2022-06-14 05:51:27.402338
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    file_contents = ['a=b', 'c=d', '~/test=~test/test', '~test/test=~test/test']
    values = ['b', 'd', '~test/test', '~test/test']

    for val, (k, v) in zip(values, parse_env_file_contents(file_contents)):
        assert val == v



# Generated at 2022-06-14 05:51:37.055925
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    results = collections.OrderedDict(list(parse_env_file_contents(lines)))
    assert len(results) == 3
    assert 'YOLO' in results
    assert '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST' == results['YOLO']
    assert 'TEST' in results
    assert results['TEST'].endswith('yeee')
    assert 'THISIS' in results
    assert results['THISIS'].endswith('a/test')

# Generated at 2022-06-14 05:51:41.089538
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import doctest
    doctest.testmod()



# Generated at 2022-06-14 05:51:50.477387
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert list(
        parse_env_file_contents(lines)
    ) == [('TEST', '.../yeee'), ('THISIS', '.../a/test'), ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]

    lines = ['TEST="${HOME}"/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

# Generated at 2022-06-14 05:52:03.081879
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    test_cases = [
        ('TEST=${HOME}/yeee', {'TEST': '.../yeee'}),
        ('THISIS=~/a/test', {'THISIS': '.../a/test'}),
        ('YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST', {'YOLO': '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'})
    ]
    for test_case in test_cases:
        test_string, expected = test_case
        result = next(parse_env_file_contents([test_string]))
        assert list(result) == list(expected.keys())
        assert list(result) == list(expected.values())



# Generated at 2022-06-14 05:52:04.969069
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert parse_env_file_contents(['']) is not None



# Generated at 2022-06-14 05:52:17.890082
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert list(parse_env_file_contents(lines=None)) == []

    assert list(parse_env_file_contents(lines=[''])) == []

    assert list(parse_env_file_contents(lines=['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test'])) == [
        ('TEST', '{}/yeee-'.format(os.getenv('HOME')) + os.getenv('PATH')),
        ('THISIS', '{}/a/test'.format(os.getenv('HOME')))]


# Generated at 2022-06-14 05:52:29.297788
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    expected = [('TEST', '.../yeee'), ('THISIS', '.../a/test'), ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]

    # Later dictionaries take precedence
    actual = list(parse_env_file_contents(lines))
    print(actual)
    assert actual == expected
    assert len(actual) == len(expected)



# Generated at 2022-06-14 05:52:37.827709
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    f = expand(os.path.expanduser("~/.secrets/test.env"))

    with open(f, "w") as fp:
        fp.write("""
            VALUE_A=something
            VALUE_B=something else
            VALUE_C=${VALUEX} and ${VALUE_Y}
            VALUE_D="a value with \"quotes\" and spaces"
        """)

    with open(f, "r") as fp:
        lines = fp.readlines()


# Generated at 2022-06-14 05:52:50.224819
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    assert dict(parse_env_file_contents(lines)) == {
        'TEST': '${HOME}/yeee',
        'THISIS': '~/a/test',
        'YOLO': '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    }

    lines = []

    assert dict(parse_env_file_contents(lines)) == {
    }



# Generated at 2022-06-14 05:53:02.210229
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = [
        '# This is a comment',
        'TEST=${HOME}/yeee',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST',
        'KEY_WITH_EQUALS=${HOME}/yeee=$PATH',
        'QUOTED_VAR="$FOO"',
        "RAW_VAR='$FOO'",
        'MULTILINE=$(echo "a\nb\nc")',
    ]


# Generated at 2022-06-14 05:53:14.658866
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    test_set = [None, "", "a b", "a=b"]
    for line in test_set:
        with raises(StopIteration):
            next(parse_env_file_contents(line))

    for line in ["b=c"]:
        assert next(parse_env_file_contents(line)) == ("b", "c")

    for line in ["a=b"]:
        assert next(parse_env_file_contents(line)) == ("a", "b")

    for line in ["a = b"]:
        assert next(parse_env_file_contents(line)) == ("a", "b")

    for line in ["a= b"]:
        assert next(parse_env_file_contents(line)) == ("a", " b")


# Generated at 2022-06-14 05:53:25.326589
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    result = load_env_file(lines, write_environ=dict())
    assert result == collections.OrderedDict(
        [
            ('TEST', '.../.../yeee-...:...'),
            ('THISIS', '.../a/test'),
            ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
        ]
    )



# Generated at 2022-06-14 05:53:37.751974
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = [
        'TEST=${HOME}/yeee-$PATH',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST',
    ]
    assert list(parse_env_file_contents(lines)) == [('TEST', '.../.../yeee-...:...'), ('THISIS', '.../a/test'), ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]


# Generated at 2022-06-14 05:53:49.611944
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    res = parse_env_file_contents(lines)
    assert res == [('TEST', '${HOME}/yeee'), ('THISIS', '~/a/test'),
                   ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]
    res = list(parse_env_file_contents(lines))

# Generated at 2022-06-14 05:54:00.100790
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    values = parse_env_file_contents(lines)

    # assert type(values) == dict
    assert len(values) == 3

    assert values['TEST'] == expand("${HOME}/yeee")
    assert values['THISIS'] == expand("~/a/test")
    assert values['YOLO'] == expand("~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST")

# Generated at 2022-06-14 05:54:08.889168
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = [
        'TEST=${HOME}/yeee',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST',
        'YO=test',
        'THIS=is',
        'A=test',
    ]

    results = parse_env_file_contents(lines)

    for line in lines:
        assert next(results)



# Generated at 2022-06-14 05:54:20.238942
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert list(parse_env_file_contents(['TEST=${HOME}/yeee', 'THISIS=~/a/test'])) == [('TEST', '.../yeee'), ('THISIS', '.../a/test')]
    assert list(parse_env_file_contents(['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test'])) == [('TEST', '.../.../yeee-...:...'), ('THISIS', '.../a/test')]

# Generated at 2022-06-14 05:54:26.289468
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    load_env_file(lines, write_environ=dict())


if __name__ == '__main__':
    test_parse_env_file_contents()

# Generated at 2022-06-14 05:54:37.738457
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():

    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    res = parse_env_file_contents(lines)

    assert res
    assert len(res) == 3

    d = collections.OrderedDict()

    for k, v in res:
        d[k] = v

    assert d['TEST'] == expand('${HOME}/yeee')
    assert d['THISIS'] == expand('~/a/test')
    assert d['YOLO'] == expand('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')


# Generated at 2022-06-14 05:54:49.253021
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



# Generated at 2022-06-14 05:54:51.206999
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import doctest
    doctes

# Generated at 2022-06-14 05:55:12.782223
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import sys

    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    environ = dict()
    load_env_file(lines, write_environ=environ)

    values = parse_env_file_contents(lines)
    assert sys.platform == "linux" or sys.platform.startswith("cygwin")
    # For some reason, Travis CI (trusty, standard image) was returning '/home/travis/.local/bin:/home/travis/.rvm/gems/ruby-2.3.1/bin:/home/travis/.rvm/gems/ruby-2.3.1@global/bin:/home/travis

# Generated at 2022-06-14 05:55:24.060628
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    expected = [('TEST', '.../yeee'),
                ('THISIS', '.../a/test'),
                ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]

    result = list(parse_env_file_contents(lines))

    assert len(result) == len(expected)

    for (key1, val1), (key2, val2) in zip(result, expected):
        assert key1 == key2
        assert val1 == val2



# Generated at 2022-06-14 05:55:37.392528
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert tuple(parse_env_file_contents(lines=['TEST=${HOME}/yeee-$PATH'])) == (('TEST', '${HOME}/yeee-$PATH'),)
    assert tuple(parse_env_file_contents(lines=['TEST=${HOME}/yeee-$PATH'])) != (('TEST', '${HOME}/yeee-$PATH'), ('TEST', '${HOME}/yeee-$PATH'))


# Generated at 2022-06-14 05:55:49.458256
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import io

# Generated at 2022-06-14 05:55:59.801740
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    content = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    expected = [
        ('TEST', '${HOME}/yeee'),
        ('THISIS', '~/a/test'),
        ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'),
    ]
    assert list(parse_env_file_contents(content)) == expected



# Generated at 2022-06-14 05:56:06.686400
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    val = parse_env_file_contents(["TEST=${HOME}/yeee", "THISIS=~/a/test", "YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"])

    expected = [("TEST", "..."), ("THISIS", "..."), ("YOLO", "...")]

    for i, v in enumerate(val):
        assert v[1] == expected[i][1]



# Generated at 2022-06-14 05:56:11.530068
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())



# Generated at 2022-06-14 05:56:19.625412
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    values = parse_env_file_contents(lines)

    # Just tests the first one
    assert list(values)[0] == ("TEST", os.path.expanduser("~") + "/yeee")


# Generated at 2022-06-14 05:56:24.475125
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    vals = ['HOME=/home/somehome', 'USER=someuser']
    output = load_env_file(vals)
    assert output['HOME'] == expand(vals[0])
    assert output['USER'] == vals[1]



# Generated at 2022-06-14 05:56:34.139877
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert list(parse_env_file_contents(lines)) == [('TEST', os.path.expandvars(os.path.expanduser('${HOME}/yeee'))),
                                                    ('THISIS', os.path.expandvars(os.path.expanduser('~/a/test'))),
                                                    (
                                                        'YOLO', os.path.expandvars(os.path.expanduser('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')))]



# Generated at 2022-06-14 05:56:59.399696
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert list(parse_env_file_contents(lines)) == [
        ('TEST', '${HOME}/yeee'),
        ('THISIS', '~/a/test'),
        ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'),
    ]

    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

# Generated at 2022-06-14 05:57:11.919005
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    """
    Tests if env file is parsed correctly
    """
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    mapping = dict()
    for (k, v) in parse_env_file_contents(lines):
        mapping[k] = v
    assert "TEST" in mapping
    assert "THISIS" in mapping
    assert "YOLO" in mapping
    assert mapping["TEST"] == os.path.expanduser(os.path.expandvars('${HOME}/yeee'))
    assert mapping["THISIS"] == os.path.expanduser(os.path.expandvars('~/a/test'))

# Generated at 2022-06-14 05:57:14.536295
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import doctest
    doctest.testmod(verbose=True)


if __name__ == '__main__':
    test_parse_env_file_contents()

# Generated at 2022-06-14 05:57:26.641160
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # Test invalid input
    try:
        parse_env_file_contents(lines={"thing": None})
    except TypeError:
        pass

    # Test invalid input
    try:
        parse_env_file_contents(lines=[{}])
    except TypeError:
        pass

    # Test invalid input
    try:
        parse_env_file_contents(lines=[{"thing": None}])
    except TypeError:
        pass

    # Test invalid input
    try:
        parse_env_file_contents(lines=[{"thing": None}])
    except TypeError:
        pass

    # Test invalid input
    try:
        parse_env_file_contents(lines=[])
    except StopIteration:
        pass

    # Test invalid input

# Generated at 2022-06-14 05:57:32.146804
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())
    assert True

# Generated at 2022-06-14 05:57:41.422327
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    actual = parse_env_file_contents(lines)
    expected = (('TEST', '.../yeee'), ('THISIS', '.../a/test'), ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'))
    assert(tuple(actual) == expected)



# Generated at 2022-06-14 05:57:48.980417
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    import pprint
    pp = pprint.PrettyPrinter()
    pp.pprint(list(parse_env_file_contents(lines)))



# Generated at 2022-06-14 05:57:53.290856
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIT']
    load_env_file(lines)



# Generated at 2022-06-14 05:58:03.680742
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # Here we test the load_env_file function and parse_env_file_contents.
    # As the parse_env_file_contents function isn't exported.
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert dict(parse_env_file_contents(lines)) == {
        'TEST': '${HOME}/yeee',
        'THISIS': '~/a/test',
        'YOLO': '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'}



# Generated at 2022-06-14 05:58:12.524935
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    from io import StringIO

    lines = StringIO('TEST=${HOME}/yeee-$PATH\n'
                     'THISIS=~/a/test\n'
                     'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST\n')

    changes = load_env_file(lines, write_environ=None)

    assert 'TEST' in changes
    assert 'THISIS' in changes
    assert 'YOLO' in changes



# Generated at 2022-06-14 05:59:01.312421
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import tempfile
    from . import TestUtil

    fd, fname = tempfile.mkstemp()
    with os.fdopen(fd, "w") as f:
        f.write('TEST=${HOME}/yeee\nTHISIS=~/a/test\nYOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')

    with open(fname, "r") as f:
        contents = parse_env_file_contents(f)
    os.remove(fname)

    assert next(contents) == ('TEST', os.path.expanduser('$HOME/yeee'))
    assert next(contents) == ('THISIS', os.path.expanduser('~/a/test'))