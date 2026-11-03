

# Generated at 2026-11-03 02:17:25.855033
# Unit test for constructor of class SetupCfgCommandConfig
def test_SetupCfgCommandConfig():
    obj = SetupCfgCommandConfig(
        name='test',
        camel='Test',
        description='a test command',
        commands=('ls -al',)
    )
    assert obj.name == 'test'
    assert obj.camel == 'Test'
    assert obj.description == 'a test command'
    assert obj.commands == ('ls -al',)


def test_SetupCfgCommandConfig_attributes():
    obj = SetupCfgCommandConfig(
        name='build',
        camel='Build',
        description='',
        commands=('python setup.py build', 'python setup.py bdist_wheel')
    )
    assert obj._fields == ('name', 'camel', 'description', 'commands')
    assert obj[0] == 'build'
    assert obj[1] == 'Build'
    assert obj[2] == ''
    assert obj[3] == ('python setup.py build', 'python setup.py bdist_wheel')


def test_SetupCfgCommandConfig_replace():
    obj = SetupCfgCommandConfig(
        name='test',
        camel='Test',
        description='a test command',
        commands=('ls -al',)
    )
    obj2 = obj._replace(name='other')
    assert obj2.name == 'other'
    assert obj2.camel == 'Test'
    assert obj2.description == 'a test command'
    assert obj2.commands == ('ls -al',)

# Generated at 2026-11-03 02:21:20.970879
# Unit test for function each_sub_command_config

# Generated at 2026-11-03 02:26:10.045816
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile