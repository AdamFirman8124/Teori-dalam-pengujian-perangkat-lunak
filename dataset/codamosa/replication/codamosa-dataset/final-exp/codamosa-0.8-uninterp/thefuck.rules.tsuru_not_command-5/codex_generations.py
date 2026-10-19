

# Generated at 2022-06-14 10:57:34.233419
# Unit test for function match
def test_match():
    assert match(Command('tsru app-create test', 'tsuru: "tsru" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tapp-create'))
    assert not match(Command('tsuru app-create', 'tsuru: "tsru" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tapp-create'))
    assert not match(Command('tsuru app-create test', ''))


# Generated at 2022-06-14 10:57:44.922369
# Unit test for function match
def test_match():
    output_cmd_not_exists = 'tsuru: "tsuru hlp" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\ttsuru help'
    output_no_suggestion = 'tsuru: "tsuru no-suggestion" is not a tsuru command. See "tsuru help".'
    command_cmd_not_exists = Command('tsuru hlp', '', output_cmd_not_exists)
    assert match(command_cmd_not_exists)

    command_no_suggestion = Command('tsuru no-suggestion', '', output_no_suggestion)
    assert not match(command_no_suggestion)



# Generated at 2022-06-14 10:57:49.928137
# Unit test for function get_new_command
def test_get_new_command():
    output = 'tsuru: "app-delet" is not a tsuru command.\nDid you mean?\n\tapp-deploy'
    command = type('Command', (object,), {'output': output})
    assert get_new_command(command) == 'tsuru app-deploy'

# Generated at 2022-06-14 10:57:57.652273
# Unit test for function get_new_command
def test_get_new_command():
    output = "tsuru: \"gitlab-user-list\" is not a tsuru command. See \"tsuru help\".\n\nDid you mean?\n\tgitlab-list\n\tglb-list\n\tgl-list\n\tgl-user-list"
    command = "tsuru gitlab-user-list"
    assert get_new_command(command, output) == "tsuru gitlab-list"
    

# Generated at 2022-06-14 10:58:03.640662
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("tsuru: \"tsur\" is not a tsuru command. See \"tsuru help\".\nDid you mean?\ntsurud\ntsurus") == "tsurus"
    assert get_new_command("tsuru: \"tsursu\" is not a tsuru command. See \"tsuru help\".\nDid you mean?\ntsurud\ntsurus") == "tsurus"

# Generated at 2022-06-14 10:58:15.702806
# Unit test for function get_new_command
def test_get_new_command():
    def c(output):
        return Command('tsuru', output=output)

    assert get_new_command(c('tsuru: "a" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tapp-list\n\tapp-info\n\tapp')) == 'tsuru app-list'
    assert get_new_command(c('tsuru: "a" is not a tsuru command. See "tsuru help".')) == 'tsuru'
    assert get_new_command(c('tsuru: "a" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tapp-list')) == 'tsuru app-list'

# Generated at 2022-06-14 10:58:20.606293
# Unit test for function match
def test_match():
    assert match(Command('tsuru app-list', 'tsuru: "app-list" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-create'))


# Generated at 2022-06-14 10:58:28.443062
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('tsuru app-list',
                                   'tsuru: "app-list" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-create\n\tapp-list-unit\n\tapp-remove\n\tapp-update\n\tapp-info\n\tapp-remove-unit\n\tapp-deploy\n\tapp-log\n', '')) == 'tsuru app-list'

# Generated at 2022-06-14 10:58:32.576509
# Unit test for function match
def test_match():
    assert match, ("tsuru: \"docker\" is not a tsuru command. See \"tsuru help\"." +
               "\nDid you mean?\n\tdockerize")


# Generated at 2022-06-14 10:58:36.819739
# Unit test for function match
def test_match():
    assert match(Command('tsuru sdf',
                         """tsuru: "sdf" is not a tsuru command.
See "tsuru help".

Did you mean?
    ssh-agent
    ssh-key-add
    ssh-key-remove
    ssh-key-list
""", '', 1))


# Generated at 2022-06-14 10:58:41.795049
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("tsuru app-inf not_an_command_value", "")
    assert get_new_command(command) == "tsuru app-info not_an_command_value"

# Generated at 2022-06-14 10:58:44.080430
# Unit test for function match
def test_match():
    assert match(Command('tsuru app-info  mongodb', ''))
    assert not match(Command('tsuru app-info mongodb', 'mongodb'))



# Generated at 2022-06-14 10:58:58.335829
# Unit test for function match

# Generated at 2022-06-14 10:59:03.789588
# Unit test for function get_new_command
def test_get_new_command():
    #cmd = Command('tsuru app-ls', '')
    cmd = Command('tsuru create-app -t python test', '')
    assert get_new_command(cmd) == 'tsuru app-create -t python test'

# Generated at 2022-06-14 10:59:11.173547
# Unit test for function get_new_command
def test_get_new_command():
    # Test for regex in input
    assert get_new_command(Command('tsuru aount-create parawe',
                                   output='tsuru: "aount-create" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\taccount-create')) == 'tsuru account-create parawe'
    assert get_new_command(Command('tsuru ervice-info',
                                   output='tsuru: "ervice-info" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tnode-list')) == 'tsuru node-list'
    # Test for no match in input

# Generated at 2022-06-14 10:59:14.195691
# Unit test for function get_new_command
def test_get_new_command():
    new_command = get_new_command(Command('tsuru pllatform-add python',
                                          'tsuru: "pllatform-add" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tplatform-add\n'))
    assert new_command == 'tsuru platform-add python'

# Generated at 2022-06-14 10:59:17.094498
# Unit test for function match
def test_match():
    assert match(Command('tsuru version', 'tsuru: "version" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tversio', ''))
    assert not match(Command('tsuru version', 'tsuru: "version" is not a tsuru command. See "tsuru help".', ''))



# Generated at 2022-06-14 10:59:22.203429
# Unit test for function match
def test_match():
    command = Command('tsuru psaas', 'tsuru: "psaas" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tplatform-add\n\tplatform-remove\n\tplatform-list')
    assert match(command)


# Generated at 2022-06-14 10:59:32.301199
# Unit test for function match
def test_match():
    assert match(Command('tsuru uelp -a abc', 'tsuru: "uelp" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tlogin\n\tlogout\n\thelp\n\tversion\n')) == True
    assert match(Command('tsuru', 'tsuru: "tsuru" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tlogin\n\tlogout\n\thelp\n\tversion\n')) == True


# Generated at 2022-06-14 10:59:34.651810
# Unit test for function match
def test_match():
    assert match(Command('tsuru app-create test1', ''))
    assert match(Command('tsuru app-creat test1', ''))



# Generated at 2022-06-14 10:59:45.367957
# Unit test for function match
def test_match():
    assert match(Command('tsuru app-invalid test', 'tsuru: "app-invalid" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-info'))
    assert match(Command('tsuru app-remove-invalid test', 'tsuru: "app-remove-invalid" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-remove'))


# Generated at 2022-06-14 10:59:49.051290
# Unit test for function match
def test_match():
    assert match('tsuru: "doge" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tdoc\ntsuru help\n')


# Generated at 2022-06-14 10:59:54.918989
# Unit test for function match
def test_match():
    assert match(Command('tsuru aaa', 'tsuru: "aaa" is not a tsuru command. '
                         'See "tsuru help".\nDid you mean?\n\tapp-add\n\t'
                         'app-remove\n\tapp-list\n\tapp-info\n\tapp-log'))
    assert not match(Command('tsuru aaa', ''))
# Unit tests for function get_new_command

# Generated at 2022-06-14 11:00:00.052312
# Unit test for function get_new_command
def test_get_new_command():
    output = (
        'tsuru: "nodee" is not a tsuru command. See "tsuru help".\n'
        '\n'
        'Did you mean?\n'
        '\tnode'
    )
    command = Command('nodee', output)
    assert get_new_command(command) == 'tsuru node'



# Generated at 2022-06-14 11:00:05.741798
# Unit test for function match
def test_match():
	#assert match(Command('tsuru app-info', 'tsuru: "app-info" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-info'))
	assert match(Command('tsuru app-info', 'tsuru: "app-info" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-info'))
	assert not match(Command('tsuru app-info', 'tsuru: "app-info" is not a tsuru command. See "tsuru help".'))

# Generated at 2022-06-14 11:00:18.940440
# Unit test for function get_new_command
def test_get_new_command():
    """Function that returns the right new command"""

# Generated at 2022-06-14 11:00:24.511078
# Unit test for function match
def test_match():
    assert match(Command('tsuru myapp-lis',
                         'tsuru: "myapp-lis" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tmyapp-list\n\n'))
    assert not match(Command('tsuru myapp-list', ''))


# Generated at 2022-06-14 11:00:31.355600
# Unit test for function get_new_command
def test_get_new_command():
    output = """tsuru: "team-add" is not a tsuru command.  See "tsuru help".

Did you mean?
	team-remove"""
    assert 'team add' == get_new_command(Command('tsuru team-add', output))

# Generated at 2022-06-14 11:00:38.038565
# Unit test for function match
def test_match():
    assert(match(Command('tsuru do', 'tsuru: "do" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tdeploy\n\tdocker-exec\n\tlogin\n')) == True)
    assert(match(Command('ls', 'tsuru: "ls" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tdelete\n\tdeploy\n\tdocker-exec\n\tlogin\n')) == True)


# Generated at 2022-06-14 11:00:48.789526
# Unit test for function match
def test_match():
    match_func = match
    assert match_func('tsuru: "provi" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tprovide')
    assert match_func('tsuru: "aa" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tapp')
    assert match_func('tsuru: "test" is not a tsuru command. See "tsuru help".\nDid you mean?\n\ttest')
    assert not match_func('tsuru: "test" is not a tsuru command. See "tsuru help".\nDid you mean?\n\t')

# Generated at 2022-06-14 11:00:58.529729
# Unit test for function match
def test_match():
    assert match(Command('tsuru app-imit', 'tsuru: "app-imit" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-info'))
    assert not match(Command('tsuru app', 'App "mariadb" not found.'))


# Generated at 2022-06-14 11:01:11.350886
# Unit test for function match

# Generated at 2022-06-14 11:01:15.766443
# Unit test for function get_new_command
def test_get_new_command():
    new_command = get_new_command(Command('tsuru tgt', 'tsuru: "tgt" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\ttarget', '', 1))
    assert new_command == "tsuru target"

# Generated at 2022-06-14 11:01:21.168816
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("tsuru app-info",
                                   "tsuru: \"app-info\" is not a tsuru command. See \"tsuru help\".\n\nDid you mean?\n\tapp-info\n\tapp-remove")) == "tsuru app-info"

# Generated at 2022-06-14 11:01:25.368356
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(type('Obj', (object,),
                          {'output': 'tsuru: "app-create" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tapp-add\n\tapp-remove'})) == 'tsuru app-add'

# Generated at 2022-06-14 11:01:31.245659
# Unit test for function match
def test_match():
    assert match(Command('tsuru servic',
                output='tsuru: "servic" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tservice-add\n\tservice-bind\n\tservice-doc\n\tservice-list\n\tservice-remove\n\tservice-status\n\tservice-unbind\n'))



# Generated at 2022-06-14 11:01:34.275063
# Unit test for function match
def test_match():
    command = Command('sudo tsuru app-remove gitlab-ce', 'tsuru: "sudo" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-remove\n\n')
    assert match(command)


# Generated at 2022-06-14 11:01:37.962381
# Unit test for function match
def test_match():
    command = Command('tsuru app-list', """tsuru: "list" is not a tsuru command. See "tsuru help".

Did you mean?
	app-list
	target""")
    assert match(command)



# Generated at 2022-06-14 11:01:41.768511
# Unit test for function match
def test_match():
    assert match(Command('tsuru target-add', 'tsuru: "target-add" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tadd-target\n'))


# Generated at 2022-06-14 11:01:47.196630
# Unit test for function match
def test_match():
    output = '''tsuru: "hello" is not a tsuru command. See "tsuru help".

Did you mean?
        target-add
        target-get
        target-remove
'''
    assert match(Command(script="tsuru", stderr=output))
    assert not match(Command(script="tsuru", stderr="no matching"))


# Generated at 2022-06-14 11:02:00.624641
# Unit test for function get_new_command
def test_get_new_command():
    cmd = Command('tsuru app-list', 'tsuru: "app-list" is not a tsuru command. See "tsuru help".', '', '')
    assert get_new_command(cmd) == 'tsuru app-list'

# Generated at 2022-06-14 11:02:07.073719
# Unit test for function get_new_command
def test_get_new_command():
    fmt_cmd = 'tsuru: "{}" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-info\n\tapp-remove\n\tservice-info\n\tservice-remove'
    expected_command = 'tsuru app-info'
    assert get_new_command(Command('tsuru app-inf', fmt_cmd.format('app-inf') + '\n')) == expected_command
    assert get_new_command(Command('tsuru app-in', fmt_cmd.format('app-in') + '\n')) == expected_command

# Generated at 2022-06-14 11:02:14.081678
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    command = Command('tsuru blabla',
                      'tsuru: "blabla" is not a tsuru command. See "tsuru help".\n'
                      '\n'
                      'Did you mean?\n'
                      '\tlogin\n'
                      '\tservice-list\n'
                      '\tapp-add\n'
                      '\tapp-list',
                      '', 0, '', '')
    assert get_new_command(command) == 'tsuru login'

# Generated at 2022-06-14 11:02:20.343738
# Unit test for function match
def test_match():
    assert match(Command('tsr dd', 'tsr: "dd" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tadd-key', '', 0))
    assert not match(Command('tsr add', 'tsr: "add" is a tsuru command. See "tsuru help".'))


# Generated at 2022-06-14 11:02:35.554447
# Unit test for function match
def test_match():
    command_output=''''tsuru: "app-" is not a tsuru command. See "tsuru help".
Did you mean?
        app-add-unit
        app-autoscale
        app-change
        app-deploy
        app-destroy
        app-info
        app-list
        app-log
        app-remove-unit
        app-run
        app-start
        app-stop
        app-swap
        app-team-owner-change
        app-team-owner-list
        app-unit-add
        app-unit-remove
        app-unit-status
        app-update
        app-update-cname-add
        app-update-cname-remove
        app-update-platform'''
    assert match(Command(script='tsuru app-',output=command_output))



# Generated at 2022-06-14 11:02:40.953489
# Unit test for function match
def test_match():
    assert match(Command('tsuru srv help', 'tsuru: "srv" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tservice'))
    assert not match(Command('tsuru srv help', 'tsuru: "hello" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tgo'))

# Generated at 2022-06-14 11:02:47.267705
# Unit test for function match
def test_match():
    assert match(Command('tsuru team-create', 'tsuru: "team-create" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tteam-add\n\tteam-remove\n\n'))
    assert not match(Command('tsuru team-add', 'tsuru team-add ...'))


# Generated at 2022-06-14 11:02:50.954812
# Unit test for function match
def test_match():
    match_output = "tsuru: \"test\" is not a tsuru command. See \"tsuru help\"."
    assert match(Command('test', match_output))
    assert not match(Command('test', ''))


# Generated at 2022-06-14 11:02:56.087995
# Unit test for function match
def test_match():
    assert match(Command('tsuru target-add test', 'tsuru: "target-add" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\ttarget-add\n\ttarget-remove'))



# Generated at 2022-06-14 11:03:09.818565
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('tsuru start-app APP',
                                   'tsuru: "start-app" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tstart-app')) == ['tsuru start-app']
    assert get_new_command(Command('tsuru start-a APP',
                                   'tsuru: "start-a" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tstart-app')) == ['tsuru start-app']

# Generated at 2022-06-14 11:03:32.871816
# Unit test for function match
def test_match():
    assert match(Command('tsuru help', 'tsuru: "help" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tversion\n\n'))

# Generated at 2022-06-14 11:03:37.181658
# Unit test for function match
def test_match():
    assert match(Command(script="tsru", stderr='tsuru: "tsru" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tversion'))


# Generated at 2022-06-14 11:03:40.257009
# Unit test for function match
def test_match():
    assert match(Command('tsuru asdasd', 'tsuru: "asdasd" is not a tsuru command.'))
    assert not match(Command('tsuru help', 'tsuru: "help" is not a tsuru command.'))


# Generated at 2022-06-14 11:03:53.307154
# Unit test for function match
def test_match():
    assert not match(Command('tsuru foo', 'tsuru: "foo" is not a tsuru command. See "tsuru help".\n'))
    assert not match(Command('tsuru foo', 'Did you mean?\n\tfoo\n'))
    assert not match(Command('tsuru foo', 'tsuru: "tsuru foo" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tfoo\n'))
    assert match(Command('tsuru foo', 'tsuru: "foo" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tfoo\n'))


# Generated at 2022-06-14 11:03:58.353285
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('tsuruu', 'tsuru: "tsuruu" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tunit-add\n\tunit-remove')
    new_command = get_new_command(command)
    assert new_command == 'tsuru unit-add'

# Generated at 2022-06-14 11:04:04.894583
# Unit test for function get_new_command
def test_get_new_command():
    command = type('Command', (object,), {'script': 'tsuru env-set', 'output': 'tsuru: "env-set" is not a tsuru command\n\nDid you mean?\n\tcreate-env\n\tstatus\n\tenv-set'})
    new_command = get_new_command(command)
    assert new_command == 'tsuru create-env env-set'

# Generated at 2022-06-14 11:04:09.047009
# Unit test for function match
def test_match():
    assert match(Command('tsurru help'))
    assert not match(Command('tsuru help'))


# Generated at 2022-06-14 11:04:18.711374
# Unit test for function match
def test_match():
    from thefuck.types import Command

    command = Command('tsuru loadbalancel -a myapp',
                      'tsuru: "loadbalancel" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tloadbalancer-add\n\tloadbalancer-list\n\tloadbalancer-remove')
    assert match(command)

    command = Command('tsuru loadbalancel -a myapp', 'tsuru: "loadbalancel" is not a tsuru command. See "tsuru help".')
    assert not match(command)

    command = Command('tsuru loadbalancel -a myapp', "")
    assert not match(command)



# Generated at 2022-06-14 11:04:33.109645
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.tsuru_did_you_mean import get_new_command
    command = Command('tsuru app-info --app XXX',
                      'tsuru: "app-info" is not a tsuru command. '
                      'See "tsuru help".\n'
                      '\n'
                      'Did you mean?\n'
                      '\tapp-info-set\n'
                      '\tapp-log')
    assert get_new_command(command) == 'tsuru app-info-set --app XXX'

# Generated at 2022-06-14 11:04:41.673089
# Unit test for function match
def test_match():
    assert not match(Command('tsur --verbose', ''))
    assert not match(Command('tsur --verbose', 'tsuru: "tsur --verbose" is not a tsuru command. See "tsuru help".\nDid you mean?\n\t--verbose\n'))
    assert match(Command('tsur --verbose', 'tsuru: "tsur --verbose" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tadd-key\n\tremove-key\n\t--verbose\n'))



# Generated at 2022-06-14 11:05:29.588661
# Unit test for function match
def test_match():
    """
    Test the match function
    """

# Generated at 2022-06-14 11:05:32.917858
# Unit test for function get_new_command
def test_get_new_command():
    from tests.utils import Command

    command_output = 'tsuru: "app-info" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-create\n\tapp-remove\n\tapp-restart\n\tapp-run\n\tapp-start\n\tapp-stop\n\tapp-swap\n\tapp-update\n'
    thefuck_output = 'tsuru app-create'
    assert get_new_command(Command('tsuru app-info', command_output)) == thefuck_output

# Generated at 2022-06-14 11:05:39.658806
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('tsuru command', 'tsuru: "command" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tcommand-cancel')) == Command('tsuru command-cancel', 'tsuru: "command" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tcommand-cancel')

# Generated at 2022-06-14 11:05:41.927720
# Unit test for function match
def test_match():
    assert match(Command('tsuru app-info'))
    assert not match(Command('date'))


# Generated at 2022-06-14 11:05:48.056150
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    assert get_new_command(Command('tsuruu', 'tsuru: "tsuruu" is not a tsuru command. See "tsuru help".'
                                   '\nDid you mean?\n\tapp-info\n\tapp-list\n\tapp-remove')) == 'tsuru app-info'
    assert get_new_command(Command('tsuruu', 'tsuru: "tsuruu" is not a tsuru command. See "tsuru help".'
                                   '\nDid you mean?\n\tapp-log\n\tapp-run\n\tapp-run-result')) == 'tsuru app-run'

# Generated at 2022-06-14 11:05:55.500036
# Unit test for function match
def test_match():
    assert match(Command('tsuru app-info blah blah blah', 'tsuru: "app-info" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-create\tCreate an app.\n\tapp-remove\tRemove an app.\n\tapp-restart\tRestart an app.'))
    assert not match(Command('tsuru app-create', ''))



# Generated at 2022-06-14 11:06:05.089308
# Unit test for function match

# Generated at 2022-06-14 11:06:17.455628
# Unit test for function match
def test_match():
    assert match(u'tsuru: "key-unset" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tkey-unsetkey-unset')

# Generated at 2022-06-14 11:06:20.501500
# Unit test for function match
def test_match():
    msg = Command('tsuru user-create', '').output
    assert match(Command('tsuru users', msg))
    assert not match(Command('tsuru users', 'help'))


# Generated at 2022-06-14 11:06:27.841125
# Unit test for function get_new_command
def test_get_new_command():
    output = """tsuru: "app-not-found" is not a tsuru command. See "tsuru help".

Did you mean?
	app-add
	app-remove
	app-info
	app-ls
	app-log
	app-restart
	app-run
	app-grant
	app-revoke"""
    command = Command('')
    command.output = output
    assert get_new_command(command) == 'tsuru app-info'