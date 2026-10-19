

# Generated at 2022-06-14 10:57:33.535726
# Unit test for function get_new_command
def test_get_new_command():
    example_command = Command('tsuruu',
                              'tsuru: "tsuruu" is not a tsuru command. See "tsuru help".\nDid you mean?\n\ttsuru\n\tlogout')
    assert get_new_command(example_command) == 'tsuru'

# Generated at 2022-06-14 10:57:40.577961
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('tsuru user',
                                   'tsuru: "user" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tusers-list\n\tteam-user-add\n\tteam-user-remove\n\tteam-user-list')) == 'tsuru team-user-list'



# Generated at 2022-06-14 10:57:48.989158
# Unit test for function match
def test_match():
    assert match(Command('tsuru app-node-add app_name node_addr', 'tsuru: "app-node-add" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tapp-node-add'))
    assert not match(Command('ls', 'tsuru: "ls" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tls'))


# Generated at 2022-06-14 10:57:51.900765
# Unit test for function match
def test_match():
    """
    Unit test for function match
    """
    assert(match('tsuru: "balh" is not a tsuru command. See "tsuru help".'))



# Generated at 2022-06-14 10:58:03.734936
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('tsuru',
                                   output='tsuru: "app" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tapp-change\n\tapp-create\n\tapp-list\n\tapp-remove\n\tapp-run\n\tapp-info\n')) == 'tsuru app-list'
    assert get_new_command(Command('tsuru',
                                   output='tsuru: "app-create" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tapp-change\n\tapp-create\n\tapp-list\n\tapp-remove\n\tapp-run\n\tapp-info\n')) == 'tsuru app-create'

# Generated at 2022-06-14 10:58:08.173079
# Unit test for function match
def test_match():
    assert match(Command('tsuru app-info', 'tsuru: "app-info" is not a tsuru command.\nDid you mean?\n\tapp-create\n\tapp-info'))


# Generated at 2022-06-14 10:58:11.640220
# Unit test for function get_new_command
def test_get_new_command():
	assert get_new_command(Command('tsuru app-create test', '')) == 'tsuru app-create test'

# Generated at 2022-06-14 10:58:19.763238
# Unit test for function match
def test_match():
    assert match(Command('tsuru foo', 'tsuru: "foo" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tfoo-bar\n\tfoo-bar-baz\n'))
    assert not match(Command('tsuru foo', ''))



# Generated at 2022-06-14 10:58:23.159976
# Unit test for function match
def test_match():
    assert match(Command('foo is not a tsuru command. See "tsuru help".'
                         '\nDid you mean?\n\tbar', ''))


# Generated at 2022-06-14 10:58:29.902632
# Unit test for function get_new_command
def test_get_new_command():
    output = 'tsuru: "config" is not a tsuru command. See "tsuru help".\n'\
        '\n'\
        'Did you mean?\n'\
        '\tconfig-get\n'\
        '\tconfig-set\n'\
        '\tconfig-unset'
    command = Command('tsuru config', output)
    assert get_new_command(command) == 'tsuru config-get'

# Generated at 2022-06-14 10:58:38.933682
# Unit test for function match
def test_match():
    assert match(Command('tsuru app-create -t java myapp',
                         'tsuru: "app-create" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-add-unit\n\tapp-archive\n\tapp-deploy'))
    assert not match(Command('tsuru app-create -t java myapp',
                             'tsuru: "app-create" is not a tsuru command'))



# Generated at 2022-06-14 10:58:42.568344
# Unit test for function match
def test_match():
    command = Command('tsuru help', 'tsuru: "help" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tlogin\n\tlogout\n\tservice-bind\n\tset')
    assert match(command)



# Generated at 2022-06-14 10:58:46.034347
# Unit test for function match
def test_match():
	assert match(Command('tsuru u', 'tsuru: "u" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tunit-add', ''))
	assert not match(Command('tsuru login', '', ''))
	assert not match(Command('tsuru', '', ''))


# Generated at 2022-06-14 10:58:57.548760
# Unit test for function match
def test_match():
    assert match(Command('tsuru unit-add unittest', 'tsuru: "unit-add" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tunit-add')) is True
    assert match(Command('tsuru unit-add unittest', 'tsuru: "unit-add" is a tsuru command. See "tsuru help".\n\nDid you mean?\n\tunit-add')) is False



# Generated at 2022-06-14 10:59:07.876795
# Unit test for function match
def test_match():
    assert match(Command('tsuru sdf', 'tsuru: "sdf" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-create\n\tapp-delete\n\tapp-info\n\tapp-list\n\tapp-rebuild', '')) is True
    assert match(Command('tsuru sdf', 'tsuru: "sdf" is not a tsuru command', '')) is False
    assert match(Command('tsuru sdf', 'tsuru: "sdf" is not tsuru', '')) is False


# Generated at 2022-06-14 10:59:13.558719
# Unit test for function match
def test_match():
    assert match(Command('tsuru version', 'tsuru: "version" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapps-info\n\tapp-log'))
    assert not match(Command('tsuru version', 'tsuru version 1'))


# Generated at 2022-06-14 10:59:19.504449
# Unit test for function match
def test_match():
    assert match(Command('tsuru app-deploy',
                         'tsuru: "app-deploy" is not a tsuru command. See "tsuru help".\n\n' +
                         'Did you mean?\n\tapp-deploy'))
    assert not match(Command('tsuru -h', ''))
    assert not match(Command('tsuru app-deploy', ''))



# Generated at 2022-06-14 10:59:21.313270
# Unit test for function get_new_command

# Generated at 2022-06-14 10:59:22.501336
# Unit test for function get_new_command
def test_get_new_command():
	assert get_new_command('') == ''

# Generated at 2022-06-14 10:59:29.150692
# Unit test for function get_new_command
def test_get_new_command():
    assert_equals(get_new_command(Command(script='tsuru user-add',
                                          output='tsuru: "user-add" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tuser-create')),
                  'tsuru user-create')


# Generated at 2022-06-14 10:59:37.037433
# Unit test for function match
def test_match():
    expected_output1 = 'tsuru: "targettsuru" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\ttarget-add\n\ttarget-remove'
    expected_output2 = 'tsuru: "target-remove" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\ttarget'
    assert match(Command('targettsuru', expected_output1))
    assert not match(Command('target-remove', expected_output2))


# Generated at 2022-06-14 10:59:51.107182
# Unit test for function match
def test_match():
    assert match(Command('tsuru deploy -a appname', 'tsuru: "deploy" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tdeploy-app'))
    assert not match(Command('tsuru deploy', 'tsuru: "deploy" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tdeploy-app'))



# Generated at 2022-06-14 10:59:54.225063
# Unit test for function match
def test_match():
    assert match(Command('tsuru app-infors', 'no matches for "app-infors" in command list'))
    assert match(Command('tsuru app-info', 'unknown command "app-info"'))


# Generated at 2022-06-14 11:00:07.220353
# Unit test for function match
def test_match():
    # pylint: disable-msg=protected-access
    command = Command('tsuru app-logs -a appname', 'Error: "app-logs" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tget-logs', '', 123, 101, '')
    assert match(command)
    command = Command('tsuru app-logs -a appname', 'Error: "app-logs" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tget-logs')
    assert match(command)
    command = Command('tsuru invalidcommand -a appname', 'Error: "app-logs" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tget-logs')


# Generated at 2022-06-14 11:00:12.428969
# Unit test for function match
def test_match():
    assert match(Command("tsuru unit-add", Error("tsuru: \"unit-add\" is not a tsuru command. See \"tsuru help\".")))
    assert not match(Command("tsuru unit-add", "") )


# Generated at 2022-06-14 11:00:23.436307
# Unit test for function match
def test_match():
    assert match(Command('tsuru app-ssssssssssssssssssss', 'tsuru: "app-ssssssssssssssssssss" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-list', ''))
    assert match(Command('tsuru app-ssssssssssssssssssss', 'tsuru: "app-ssssssssssssssssssss" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-list\n\tapp-info', ''))
    assert not match(Command('tsuru do-this-command', 'tsuru: "do-this-command" is not a tsuru command. See "tsuru help".', ''))

# Generated at 2022-06-14 11:00:31.173088
# Unit test for function get_new_command
def test_get_new_command():
    command = mock.MagicMock(output='tsuru: "app" is not a tsuru command. See "tsuru help".', script='tsuru app')
    assert get_new_command(command) == 'tsuru app-list'

enabled_by_default = True

# Generated at 2022-06-14 11:00:37.286797
# Unit test for function get_new_command
def test_get_new_command():
    output = 'tsuru: "token-show" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\ttoken-add\ttoken-remove'
    command = 'tsuru token-show'
    assert get_new_command(commands.Command(script=command, stderr=output)) == 'tsuru token-add'

# Generated at 2022-06-14 11:00:43.448453
# Unit test for function match
def test_match():
    output = 'tsuru: "hello" is not a tsuru command. See "tsuru help".\n\n\nDid you mean?\n\thelp\n'
    assert (match(Command('hello world', '', output)) == True)
    assert (match(Command('hello world', '', '')) == False)
    assert (match(Command('tsuru hello world', '', output)) == True)


# Generated at 2022-06-14 11:00:56.047061
# Unit test for function match
def test_match():
    """Checks if match function is working as expected.
    
    There are some tricky cases. This function tests for those cases by
    use of 5 examples. The first and second examples test for a scenario
    where there is no misspelling. The last three test for scenarios where
    the spelling is not correct.
    
    Example 1
    ----------
    
    
    Example 2
    ----------
    
    
    Example 3
    ----------
    
    
    Example 4
    ----------
    
    
    Example 5
    ----------
    
    
    """
    

# Generated at 2022-06-14 11:01:10.722914
# Unit test for function get_new_command

# Generated at 2022-06-14 11:01:15.860845
# Unit test for function match
def test_match():
    output_1 = 'tsuru: "alo" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tallow-rule\n\tall-rules\n\tlogin'
    output_2 = 'tsuru: "aog" is not a tsuru command. See "tsuru help".'

    assert match(Command('tsuru aog', output_1))
    assert not match(Command('tsuru aog', output_2))



# Generated at 2022-06-14 11:01:28.281996
# Unit test for function match
def test_match():
    assert match(Command('tsuru version',
                         'tsuru: "version" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\t-v, --version, --info, --print-version\n',
                         ""))
    assert match(Command('tsuru app-log',
                         'tsuru: "app-log" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tlog-unit\n',
                         ""))
    assert not match(Command('tsuru app-deploy',
                             'tsuru: "app-deploy" is not a tsuru command. See "tsuru help".',
                             ""))
    


# Generated at 2022-06-14 11:01:37.681428
# Unit test for function match
def test_match():
    assert match(Command('tsuru rw',
                         'tsuru: "rw" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\trw-app\n\trw-container\n\trw-node',
                         '', 2))

    assert not match(Command('command', '', '', 1))
    assert not match(Command('command', '', '', 2))
    assert not match(Command('command', '', '', 0))
    assert not match(Command('tsuru rw', '', '', 0))


# Generated at 2022-06-14 11:01:48.311606
# Unit test for function match

# Generated at 2022-06-14 11:01:51.509599
# Unit test for function match
def test_match():
    assert match(Command('tsuru rm', 'tsuru: "rm" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tremove\n\tremove-machine\n\tremove-service\n\tremove-unit\n\tremove-user', '', 1))
    assert not match(Command('tsuru app-info mongodb', "tsuru: Warning: settings for 'mongodb' are not available. You need to do 'tsuru app-create' first.\n", '', 0))


# Generated at 2022-06-14 11:01:56.081133
# Unit test for function match
def test_match():
    from thefuck.rules.tsuru_did_you_mean import match
    command = 'tsuru: "ftp" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tfd'
    assert match(command)



# Generated at 2022-06-14 11:02:05.388188
# Unit test for function match
def test_match():
    from thefuck.types import Command


# Generated at 2022-06-14 11:02:15.127434
# Unit test for function match
def test_match():
    #AssertionError: output did not match "tsuru: "([^"]*)" is not a tsuru command."
    assert match(Command('tsuru any',
                         'tsuru: "any" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-list\n\tapp-info\n\tapp-remove\n\tapp-create\n\tapp-log\n\tapp-grant\n\tapp-run\n\tapp-revoke\n\tapp-deploy\n\tapp-start')) 
    #assert not match(Command('tsuru target-add tsuru-admin https://tsuru.platan.us --set default', ''))
    #assert match(Command('sudo tsuru target-add tsuru

# Generated at 2022-06-14 11:02:19.822353
# Unit test for function match
def test_match():
    output = """tsuru: "target-list" is not a tsuru command. See "tsuru help".

Did you mean?
	target-add
	target-remove
	targe
"""
    assert match(Command("target-list", output))

# Generated at 2022-06-14 11:02:30.160621
# Unit test for function match
def test_match():
    assert match(Command('tsuru unauthorize --admin something',
                         'tsuru: "unauthorize" is not a tsuru command. See '
                         '"tsuru help".\n\nDid you mean?\n\tapp-unbind\n\t'
                         'app-unset\n\tkey-remove'))


# Generated at 2022-06-14 11:02:38.476078
# Unit test for function get_new_command
def test_get_new_command():
    # Example output of a wrong command
    output = '''tsuru: "admin-create" is not a tsuru command. See "tsuru help".

Did you mean?
	api-create
	app-create
	app-info
	app-log
	app-remove
	app-restart
	app-run
'''
    command = Command('admin-create', output=output)
    assert get_new_command(command) == 'api-create'

# Generated at 2022-06-14 11:02:47.143452
# Unit test for function match
def test_match():
    assert match(Command('foo',
                         output='tsuru: "foo" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tfoo\n\tbar'))
    assert not match(Command('foo', output='tsuru: "foo" is not a tsuru command'))
    assert match(Command('foo',
                         output='tsuru: "foo" is not a tsuru command. See "tsuru help".'))



# Generated at 2022-06-14 11:02:54.675970
# Unit test for function match
def test_match():
    from thefuck.rules.tsuru_did_you_mean import match
    command = "tsuru app-info: \"app-info\" is not a tsuru command. See \"tsuru help\".\n\nDid you mean?\n\tapp-remove\n\tapp-create\n\tapp-info\n\tapp-list\n\tapp-run\n\tapp-deploy"
    assert match(command)


# Generated at 2022-06-14 11:02:58.865488
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('tsuru beua', 'tsuru: "beua" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tbeau')) == "tsuru beau"

# Generated at 2022-06-14 11:03:00.807906
# Unit test for function match
def test_match():
    assert match(Command('tsuruu'))
    assert not match(Command('tsuru'))



# Generated at 2022-06-14 11:03:06.916212
# Unit test for function get_new_command
def test_get_new_command():
    output = """tsuru: "target-create" is not a tsuru command. See "tsuru help".

Did you mean?
\tcreate
\tuser-create
\ttarget-remove
\tpermission-add
\ttarget-list"""
    c = Command('tsuru target-create', output)
    assert get_new_command(c) == 'tsuru target-remove'

# Generated at 2022-06-14 11:03:14.398125
# Unit test for function match
def test_match():
    assert match(Command('tsuru add-key', 'tsuru: "add-key" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tadd-key\n\tapp-add-key\n\tapp-add-unit\n\tapp-remove-key\n\tapp-remove-unit\n\tapp-run\n'))
    assert not match(Command('tsuru add-key', 'tsuru: "add-key" is not a tsuru command. See "tsuru help".'))
    assert not match(Command('tsuru app-add', 'tsuru: "app-add" is not a tsuru command. See "tsuru help".'))

# Generated at 2022-06-14 11:03:16.044295
# Unit test for function match
def test_match():
    assert match(Command('tsuru permition-ls', 'tsuru: "permition-ls" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tpermission-list'))


# Generated at 2022-06-14 11:03:19.420378
# Unit test for function match
def test_match():
    assert match(Command('tsru',
                         output = 'tsuru: "tsru" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\ttsuru hello-world'))


# Generated at 2022-06-14 11:03:26.604045
# Unit test for function match
def test_match():
    assert match(Command('tsuru app-create', ''))
    assert not match(Command('tsuru app-create', 'tsuru: "app-creat" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tapp-create\n'))



# Generated at 2022-06-14 11:03:39.559842
# Unit test for function match
def test_match():
    output1 = 'Error: "--add" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tadd-key\n\tadd-permission\n\tapp-add-cname'
    command1 = Command('tsuru --add test_key', output1)
    assert match(command1)

    output2 = 'Error: "--remover-cname" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tadd-cname'
    command2 = Command('tsuru --remover-cname test_cname', output2)
    assert match(command2)

    output3 = 'Error: "--init" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tapp-init'

# Generated at 2022-06-14 11:03:47.581693
# Unit test for function get_new_command
def test_get_new_command():
    new_command = get_new_command(MagicMock(output=(
        "tsuru: \"deploy\" is not a tsuru command. See \"tsuru help\"."
        "\n\nDid you mean?\n\tdeploy-app"
    )))
    assert new_command == ['tsuru deploy-app']

# Generated at 2022-06-14 11:03:51.817729
# Unit test for function match
def test_match():
    output = 'tsuru: "target" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tteam-set-env  targets  team-create\n'
    assert match({'output': output})



# Generated at 2022-06-14 11:03:57.894053
# Unit test for function match
def test_match():
    output =  "tsuru: \"team-member-add\" is not a tsuru command. See \"tsuru help\"." + "\n"
    output += "Did you mean?" + "\n"
    output += "        team-user-add"

    command = Command(script='tsuru team-member-add',
                      stderr=output)

    assert match(command) == True



# Generated at 2022-06-14 11:04:06.899683
# Unit test for function match
def test_match():
    # If the output is correct
    assert match(Command('tsuru app-ls', 'tsuru: "app-ls" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tapp-list'))
    # If the output is not correct
    assert not match(Command('tsuru app-ls', ''))
    # If the output is not as expected
    assert not match(Command('tsuru app-ls', 'tsuru: "app-ls" is not a tsuru command. See "tsuru help".'))



# Generated at 2022-06-14 11:04:13.044146
# Unit test for function match
def test_match():
    assert match(Command('tsuru target-list', 'tsuru: "target-list" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tapp-info\n\tapp-log\n\tapp-remove\n\tapp-restart\n\tapp-run'))



# Generated at 2022-06-14 11:04:24.735355
# Unit test for function match

# Generated at 2022-06-14 11:04:28.144726
# Unit test for function get_new_command
def test_get_new_command():
    output = 'tsuru: "apps-info" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-info'
    assert get_new_command(FakeCommand('tsuru apps-info', output=output)) == 'tsuru app-info'



# Generated at 2022-06-14 11:04:35.094739
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('tsuru target-add teste https://192.168.50.4:8443/',
                                   'tsuru: "target-add" is not a tsuru command. See "tsuru help".\n\n\nDid you mean?\n\ttarget-add\n\ttarget-remove\n\ttarget-list',
                                   1)) == 'tsuru target-add teste https://192.168.50.4:8443/'

# Generated at 2022-06-14 11:04:46.205392
# Unit test for function match
def test_match():
    assert match(Command('tsuru version',
                         "tsuru: \"version\" is not a tsuru command. See \"tsuru help\".\n\nDid you mean?\n\tversion-set\n\tversion-remove\n\tversion-list\n")) is True


# Generated at 2022-06-14 11:04:55.225735
# Unit test for function get_new_command
def test_get_new_command():
    from . import MockCommand

    mock_command = MockCommand('tsuru myapp-list', '''tsuru: "myapp-list" is not a tsuru command. See "tsuru help".

Did you mean?
	myapp-list-build
	myapp-list-repository
	myapp-list-teams
	myapp-log-remove
	myapp-log-set
	myapp-metric-add
	myapp-metric-remove
	myapp-metric-set
	myapp-plan-remove
	myapp-plan-set
	myapp-remove
	myapp-repository-remove
	myapp-router-add
	myapp-router-remove
	myapp-set
	myapp-team-remove
	myapp-team-set''')

   

# Generated at 2022-06-14 11:05:01.111240
# Unit test for function match
def test_match():
    command = Command('tsuru bla', 'tsuru: "bla" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tbla')
    assert match(command)


# Generated at 2022-06-14 11:05:09.102929
# Unit test for function match
def test_match():
    assert match(Command('tsuru target-machines',
                         'tsuru: "target-machines" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\ttarget-machine\n\n')) # NOQA
    assert not match(Command('tsuru target-machines', '\n'))
    assert not match(Command('tsuru target-machines', 'tsuru: "target-machines" is not a tsuru command')) # NOQA


# Generated at 2022-06-14 11:05:17.390111
# Unit test for function match
def test_match():
    assert match(Command('tsuru help', 'tsuru: "help" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\thelp-app\n\thelp-node'))
    assert match(Command('tsuru target', 'tsuru: "target" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\ttarget-add\n\ttarget-remove'))
    assert match(Command('tsuru run', 'tsuru: "run" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\trun-app'))
    assert not match(Command('tsuru target-add', 'usage: tsuru target-add <name> <url> [flags]'))

# Generated at 2022-06-14 11:05:18.546444
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('tsuru app-create')) == 'tsuru app-create'



# Generated at 2022-06-14 11:05:28.652491
# Unit test for function match

# Generated at 2022-06-14 11:05:32.025866
# Unit test for function match
def test_match():
    assert match(Command('tsuru servicelist',
                         """tsuru: "servicelist" is not a tsuru command. See "tsuru help".

Did you mean?
	service-list
"""))
    assert not match(Command('tsuru servicelist',
                             """tsuru: "servicelist" is not a tsuru command. See "tsuru help".

Did you mean?
	service-list
""", '', 0, ''))


# Generated at 2022-06-14 11:05:41.868815
# Unit test for function match
def test_match():
    assert match(Command('tsuru curret', "tsuru: \"curret\" is not a tsuru command. See \"tsuru help\".\n\nDid you mean?\n\tcurrent"))
    assert match(Command('tsuru curret', "tsuru: \"curret\" is not a tsuru command. See \"tsuru help\".\n\nDid you mean?\n\tcurrent\n\ttsuru current-user"))
    assert not match(Command('tsuru', "tsuru: \"\" is not a tsuru command. See \"tsuru help\"."))


# Generated at 2022-06-14 11:05:50.683381
# Unit test for function match
def test_match():
	command = Command('tsuru --version', 'tsuru: "--version" is not a tsuru command. See "tsuru help".\nDid you mean?\n\t-v', '', 1)
	assert match(command)
	command = Command('tsuru --version', 'tsuru: "--version" is not a tsuru command. See "tsuru help".', '', 1)
	assert not match(command)
	command = Command('tsuru --version', 'tsuru: "--version" is not a tsuru command. See "tsuru help".\nDid you mean?\n\t-v', '', 1)
	assert match(command)
	command = Command('tsuru --version', 'tsuru: "--version" is not a tsuru command. See "tsuru help".', '', 1)
	

# Generated at 2022-06-14 11:06:08.368444
# Unit test for function match
def test_match():
    from tests.utils import Command
    assert match(Command('tsrtu app-create'))
    assert not match(Command('tsuru help'))
    assert not match(Command('tsuru app-create'))
    assert not match(Command('ls'))


# Generated at 2022-06-14 11:06:17.593962
# Unit test for function match
def test_match():
    stderr1 = "tsuru: \"p\" is not a tsuru command. See \"tsuru help\".\n\nDid you mean?\n\tps\n\n"
    stderr2 = "tsuru: \"ps\" is not a tsuru command. See \"tsuru help\".\n\nDid you mean?\n\tps\n\n"

    assert match(Command(script="tsuru p", stderr=stderr1))
    assert not match(Command(script="tsuru ps", stderr=stderr2))


# Generated at 2022-06-14 11:06:24.736315
# Unit test for function get_new_command
def test_get_new_command():
    correct_cmd = 'tsuru app-tsurudd'
    command = Command(script=correct_cmd,
                      output="""tsuru: "app-tsurud" is not a tsuru command. See "tsuru help".
Did you mean?
	app-list
	app-restart
	app-remove
	app-create
	app-info""")
    assert get_new_command(command) == 'tsuru app-list'

# Generated at 2022-06-14 11:06:27.928369
# Unit test for function match
def test_match():
    assert match(Command('tsuru add-key', "tsuru: \"add-key\" is not a tsuru command. See \"tsuru help\".\n\nDid you mean?\n\tadd-key-authori"))


# Generated at 2022-06-14 11:06:33.939778
# Unit test for function match
def test_match():
    # True
    assert match(Command('tsuru app-list', 'tsuru: "app-list" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-log\n\tapp-remove\n\tapp-router-add\n\tapp-router-remove\n\twapp-list'))
    # False
    assert not match(Command('tsuru app-list', 'tsuru: "app-list" is not a tsuru command'))


# Generated at 2022-06-14 11:06:42.553542
# Unit test for function match
def test_match():
    output1 = 'tsuru: "app-log" is not a tsuru command. See "tsuru help".\n \
    Did you mean?\n\tapp-list\n\tapp-run'
    output2 = 'tsuru: "app-deploy" is not a tsuru command. See "tsuru help".\n \
    Did you mean?\n\tapp-create'
    assert match(Command('tsuru app-log', output1))
    assert match(Command('tsuru app-deploy', output2))
    assert not match(Command('tsuru app-list', ''))
    assert not match(Command('sudo tsuru app-list', ''))


# Generated at 2022-06-14 11:06:48.734535
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.tsuru_did_you_mean import get_new_command
    output = ('''tsuru: "target" is not a tsuru command. See "tsuru help".\n
Did you mean?
        target-add
        target-remove''')
    command = type('', (object,), {'script': 'target', 'output': output})
    assert get_new_command(command) == 'tsuru target-add'

# Generated at 2022-06-14 11:06:53.652708
# Unit test for function match
def test_match():
    command = 'tsuru: "tsssss" is not a tsuru command. See "tsuru help".\nDid you mean?\n\ttsuru app-create'
    assert match(Command('', command))


# Generated at 2022-06-14 11:07:01.712264
# Unit test for function match
def test_match():
    command1 = Command('tsuru environment-list', 'Error: "environment-list" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tenvironment-get\n\tenvironment-set', '')
    command2 = Command('tsuru support', 'Error: "support" is not a tsuru command. See "tsuru help".', '')
    assert(match(command1) == True)
    assert(match(command2) == False)


# Generated at 2022-06-14 11:07:03.459064
# Unit test for function match
def test_match():
    command = Command('tsuru -u http://tsuru.plataformas.gl app-info appname',
                      'tsuru: "app-info" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-info', 1)
    assert match(command)

