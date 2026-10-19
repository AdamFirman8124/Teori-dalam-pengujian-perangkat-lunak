

# Generated at 2022-06-14 05:49:07.217781
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import doctest

    doctest.testmod()


if __name__ == "__main__":
    test_parse_env_file_contents()

# Generated at 2022-06-14 05:49:16.395723
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    filename = os.path.join(os.path.dirname(__file__), 'test-env')
    lines = open(filename).readlines()

    values = parse_env_file_contents(lines)
    result = load_env_file(lines, write_environ=dict())

    assert result == {
        'TEST': 'hello/yeee-test-path',
        'THISIS': 'hello/a/test',
        'YOLO': 'hello/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST',
    }



# Generated at 2022-06-14 05:49:25.278631
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    output = load_env_file(lines, write_environ=dict())

    assert output['TEST'].endswith('/yeee')
    assert output['THISIS'].endswith('/a/test')
    assert output['YOLO'].endswith('/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')

# Generated at 2022-06-14 05:49:32.966348
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    values = parse_env_file_contents(lines)

    for k, v in values:
        assert k in {'TEST', 'THISIS', 'YOLO'}
        assert 'PATH' in v



# Generated at 2022-06-14 05:49:42.863565
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    d = dict(parse_env_file_contents(lines))
    assert d['TEST'] == '${HOME}/yeee-$PATH'
    assert d['THISIS'] == '~/a/test'
    assert d['YOLO'] == '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    d = dict(load_env_file(lines, write_environ=None))
    assert d['TEST'] == '${HOME}/yeee-$PATH'

# Generated at 2022-06-14 05:49:55.110964
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    parsed = parse_env_file_contents(lines)

    assert isinstance(parsed, collections.Generator)

    assert next(parsed) == ('TEST', '${HOME}/yeee-$PATH')
    assert next(parsed) == ('THISIS', '~/a/test')
    assert next(parsed) == ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')


# Generated at 2022-06-14 05:50:06.412890
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    """Unit tests for function parse_env_file_contents((): """
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert parse_env_file_contents(lines) == [
        ('TEST', '.../yeee'),
        ('THISIS', '.../a/test'),
        ('YOLO',
         '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    ]


if __name__ == '__main__':
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 05:50:14.997931
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ["# comment",
             "TEST=${HOME}/yeee-$PATH",
             "THISIS=~/a/test",
             "YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"]

    values = parse_env_file_contents(lines)

    from unittest import TestCase
    from unittest.mock import patch


# Generated at 2022-06-14 05:50:26.160768
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert list(parse_env_file_contents(lines)) == [('TEST', os.path.join(expand('${HOME}'), 'yeee')),
                                                    ('THISIS', os.path.join(expand('~'), 'a', 'test')),
                                                    ('YOLO', os.path.join(expand('~'), 'swaggins', '$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'))]


# Generated at 2022-06-14 05:50:28.065056
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import doctest
    doctest.testmod()



# Generated at 2022-06-14 05:50:41.782271
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    env_dict = {k: v for k, v in parse_env_file_contents(lines)}
    assert env_dict['TEST'] == f'{expand("$HOME")}/yeee'
    assert env_dict['THISIS'] == f'{expand("~")}/a/test'
    assert env_dict['YOLO'] == f'{expand("~")}/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'

# Generated at 2022-06-14 05:50:52.493713
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import io

    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    result = list(parse_env_file_contents(lines))

    assert result == [('TEST', '${HOME}/yeee'), ('THISIS', '~/a/test'), ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]

    # Try with a file object
    result = parse_env_file_contents(io.StringIO(''.join(lines)))


# Generated at 2022-06-14 05:50:55.194617
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    try:
        import doctest
        doctest.testmod()
    except ImportError:
        print("Failed to import doctest")

# Generated at 2022-06-14 05:51:05.529334
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    """
    Tests parse_env_file_contents.

    >>> lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    >>> load_env_file(lines, write_environ=dict())
    OrderedDict([('TEST', '.../yeee'),
             ('THISIS', '.../a/test'),
             ('YOLO',
              '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])

    """

# Generated at 2022-06-14 05:51:09.255292
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = [
        "TEST=${HOME}/yeee",
        "THISIS=~/a/test",
        "YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST",
    ]
    for i, j in parse_env_file_contents(lines):
        print(i, j)

# Generated at 2022-06-14 05:51:15.013722
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    from pprint import pprint

    lines = ["HOME=/Users/...", "PATH=...:..."]

    print("\n# test_parse_env_file_contents")

    pprint(list(parse_env_file_contents(lines)))


if __name__ == "__main__":
    # unit tests for this module
    test_parse_env_file_contents()

# Generated at 2022-06-14 05:51:24.759810
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    results = parse_env_file_contents(lines)
    results = list(results)
    expected_results = [('TEST', '$HOME/yeee-$PATH'), ('THISIS', '~/a/test'), ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]
    assert results == expected_results



# Generated at 2022-06-14 05:51:25.725492
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 05:51:36.741313
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import tempfile
    with tempfile.NamedTemporaryFile('wt') as fh:
        fh.write('TEST=${HOME}/yeee-$PATH\n')
        fh.write('THISIS=c:/a/test\n')
        fh.write('YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')

        fh.flush()

        with open(fh.name) as fh2:
            b = parse_env_file_contents(lines=fh2)
            d = dict(b)

            assert d['TEST'] == os.path.expanduser('~/yeee-{PATH}'.format(**os.environ))  # XXX: Is there a better way to ensure the path is expanded?


# Generated at 2022-06-14 05:51:48.529277
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    parsed_env_file_contents = parse_env_file_contents(lines)

    # Test if returned values are correct
    assert next(parsed_env_file_contents) == ('TEST', '.../yeee')
    assert next(parsed_env_file_contents) == ('THISIS', '.../a/test')
    assert next(parsed_env_file_contents) == ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')

    # Test expected exceptions

# Generated at 2022-06-14 05:51:54.564351
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import unittest

    class P(unittest.TestCase):
        def test_regex_match(self):
            res = re.match(r'\A([A-Za-z_0-9]+)=(.*)\Z', 'TEST=${HOME}/yeee-$PATH')
            self.assertEqual(res.group(1), 'TEST')
            self.assertEqual(res.group(2), '${HOME}/yeee-$PATH')

    unittest.main(module='__main__')



# Generated at 2022-06-14 05:52:07.159876
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    lines = parse_env_file_contents(lines)

    assert type(lines) == list
    assert lines[0][1] == os.environ.get('HOME', '...') + '/yeee-' + os.environ.get('PATH', '...')
    assert lines[1][1] == expand('~/a/test')
    assert lines[2][1] == expand('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')

# Generated at 2022-06-14 05:52:16.999779
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    d = dict(parse_env_file_contents(lines))
    assert d['TEST'] == expand('${HOME}/yeee')
    assert d['THISIS'] == expand('~/a/test')
    assert d['YOLO'] == expand('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')



# Generated at 2022-06-14 05:52:25.174176
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    vars = collections.OrderedDict(parse_env_file_contents(lines))

    assert vars['TEST'] == os.path.expandvars('${HOME}/yeee-$PATH')
    assert vars['THISIS'] == os.path.expandvars('~/a/test')
    assert vars['YOLO'] == os.path.expandvars('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')



# Generated at 2022-06-14 05:52:35.440824
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # Test on a valid env file
    assert list(parse_env_file_contents(['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'])) == [
        ('TEST', '${HOME}/yeee'),
        ('THISIS', '~/a/test'),
        ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    ]

    # Test on a invalid env file
    assert list(parse_env_file_contents(['TEST=', '', 'YOLO='])) == [('TEST', ''), ('YOLO', '')]

    # Test on an

# Generated at 2022-06-14 05:52:45.239278
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    expected_output = [('TEST', '.../yeee'),
                       ('THISIS', '.../a/test'),
                       ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]

    assert list(parse_env_file_contents(lines)) == expected_output


# Generated at 2022-06-14 05:52:50.804397
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())
    assert True

# Generated at 2022-06-14 05:53:04.247665
# Unit test for function parse_env_file_contents

# Generated at 2022-06-14 05:53:12.328726
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert dict(parse_env_file_contents(lines)) == {'TEST': '$HOME/yeee',
                                                    'THISIS': '~/a/test',
                                                    'YOLO': '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'}



# Generated at 2022-06-14 05:53:21.368394
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    file_lines = [
        'TEST=${HOME}/yeee-$PATH',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST',
    ]

    values = parse_env_file_contents(file_lines)
    changes = collections.OrderedDict(values)

    HOME = os.path.expanduser('~')
    PATH = os.getenv('PATH')


# Generated at 2022-06-14 05:53:32.744801
# Unit test for function parse_env_file_contents

# Generated at 2022-06-14 05:53:42.660567
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    test_data = """
    TEST=${HOME}/yeee-$PATH
    THISIS=~/a/test
    YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST
    """
    loaded = load_env_file(lines=test_data.strip().split("\n")[1:], write_environ=None)
    expected_data = collections.OrderedDict([
        ('TEST', '.../.../yeee-...:...'),
        ('THISIS', '.../a/test'),
        ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    ])
    assert loaded == expected_data

# Generated at 2022-06-14 05:53:52.514777
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    actual = []

    for line in ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']:
        actual.append(list(parse_env_file_contents([line])))

    expected = [[('TEST', '.../yeee')], [('THISIS', '.../a/test')], [('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]]

    assert all(len(a) == len(b) for a, b in zip(actual, expected))
    assert all(a == b for a, b in zip(actual, expected))



# Generated at 2022-06-14 05:53:57.976676
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())
    assert lines == ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']



# Generated at 2022-06-14 05:54:04.423776
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # From honcho.
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())
    assert True

# Generated at 2022-06-14 05:54:05.064037
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 05:54:14.000881
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    """
    Note:
    - must pass this to test_load_env_file.py
    - the first line will cause the test to fail because the path to ~/.bashrc is probably different

    >>> lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    >>> load_env_file(lines, write_environ=dict())
    OrderedDict([('TEST', '/.../yeee'),
             ('THISIS', '.../a/test'),
             ('YOLO',
              '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])
    """

# Generated at 2022-06-14 05:54:20.014973
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ["KEY=value", "ANOTHER_KEY=another value", "PATH=${HOME}/my/path"]

    result = dict(parse_env_file_contents(lines))
    expected = {"KEY": "value", "ANOTHER_KEY": "another value", "PATH": "${HOME}/my/path"}
    assert result == expected

# Generated at 2022-06-14 05:54:25.715062
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    """
    Unit test for function parse_env_file_contents.
    """

    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    load_env_file(lines, write_environ=dict())

# Generated at 2022-06-14 05:54:32.046985
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import io

    lines = ['TEST=${HOME}/yeee-${PATH}', 'THISIS=~/a/test']

    output = collections.OrderedDict(parse_env_file_contents(lines))

    expected = collections.OrderedDict([('TEST', os.path.join(os.path.expanduser('~'), 'yeee-' + os.environ['PATH'])),
                                        ('THISIS', os.path.join(os.path.expanduser('~'), 'a', 'test'))])

    assert output == expected



# Generated at 2022-06-14 05:54:43.765399
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    test_env_file = [
        "TEST=${HOME}/yeee",
        "THISIS=~/a/test",
        "YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST",
    ]

    results = parse_env_file_contents(test_env_file)

    # assert isinstance(results, tuple)
    for k, v in results:
        assert isinstance(k, str)
        assert isinstance(v, str)


# Generated at 2022-06-14 05:54:54.682344
# Unit test for function parse_env_file_contents

# Generated at 2022-06-14 05:55:06.116264
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    parsed = parse_env_file_contents(lines)

    assert parsed.__next__() == ('TEST', os.path.join(os.environ['HOME'], 'yeee'))
    assert parsed.__next__() == ('THISIS', os.path.join(os.environ['HOME'], 'a/test'))
    assert parsed.__next__() == ('YOLO', os.path.join(os.environ['HOME'], 'swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'))



# Generated at 2022-06-14 05:55:16.300508
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    """
    Tests the function parse_env_file_contents
    """

    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    assert list(parse_env_file_contents(lines)) == [
        ('TEST', expand('${HOME}/yeee')),
        ('THISIS', expand('~/a/test')),
        ('YOLO', expand('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')),
    ]



# Generated at 2022-06-14 05:55:28.979853
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    test_lines = '''
    TEST=$HOME/yeee
    THISIS=~/a/test
    YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST
    '''

    lines = test_lines.split('\n')

    values = parse_env_file_contents(lines)
    # Test string variables
    for k, v in values:
        if k == 'TEST':
            assert v == '${HOME}/yeee'
        elif k == 'THISIS':
            assert v == '~/a/test'
        elif k == 'YOLO':
            assert v == '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'

    # Test escaped varibles
   

# Generated at 2022-06-14 05:55:37.104165
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOMEPATH}', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    values = parse_env_file_contents(lines)

    # test that output is ordered
    assert next(values)[0] == 'TEST'

    for k, v in values:
        assert '$' not in v or '${' in v

# Generated at 2022-06-14 05:55:49.327134
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    print(parse_env_file_contents(['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']))

# Generated at 2022-06-14 05:56:00.060967
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    result = collections.OrderedDict(parse_env_file_contents(lines))
    assert result == collections.OrderedDict([('TEST', '.../yeee'),
                                   ('THISIS', '.../a/test'),
                                   ('YOLO',
                                    '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])

# Generated at 2022-06-14 05:56:10.435079
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import sys

    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    changes = collections.OrderedDict()

    for k, v in parse_env_file_contents(lines):
        changes[k] = expand(v)

    assert len(changes) == 3

    assert 'TEST' in changes
    assert changes['TEST'] == '{}/yeee'.format(os.path.expanduser('~'))

    assert 'THISIS' in changes
    assert changes['THISIS'] == '{}/a/test'.format(os.path.expanduser('~'))

    assert 'YOLO' in changes
    assert changes

# Generated at 2022-06-14 05:56:22.441766
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = """
TEST=$HOME/yeee-$PATH
THISIS=~/a/test
YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST
    """.strip().splitlines()

    env = {}

    for k, v in parse_env_file_contents(lines):
        env[k] = v

    assert env == {
        'TEST': '{}/yeee-{}'.format(
            expand('$HOME'), expand('$PATH'),
        ),
        'THISIS': expand('~/a/test'),
        'YOLO': expand('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'),
    }

# Generated at 2022-06-14 05:56:41.502606
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import pprint

    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert list(parse_env_file_contents(lines)) == [
        ('TEST', expand('${HOME}/yeee')),
        ('THISIS', expand('~/a/test')),
        ('YOLO', expand('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')),
    ]

    # Unit test for function load_env_file
    def test_load_env_file():
        import pprint
        os_environ = dict()


# Generated at 2022-06-14 05:56:54.410923
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert parse_env_file_contents(['TEST=${HOME}/yeee']) == [('TEST', '.../yeee')]
    assert parse_env_file_contents(['THISIS=~/a/test']) == [('THISIS', '.../a/test')]
    assert parse_env_file_contents(['YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']) == [
        ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]

# Generated at 2022-06-14 05:56:59.449285
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())



# Generated at 2022-06-14 05:57:11.918142
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    values = parse_env_file_contents(lines)

    changes = collections.OrderedDict()

    for k, v in values:
        v = expand(v)

        changes[k] = v

    assert len(changes) == 3
    assert changes['TEST'] == '.../.../yeee-...:...'
    assert changes['THISIS'] == '.../a/test'
    assert changes['YOLO'] == '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'

# Generated at 2022-06-14 05:57:20.774989
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert list(parse_env_file_contents(lines)) == [('TEST', '${HOME}/yeee'),
                                                    ('THISIS', '~/a/test'),
                                                    ('YOLO',
                                                     '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]



# Generated at 2022-06-14 05:57:29.325440
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import io
    import unittest

    class TestParseEnvFileContents(unittest.TestCase):
        def test_01(self):
            # Test 1
            lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
            lines_iter = iter(lines)
            parsed_lines = parse_env_file_contents(lines_iter)
            results = []
            for line in parsed_lines:
                results.append(line)


# Generated at 2022-06-14 05:57:40.699937
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    values = parse_env_file_contents(lines)

    for k, v in values:
        v = expand(v)


# Generated at 2022-06-14 05:57:53.848987
# Unit test for function parse_env_file_contents

# Generated at 2022-06-14 05:58:03.074916
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    env = load_env_file(lines, write_environ=dict())
    assert env == collections.OrderedDict([('TEST', '.../yeee'),
                                     ('THISIS', '.../a/test'),
                                     ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])



# Generated at 2022-06-14 05:58:09.212180
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['HOME=~/', 'PATH=${HOME}/bin:${HOME}/lib']
    contents = parse_env_file_contents(lines)
    contents_expanded = [(k, expand(v)) for k, v in contents]
    assert contents_expanded == [('HOME', '.../'), ('PATH', '.../bin:.../lib')]



# Generated at 2022-06-14 05:58:28.324095
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert dict(parse_env_file_contents(lines)) == {
        'TEST': '${HOME}/yeee', 'THISIS': '~/a/test', 'YOLO': '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    }



# Generated at 2022-06-14 05:58:39.005932
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    values = parse_env_file_contents(lines)

    assert list(values) == [('TEST', '${HOME}/yeee-$PATH'), ('THISIS', '~/a/test'), ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]



# Generated at 2022-06-14 05:58:50.091515
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    result = {}
    for k, v in parse_env_file_contents(lines):
        result[k] = v


# Generated at 2022-06-14 05:59:01.793412
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    assert list(parse_env_file_contents(lines)) == [('TEST', '${HOME}/yeee'), ('THISIS', '~/a/test'), ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]

    lines = ['TEST=$HOME/yeee', 'THISIS=~/a/test']
    assert list(parse_env_file_contents(lines)) == [('TEST', '$HOME/yeee'), ('THISIS', '~/a/test')]
