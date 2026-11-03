

# Generated at 2026-11-02 07:04:50.786710
# Unit test for function each_sub_command_config

# Generated at 2026-11-02 07:07:30.427921
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        setup_dir = os.path.realpath(tmp)
        with open(os.path.join(tmp, 'setup.py'), 'w') as fh:
            fh.write('# setup\n')
        with open(os.path.join(tmp, 'setup.cfg'), 'w') as fh:
            fh.write(
                '[metadata]\n'
                'name = my_pkg\n'
                '\n'
                '[setup.command.build]\n'
                'commands =\n'
                '    echo {setup_dir}\n'
                '    echo {home}\n'
                'description = build the thing\n'
                '\n'
                '[setup.command.doc]\n'
                'name = {name} doc\n'
                'command = sphinx-build {setup_dir}/docs docs\n'
            )
        result = list(module_0.each_sub_command_config(tmp))
    home = os.path.expanduser('~')
    assert result == [
        SetupCfgCommandConfig(
            'build',
            'Build',
            'build the thing',
            ('echo %s' % setup_dir, 'echo %s' % home),
        ),
        SetupCfgCommandConfig(
            'my_pkg doc',
            'MyPkgDoc',
            '',
            ('sphinx-build %s/docs docs' % setup_dir,),
        ),
    ]

# Generated at 2026-11-02 07:09:45.709249
# Unit test for constructor of class SetupCfgCommandConfig
def test_SetupCfgCommandConfig():
    obj = SetupCfgCommandConfig(
        name='test',
        camel='Test',
        description='A test command',
        commands=('echo hello',)
    )
    assert obj.name == 'test'
    assert obj.camel == 'Test'
    assert obj.description == 'A test command'
    assert obj.commands == ('echo hello',)

    # Test with empty commands tuple
    obj = SetupCfgCommandConfig(
        name='foo.bar',
        camel='FooBar',
        description='',
        commands=()
    )
    assert obj.name == 'foo.bar'
    assert obj.camel == 'FooBar'
    assert obj.description == ''
    assert obj.commands == ()

    # Test equality
    obj1 = SetupCfgCommandConfig('a', 'A', 'desc a', ('cmd1',))
    obj2 = SetupCfgCommandConfig('a', 'A', 'desc a', ('cmd1',))
    assert obj1 == obj2

    # Test inequality
    obj3 = SetupCfgCommandConfig('b', 'B', 'desc b', ('cmd2',))
    assert obj1 != obj3

    # Test immutability (NamedTuple is immutable)
    try:
        obj1.name = 'changed'
        assert False, "Expected AttributeError"
    except AttributeError:
        pass

    # Test tuple unpacking
    name, camel, description, commands = obj1
    assert name == 'a'
    assert camel == 'A'
    assert description == 'desc a'
    assert commands == ('cmd1',)

    # Test _fields attribute
    assert SetupCfgCommandConfig._fields == (
        'name', 'camel', 'description', 'commands'
    )