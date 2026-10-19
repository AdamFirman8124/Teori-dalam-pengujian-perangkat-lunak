

# Generated at 2022-06-14 05:49:14.421512
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    res = parse_env_file_contents(lines)
    res = list(res)

    assert len(res) == 3
    assert res[0][0] == 'TEST'
    assert res[0][1] == '${HOME}/yeee'
    assert res[1][0] == 'THISIS'
    assert res[1][1] == '~/a/test'
    assert res[2][0] == 'YOLO'

# Generated at 2022-06-14 05:49:26.158233
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert tuple(parse_env_file_contents(["THISIS=~/a/test"])) == (('THISIS', '~/a/test'),)
    assert tuple(parse_env_file_contents(["THISIS='~/a/test'"])) == (('THISIS', '~/a/test'),)
    assert tuple(parse_env_file_contents(['THISIS="~/a/test"'])) == (('THISIS', '~/a/test'),)

    # Test for \n
    assert tuple(parse_env_file_contents(['THISIS="~/a/test\ntest2"'])) == (('THISIS', '~/a/test\ntest2'),)

    # Test for \r\n

# Generated at 2022-06-14 05:49:35.247448
# Unit test for function load_env_file
def test_load_env_file():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    os.environ = {}
    load_env_file(lines, write_environ=os.environ)
    assert os.environ == {'TEST': '.../.../yeee', 'THISIS': '.../a/test', 'YOLO': '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'}



# Generated at 2022-06-14 05:49:43.116237
# Unit test for function load_env_file
def test_load_env_file():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    write_environ = dict()
    expected = OrderedDict([('TEST', '.../yeee'),
                            ('THISIS', '.../a/test'),
                            ('YOLO',
                             '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])
    result = load_env_file(lines, write_environ)
    assert result == expected



# Generated at 2022-06-14 05:49:55.169524
# Unit test for function load_env_file
def test_load_env_file():
    from io import StringIO

    lines = StringIO('TEST=${HOME}/yeee-$PATH\nTHISIS=~/a/test\nYOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    d = load_env_file(lines, write_environ=dict())

    assert d['TEST'] == '{}/yeee-{}'.format(os.environ['HOME'], os.environ['PATH'])
    assert d['THISIS'] == '{}/a/test'.format(os.environ['HOME'])
    assert d['YOLO'] == '{}/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'.format(os.environ['HOME'])

# Generated at 2022-06-14 05:50:07.271369
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    values = parse_env_file_contents(lines)

    changes = collections.OrderedDict()

    for k, v in values:
        assert k in changes or k not in os.environ, 'Key {} is already in env, skip adding this key to env.'.format(k)
        changes[k] = v


# Generated at 2022-06-14 05:50:14.698031
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert load_env_file(lines, write_environ=None) == collections.OrderedDict({
        'TEST': os.path.expanduser('~/yeee'),
        'THISIS': os.path.expanduser('~/a/test'),
        'YOLO': os.path.expanduser('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'),
    })



# Generated at 2022-06-14 05:50:22.873200
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    kv = list(parse_env_file_contents(lines))
    assert kv == [
        ('TEST', '${HOME}/yeee'),
        ('THISIS', '~/a/test'),
        ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    ]



# Generated at 2022-06-14 05:50:31.172463
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    test_strings = [
        "HONEST=TRUE",
        "RESTART_TRIES=2  # comment",
        "'THIS'='\"THAT\"'",
        "THIS=\"'THAT'\"",
        "$PATH",
        "~/directory",
        "~$USER",  # this is also a valid env file entry
        "$HOME/directory",
        "a$b",
    ]

    # Now, test the function.
    for line in test_strings:
        yield check_parse_env_file_contents_results, line



# Generated at 2022-06-14 05:50:39.577197
# Unit test for function load_env_file
def test_load_env_file():
    import doctest

    env_file_contents = ['TEST=${HOME}/yeee',
                         'THISIS=~/a/test',
                         'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST',
                         ]

    doctest.run_docstring_examples(load_env_file, globals(), verbose=True, name="load_env_file",
                                   example_globals=dict(lines=env_file_contents))