

# Generated at 2022-06-14 05:49:09.092172
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import sys
    import doctest
    doctest.testmod(sys.modules[__name__])


if __name__ == '__main__':
    test_parse_env_file_contents()

# Generated at 2022-06-14 05:49:14.421920
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())



# Generated at 2022-06-14 05:49:26.165024
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee']
    assert list(parse_env_file_contents(lines)) == [('TEST', os.path.expanduser('~/yeee'))]

    lines = ['TEST=${HOME}/yeee-$PATH']
    assert list(parse_env_file_contents(lines)) == [('TEST', os.path.expanduser('~/yeee-{}'.format(os.environ.get('PATH'))))]

    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

# Generated at 2022-06-14 05:49:29.889716
# Unit test for function load_env_file
def test_load_env_file():
    import doctest
    doctest.testmod()



# Generated at 2022-06-14 05:49:38.660365
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    """
    parse_env_file_contents
    """
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())
    # expected OrderedDict([('TEST', '.../yeee'),
    #              ('THISIS', '.../a/test'),
    #              ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])



# Generated at 2022-06-14 05:49:50.010528
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    env = dict(parse_env_file_contents(lines))

    assert env['TEST'] == os.environ['HOME'] + '/yeee-' + os.environ.get('PATH', '')
    assert env['THISIS'] == os.environ['HOME'] + '/a/test'
    assert env['YOLO'] == os.environ['HOME'] + '/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'



# Generated at 2022-06-14 05:49:52.663625
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import doctest
    doctest.testmod(extraglobs={'HOME': 'This is the nastiest hack for doctests'})



# Generated at 2022-06-14 05:50:00.676988
# Unit test for function load_env_file
def test_load_env_file():
    examples_dir = os.path.join(os.path.dirname(__file__), 'examples')
    env_file = os.path.join(examples_dir, 'env_file.txt')

    expected_content = collections.OrderedDict()
    expected_content['VAR1'] = 'value1'
    expected_content['VAR2'] = 'value2'
    expected_content['VAR3'] = '${VAR1}'
    expected_content['VAR4'] = 'value4'

    with open(env_file, 'rt') as fh:
        assert load_env_file(fh) == expected_content



# Generated at 2022-06-14 05:50:12.407480
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert load_env_file(lines, write_environ=dict()) == collections.OrderedDict([
        ('TEST', '.../yeee'),
        ('THISIS', '.../a/test'),
        ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    ])


if __name__ == '__main__':
    test_parse_env_file_contents()

# Generated at 2022-06-14 05:50:24.443055
# Unit test for function load_env_file
def test_load_env_file():
    import io
    import unittest.mock

    lines = io.StringIO()
    lines.write('TEST=${HOME}/yeee-PATH\n')
    lines.write('THISIS=~/a/test\n')
    lines.write('YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST\n')

    with unittest.mock.patch('os.path.expanduser', lambda x: x.replace('~', '...')):
        with unittest.mock.patch('os.path.expandvars', lambda x: x.replace('$', '*')):
            with unittest.mock.patch.dict('os.environ', {'HOME': '...', 'PATH': ':'}):
                assert load

# Generated at 2022-06-14 05:50:36.450624
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['# DO NOT DISCLOSE', '# this is a comment', '',
             'TEST=${HOME}/yeee', 'THISIS=~/a/test',
             'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    items = list(parse_env_file_contents(lines))

    assert items == [('TEST', '.../yeee'),
                     ('THISIS', '.../a/test'),
                     ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]



# Generated at 2022-06-14 05:50:43.075285
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert expand("$HOME") == os.environ.get("HOME")

    lines = ['TEST=$HOME/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    values = parse_env_file_contents(lines)

    for k, v in values:
        v = expand(v)
        assert v.startswith(os.environ.get("HOME"))

    assert expand("$HOME/a") == os.environ.get("HOME") + "/a"



# Generated at 2022-06-14 05:50:48.153128
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    from pprint import pprint
    pprint(dict(parse_env_file_contents(lines)))



# Generated at 2022-06-14 05:50:54.769858
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = [
        "export VAR1='VALUE1'",
        "export VAR2='VALUE2'",
        "export VAR3='VALUE3'"
    ]

    output = parse_env_file_contents(lines)
    expected_output = [("VAR1", "'VALUE1'"), ("VAR2", "'VALUE2'"), ("VAR3", "'VALUE3'")]
    assert list(output) == expected_output



# Generated at 2022-06-14 05:50:56.197038
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import doctest
    doctest.testmod()



# Generated at 2022-06-14 05:51:04.992393
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert len([x for x in parse_env_file_contents(lines)]) == 3

    contents = [('TEST', '${HOME}/yeee'),
                ('THISIS', '~/a/test'),
                ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]
    assert list(parse_env_file_contents(lines)) == contents



# Generated at 2022-06-14 05:51:11.401069
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    """
    Test `parse_env_file_contents`
    """
    lines = [
        'TEST=$HOME/yeee',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST',
    ]
    for k, v in parse_env_file_contents(lines):
        assert k in ['TEST', 'THISIS', 'YOLO']
        assert v not in ['$HOME/yeee', '~/a/test', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']



# Generated at 2022-06-14 05:51:23.096675
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = [
        'TEST=${HOME}/yeee',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    ]
    env_file = parse_env_file_contents(lines)
    print(env_file)  # OrderedDict([('TEST', '.../yeee'), ('THISIS', '.../a/test'), ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])
    assert isinstance(env_file, collections.OrderedDict)  # True
    assert len(env_file) == 3
    assert env_file == load_env_file(lines)




# Generated at 2022-06-14 05:51:29.791099
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():  # noqa: D103
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    changes = []
    for k, v in parse_env_file_contents(lines):
        changes.append((k, expand(v)))

    assert changes == [('TEST', os.path.expanduser('~/yeee')),
                       ('THISIS', os.path.expanduser('~/a/test')),
                       ('YOLO', os.path.expanduser('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'))]



# Generated at 2022-06-14 05:51:36.635879
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    output = {'TEST': '${HOME}/yeee', 'THISIS': '~/a/test', 'YOLO': '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'}
    assert collections.OrderedDict(parse_env_file_contents(lines)) == output

# Generated at 2022-06-14 05:51:47.813916
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    assert dict(load_env_file(lines, write_environ=dict())) == dict([('TEST', '.../yeee'),
                                                                     ('THISIS', '.../a/test'),
                                                                     ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])



# Generated at 2022-06-14 05:52:00.888940
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    result = load_env_file(lines, write_environ=dict())

    # Just make sure it's an ordered dict
    assert isinstance(result, collections.OrderedDict)

    # Check the first line
    home_dir = os.path.expanduser("~")
    assert result['TEST'] == '{}/yeee'.format(home_dir)

    # Check the second line
    assert result['THISIS'] == '{}/a/test'.format(home_dir)

    # And the third

# Generated at 2022-06-14 05:52:10.177910
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # correct input
    lines = [
        'TEST=${HOME}/yeee',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST',
        'TEST2=\'$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST\''
    ]

    data = parse_env_file_contents(lines)
    for i in range(len(lines)):
        key, val = data.__next__()
        assert key == list(expand_dict(lines[i]).keys())[0]
        assert val == list(expand_dict(lines[i]).values())[0]



# Generated at 2022-06-14 05:52:21.099177
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ["TEST=${HOME}/yeee", "THISIS=~/a/test", "YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"]
    same = [("TEST", "${HOME}/yeee"), ("THISIS", "~/a/test"), ("YOLO", "~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST")]
    assert list(parse_env_file_contents(lines)) == same

    lines = ["TEST='${HOME}/yeee'", "THISIS=\"~/a/test\"", "YOLO='~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'"]

# Generated at 2022-06-14 05:52:30.383615
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    expected = [('TEST', '.../yeee'), ('THISIS', '.../a/test'), ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]

    assert list(parse_env_file_contents(lines)) == expected



# Generated at 2022-06-14 05:52:38.160499
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import io
    import unittest

    import mock

    class TestParseEnvFileContents(unittest.TestCase):
        """Test parse_env_file_contents."""

        @mock.patch("sys.stdout", new_callable=io.StringIO)
        def test_no_env_file(self, stdout: io.StringIO) -> None:
            """Test parse_env_file_contents with an empty file."""
            self.assertEqual(list(parse_env_file_contents("")), [])


# Generated at 2022-06-14 05:52:51.640637
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # pylint: disable=unexpected-keyword-arg
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    changes = load_env_file(lines, write_environ=dict())

    assert 'TEST' in changes
    assert 'THISIS' in changes
    assert 'YOLO' in changes

    assert changes['TEST'] != '${HOME}/yeee'
    assert changes['TEST'] != '~/yeee'
    assert changes['TEST'].endswith('/yeee')

    assert changes['THISIS'] != '~/a/test'

# Generated at 2022-06-14 05:53:04.143120
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import itertools

    lines = ["TEST= ${HOME}/yeee-$PATH ",
             "'THISIS= ~ /a/test",
             '"YOLO= ~ /swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"  # Comment']

    expected = [('TEST', '${HOME}/yeee-$PATH'),
                ('THISIS', '~/a/test'),
                ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]

    actual = list(parse_env_file_contents(lines))

    assert list(zip(expected, actual)) == list(zip(expected, actual))

# Generated at 2022-06-14 05:53:13.768596
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    d = load_env_file(lines)
    assert len(d) == 3

    assert d['TEST'][-1] == 'e'  # Make sure $HOME has been expanded
    assert d['THISIS'][-1] == 't'  # Make sure ~ has been expanded
    assert d['YOLO'][:4] == '~/s'  # Make sure $NONEXISTENT_VAR_THAT_DOES_NOT_EXIST has not been expanded



# Generated at 2022-06-14 05:53:24.280078
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import pytest


# Generated at 2022-06-14 05:53:34.807444
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    try:
        from StringIO import StringIO as BytesIO
    except ImportError:
        from io import BytesIO
    with BytesIO(
            'TEST=${HOME}/yeee\nTHISIS=~/a/test\nYOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    ) as f:
        lines = f.readlines()
    assert list(parse_env_file_contents(lines)) == [
        ('TEST', '${HOME}/yeee'), ('THISIS', '~/a/test'),
        ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    ]



# Generated at 2022-06-14 05:53:40.730424
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = [
        'TEST=${HOME}/yeee',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    ]
    actual = parse_env_file_contents(lines)
    expected = [('TEST', '${HOME}/yeee'), ('THISIS', '~/a/test'), ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]
    assert list(actual) == expected


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 05:53:52.027879
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    actual = load_env_file(lines, write_environ=dict())

    assert actual == {'TEST': os.path.expanduser('~') + '/yeee',
                      'THISIS': os.path.expanduser('~') + '/a/test',
                      'YOLO': os.path.expanduser('~') + '/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'}
    assert '$' in actual['YOLO']

# Generated at 2022-06-14 05:54:03.789187
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():  # pragma: no cover
    # Test strings
    s1 = 'TEST=${HOME}/yeee'
    s2 = 'THISIS=~/a/test'
    s3 = 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'

    # Test lines
    lines = [s1, s2, s3]

    # Get output
    output = parse_env_file_contents(lines)

    # Test output
    test_dict = collections.OrderedDict()
    test_dict.setdefault('TEST', '.../yeee')
    test_dict.setdefault('THISIS', '.../a/test')

# Generated at 2022-06-14 05:54:10.909082
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    expected = {'TEST': '.../.../yeee-...:...', 'THISIS': '.../a/test',
                'YOLO': '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'}
    actual = collections.OrderedDict(parse_env_file_contents(lines))
    assert actual == expected



# Generated at 2022-06-14 05:54:16.690379
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    env = load_env_file(['TEST=${HOME}/yeee'], write_environ=None)
    assert os.path.normpath(env['TEST']) == os.path.normpath('%s/yeee' % os.environ['HOME'])


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 05:54:29.575177
# Unit test for function parse_env_file_contents

# Generated at 2022-06-14 05:54:39.759056
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import io
    import unittest.mock as mock

    with mock.patch('os.path.expandvars', lambda x: x):
        with mock.patch('os.path.expanduser', lambda x: x):
            with mock.patch('os.environ', {'HOME': '~', 'PATH': ':', 'FOO': 'FOO'}):
                lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
                f = io.StringIO('\n'.join(lines))
                result = parse_env_file_contents(f)

# Generated at 2022-06-14 05:54:48.577009
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert list(parse_env_file_contents(lines)) == [('TEST', '${HOME}/yeee'), ('THISIS', '~/a/test'), ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]



# Generated at 2022-06-14 05:54:59.086602
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    env_output = """TEST=${HOME}/yeee
        THISIS=~/a/test
        YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"""
    env_file_content = parse_env_file_contents(env_output.split("\n"))
    assert next(env_file_content) == ("TEST", "${HOME}/yeee")
    assert next(env_file_content) == ("THISIS", "~/a/test")
    assert next(env_file_content) == ("YOLO", "~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST")
    assert list(env_file_content) == []


# Unit test function load_env_file


# Generated at 2022-06-14 05:55:13.665163
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert list(parse_env_file_contents([])) == []
    assert list(parse_env_file_contents(["TEST=${HOME}/yeee", "THISIS=~/a/test", "YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"])) == \
        [("TEST", "${HOME}/yeee"),
         ("THISIS", "~/a/test"),
         ("YOLO", "~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST")]



# Generated at 2022-06-14 05:55:20.216825
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # Setup test
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    expected = [('TEST', '.../yeee'),
                ('THISIS', '.../a/test'),
                ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]

    # Execute and assert
    result = list(parse_env_file_contents(lines))
    assert result == expected


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 05:55:31.307553
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    test_str = "\n".join([
        'TEST=${HOME}/yeee-$PATH',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST',
    ])

    lines = test_str.splitlines()

    parsed = parse_env_file_contents(lines)

    assert list(parsed) == [
        ('TEST', '${HOME}/yeee-$PATH'),
        ('THISIS', '~/a/test'),
        ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'),
    ]



# Generated at 2022-06-14 05:55:38.331058
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())


if __name__ == '__main__':
    test_parse_env_file_contents()

# Generated at 2022-06-14 05:55:45.760256
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    contents = 'TEST=${HOME}/yeee-$PATH\nTHISIS=~/a/test\nYOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    for k, v in parse_env_file_contents(contents.split('\n')):
        assert k in contents
        assert v in contents.replace('$', '')



# Generated at 2022-06-14 05:55:52.593593
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert parse_env_file_contents() is not None

    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    contents = parse_env_file_contents(lines)
    assert len(list(contents)) == len(lines)



# Generated at 2022-06-14 05:56:02.700140
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    values = parse_env_file_contents(lines)

    assert next(values) == ('TEST', '.../yeee')
    assert next(values) == ('THISIS', '.../a/test')
    assert next(values) == ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')



# Generated at 2022-06-14 05:56:06.477969
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    print(dict(parse_env_file_contents(lines)))

# Generated at 2022-06-14 05:56:17.818453
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert parse_env_file_contents(lines) == [
        ('TEST', '${HOME}/yeee'),
        ('THISIS', '~/a/test'),
        ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'),
    ]

    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', {'YOLO': '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'}]
   

# Generated at 2022-06-14 05:56:28.356146
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    from io import StringIO
    from unittest import TestCase

    input_lines = ['TEST=$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    f = StringIO(''.join('{}\n'.format(s) for s in input_lines))
    output_lines = parse_env_file_contents(lines=f)

    # print(output_lines)

    # def test_load_env_file():
    #     expected_output = collections.OrderedDict(
    #         [
    #             ('TEST', '.../yeee'),
    #             ('THISIS', '.../a/test'),
    #             ('YOLO',
    #              '.../swagg

# Generated at 2022-06-14 05:56:49.557502
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import textwrap
    contents = textwrap.dedent("""\
        TEST=${HOME}/yeee-$PATH
        PARENT_DIR=$(dirname "${CURRENT_DIR}")
        THISIS=~/a/test
        YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST
    """)

    lines = contents.split('\n')
    lines = [l for l in lines if l.strip() != '']
    out = parse_env_file_contents(lines)

    out_d = load_env_file(lines)
    out_d = {k: v for k, v in out_d.items()}
    assert out_d['TEST'] == expand('${HOME}/yeee-$PATH')
    assert out_d

# Generated at 2022-06-14 05:56:58.515263
# Unit test for function parse_env_file_contents

# Generated at 2022-06-14 05:57:09.916268
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    d1 = collections.OrderedDict(parse_env_file_contents(lines))
    d2 = collections.OrderedDict([('TEST', expand('${HOME}/yeee')),
                                  ('THISIS', expand('~/a/test')),
                                  ('YOLO', expand('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'))])
    assert d1 == d2



# Generated at 2022-06-14 05:57:19.698133
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    assert load_env_file(lines) == collections.OrderedDict([('TEST', '.../yeee'),
                                                             ('THISIS', '.../a/test'),
                                                             ('YOLO',
                                                              '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])

# Generated at 2022-06-14 05:57:24.982139
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    parsed = parse_env_file_contents(lines)

    assert parsed == [
        ("TEST", "..."),
        ("THISIS", "..."),
        ("YOLO", "...")
    ]



# Generated at 2022-06-14 05:57:34.808638
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    values = parse_env_file_contents(lines)

    assert list(values) == [('TEST', '${HOME}/yeee'), ('THISIS', '~/a/test'), ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]



# Generated at 2022-06-14 05:57:43.114607
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # Valid lines
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/${NONEXISTENT_VAR_THAT_DOES_NOT_EXIST}']
    env = parse_env_file_contents(lines)
    print(list(env))

    # Lines without assignment
    lines = ['TEST_WITHOUT_ASSIGNMENT', '', 'THISIS=~/a/test']
    env = parse_env_file_contents(lines)
    print(list(env))



# Generated at 2022-06-14 05:57:55.224774
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    test_contents = 'TEST=${HOME}/yeee-$PATH\nTHISIS=~/a/test\nYOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    result = parse_env_file_contents(test_contents.splitlines())
    assert result == [
        ('TEST', '.../.../yeee-...:...'),
        ('THISIS', '.../a/test'),
        ('YOLO',
         '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    ]


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 05:58:03.487899
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    parsed_lines = parse_env_file_contents(lines)

    assert parsed_lines == [('TEST', '${HOME}/yeee'), ('THISIS', '~/a/test'), ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]



# Generated at 2022-06-14 05:58:16.129735
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import unittest

    class TestCase(unittest.TestCase):
        def test_test(self):
            lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
            actual = load_env_file(lines, write_environ=dict())

            self.assertTrue("TEST" in actual)
            self.assertTrue("THISIS" in actual)
            self.assertTrue("YOLO" in actual)

            self.assertTrue("HOME" in actual["TEST"])
            self.assertTrue("a" in actual["THISIS"])
            self.assertTrue("swaggins" in actual["YOLO"])

    unittest.main

# Generated at 2022-06-14 05:58:44.898059
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert parse_env_file_contents(lines) == [
        ('TEST', '.../yeee'),
        ('THISIS', '.../a/test'),
        ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    ]



# Generated at 2022-06-14 05:58:54.637963
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert parse_env_file_contents(lines) == [
        ('TEST', '${HOME}/yeee'),
        ('THISIS', '~/a/test'),
        ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'),
    ]



# Generated at 2022-06-14 05:59:00.796943
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    lines = parse_env_file_contents(lines)
    assert len(lines) == 3



# Generated at 2022-06-14 05:59:09.268473
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=$HOME/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    assert list(parse_env_file_contents(lines)) == [('TEST', '$HOME/yeee-$PATH'), ('THISIS', '~/a/test'), ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]

    os.environ['HOME'] = '/test'
