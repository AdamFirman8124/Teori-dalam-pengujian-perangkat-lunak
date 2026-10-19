

# Generated at 2022-06-14 05:49:16.056696
# Unit test for function load_env_file
def test_load_env_file():
    # Test with default case
    input_str = """
    TEST=${HOME}/yeee
    THISIS=~/a/test
    YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST
    """
    lines = input_str.splitlines()
    lines = [x for x in lines if x]
    output = load_env_file(lines)

    # Test with nested variable expansion
    input_str = """
    TEST=${HOME}/yeee-$PATH
    THISIS=~/a/test
    YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST
    """
    lines = input_str.splitlines()
    lines = [x for x in lines if x]
    output

# Generated at 2022-06-14 05:49:27.279870
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines_one = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    lines_two = ["TEST='${HOME}/yeee'", "THISIS='~/a/test'", "YOLO='~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'"]
    lines_three = ['TEST="/${HOME}/yeee"', 'THISIS="~/a/test"', 'YOLO="~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"']

    values_one = parse_env_file_contents(lines_one)

# Generated at 2022-06-14 05:49:38.195504
# Unit test for function load_env_file
def test_load_env_file():
    """
    Unit test for function load_env_file.
    """
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    values = load_env_file(lines, write_environ=None)
    print(values)
    assert len(values) == 3
    assert values['TEST'].startswith(os.path.expanduser('~/yeee'))
    assert values['THISIS'].startswith(os.path.expanduser('~/a'))

# Generated at 2022-06-14 05:49:50.514726
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    for k, v in parse_env_file_contents(lines):
        if k == 'TEST':
            assert v == '${HOME}/yeee'
            assert v.startswith(os.environ['HOME'])
        if k == 'THISIS':
            assert v == '~/a/test'
            assert v.startswith(os.environ['HOME'])
        if k == 'YOLO':
            assert v == '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
            assert v.startsw

# Generated at 2022-06-14 05:49:58.789375
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # Create a test env file
    test_env_file_contents = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    result = parse_env_file_contents(test_env_file_contents)

    # Ensure that the result of the function is iterable
    assert isinstance(result, collections.Iterable)

    # Ensure that the result of the function returns tuples
    for i in result:
        assert isinstance(i, tuple)



# Generated at 2022-06-14 05:50:07.878729
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert load_env_file(lines, write_environ=dict()) == collections.OrderedDict(
        [('TEST', '.../.../yeee-...:...'), ('THISIS', '.../a/test'), ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])



# Generated at 2022-06-14 05:50:08.708878
# Unit test for function load_env_file
def test_load_env_file():
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 05:50:21.278122
# Unit test for function load_env_file
def test_load_env_file():
    lines = [
        'TEST=${HOME}/yeee',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    ]
    test_environ = dict()
    load_env_file(lines, test_environ)

    assert test_environ.get('TEST') == '.../yeee'
    assert test_environ.get('THISIS') == '.../a/test'
    assert test_environ.get('YOLO') == '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'

# Generated at 2022-06-14 05:50:29.192272
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import io
    import sys

    f = io.StringIO()
    old = sys.stdout
    sys.stdout = f


# Generated at 2022-06-14 05:50:40.460290
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    #
    # test normal lines
    #

    lines = ['TEST1=test2', 'TEST3=test4']

    v = collections.OrderedDict(parse_env_file_contents(lines))
    assert v['TEST1'] == 'test2'
    assert v['TEST3'] == 'test4'

    #
    # test lines with escaped characters
    #

    lines = [r'TEST1="test2\"']
    v = collections.OrderedDict(parse_env_file_contents(lines))
    assert v['TEST1'] == 'test2"'

    lines = [r'TEST1="test2\"\"\"']
    v = collections.OrderedDict(parse_env_file_contents(lines))

# Generated at 2022-06-14 05:50:50.447881
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():

    env_file = """
    TEST=${HOME}/yeee
    THISIS=~/a/test
    YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST
    """

    result = list(parse_env_file_contents(env_file.splitlines()))
    assert result == [('TEST', '.../yeee'),
                      ('THISIS', '.../a/test'),
                      ('YOLO',
                       '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]



# Generated at 2022-06-14 05:50:53.850090
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import doctest
    import sys

    failed, tested = doctest.testmod()
    if failed:
        sys.exit(1)


if __name__ == '__main__':
    test_parse_env_file_contents()

# Generated at 2022-06-14 05:51:00.185910
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    lines2 = [
        '# Comment',
        'TEST=${HOME}/yeee-$PATH',
        '# Comment',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST',
    ]


# Generated at 2022-06-14 05:51:09.064724
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = [
        'TEST=${HOME}/yeee-$PATH',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    ]

    result = load_env_file(lines, write_environ=dict())


# Generated at 2022-06-14 05:51:21.663288
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    """
    From honcho.
    """
    assert list(parse_env_file_contents(lines=['FOO=bar'])) == [('FOO', 'bar')]
    assert list(parse_env_file_contents(lines=['FOO=bar', 'BAR=foo'])) == [
        ('FOO', 'bar'),
        ('BAR', 'foo'),
    ]
    assert list(parse_env_file_contents(lines=['FOO=bar\n'])) == [('FOO', 'bar')]

    # Test single-quoted values
    assert list(parse_env_file_contents(lines=["FOO='bar'"])) == [('FOO', 'bar')]

# Generated at 2022-06-14 05:51:29.281001
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    result = parse_env_file_contents(lines)
    assert ['TEST', 'THISIS', 'YOLO'] == list(result)[0]

    env_dict = load_env_file(lines, write_environ=dict())
    assert ('/home', '/a/test') == (env_dict['HOME'], env_dict['THISIS'])
    assert env_dict['YOLO'] == f'{env_dict["HOME"]}/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'


# Generated at 2022-06-14 05:51:37.412115
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    environ = dict()

    load_env_file(lines, write_environ=environ)

    assert environ == {
        'TEST': os.environ['HOME'] + '/yeee',
        'THISIS': os.environ['HOME'] + '/a/test',
        'YOLO': os.environ['HOME'] + '/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    }



# Generated at 2022-06-14 05:51:46.375215
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    """
    Tests the function parse_env_file_contents.
    """
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert load_env_file(lines, write_environ=dict()) is not None, 'parse_env_file_contents returned None instead of an OrderedDict.'



# Generated at 2022-06-14 05:51:56.683820
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    env_file_contents = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    result = parse_env_file_contents(env_file_contents)
    assert result == [('TEST', expand('${HOME}/yeee')), ('THISIS', expand('~/a/test')), ('YOLO', expand('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'))]



# Generated at 2022-06-14 05:52:07.159979
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    environ = load_env_file(lines, write_environ=dict())

    assert environ['TEST'] == expand('${HOME}/yeee-$PATH')
    assert environ['THISIS'] == expand('~/a/test')
    assert environ['YOLO'] == expand('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')



# Generated at 2022-06-14 05:52:14.977901
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = """
        key=value
        key2='value'
        key3="value" 
        key4='${PATH}'
        """

    items = list(parse_env_file_contents(lines.splitlines()))
    assert items[0] == ("key", "value")
    assert items[1] == ("key2", "value")
    assert items[2] == ("key3", "value")
    assert items[3] == ("key4", "${PATH}")



# Generated at 2022-06-14 05:52:23.085147
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = [
        'TEST=${HOME}/yeee',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    ]

    assert list(parse_env_file_contents(lines)) == [
        ('TEST', '.../yeee'),
        ('THISIS', '.../a/test'),
        ('YOLO',
         '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    ]



# Generated at 2022-06-14 05:52:29.351138
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    results = parse_env_file_contents(lines)
    for result in results:
        print(result)
    return



# Generated at 2022-06-14 05:52:36.840467
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    output = load_env_file(lines, write_environ=dict())
    assert output == collections.OrderedDict([('TEST', '.../yeee'),
                                              ('THISIS', '.../a/test'),
                                              ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])



# Generated at 2022-06-14 05:52:48.352746
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # test for successful parsing
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    parsed_lines = parse_env_file_contents(lines)

    # check that test.env file is parsed successfully
    assert parsed_lines.__next__() == ('TEST', f'{os.environ["HOME"]}/yeee')
    assert parsed_lines.__next__() == ('THISIS', f'{os.environ["HOME"]}/a/test')

# Generated at 2022-06-14 05:52:59.498793
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    parsed = parse_env_file_contents(lines)
    new_env = dict(parsed)
    assert new_env == {
        'TEST': '$HOME/yeee',
        'THISIS': '~/a/test',
        'YOLO': '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST',
    }



# Generated at 2022-06-14 05:53:07.312873
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    parsed = parse_env_file_contents(lines)
    parsed_list = list(parsed)
    assert parsed_list[0][0] == 'TEST'
    assert parsed_list[0][1] == '${HOME}/yeee-$PATH'
    assert parsed_list[1][0] == 'THISIS'
    assert parsed_list[1][1] == '~/a/test'
    assert parsed_list[2][0] == 'YOLO'

# Generated at 2022-06-14 05:53:14.627075
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    result = load_env_file(lines, write_environ=dict())

    assert result['TEST'] == expand('${HOME}/yeee')
    assert result['THISIS'] == expand('~/a/test')
    assert result['YOLO'] == expand('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')



# Generated at 2022-06-14 05:53:23.485919
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    out = parse_env_file_contents(lines=['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'])

    assert hasattr(out, '__iter__')
    assert out == [('TEST', '.../yeee'),
                   ('THISIS', '.../a/test'),
                   ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]



# Generated at 2022-06-14 05:53:36.272666
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    d = load_env_file(lines, write_environ=dict())
    d.get('TEST', 'FAIL').startswith('.../yeee')
    d.get('THISIS', 'FAIL').startswith('.../a/test')
    d.get('YOLO', 'FAIL').startswith('.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')


if __name__ == "__main__":
    test_parse_env_file_contents()

# Generated at 2022-06-14 05:53:48.271992
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # Positive test
    lines = [
        'TEST=${HOME}/yeee',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST',
    ]
    expected = collections.OrderedDict([
        ('TEST', '.../yeee'),
        ('THISIS', '.../a/test'),
        ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    ])
    actual = collections.OrderedDict(parse_env_file_contents(lines))
    assert expected == actual



# Generated at 2022-06-14 05:53:52.642384
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    parse_env_file_contents(lines)



# Generated at 2022-06-14 05:53:58.827116
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    from vistir.compat import FileNotFoundError, IOError

    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    load_env_file(lines, write_environ=dict())

    try:
        with open('non-existing.file') as f:
            lines = f.readlines()
    except (FileNotFoundError, IOError):
        lines = ['UNIT=TESTING']

    load_env_file(lines, write_environ=dict())



# Generated at 2022-06-14 05:54:06.548356
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    r = parse_env_file_contents(lines)

    for l in lines:
        assert next(r) == l.split("=")

    try:
        next(r)
        assert False
    except StopIteration:
        pass



# Generated at 2022-06-14 05:54:16.479939
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



# Generated at 2022-06-14 05:54:25.663173
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    results = load_env_file(lines, write_environ=dict())
    print(results)
    assert results == {'TEST': '~/yeee', 'THISIS': '~/a/test', 'YOLO': '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'}



# Generated at 2022-06-14 05:54:32.967601
# Unit test for function parse_env_file_contents

# Generated at 2022-06-14 05:54:41.831979
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert dict(parse_env_file_contents(lines)) == {'TEST': '${HOME}/yeee', 'THISIS': '~/a/test',
                                                    'YOLO': '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'}



# Generated at 2022-06-14 05:54:43.711622
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import doctest
    doctest.testmod()



# Generated at 2022-06-14 05:54:46.339351
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import doctest

    doctest.testmod()


if __name__ == '__main__':
    test_parse_env_file_contents()

# Generated at 2022-06-14 05:54:54.775370
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert list(parse_env_file_contents(['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'])) == [
        ('TEST',  '${HOME}/yeee'),
        ('THISIS', '~/a/test'),
        ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    ]



# Generated at 2022-06-14 05:55:00.797356
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import textwrap

    test_data = textwrap.dedent('''\
        TEST=${HOME}/yeee-$PATH
        A=B
        C=D
        E=F
        ''')
    lines = test_data.split('\n')

    assert list(parse_env_file_contents(lines)) == [
        ('TEST', expand('${HOME}/yeee-$PATH')),
        ('A', 'B'),
        ('C', 'D'),
        ('E', 'F'),
    ]

# Generated at 2022-06-14 05:55:13.517697
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = [
        'TEST=${HOME}/yeee',
        'TEST2="hello world"',
        'TEST3=$TEST2',
        """TEST4="hello \"world" world" """,
        "select = from where \\\"=",
        'select = from where \\=',
        'select = from where \\',
        "select = from where '",
        'select = from where "',
        """select = from where " '""",
        'select = from where " "',
        "select = from where ' '",
    ]

    result = list(parse_env_file_contents(lines))


# Generated at 2022-06-14 05:55:20.548994
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    values = parse_env_file_contents(lines)

    prof_directory = os.path.abspath(os.path.expanduser("~"))
    for k, v in values:
        if k == "TEST":
            assert v == prof_directory + "/yeee-" + os.environ["PATH"]
        elif k == "THISIS":
            assert v == prof_directory + "/a/test"

# Generated at 2022-06-14 05:55:30.856142
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    expected = [
        ('TEST', '.../yeee'),
        ('THISIS', '.../a/test'),
        ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'),
    ]

    out = parse_env_file_contents(lines)

    for x, y in zip(out, expected):
        assert x == y



# Generated at 2022-06-14 05:55:40.784771
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert list(parse_env_file_contents(lines)) == [
        ('TEST', '${HOME}/yeee'),
        ('THISIS', '~/a/test'),
        ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'),
    ]

# Generated at 2022-06-14 05:55:53.326122
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    test = 'TEST=${HOME}/yeee-$PATH'
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    expected_results = [('TEST', '.../.../yeee-...:...'),
                        ('THISIS', '.../a/test'),
                        ('YOLO',
                         '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]

    lines = [x for x in parse_env_file_contents(lines)]

    for x, y in zip(lines, expected_results):
        assert x == y



# Generated at 2022-06-14 05:56:03.021817
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    setting_dict = collections.OrderedDict(parse_env_file_contents(lines=lines))

    assert len(setting_dict) == 3
    assert setting_dict['TEST'].endswith('/yeee')
    assert setting_dict['THISIS'].endswith('/a/test')
    assert setting_dict['YOLO'].endswith('/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')

# Generated at 2022-06-14 05:56:10.104750
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = [
        'TEST=${HOME}/yeee',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST',
    ]

    result = parse_env_file_contents(lines)

    assert result == [
        ('TEST', '${HOME}/yeee'),
        ('THISIS', '~/a/test'),
        ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'),
    ]



# Generated at 2022-06-14 05:56:20.559121
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = """
    TEST=${HOME}/yeee
    THISIS=~/a/test
    YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST
    """.splitlines()

    contents = dict(parse_env_file_contents(lines))

    assert contents == {
        'TEST': expand('${HOME}/yeee'),
        'THISIS': expand('~/a/test'),
        'YOLO': expand('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'),
    }

