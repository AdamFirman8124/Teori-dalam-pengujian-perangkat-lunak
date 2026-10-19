

# Generated at 2022-06-14 05:49:11.689711
# Unit test for function load_env_file
def test_load_env_file():
    """
    >>> load_env_file(['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'], write_environ=dict())
    OrderedDict([('TEST', '.../.../yeee-...:...'),
             ('THISIS', '.../a/test'),
             ('YOLO',
              '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])
    """
    import doctest

    doctest.testmod()



# Generated at 2022-06-14 05:49:23.205008
# Unit test for function load_env_file
def test_load_env_file():
    old = os.environ.copy()

    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    os.environ.clear()


# Generated at 2022-06-14 05:49:34.830127
# Unit test for function load_env_file
def test_load_env_file():
    # Ignore incorrect units as we are only unit testing this file
    # pylint: disable=invalid-name
    lines = ['TEST=${HOME}/yeee-$PATH',
             'THISIS=~/a/test',
             'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    obtained = load_env_file(lines, write_environ=dict())

# Generated at 2022-06-14 05:49:44.354040
# Unit test for function load_env_file
def test_load_env_file():
    import os
    import tempfile
    import shutil

    tempdir = tempfile.mkdtemp(prefix="test_load_env_file_")
    os.chdir(tempdir)

    try:
        env_file = os.path.join(tempdir, "env.txt")

        with open(env_file, "w") as f:
            f.write("ONE=one\n")
            f.write("TWO=two\n")
            f.write("THREE=three\n")

        overwrite_environ = dict()

        result = load_env_file(lines=env_file, write_environ=overwrite_environ)

        assert result == collections.OrderedDict([("ONE", "one"), ("TWO", "two"), ("THREE", "three")])

    finally:
        os

# Generated at 2022-06-14 05:49:55.622693
# Unit test for function load_env_file
def test_load_env_file():
    import tempfile

    def write_env_file(**kwargs):
        fd, filename = tempfile.mkstemp(text=True)
        with open(fd, 'w') as f:
            for key, value in kwargs.items():
                f.write(f'{key}={value}')
        return filename

    import os

    os.environ.update(TEST='this is a test')
    os.environ['TEST2'] = 'this is another test'

    env = load_env_file(filename=write_env_file(TEST='test', TEST2='test2'))

    assert 'TEST' in env
    assert env['TEST'] == 'test'
    assert 'TEST2' in env
    assert env['TEST2'] == 'test2'

# Generated at 2022-06-14 05:49:56.650826
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 05:49:57.906338
# Unit test for function load_env_file
def test_load_env_file():
    # TODO
    pass



# Generated at 2022-06-14 05:50:01.945450
# Unit test for function load_env_file
def test_load_env_file():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test']
    load_env_file(lines, write_environ=dict())



# Generated at 2022-06-14 05:50:04.445742
# Unit test for function load_env_file
def test_load_env_file():
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)

# Generated at 2022-06-14 05:50:14.667971
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    actual = load_env_file(lines, write_environ=dict())
    expected = collections.OrderedDict([('TEST', os.path.expanduser('${HOME}/yeee')),
                                        ('THISIS', os.path.expanduser('~/a/test')),
                                        ('YOLO', os.path.expanduser('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'))])

    assert actual == expected


if __name__ == '__main__':
    import doctest

# Generated at 2022-06-14 05:50:24.736249
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    result = load_env_file(lines, write_environ=dict())
    assert result['TEST'] == expand('${HOME}/yeee')
    assert result['THISIS'] == expand('~/a/test')
    assert result['YOLO'] == expand('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')

# Generated at 2022-06-14 05:50:37.226888
# Unit test for function load_env_file
def test_load_env_file():
    def assert_dict_is_equal(d1: typing.MutableMapping, d2: typing.MutableMapping):
        assert d1.keys() == d2.keys()

        for k in d1:
            assert d1[k] == d2[k]

    lines = [
        'TEST=${HOME}/yeee-$PATH',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    ]

    result = load_env_file(lines)

# Generated at 2022-06-14 05:50:45.944415
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import tempfile
    import collections

    tdir = tempfile.TemporaryDirectory()
    env_file = os.path.join(tdir.name, 'e1.env')

    with open(env_file, 'w') as f:
        f.write('# This is a comment\n')
        f.write('\n')
        f.write('DEBUG=1\n')
        f.write('PORT=5000\n')
        f.write('DATABASE_URL=postgres://localhost/mydb\n')
        f.write('# This is another comment\n')
        f.write('EMPTY=\n')
        f.write('FOO=BAR\n')
        f.write('BAZ=QUX\n')
        f.write('QUX="This is a test"\n')

# Generated at 2022-06-14 05:50:54.855029
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    data = [
        'TEST=${HOME}/yeee',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'

    ]
    res = load_env_file(data)
    assert 'TEST' in res
    assert 'THISIS' in res
    assert 'YOLO' in res
    # print(res)


if __name__ == '__main__':
    test_parse_env_file_contents()

# Generated at 2022-06-14 05:51:05.267249
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    env_vars = [
        'PYTHONPATH=~/test',
        'PATH=~/test:$PATH',
        'NOT_IN_PATH=$NOT_IN_PATH',
        'THIS=${NOT_IN_PATH}',
        'EUID=1000',
        'USER=testuser',
        'LOGNAME=testuser'
    ]
    env_vars = parse_env_file_contents(env_vars)
    env_vars = dict(env_vars)

    assert env_vars['PYTHONPATH'] == '~/test'
    assert env_vars['PATH'] == '~/test:$PATH'
    assert env_vars['NOT_IN_PATH'] == '$NOT_IN_PATH'

# Generated at 2022-06-14 05:51:06.513062
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import doctest

    doctest.testmod()



# Generated at 2022-06-14 05:51:07.262152
# Unit test for function load_env_file
def test_load_env_file():
    pass



# Generated at 2022-06-14 05:51:15.480079
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # Unit test for function parse_env_file_contents
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    dict_lhs = dict()
    dict_lhs['TEST'] = '${HOME}/yeee'
    dict_lhs['THISIS'] = '~/a/test'
    dict_lhs['YOLO'] = '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'

    dict_rhs = dict()
    for key, val in parse_env_file_contents(lines):
        dict_rhs[key] = val

    assert dict_l

# Generated at 2022-06-14 05:51:26.601410
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    res = list(parse_env_file_contents(lines))

    # NOTE: We cannot assume that the $PATH will be the same on all machines.
    #       So we assume that it contains at least 2 path-elements and replace the first
    #       path-element with 3 dots:
    path_elements = list(filter(len, res[0][1].split('/')))
    if len(path_elements) > 1:
        path_elements[0] = '...'
    res[0] = (res[0][0], '/'.join(path_elements))



# Generated at 2022-06-14 05:51:30.967282
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines)



# Generated at 2022-06-14 05:51:45.561752
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import io
    import unittest

    class ParseEnvFileContentsTestCase(unittest.TestCase):
        def test_simple_env_file_mode(self):
            envfile = io.StringIO("""
export CLASSPATH=$CLASSPATH:$(find $HADOOP_HOME_LOCAL -iname "*.jar" | tr '\n' ':')
export PATH=$PATH:$HADOOP_HOME_LOCAL/bin
            """)

            values = parse_env_file_contents(envfile)


# Generated at 2022-06-14 05:51:56.075489
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    result = dict(parse_env_file_contents(lines))
    assert result['TEST'] == os.path.expanduser('~/yeee-$PATH')
    assert result['THISIS'] == os.path.expanduser('~/a/test')
    assert result['YOLO'] == os.path.expanduser('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')

# Generated at 2022-06-14 05:52:08.577598
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = [
        "TEST=${HOME}/yeee-$PATH",
        "THISIS=~/a/test",
        "YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"
    ]

    result = parse_env_file_contents(lines)

    assert isinstance(result, collections.Generator)


# Generated at 2022-06-14 05:52:17.433809
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ["a=b", "c=d", "e='f'", 'g="h"', r'i=\n', "j='\n'", 'k="\n"', "l='\n\n'", 'm="\n\n"']
    expected = [("a", "b"), ("c", "d"), ("e", "f"), ("g", "h"), ("i", "\\n"),
                ("j", "\n"), ("k", "\n"), ("l", "\n\n"), ("m", "\n\n")]
    actual = [i for i in parse_env_file_contents(lines)]

    assert actual == expected

# Generated at 2022-06-14 05:52:25.827605
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = [
        'TEST=${HOME}/yeee',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST',
    ]

    result = parse_env_file_contents(lines)

    assert any(k == 'TEST' and v == expand('${HOME}/yeee') for k, v in result)
    assert any(k == 'THISIS' and v == expand('~/a/test') for k, v in result)
    assert any(k == 'YOLO' and v == expand('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST') for k, v in result)



# Generated at 2022-06-14 05:52:34.603910
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert list(parse_env_file_contents()) == []
    assert list(parse_env_file_contents(["   ", " ", "\n", "\r", "\r", "\r\n"])) == []
    assert list(parse_env_file_contents(["# this line is commented", "   # this line is only whitespace and comment", '"name"=value', "'n'='v'", "k=v"])) == [
        ("name", "value"),
        ("n", "v"),
        ("k", "v"),
    ]



# Generated at 2022-06-14 05:52:44.470318
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    changes = parse_env_file_contents(lines)
    assert changes == [('TEST', '.../.../yeee-...:...'),
                       ('THISIS', '.../a/test'),
                       ('YOLO',
                        '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]



# Generated at 2022-06-14 05:52:54.415041
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = [
        "export TEST=${HOME}/yeee-$PATH",
        "export THISIS=~/a/test",
        "export YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST",
    ]
    changes = parse_env_file_contents(lines)

    result = collections.OrderedDict(changes)

    expected_result = collections.OrderedDict(
        [
            ("TEST", "{}/yeee-{}".format(expand("${HOME}"), expand("${PATH}"))),
            ("THISIS", expand("~/a/test")),
            ("YOLO", "$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"),
        ]
    )

    assert result == expected

# Generated at 2022-06-14 05:53:07.705998
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    def _assert_expected(expected, lines):
        actual = parse_env_file_contents(lines)
        assert expected == list(actual)

    # Empty file
    _assert_expected([], [])

    # A couple good lines
    _assert_expected([
        ('FOO', 'bar'),
        ('BAR', 'baz')
    ], [
        'FOO=bar',
        'BAR=baz'
    ])

    # A couple good lines with comments
    _assert_expected([
        ('FOO', 'bar'),
        ('BAR', 'baz')
    ], [
        'FOO=bar',
        '# comment',
        'BAR=baz'
    ])

    # Line with spaces and comments

# Generated at 2022-06-14 05:53:09.469646
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import doctest
    doctest.run_docstring_examples(parse_env_file_contents, globals())

