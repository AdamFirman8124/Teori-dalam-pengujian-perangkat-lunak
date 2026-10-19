

# Generated at 2022-06-14 05:49:11.012603
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    expected = [('TEST', '${HOME}/yeee'),
                ('THISIS', '~/a/test'),
                ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert list(parse_env_file_contents(lines)) == expected



# Generated at 2022-06-14 05:49:21.363385
# Unit test for function load_env_file
def test_load_env_file():
    this_directory = os.path.dirname(__file__)
    env_path = os.path.join(this_directory, 'test_env_file')

    with open(env_path, 'rt') as f:
        changes = load_env_file(f, dict())

    assert changes == collections.OrderedDict(
        (('TEST', '/tmp/yeee-$PATH'),
         ('THISIS', '~/a/test'),
         ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'))
    )


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 05:49:29.046865
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    kvs = list(parse_env_file_contents(lines))
    assert len(kvs) == 3
    assert kvs[0] == ('TEST', f'{os.path.expanduser("~")}/yeee')
    assert kvs[1] == ('THISIS', f'{os.path.expanduser("~")}/a/test')
    assert kvs[2] == ('YOLO', f'{os.path.expanduser("~")}/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')

# Generated at 2022-06-14 05:49:39.078695
# Unit test for function load_env_file
def test_load_env_file():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    environ = {}
    load_env_file(lines, write_environ=environ)
    expected = {'TEST': os.path.expanduser('~/yeee-' + os.environ['PATH']), 'THISIS': os.path.expanduser('~/a/test'), 'YOLO': os.path.expanduser('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')}
    assert environ == expected


# Generated at 2022-06-14 05:49:51.036537
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    os.environ['TEST'] = 'this is an example of a test'

    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    # Test without tests
    results = list(parse_env_file_contents(lines))

    assert results == [
        ('TEST', '.../yeee-...:...'),
        ('THISIS', '.../a/test'),
        ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    ]

    # Test with tests
    results = list(parse_env_file_contents(lines, tests=True))

# Generated at 2022-06-14 05:49:58.617463
# Unit test for function load_env_file
def test_load_env_file():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    environ = dict()
    result = load_env_file(
        lines,
        write_environ=environ
    )
    print(result)


if __name__ == '__main__':
    test_load_env_file()
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 05:50:08.793674
# Unit test for function load_env_file
def test_load_env_file():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    write_environ = dict()
    load_env_file(lines, write_environ)
    assert write_environ['TEST'] == '.../.../yeee-...:...'
    assert write_environ['THISIS'] == '.../a/test'
    assert write_environ['YOLO'] == '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'



# Generated at 2022-06-14 05:50:18.376369
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    """
    from honcho.tests.test_manager import test_parse_env_file_contents
    import sys
    if sys.version_info.major == 3:
        from honcho.tests.test_manager import __file__ as honcho_tests
    elif sys.version_info.major == 2:
        from honcho.tests.test_manager import test_parse_env_file_contents as honcho_tests
    import logging
    logging.error(honcho_tests)
    import doctest
    doctest.testmod(honcho_tests)
    """
    pass

# Generated at 2022-06-14 05:50:27.959053
# Unit test for function load_env_file
def test_load_env_file():
    # test empty file
    assert dict(load_env_file('')) == dict()

    # test empty line
    assert dict(load_env_file('')) == dict()

    # test env file without spaces
    assert dict(load_env_file('TEST=YOLO')) == dict(TEST='YOLO')

    # test env file with spaces
    assert dict(load_env_file('  TEST  =  YEE  ')) == dict(TEST='YEE')

    # check if var is loaded
    os.environ['TEST'] = 'YOLO'
    assert dict(load_env_file('TEST=YOLO')) == dict(TEST='YOLO')

    # test env file with equals
    assert dict(load_env_file('TEST=YEE=')) == dict

# Generated at 2022-06-14 05:50:40.630353
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import os
    import tempfile

    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.write(b'''
TEST=${HOME}/yeee-$PATH
THISIS=~/a/test
YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST
    ''')
    temp.close()
    fp = open(temp.name)


# Generated at 2022-06-14 05:50:52.589655
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    out = load_env_file(lines, write_environ=dict())
    expected = {'TEST': os.path.expandvars(os.path.expanduser('${HOME}/yeee')),
                'THISIS': os.path.expandvars(os.path.expanduser('~/a/test')),
                'YOLO': os.path.expandvars(os.path.expanduser('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'))}

# Generated at 2022-06-14 05:50:54.918432
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert list(parse_env_file_contents(lines)) == [('TEST', '${HOME}/yeee'), ('THISIS', '~/a/test'), ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]



# Generated at 2022-06-14 05:51:05.267231
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert list(parse_env_file_contents(lines)) == [('TEST', expand('${HOME}/yeee')),
                                                    ('THISIS', expand('~/a/test')),
                                                    ('YOLO', expand('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'))]

    # Ensure that parsing is not affected by line endings

# Generated at 2022-06-14 05:51:11.554503
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert list(parse_env_file_contents(lines)) == [('TEST', os.path.expandvars('${HOME}/yeee')),
                                                    ('THISIS', os.path.expandvars('~/a/test')),
                                                    ('YOLO', os.path.expandvars('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'))]



# Generated at 2022-06-14 05:51:16.893237
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert load_env_file(lines, write_environ=dict()) == load_env_file(lines, write_environ=dict())



# Generated at 2022-06-14 05:51:27.282153
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = [
        'ABC=a-b-c',
        'DEF=${ABC}-d-e',
        'GHI=${DEF}-f-g',
        "JKL='${GHI}'-h-i",
        "MNO=\"${JKL}-j-k\"",
        "PQR=$HOME/foo",
        "STU=~/bar",
        "UVW=${STU}/baz",
        "XYZ=${STU}/${HOME}",
    ]

    lines = [
        'TEST=${HOME}/yeee-$PATH',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST',
    ]


# Generated at 2022-06-14 05:51:37.221909
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    try:
        import hypothesis.strategies as st
        import hypothesis.extra.numpy as npst
    except ImportError:
        return

    import numpy as np

    from .test_collections import CollectionStrategy

    from .test_numpy import Uint8Strategy

    def np_to_bytes(a):
        return a.tobytes()


# Generated at 2022-06-14 05:51:42.646096
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    from confu.tests_utils import Data

    data = Data(
        "foo=a$b\nbar=b",
        {
            "foo": "a$b",
            "bar": "b"
        }
    )

    next(data)



# Generated at 2022-06-14 05:51:50.708986
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    result = load_env_file(lines, write_environ=dict())

    expected = collections.OrderedDict([
        ('TEST', expand('${HOME}/yeee')),
        ('THISIS', expand('~/a/test')),
        ('YOLO', expand('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'))
    ])

    assert result == expected, "test_parse_env_file_contents: incorrect result"

# Generated at 2022-06-14 05:52:03.206623
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # pylint: disable=import-outside-toplevel

    import os

    # test that this does not fail
    parse_env_file_contents()

    os.environ['YOLID'] = 'swag'

    changes = load_env_file(['TEST=${HOME}/yeee-$YOLID', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'], dict())


# Generated at 2022-06-14 05:52:17.377708
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    result = load_env_file(lines, write_environ=dict())

    assert result == collections.OrderedDict([('TEST', '.../.../yeee'),
                                              ('THISIS', '.../a/test'),
                                              ('YOLO',
                                               '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])


# Generated at 2022-06-14 05:52:25.802043
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    contents = '''
    TEST=${HOME}/yeee-$PATH
    THISIS=~/a/test
    YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST
    '''.splitlines()

    out = load_env_file(contents)

    # Ensure that the output is of the correct type
    assert isinstance(out, collections.OrderedDict)

    # Ensure that the output has the correct keys
    assert list(out.keys()) == ['TEST', 'THISIS', 'YOLO']

    # Ensure that the output has the correct values
    assert out['TEST'] == os.path.expandvars('${HOME}/yeee-$PATH')

# Generated at 2022-06-14 05:52:30.935806
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())



# Generated at 2022-06-14 05:52:37.054398
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    args = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    expected = [('TEST', '.../yeee'), ('THISIS', '.../a/test'), ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]
    result = list(parse_env_file_contents(args))
    assert expected == result



# Generated at 2022-06-14 05:52:48.554626
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = [
        'TEST=${HOME}/yeee',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST',
    ]

    r = load_env_file(lines, write_environ=None)
    r['TEST'] = r['TEST'].split(os.path.sep)[-1]
    r['THISIS'] = r['THISIS'].split(os.path.sep)[-1]
    r['YOLO'] = r['YOLO'].split(os.path.sep)[-1]


# Generated at 2022-06-14 05:52:59.171139
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    read = list(parse_env_file_contents(lines))

    expected = [
        ('TEST', '${HOME}/yeee'),
        ('THISIS', '~/a/test'),
        ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'),
    ]

    assert read == expected



# Generated at 2022-06-14 05:53:04.694956
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    assert collections.OrderedDict(parse_env_file_contents(lines)) == load_env_file(lines)

# Generated at 2022-06-14 05:53:14.660542
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # Check one env file line
    line = 'TEST=${HOME}/yeee'
    assert set(parse_env_file_contents((line,))) == set([('TEST', '.../yeee')])

    # Check multiple env file lines
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert set(parse_env_file_contents(lines)) == set([
        ('TEST', '.../yeee'), ('THISIS', '.../a/test'), ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])

# Generated at 2022-06-14 05:53:24.698858
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():

    # Explicit case
    assert list(parse_env_file_contents(["FOO=bar"])) == [("FOO", "bar")]
    assert list(parse_env_file_contents(["FOO=bar "])) == [("FOO", "bar")]
    assert list(parse_env_file_contents([" FOO=bar"])) == [("FOO", "bar")]
    assert list(parse_env_file_contents([" FOO=bar "])) == [("FOO", "bar")]

    # Single quotes
    assert list(parse_env_file_contents(["FOO='bar'"])) == [("FOO", "bar")]
    assert list(parse_env_file_contents(["FOO='bar '"])) == [("FOO", "bar")]

# Generated at 2022-06-14 05:53:36.029815
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert collections.OrderedDict(parse_env_file_contents(lines)) == collections.OrderedDict([('TEST', '.../yeee'),
                                                                                              ('THISIS', '.../a/test'),
                                                                                              ('YOLO',
                                                                                               '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])

# Generated at 2022-06-14 05:53:49.564513
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import io

    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    result = list(parse_env_file_contents(iter(lines)))

    assert '${HOME}' not in result[0][1]
    assert '${PATH}' not in result[0][1]

    assert '~' not in result[1][1]

    assert '${HOME}' not in result[2][1]
    assert '${NONEXISTENT_VAR_THAT_DOES_NOT_EXIST}' in result[2][1]

    # Test with an empty file

# Generated at 2022-06-14 05:54:01.384557
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert list(parse_env_file_contents(lines)) == [('TEST', os.path.expanduser(os.path.expandvars('${HOME}/yeee'))), ('THISIS', os.path.expanduser(os.path.expandvars('~/a/test'))), ('YOLO', os.path.expanduser(os.path.expandvars('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')))]



# Generated at 2022-06-14 05:54:11.842244
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    assert tuple(parse_env_file_contents(lines)) == (
        ('TEST', expand('${HOME}/yeee')),
        ('THISIS', expand('~/a/test')),
        ('YOLO', expand('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'))
    )



# Generated at 2022-06-14 05:54:13.469604
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import doctest
    doctest.testmod(verbose=True)


# Generated at 2022-06-14 05:54:22.933784
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    result = load_env_file(lines, write_environ=dict())

    assert result == {'TEST': expand('${HOME}/yeee'), 'THISIS': expand('~/a/test'), 'YOLO': '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'}

# Generated at 2022-06-14 05:54:32.201200
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    """
    >>> list(parse_env_file_contents(['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']))
    [('TEST', '.../yeee'), ('THISIS', '.../a/test'), ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]
    """



# Generated at 2022-06-14 05:54:42.083559
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import io

    env_file = io.StringIO()
    env_file.write("""
    TEST=${HOME}/yeee-$PATH
    THISIS=~/a/test
    YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST
    """)
    env_file.seek(0)

    values = parse_env_file_contents(env_file)
    res = load_env_file(env_file)

    # res = dict(values)
    import pprint

    pprint.pprint(res)

# Generated at 2022-06-14 05:54:48.864625
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())


if __name__ == '__main__':
    test_parse_env_file_contents()

# Generated at 2022-06-14 05:54:58.087003
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    values = list(parse_env_file_contents(lines))

    assert len(values) == 3
    assert values[0] == ('TEST', '{HOME}/yeee')
    assert values[1] == ('THISIS', '~/a/test')
    assert values[2] == ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')



# Generated at 2022-06-14 05:55:08.015108
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert list(parse_env_file_contents(lines)) == [('TEST', '${HOME}/yeee'), ('THISIS', '~/a/test'), ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]
    cwd = os.getcwd()
    assert list(parse_env_file_contents(['TEST=%s' % cwd])) == [('TEST', cwd)]



# Generated at 2022-06-14 05:55:22.819524
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH',
             'THISIS=~/a/test',
             'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    r = parse_env_file_contents(lines)

    t1 = ('TEST', '.../.../yeee-...:...')
    t2 = ('THISIS', '.../a/test')
    t3 = ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')

    assert next(r) == t1
    assert next(r) == t2
    assert next(r) == t3
    assert next(r, None) is None



# Generated at 2022-06-14 05:55:32.472596
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():

    # TEST=${HOME}/yeee-$PATH
    # THISIS=~/a/test
    # YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST

    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']


# Generated at 2022-06-14 05:55:35.597116
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():

    import doctest

    doctest.testmod()


if __name__ == '__main__':
    test_parse_env_file_contents()
    exit(0)

# Generated at 2022-06-14 05:55:48.501661
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    print('Testing function parse_env_file_contents')

    import io
    import contextlib

    @contextlib.contextmanager
    def _mock_lines(lines):
        yield io.StringIO(''.join(lines))

    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    with _mock_lines(lines) as f:
        environ = load_env_file(f.readlines(), write_environ={})


# Generated at 2022-06-14 05:56:01.133185
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # Uncomment for manual test
    #import sys
    #files = load_env_files(sys.argv[1:])
    #print(files)

    # Test
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    m = load_env_file(lines, write_environ=dict())

    # Test
    if not isinstance(m, collections.OrderedDict):
        raise Exception('Not a dictionary')
    if m.get('TEST') is None:
        raise Exception('Test is None')
    if m.get('THISIS') is None:
        raise Exception('Test is None')

# Generated at 2022-06-14 05:56:06.782732
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert list(parse_env_file_contents(['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins'])) == \
        [('TEST', '.../yeee'), ('THISIS', '.../a/test'), ('YOLO', '.../swaggins')]



# Generated at 2022-06-14 05:56:18.118707
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    env_str = (
        'TEST=${HOME}/yeee\n',
        'THISIS=~/a/test\n',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST\n',
    )
    env = [line for line in parse_env_file_contents(env_str)]
    assert env[0][0] == 'TEST'
    assert env[0][1].endswith('/yeee')
    assert env[1][0] == 'THISIS'
    assert env[1][1].endswith('/a/test')
    assert env[2][0] == 'YOLO'

# Generated at 2022-06-14 05:56:28.634677
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    test_input = r'TEST=${HOME}/yeee-$PATH\n\
THISIS=~/a/test\n\
YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST\n'
    test_output = parse_env_file_contents([line.strip() for line in test_input.split("\n")])

# Generated at 2022-06-14 05:56:41.067605
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    expected = collections.OrderedDict([
        ('TEST', os.path.expanduser('~/yeee-%s' % os.environ['PATH'])),
        ('THISIS', os.path.expanduser('~/a/test')),
        ('YOLO', os.path.expanduser('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'))
    ])

    actual = parse_env_file_contents(lines)
    actual = collections.OrderedDict(actual)


# Generated at 2022-06-14 05:56:53.992552
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert list(parse_env_file_contents([])) == []
    assert list(parse_env_file_contents(['TEST=value'])) == [('TEST', 'value')]
    assert list(parse_env_file_contents([
        'TEST=value',
        'TEST2=test=value',
        'TEST3=test2="test=value"'
    ])) == [
        ('TEST', 'value'),
        ('TEST2', 'test=value'),
        ('TEST3', 'test2="test=value"'),
    ]

# Generated at 2022-06-14 05:57:11.222657
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = """
        A=a
        B=b
        C='c'
        D="d"
        E=e
        F='f' g
        G=g
        H="h" i
        I=i
        J='j' "k"
        K=k
        L="l" 'm'
        M=m
        N='n' "o" 'p'
        O=o
        P="p" 'q' "r"
        Q=q
        R="s"t
        S=s
        T='u'v
        U=u
        V="w"x
        W=w
        X='y'z
        Y=y
        Z="${HOME}"
    """.split('\n')


# Generated at 2022-06-14 05:57:22.740060
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    """
    Tests function `parse_env_file_contents()`
    """
    sample_str = 'TEST=${HOME}/yeee $PATH\nTHISIS=~/a/test\nYOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST\n'
    assert list(parse_env_file_contents(iter(sample_str.split('\n')))) == [
        ('TEST', '${HOME}/yeee $PATH'),
        ('THISIS', '~/a/test'),
        ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    ]


# Unit tests for function load_env_file

# Generated at 2022-06-14 05:57:33.132622
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert load_env_file(lines, write_environ=dict()) == OrderedDict(
        [('TEST', expand('${HOME}/yeee')),
         ('THISIS', expand('~/a/test')),
         ('YOLO',
          expand('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'))])



# Generated at 2022-06-14 05:57:41.572617
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    """
    # Doctest for function parse_env_file_contents
    """
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    # (allow_unicode=True) allows us to use the '...' in the results of the doctest
    doctest.testmod(optionflags=(doctest.IGNORE_EXCEPTION_DETAIL))


# Generated at 2022-06-14 05:57:54.305343
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert dict(parse_env_file_contents(['A=B'])) == {'A': 'B'}
    assert dict(parse_env_file_contents(['A="B"'])) == {'A': 'B'}
    assert dict(parse_env_file_contents(['A="B C"'])) == {'A': 'B C'}
    assert dict(parse_env_file_contents(['A="B\\"C"'])) == {'A': 'B"C'}
    assert dict(parse_env_file_contents(["A='B'"])) == {'A': 'B'}
    assert dict(parse_env_file_contents(["A='B C'"])) == {'A': 'B C'}

# Generated at 2022-06-14 05:58:05.612711
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    data = [
        'TEST=${HOME}/yeee',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST',
    ]

    res = collections.OrderedDict(parse_env_file_contents(data))

    assert res['TEST'] == '${HOME}/yeee'
    assert res['THISIS'] == '~/a/test'
    assert res['YOLO'] == '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'

    res = collections.OrderedDict(parse_env_file_contents(iter(data)))

    assert res['TEST'] == '${HOME}/yeee'

# Generated at 2022-06-14 05:58:11.187572
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())



# Generated at 2022-06-14 05:58:24.073982
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert list(parse_env_file_contents()) == []
    assert list(parse_env_file_contents(["TEST=123"])) == [("TEST", "123")]
    assert list(parse_env_file_contents(["TEST=123", "YOLO=yee"])) == [("TEST", "123"), ("YOLO", "yee")]
    assert list(parse_env_file_contents(["TEST=123", "YOLO=yee", "FOO=BAR"])) == [("TEST", "123"), ("YOLO", "yee"), ("FOO", "BAR")]

# Generated at 2022-06-14 05:58:33.605835
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert dict(parse_env_file_contents(lines)) == {
        'TEST': '.../yeee',
        'THISIS': '.../a/test',
        'YOLO': '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST',
    }



# Generated at 2022-06-14 05:58:43.678420
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    env = dict(parse_env_file_contents(lines))
    assert env['TEST'].endswith('/yeee')
    assert env['THISIS'].endswith('/a/test')
    assert env['YOLO'].endswith('/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')

