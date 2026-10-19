

# Generated at 2022-06-14 05:49:17.174298
# Unit test for function load_env_file
def test_load_env_file():
    import pytest
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    loads = load_env_file(lines, write_environ=dict())

    # Testing the number of values in the returned dictionary
    assert len(loads) == 3

    # Testing a key-value pair in the returned dictionary
    assert loads['TEST'] == os.path.expanduser(os.path.expandvars('${HOME}/yeee'))

    # Testing a key-value pair in the returned dictionary

# Generated at 2022-06-14 05:49:27.538363
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert parse_env_file_contents(lines) == [('TEST', expand('${HOME}/yeee')), ('THISIS', expand('~/a/test')), ('YOLO', expand('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'))]
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert parse_env_file_

# Generated at 2022-06-14 05:49:37.424819
# Unit test for function load_env_file
def test_load_env_file():
    import unittest

    class Test(unittest.TestCase):
        def test_load_env_file(self):
            lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
            load_env_file(lines, write_environ=dict())

    unittest.main(module='pipx.envfile')


if __name__ == '__main__':
    test_load_env_file()

# Generated at 2022-06-14 05:49:45.300634
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    parsed_tuple = list(parse_env_file_contents(lines))
    assert len(parsed_tuple) == 3
    assert parsed_tuple[0] == ('TEST', expand('${HOME}/yeee-$PATH'))
    assert parsed_tuple[1] == ('THISIS', expand('~/a/test'))
    assert parsed_tuple[2] == ('YOLO', expand('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'))



# Generated at 2022-06-14 05:49:56.017044
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert load_env_file(lines, write_environ=dict()) == collections.OrderedDict([
        ('TEST', '{HOME}/yeee'.format(**os.environ)),
        ('THISIS', '{HOME}/a/test'.format(**os.environ)),
        ('YOLO', '{HOME}/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'.format(**os.environ))
    ])

    #
    # nested variables that are not defined
    #

# Generated at 2022-06-14 05:50:03.672375
# Unit test for function load_env_file
def test_load_env_file():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    environ = dict()
    result = load_env_file(lines, write_environ=environ)

    print(result)


if __name__ == '__main__':
    test_load_env_file()

# Generated at 2022-06-14 05:50:09.582503
# Unit test for function load_env_file
def test_load_env_file():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=None)



# Generated at 2022-06-14 05:50:18.522825
# Unit test for function load_env_file
def test_load_env_file():
    """
    Tests the load_env_file function.
    """
    # Valid
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())

    # Invalid
    lines = ['NOTAVALIDVALUE']
    with pytest.raises(ValueError):
        load_env_file(lines, write_environ=dict())



# Generated at 2022-06-14 05:50:23.147300
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())
    assert 0 == 1

# Generated at 2022-06-14 05:50:32.431029
# Unit test for function load_env_file
def test_load_env_file():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    env = load_env_file(lines, write_environ=dict())

    assert env['TEST'].startswith('.../.../yeee-.')
    assert env['THISIS'] == '.../a/test'
    assert env['YOLO'] == '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'



# Generated at 2022-06-14 05:50:38.891937
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    from code_snippets.parsers.docker_env_file_parser import docker_env_file_parser
    from code_snippets.tests import test_helper

    test_helper.run_doctest(docker_env_file_parser.parse_env_file_contents)



# Generated at 2022-06-14 05:50:47.640547
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert dict(parse_env_file_contents([
        'TEST=\'${HOME}/yeee\'',
        'TEST2=${HOME}/yeee',
        'THISIS="~/a/test"',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    ])) == {
        'TEST': '${HOME}/yeee',
        'TEST2': '${HOME}/yeee',
        'THISIS': '~/a/test',
        'YOLO': '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    }



# Generated at 2022-06-14 05:50:57.346944
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    # Setup test variables
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    # Call function
    result = parse_env_file_contents(lines)

    # Test returns the correct variables
    assert list(result) == [('TEST', '.../yeee'),
                            ('THISIS', '.../a/test'),
                            ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]



# Generated at 2022-06-14 05:51:02.866030
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines, write_environ=dict())

# Generated at 2022-06-14 05:51:13.261597
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

    actual = list(parse_env_file_contents(lines))

    assert len(actual) == 3
    assert actual[0] == ('TEST', '${HOME}/yeee')
    assert actual[1] == ('THISIS', '~/a/test')
    assert actual[2] == ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')



# Generated at 2022-06-14 05:51:25.202063
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    values = parse_env_file_contents(lines)
    assert next(values) == ('TEST', expand('${HOME}/yeee'))
    assert next(values) == ('THISIS', expand('~/a/test'))
    assert next(values) == ('YOLO', expand('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'))



# Generated at 2022-06-14 05:51:36.367564
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    ans = parse_env_file_contents(lines)
    ans = collections.OrderedDict(ans)
    assert ans == collections.OrderedDict(
        [('TEST', f'{os.environ["HOME"]}/yeee'), ('THISIS', f'{os.environ["HOME"]}/a/test'), ('YOLO', f'{os.environ["HOME"]}/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])


# Generated at 2022-06-14 05:51:46.255316
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    assert (parse_env_file_contents(lines) ==
            (('TEST', '${HOME}/yeee'), ('THISIS', '~/a/test'), ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')))



# Generated at 2022-06-14 05:51:52.275427
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    import doctest

    doctest.testmod()

    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    load_env_file(lines)



# Generated at 2022-06-14 05:51:58.283071
# Unit test for function parse_env_file_contents
def test_parse_env_file_contents():
    assert parse_env_file_contents(
        lines=['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    ) == [
        ('TEST', '.../yeee'),
        ('THISIS', '.../a/test'),
        ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'),
    ]

