

# Generated at 2022-06-14 05:49:17.003327
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():

    expected = {
        "TEST": "<path>/yeee",
        "THISIS": "<path>/a/test",
        # doesn't matter what the value of this is, as parse_env_file_contents
        # doesn't expand the variables from the current os.environ.
        "YOLO": "~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST",
    }

    lines = [
        f"{key}={value}"
        for key, value in expected.items()
    ]

    actual = collections.OrderedDict(parse_env_file_contents(lines))


# Generated at 2022-06-14 05:49:19.324686
# Unit test for function load_env_file
def test_load_env_file():
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    test_load_env_file()

# Generated at 2022-06-14 05:49:28.482548
# Unit test for function load_env_file
def test_load_env_file():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    os.environ['HOME'] = '/home/user'
    os.environ['PATH'] = '/usr/bin:/usr/local/bin:/home/user/.local/bin'
    load_env_file(lines)
    assert os.environ['TEST'] == '/home/user/yeee'
    assert os.environ['THISIS'] == '/home/user/a/test'
    assert os.environ['YOLO'] == '/home/user/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    assert os.environ

# Generated at 2022-06-14 05:49:37.130153
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert list(parse_env_file_contents(["TEST=thisismytest"])) == [("TEST", "thisismytest")]
    assert list(parse_env_file_contents(["TEST=thisismytest-1", "TEST2=thisismytest-2"])) == [("TEST", "thisismytest-1"),
                                                                                             ("TEST2", "thisismytest-2")]


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 05:49:39.925529
# Unit test for function load_env_file
def test_load_env_file():
    import doctest

    doctest.testmod(optionflags=doctest.ELLIPSIS | doctest.REPORT_ONLY_FIRST_FAILURE)


# End of file __init__.py

# Generated at 2022-06-14 05:49:53.463933
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    """
    Test...
    :return:
    """
    content = [
        'TEST=${HOME}/yeee-$PATH',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    ]

    result = parse_env_file_contents(content)

    for (idx, (k, v)) in enumerate(result):
        if idx == 0:
            assert k == 'TEST'
            assert v == '${HOME}/yeee-$PATH'
        elif idx == 1:
            assert k == 'THISIS'
            assert v == '~/a/test'
        elif idx == 2:
            assert k == 'YOLO'

# Generated at 2022-06-14 05:50:03.980798
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    from . import parse_env_file_contents

    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    results = parse_env_file_contents(lines)
    assert next(results) == ('TEST', '.../yeee')
    assert next(results) == ('THISIS', '.../a/test')
    assert next(results) == ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')



# Generated at 2022-06-14 05:50:14.468722
# Unit test for function load_env_file
def test_load_env_file():
    lines = [
        'TEST=${HOME}/yeee-$PATH',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    ]
    environ_copy = os.environ.copy()
    expected = {
        'TEST': '.../.../yeee-...:...',
        'THISIS': '.../a/test',
        'YOLO': '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    }

    actual = load_env_file(lines, write_environ=dict())

    assert actual
    assert isinstance(actual, collections.OrderedDict)
    assert dict(actual)

# Generated at 2022-06-14 05:50:24.453218
# Unit test for function load_env_file
def test_load_env_file():
    from .sandbox import Sandbox

    with Sandbox() as sandbox:
        lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

        changes = load_env_file(lines)


# Generated at 2022-06-14 05:50:32.143722
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    environ = load_env_file(lines, write_environ=dict())
    assert environ['TEST'] == os.path.expanduser('~/yeee')
    assert environ['THISIS'] == os.path.expanduser('~/a/test')

# Generated at 2022-06-14 05:50:43.695219
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    """
    Tests for function load_env_file
    """
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    expected_values = [('TEST', '$HOME/yeee'), ('THISIS', '~/a/test'),
                       ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]
    results = parse_env_file_contents(lines)
    for result in results:
        assert result in expected_values



# Generated at 2022-06-14 05:50:56.819333
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    from io import StringIO

    filename = "test.env"
    contents = 'TEST=${HOME}/yeee\nTHISIS=~/a/test\nYOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST\n'
    lines = StringIO(contents)

    env_data = parse_env_file_contents(lines)

    env_data = dict(env_data)

    assert len(env_data) == 3
    assert env_data['TEST'] == "${HOME}/yeee"
    assert env_data['THISIS'] == "~/a/test"
    assert env_data['YOLO'] == "~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"

# Generated at 2022-06-14 05:51:06.322474
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=$HOME/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    assert list(parse_env_file_contents(lines)) == [('TEST', '$HOME/yeee'),
                                                    ('THISIS', '~/a/test'),
                                                    ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]



# Generated at 2022-06-14 05:51:12.421614
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    values = parse_env_file_contents(lines)

    od = collections.OrderedDict(values)

    print(od)

    assert od['TEST'] == os.path.join(os.path.expanduser('~'), 'yeee')
    assert od['THISIS'] == os.path.join(os.path.expanduser('~'), 'a', 'test')

# Generated at 2022-06-14 05:51:14.669218
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    """
    Tests function parse_env_file_contents
    """
    import doctest
    doctest.testmod()



# Generated at 2022-06-14 05:51:26.028175
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    """
    From honcho.
    """
    expected = [('TEST', '.../.../yeee-...:...'), ('THISIS', '.../a/test'), ('YOLO',
                                                                            '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]  # pylint: disable=line-too-long

    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    actual = [line for line in parse_env_file_contents(lines)]

    for i, _ in enumerate(expected):
        expected_key, expected_value = expected[i]

# Generated at 2022-06-14 05:51:27.982012
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import doctest

    doctest.testmod()



# Generated at 2022-06-14 05:51:36.016598
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert list(parse_env_file_contents(lines)) == [
        ('TEST', expand('${HOME}/yeee')),
        ('THISIS', expand('~/a/test')),
        ('YOLO', expand('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'))
    ]



# Generated at 2022-06-14 05:51:41.094538
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=None)



# Generated at 2022-06-14 05:51:46.497776
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert load_env_file(lines, write_environ=dict()) == OrderedDict(
        [('TEST', '.../yeee'), ('THISIS', '.../a/test'), ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])



# Generated at 2022-06-14 05:51:58.634086
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ["TEST=${HOME}/yeee", "THISIS=~/a/test", "YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"]
    result = parse_env_file_contents(lines)

    assert list(result) == [("TEST", "{}/yeee".format(os.environ.get("HOME", None))), ("THISIS", "{}/a/test".format(os.environ.get("HOME", None))), ("YOLO", "{}/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST".format(os.environ.get("HOME", None)))]

# Generated at 2022-06-14 05:52:08.613677
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    result = load_env_file(lines, write_environ=dict())
    assert result == collections.OrderedDict({'TEST': expand('${HOME}/yeee'),
                                          'THISIS': expand('~/a/test'),
                                          'YOLO': expand('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')})



# Generated at 2022-06-14 05:52:19.113168
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert load_env_file(lines, write_environ=dict()) == collections.OrderedDict(
        (('TEST', '.../yeee'),
         ('THISIS', '.../a/test'),
         ('YOLO',
          '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'))
    )
    lines = ['\u0410\u0411\u0412=\u0413\u0414', '\u0415\u0416=\u0417\u0418']
    assert load_env

# Generated at 2022-06-14 05:52:31.422168
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    data = collections.OrderedDict(list(parse_env_file_contents(lines)))

    test_files = {
        "TEST": "~/yeee",
        "THISIS": "~/a/test",
        "YOLO": "~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST",
        }

    for filename, expected in test_files.items():
        actual = data[filename]
        assert os.path.expanduser(actual) == os.path.expanduser(expected)

# Generated at 2022-06-14 05:52:36.648297
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    for key, val in parse_env_file_contents(lines):
        assert key
        assert val


if __name__ == '__main__':
    import doctest

    doctest.testmod(optionflags=doctest.ELLIPSIS)

# Generated at 2022-06-14 05:52:47.545570
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = [
        "TEST=${HOME}/yeee",
        "THISIS=~/a/test",
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST',
    ]
    res = dict(parse_env_file_contents(lines))
    assert isinstance(res, dict)
    assert len(res) == 3
    assert res['TEST'].endswith('yeee')
    assert res['THISIS'].endswith('a/test')
    assert res['YOLO'].endswith('swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')



# Generated at 2022-06-14 05:52:54.732347
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    TEST_ROOT = os.path.abspath(os.path.dirname(__file__))

    lines = [
        "DB_HOST=localhost", "DB_NAME=default_db_name", "DB_USER=default_user",
        "DB_PASSWORD=default_password", "DB_PORT=5432",
        "INHABITANTS_ROOT_DIR=" + TEST_ROOT
    ]

    p = parse_env_file_contents(lines)
    changes = load_env_file(lines)

    assert len(changes) == len(lines)

    assert changes["INHABITANTS_ROOT_DIR"] == TEST_ROOT

# Generated at 2022-06-14 05:53:01.731926
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    for key, val in parse_env_file_contents(lines):
        assert val.startswith(os.path.expanduser('~'))



# Generated at 2022-06-14 05:53:13.046593
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import sys
    import tempfile

    lines = [
        'TEST=${HOME}/yeee',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST',
        'KURWA=this is some utf-8: żółć'
    ]

    # Create a temporary file to avoid messing up with the existing .env file
    with tempfile.NamedTemporaryFile() as temp:
        # Write the contents to the temporary file
        for line in lines:
            temp.write((line + '\n').encode('utf-8'))

        # Get the file pointer to the beginning of the file
        temp.seek(0)

        # Load the result of parsing temp into result

# Generated at 2022-06-14 05:53:21.676975
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # Load single line without os path expansion
    lines = ['TEST=${HOME}/yeee']
    values = parse_env_file_contents(lines)
    assert next(values) == ('TEST', '${HOME}/yeee')
    try:
        next(values)
    except StopIteration:
        pass  # This is the correct outcome

    # Load line with os path expansion
    lines = ['TEST=${HOME}/yeee']
    values = parse_env_file_contents(lines)
    assert next(values) == ('TEST', expand('${HOME}/yeee'))
    try:
        next(values)
    except StopIteration:
        pass  # This is the correct outcome

    # Load multiple lines without os path expansion

# Generated at 2022-06-14 05:53:35.222340
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    """
    >>> lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    >>> parse_env_file_contents(lines)
    <generator object parse_env_file_contents at ...>
    """
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    parse_env_file_contents(lines)



# Generated at 2022-06-14 05:53:48.070662
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = [
        '    TEST=${HOME}/yeee',
        '   THISIS=~/a/test',
        'YOLO          =~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST',
        'HASHTAG=hosue',
        '',
        '# comments are ignored',
        '  # and so are comments with leading whitespace',
        '#! and comment lines that start with #!',
    ]
    pairs = list(parse_env_file_contents(lines))

# Generated at 2022-06-14 05:53:49.547857
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import doctest
    doctest.testmod(verbose=1)



# Generated at 2022-06-14 05:53:51.005307
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import doctest
    doctest.testmod()



# Generated at 2022-06-14 05:53:58.015279
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    def load_lines(*lines: str) -> collections.OrderedDict:
        vals = parse_env_file_contents(lines)
        return collections.OrderedDict(vals)

    assert load_lines('FOO=${HOME}/path') == collections.OrderedDict([('FOO', '~/path')])
    assert load_lines('FOO1=$PATH:~/path') == collections.OrderedDict([('FOO1', '.:~/path')])
    assert load_lines('FOO2=$PATH:~/path:$PATH') == collections.OrderedDict([('FOO2', '.:~/path:.')])
    assert load_lines('FOO3="~/path:$PATH"') == collections.OrderedDict([('FOO3', '~/path:.')])

# Generated at 2022-06-14 05:54:11.626424
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # Create a string that contains the test input, column by column
    test_input = """
    TEST=${HOME}/yeee
    THISIS=~/a/test
    YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST
    """

    # Split the input by line, removing leading and trailing spaces, and filter out empty lines
    lines = [line.strip() for line in test_input.split("\n") if line.strip()]

    # Execute the test
    output = parse_env_file_contents(lines)

    # Split the output by line, and filter out empty lines
    output = [line.strip() for line in output if line.strip()]

    # Create a string that contains the expected test output, column by column

# Generated at 2022-06-14 05:54:19.249844
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert list(parse_env_file_contents(lines)) == [('TEST', '${HOME}/yeee'), ('THISIS', '~/a/test'), ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]



# Generated at 2022-06-14 05:54:30.947024
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # Simple match
    assert list(parse_env_file_contents(['TEST=HELLO'])) == [('TEST', 'HELLO')]

    # Single quoted value
    assert list(parse_env_file_contents(["TEST='HELLO'"])) == [('TEST', 'HELLO')]

    # Double quoted value
    assert list(parse_env_file_contents(['TEST="HELLO"'])) == [('TEST', 'HELLO')]

    # Unquoted value
    assert list(parse_env_file_contents(['TEST=HELLO'])) == [('TEST', 'HELLO')]

    # Empty value
    assert list(parse_env_file_contents(['TEST='])) == [('TEST', '')]



# Generated at 2022-06-14 05:54:44.038322
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import unittest

    class TestParseEnvFileContents(unittest.TestCase):

        def test_parse_env_file_1(self):
            print("test_parse_env_file_1")

            filename = os.path.join(os.path.dirname(__file__), "testdata", "envfile", "envfile1.env")

            with open(filename) as f:
                content = parse_env_file_contents(f)
                content = collections.OrderedDict(content)


# Generated at 2022-06-14 05:54:45.662307
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert parse_env_file_contents([]) == iter([])

