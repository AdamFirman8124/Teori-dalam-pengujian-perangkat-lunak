

# Generated at 2022-06-14 05:49:20.175945
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    res = load_env_file(lines)

    assert res is not None
    assert 'TEST' in res
    assert res['TEST'] == os.path.join(
        os.getenv('HOME'), 'yeee')
    assert 'THISIS' in res
    assert res['THISIS'] == os.path.join(
        os.getenv('HOME'), 'a', 'test')
    assert 'YOLO' in res

# Generated at 2022-06-14 05:49:27.590874
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import tempfile

    with tempfile.NamedTemporaryFile('w') as f:
        f.write("TEST=$HOME/yeee\nTHISIS=~/a/test\nYOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST")
        f.flush()

        lines = open(f.name).readlines()
        for k, v in parse_env_file_contents(lines):
            print("'{}' : '{}'".format(k, v))



# Generated at 2022-06-14 05:49:33.130648
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = [
        "ONE=1",
        "TWO=2",
        "THREE=3",
    ]
    result = parse_env_file_contents(lines)

    for num in [1, 2, 3]:
        assert next(result) == ("ONE" if num == 1 else "TWO" if num == 2 else "THREE", str(num))



# Generated at 2022-06-14 05:49:39.967250
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():

    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    values = parse_env_file_contents(lines)

    assert next(values) == ('TEST', '.../yeee')
    assert next(values) == ('THISIS', '.../a/test')
    assert next(values) == ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    assert list(values) == []


# Generated at 2022-06-14 05:49:46.185444
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = 'TEST=${HOME}/yeee TEST2=${HOME}/yeee-test'
    assert list(parse_env_file_contents(lines.split())) == [('TEST', '.../yeee'), ('TEST2', '.../yeee-test')]

# Generated at 2022-06-14 05:49:54.087386
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = (
        'key1=value1',
        'key2=value2',
    )
    kv_gen = parse_env_file_contents(lines)
    assert next(kv_gen) == ('key1', 'value1')
    assert next(kv_gen) == ('key2', 'value2')
    try:
        next(kv_gen)
        assert False, 'Expected StopIteration'
    except StopIteration:
        pass



# Generated at 2022-06-14 05:50:06.653257
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    test_case = """TEST=${HOME}/yeee-$PATH
THISIS=~/a/test
YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST
"""
    lines_generator = parse_env_file_contents(test_case.splitlines())

    values = collections.OrderedDict()

    for k, v in lines_generator:
        v = expand(v)

        values[k] = v

    assert values["TEST"] == os.path.expandvars("${HOME}/yeee-$PATH")
    assert values["THISIS"] == os.path.expandvars("~/a/test")

# Generated at 2022-06-14 05:50:10.292563
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 05:50:21.098651
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    output = load_env_file(lines, write_environ=dict())
    expected = collections.OrderedDict()
    expected['TEST'] = os.path.expanduser('~') + '/yeee'
    expected['THISIS'] = os.path.expanduser('~') + '/a/test'
    expected['YOLO'] = os.path.expanduser('~') + '/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'

    assert output == expected

# Generated at 2022-06-14 05:50:29.108743
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    result = parse_env_file_contents(lines)
    res1 = next(result)
    res2 = next(result)
    res3 = next(result)
    assert res1[0] == 'TEST'
    assert res1[1] == '${HOME}/yeee'
    assert res2[0] == 'THISIS'
    assert res2[1] == '~/a/test'
    assert res3[0] == 'YOLO'

# Generated at 2022-06-14 05:50:43.196780
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    """
    >>> lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    >>> parse_env_file_contents(lines)
    <generator object parse_env_file_contents at ...>
    >>> list(parse_env_file_contents(lines))
    [('TEST', '.../.../yeee-...:...'),
     ('THISIS', '.../a/test'),
     ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]
    """
    # Just testing the function, will not execute any code.
    pass


# Unit

# Generated at 2022-06-14 05:50:52.152746
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert list(parse_env_file_contents(["TEST=${HOME}/yeee", "THISIS=~/a/test", "YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"])) == [
        ('TEST', os.path.expanduser(f'~/yeee')),
        ('THISIS', os.path.expanduser(f'~/a/test')),
        ('YOLO', os.path.expanduser(f'~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'))
    ]



# Generated at 2022-06-14 05:51:01.765748
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
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 05:51:13.440153
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    test_values = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    result = parse_env_file_contents(test_values)
    result_list = list(result)
    assert len(result_list) == 3
    assert result_list[0] == ("TEST", "~/yeee")
    assert result_list[1] == ("THISIS", "~/a/test")
    assert result_list[2] == ("YOLO", "~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST")



# Generated at 2022-06-14 05:51:27.127512
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # Test 1
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    result = {}
    load_env_file(lines, result)

    assert result == {'TEST': '{}/yeee'.format(os.environ.get('HOME')),
                      'THISIS': '{}/a/test'.format(os.environ.get('HOME')),
                      'YOLO': '{}/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'.format(os.environ.get('HOME'))}

    # Test 2

# Generated at 2022-06-14 05:51:35.944085
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    TEST_ENV_VARS_LIST = """
    CUSTOM_VAR='hi'
    PATH=/usr/bin:/bin:/usr/sbin:/sbin
    ETC_VAR=etc/var
    """.strip().split()

    os.environ['PATH'] = '/usr/bin:/bin:/usr/sbin:/sbin'

    changes = load_env_file(TEST_ENV_VARS_LIST)

    assert changes['PATH'] == '/usr/bin:/bin:/usr/sbin:/sbin'
    assert changes['CUSTOM_VAR'] == 'hi'
    assert changes['ETC_VAR'] == 'etc/var'



# Generated at 2022-06-14 05:51:47.972782
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # test quoted matching
    lines = ['TEST="hello there"']
    assert list(parse_env_file_contents(lines)) == [('TEST', 'hello there')]

    lines = ["TEST='hello'"]
    assert list(parse_env_file_contents(lines)) == [('TEST', "hello")]

    lines = ['TEST="hello\nthere"']
    assert list(parse_env_file_contents(lines)) == [('TEST', 'hello\nthere')]

    # test line matching
    lines = ['TEST=hello there']
    assert list(parse_env_file_contents(lines)) == [('TEST', 'hello there')]

    lines = ['TEST = hello']

# Generated at 2022-06-14 05:51:56.026106
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=\'~/a/test\'', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    actual = dict(parse_env_file_contents(lines))

    assert os.path.exists(actual['TEST'])
    assert os.path.exists(actual['THISIS'])
    assert not os.path.exists(actual['YOLO'])



# Generated at 2022-06-14 05:52:05.171991
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test']

    results = list(parse_env_file_contents(lines))

    assert results[0][0] == 'TEST'
    assert results[0][1] == os.path.expanduser('${HOME}/yeee')
    assert results[1][0] == 'THISIS'
    assert results[1][1] == os.path.expanduser('~/a/test')

# Generated at 2022-06-14 05:52:12.419719
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import io
    assert dict(parse_env_file_contents(io.StringIO("TEST=${HOME}/yeee"))) == {"TEST": "${HOME}/yeee"}
    assert dict(parse_env_file_contents(io.StringIO("THISIS=~/a/test"))) == {"THISIS": "~/a/test"}
    assert dict(parse_env_file_contents(io.StringIO("YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"))) == {
        "YOLO": "~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"}

