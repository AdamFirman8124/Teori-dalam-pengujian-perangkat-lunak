

# Generated at 2022-06-14 10:57:38.879296
# Unit test for function match
def test_match():
    output = "\n\033[31mtsuru: \"potato\" is not a tsuru command. See \"tsuru help\"!\033[0m\n\n\033[31mDid you mean?\n\tapp-create\n\tapp-lock\n\tapp-remove\n\tapp-restart\n\tapp-unlock\n\tapp-rebuild\n\tapp-start\n\tapp-stop\033[0m\n"
    assert match(Command("potato", output))
    assert not match(Command("potato", "Error"))


# Generated at 2022-06-14 10:57:44.032867
# Unit test for function get_new_command
def test_get_new_command():
    if (os.path.isfile("/usr/local/bin/tsuru")):
        command = Command("tsuru target-add dev http://tsuru.io/", "tsuru: \"target-add\" is not a tsuru command.\nSee \"tsuru help\".\n\nDid you mean?\n\tadd-target\n\n")
    else:
        command = Command("tsuru target-add dev http://tsuru.io/", "tsuru: \"target-add\" is not a tsuru command.\nSee \"tsuru help\".\n\n")
    assert get_new_command(command) == "tsuru add-target dev http://tsuru.io/"

# Generated at 2022-06-14 10:57:56.752344
# Unit test for function match
def test_match():
    #  testing match()
    assert match(Command('tsuru target-add foo https://some.web.site', 'tsuru: "target-add" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\ttarget-remove')) == True
    assert match(Command('tsuru target-add foo https://some.web.site', 'foo')) == False
    assert match(Command('tsuru target-add foo https://some.web.site', '')) == False
    assert match(Command('tsuru target-add foo https://some.web.site', 'tsuru: "target-add" is not a tsuru command. See "tsuru help".')) == False


# Generated at 2022-06-14 10:58:05.288953
# Unit test for function match
def test_match():
    assert match(Command('tsuru app-list', ''))
    assert match(Command('tsuru service-list',''))
    assert not match(Command('tsuru app-list', 'tsuru: "app-list" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-list'))
    assert not match(Command('tsuru app-list', 'tsuru app-list'))
    assert not match(Command('tsuru app-list', 'tsuru: "app-list" is not a tsuru command. See "tsuru help".'))

# Generated at 2022-06-14 10:58:10.694284
# Unit test for function match
def test_match():
    assert match(Command('tsuru config-set -a myapp foo bar',
                         'tsuru: "config-set" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tconfig-set'))
    assert not match(Command('tsuru version', ''))


# Generated at 2022-06-14 10:58:20.935625
# Unit test for function match
def test_match():
    assert match(Command('tsuru --help', 'tsuru: "--help" is not a tsuru command\nDid you mean?\n\tapp-cancel-remove\n\tapp-change-unit\n\tapp-grant\n\tapp-revoke\n\nrun tsuru help for more details'))
    assert not match(Command('tsuru', 'No such command\n'))
    assert not match(Command('', ''))


# Generated at 2022-06-14 10:58:25.340017
# Unit test for function get_new_command
def test_get_new_command():
    output = 'tsuru: "a" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tb'
    assert "tsuru b" == str(get_new_command("tsuru a", output))

# Generated at 2022-06-14 10:58:29.187119
# Unit test for function get_new_command
def test_get_new_command():
    command = "tsuru: \"app-info\" is not a tsuru command. See \"tsuru help\".\nDid you mean?\n\tapp-deploy"
    assert get_new_command(command) == "tsuru app-deploy"

# Generated at 2022-06-14 10:58:34.317903
# Unit test for function get_new_command
def test_get_new_command():
    broken_cmd = 'tsuru: "tsur app-create" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tcreate-app'
    assert get_new_command(Command(broken_cmd)) == 'tsuru create-app'

# Generated at 2022-06-14 10:58:37.091571
# Unit test for function match
def test_match():
    assert match(Command('tsuru app-create asdfasdfasdfas', ''))
    assert not match(Command('tsuru app-list', ''))

# Generated at 2022-06-14 10:58:46.247899
# Unit test for function match
def test_match():
    assert match(Command('tsuru', 'tsuruu is not a tsuru command. See "tsuru help".\n\n\nDid you mean?\n\ttsurur is not a tsuru command. See "tsuru help".\n\ttsuru is not a tsuru command. See "tsuru help".'))
    assert not match(Command('echo', 'not a tsuru command'))



# Generated at 2022-06-14 10:58:59.557724
# Unit test for function match
def test_match():
    from thefuck.rules.tsuru_did_you_mean import match
    command = type('obj', (object,), {'output':'tsuru: "hello" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tadmin-token\n\tapp-create\n\tapp-list\n\tapp-remove\n\tapp-info\n'})
    assert match(command)
    assert not match(type('obj', (object,), {'output': 'tsuru: "hello" is not a tsuru command. See "tsuru help"'}))


# Generated at 2022-06-14 10:59:06.671695
# Unit test for function match
def test_match():
    assert match({'output': 'tsuru: "run" is not a tsuru command. See "tsuru help".\nDid you mean?\n\trun-app'})
    assert not match({'output': 'tsuru: "run" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tswitch'})


# Generated at 2022-06-14 10:59:12.002387
# Unit test for function get_new_command
def test_get_new_command():
    output = 'tsuru: "app-lsit" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tapp-list'
    command = Command('tsuru app-lsit', output)
    assert get_new_command(command).script == 'tsuru app-list'

# Generated at 2022-06-14 10:59:16.675912
# Unit test for function match
def test_match():
    assert match(Command('tsurue potatoe',
                         'tsuru: "potatoe" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tpotato\n\n'))
    assert not match(Command('git branch', ''))



# Generated at 2022-06-14 10:59:21.439582
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('tsr jusdfdfdst do something', '', "tsuru: \"jusdfdfdst\" is not a tsuru command. See \"tsuru help\".\n\nDid you mean?\n\tjust\n\tjuse", None)
    assert get_new_command(command) == 'tsuru just do something'

enabled_by_default = True

# Generated at 2022-06-14 10:59:30.297107
# Unit test for function match
def test_match():
    # Test case where output is correctly a suggestion error
    assert match(Command('tsuru app-list', 'tsuru: "app-list" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-create\n', '', 0))
    # Test case where output is not a suggestion error
    assert not match(Command('tsuru app-list', 'tsuru: "app-list" is not a tsuru command', '', 0))


# Generated at 2022-06-14 10:59:36.002007
# Unit test for function match
def test_match():
    assert match(Command('tsuru tset', 'tsuru: "tset" is not a tsuru command. See "tsuru help".\nDid you mean?\n\ttarget\n\ttarget-add\n\ttarget-remove\n\ttest-deprecation\n\tupdate-node-container\n'))
    assert not match(Command('tsuru target-add', ''))



# Generated at 2022-06-14 10:59:45.550758
# Unit test for function get_new_command
def test_get_new_command():
    class Command:
        def __init__(self, output):
            self.output = output

    assert get_new_command(Command('tsuru: "petic" is not a tsuru command. See "tsuru help".\n\n\nDid you mean?\n\tpet')) == "tsuru pet"
    assert get_new_command(Command('tsuru: "petic" is not a tsuru command. See "tsuru help".\n\n\nDid you mean?\n\tpet\n\tpetr\n')) == "tsuru pet"

# Generated at 2022-06-14 10:59:58.050607
# Unit test for function match
def test_match():
    assert match(Command('tsuru app-list',
                         'tsuru: "app-list" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-create\n\tapp-remove\n\tapp-restart\n\tapp-run\n\tapp-start\n\tapp-stop\n\tapp-swap\n'))
    assert match(Command('tsuru app-list',
                         'tsuru: "app-list" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-create\n\tapp-remove\n\tapp-run\n\tapp-start\n\tapp-stop\n\tapp-swap\n'))

# Generated at 2022-06-14 11:00:07.117566
# Unit test for function match
def test_match():
    # match
    assert match(Command('tsuru helpme', 'tsuru: "helpme" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\thelp'))
    # not match
    assert not match(Command('tsuru helpme', 'tsuru: "helpme" is not a tsuru command. See "tsuru help".'))
    assert not match(Command('tsuru helpme', 'tsuru: "helpme" is not a tsuru command. See "tsuru help".\n\n'))
    assert not match(Command('tsuru helpme', 'tsuru: "helpme" is not a tsuru command. See "tsuru help".\n\nDid you mean?'))



# Generated at 2022-06-14 11:00:15.225132
# Unit test for function match
def test_match():
    output = """tsuru: "add-key" is not a tsuru command. See "tsuru help".

Did you mean?
	add-keywords
	add-keyword
	add-keywords2
	add-keyword2
	add-keywords3
	add-keyword3"""

    assert_true(match(Command(script='',
        output=output,
        stderr='')))


# Generated at 2022-06-14 11:00:20.433656
# Unit test for function get_new_command
def test_get_new_command():
    from tests.utils import Command

    wrong_command = Command('tsuru app-list',
        'tsuru: "app-list" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-create'
    )

    assert get_new_command(wrong_command).script == 'tsuru app-create'

# Generated at 2022-06-14 11:00:23.690275
# Unit test for function match
def test_match():
    cmd = Command('tsuru plataform-add php', '')
    assert match(cmd)

    cmd = Command('tsuru app-create', '')
    assert not match(cmd)


# Generated at 2022-06-14 11:00:37.175452
# Unit test for function match
def test_match():
    assert match(Command('tsuru app-create',
                         'tsuru: "app-create" is not a tsuru command. '
                         'See "tsuru help".\n'
                         '\nDid you mean?\n'
                         '\tapp-change-quota',
                         1))

    assert match(Command('tsuru app-create',
                         'tsuru: "app-create" is not a tsuru command. '
                         'See "tsuru help".\n'
                         '\nDid you mean?\n'
                         '\tapp-change-quota',
                         1))

    assert not match(Command('tsuru app-create',
                         'tsuru: "app-create" is not a tsuru command. '
                         'See "tsuru help".',
                         1))


# Generated at 2022-06-14 11:00:40.351754
# Unit test for function get_new_command
def test_get_new_command():
    command = "tsuru: \"tsurua\" is not a tsuru command. See \"tsuru help\"."
    '\nDid you mean?'
    '\n\ttsuru app-add\n\ttsuru app-change\n\ttsuru app-create'
    assert get_new_command(command) == 'tsuru app-add'

# Generated at 2022-06-14 11:00:44.768509
# Unit test for function match
def test_match():
    assert match('tsuru: "h" is not a tsuru command. See "tsuru help".\n\n' \
                 'Did you mean?\n\thelp\n\n')

    assert not match('this is not a tsuru command')


# Generated at 2022-06-14 11:00:48.254054
# Unit test for function match
def test_match():
    assert match(Command('tsuru naoexiste', 'tsuru: "naoexiste" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tno-rebuild'))



# Generated at 2022-06-14 11:00:57.130518
# Unit test for function match
def test_match():
    output1 = 'tsuru: "role-add" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\trole-remove\n\tnumber'
    output2 = 'tsuru: "add" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tremove\n\tnumber'
    assert match(Command('tsuru role-add test aaa@company.com', output1))
    assert match(Command('tsuru add', output2))


# Generated at 2022-06-14 11:01:00.206263
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('tsuru xxx', 'tsuru: "xxx" is not a tsuru command. See "tsuru help".\nDid you mean?\n\txxx-list\n')
    assert get_new_command(command) == 'tsuru xxx-list'

# Generated at 2022-06-14 11:01:12.433615
# Unit test for function match
def test_match():
    assert match(Command('tsuru cliente', 'tsuru: "cliente" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tclient-add\n\tclient-remove\n\nRun "tsuru help cliente" for details.'))
    assert not match(Command('tsuru cliente', 'tsuru: "cliente" is not a tsuru command. See "tsuru help".\n'))


# Generated at 2022-06-14 11:01:17.719679
# Unit test for function match
def test_match():
    match_output = ('tsuru: "target-add" is not a tsuru command. See "tsuru help".\n'
                    '\nDid you mean?\n'
                    '\ttarget-add\n')
    assert match(Command('tsuru target-add', match_output))



# Generated at 2022-06-14 11:01:23.567427
# Unit test for function get_new_command
def test_get_new_command():
    command = type('command', (object,), {
        'output': ('tsuru: "plataform-add" is not a tsuru command. See "tsuru '
                   'help".\n\nDid you mean?\n\tplatform-add')
    })

    assert get_new_command(command) == 'tsuru platform-add'

# Generated at 2022-06-14 11:01:30.619349
# Unit test for function get_new_command
def test_get_new_command():
    from tests.commands import Command

    output = ("tsuru: \"abcd\" is not a tsuru command. See \"tsuru help\".\n"
              "\n"
              "Did you mean?\n"
              "\tabs\n"
              "\tabsence\n")

    assert get_new_command(Command("tsuru abcd", output="abc")) is None
    assert get_new_command(Command("tsuru abcd", output=output)) == "tsuru abs"

# Generated at 2022-06-14 11:01:38.090465
# Unit test for function match
def test_match():
    assert match(Command('tsuru app-delete', 'tsuru: "app-delete" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tapp-remove\n')) == True
    assert match(Command('tsuru app-remove', 'tsuru: "app-remove" is not a tsuru command. See "tsuru help".\n')) == False


# Generated at 2022-06-14 11:01:48.263962
# Unit test for function match
def test_match():
    assert match(Command('tsru target-add tsuru.io', 'tsuru: "tsru" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\ttarget-add\n'))
    assert not match(Command('tsuru target-add tsuru.io', ''))
    assert not match(Command('tsuru target-add tsuru.io', 'tsuru: "tsuru" is not a tsuru command. See "tsuru help".\n'))
    assert not match(Command('tsuru target-add tsuru.io', 'tsuru: "tsuru" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\t'))


# Generated at 2022-06-14 11:01:50.533501
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('tsuru app-info dokku/test', '')
    assert get_new_command(command) == 'tsuru app-info test'

# Generated at 2022-06-14 11:01:55.181478
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('tsuru deploy', '''tsuru: "deploy" is not a tsuru command. See "tsuru help".

Did you mean?
        deploy-app

''')
    assert get_new_command(command) == 'tsuru deploy-app'



# Generated at 2022-06-14 11:02:01.627490
# Unit test for function match
def test_match():
    # test for the messsage
    assert match(Command('tsuru app-list', 'tsuru: "app-list" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-create'))
    assert not match(Command('tsuru app-create', 'tsuru: "app-create" is not a tsuru command'))



# Generated at 2022-06-14 11:02:07.297340
# Unit test for function get_new_command
def test_get_new_command():
	message = "tsuru: \"bootsrap\" is not a tsuru command. See \"tsuru help\"."+"\n"+"Did you mean?\n\tbootstrap\n"
	assert get_new_command(Command('tsuru bootsrap',message)) == 'tsuru bootstrap'

# Generated at 2022-06-14 11:02:19.729070
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('tsuru app-info asdf', '')
    assert get_new_command(command) == 'tsuru app-info asdf'

# Generated at 2022-06-14 11:02:29.020854
# Unit test for function match
def test_match():
    assert match(Command("tsuru abc",
                         "tsuru: \"abc\" is not a tsuru command. "
                         "See \"tsuru help\".\n\n"
                         "Did you mean?\n\t'abcde'\n\t'abcd'\n\t'abcds'\n"))


# Generated at 2022-06-14 11:02:33.492507
# Unit test for function match
def test_match():
    assert match(Command("tsuru rck", "tsuru: \"rck\" is not a tsuru command. See \"tsuru help\"", ""))
    assert match(Command("tsuru create-app", "tsuru: \"create-app\" is not a tsuru command. See \"tsuru help\"", ""))


# Generated at 2022-06-14 11:02:40.002792
# Unit test for function get_new_command
def test_get_new_command():
    output = 'tsuru: "teast" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tteam\n\tteams\n\tdelete-team\n\tadd-user-to-team'
    command_output = Command('tsuru teast', output)

    assert get_new_command(command_output).script == 'tsuru team'

enabled_by_default = True

# Generated at 2022-06-14 11:02:45.289440
# Unit test for function match
def test_match():
    check_output = u"tsuru: \"deploy\" is not a tsuru command. See \"tsuru help\".\n\nDid you mean?\n\tdeploy-app\n\tdeploy-quota"
    assert match(Command('tsuru deploy', check_output))


# Generated at 2022-06-14 11:02:51.078327
# Unit test for function match
def test_match():
    command = Command('tsuru app-list', '')
    assert match(command)
    command = Command('tsuru app-list', 'tsuru: "app-list" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tlist-apps\n\n')
    assert match(command)



# Generated at 2022-06-14 11:03:04.090941
# Unit test for function match

# Generated at 2022-06-14 11:03:06.356321
# Unit test for function match
def test_match():
    assert match(Command('tsuru target-list', 'tsuru: "target-list" is not a tsuru command. See "tsuru help".\nDid you mean?\n\ttarget-add\n\ttarget-remove'))
    assert not match(Command('tsuru target-add', ''))


# Generated at 2022-06-14 11:03:14.153781
# Unit test for function get_new_command
def test_get_new_command():
    output = '''tsuru: "we" is not a tsuru command. See "tsuru help".

Did you mean?
	webhook-add
	webhook-list
	webhook-remove
	webhook-update
'''
    commands = get_all_matched_commands(output)
    assert get_new_command(Command('webhook-add', output)) == 'webhook-add'
    assert get_new_command(Command('webhook-list', output)) == 'webhook-list'
    assert get_new_command(Command('webhook-remove', output)) == 'webhook-remove'
    assert get_new_command(Command('webhook-update', output)) == 'webhook-update'

# Generated at 2022-06-14 11:03:20.938181
# Unit test for function get_new_command
def test_get_new_command():
    output = """tsuru: "app-change-ip" is not a tsuru command. See "tsuru help".

Did you mean?
	app-change-quota
	app-create
	app-info"""
    command = Command('tsuru app-change-ip app-name', output)
    assert get_new_command(command) == 'tsuru app-change-quota app-name'

# Generated at 2022-06-14 11:03:50.938149
# Unit test for function match
def test_match():
    assert match(Command(script='tsuru do', stderr='tsuru: "do" is not a tsuru command. See "tsuru help".\nDid you mean?\ntsd',))
    assert match(Command(script='tsuru do', stderr='tsuru: "do" is not a tsuru command. See "tsuru help".\nDid you mean?\n\ttarget',))
    assert not match(Command(script='tsuru do', stderr='tsuru: "do" is not a tsuru command. See "tsuru help".',))


# Generated at 2022-06-14 11:03:55.244134
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('tsuru target-list', 'tsuru: "target-list" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tlist-targets', None)) == 'tsuru list-targets'

# Generated at 2022-06-14 11:04:02.155329
# Unit test for function get_new_command
def test_get_new_command():
    from tests.utils import Command

    # Command: tsuru deploy --app appname teste.tar.gz
    # Output: "tsuru deploy" is not a tsuru command. See "tsuru help".
    # Did you mean?
    # 	tsuru push
    # 	tsuru rollback
    filtered_output = '''"tsuru deploy" is not a tsuru command. See "tsuru help".'''
    filtered_output += '''\nDid you mean?\n\ttsuru push\n\ttsuru rollback'''
    assert get_new_command(Command('tsuru deploy --app appname teste.tar.gz',
                                   filtered_output)) == 'tsuru push --app appname teste.tar.gz'


# Generated at 2022-06-14 11:04:12.081231
# Unit test for function match
def test_match():
    assert match(Command(script="tsuru do-something",
                                 stderr='tsuru: "do-something" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tdo',
                                 side_effect=None))
    assert match(Command(script="tsuru do-something",
                                 stderr='tsuru: "do-something" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tdo\n\tdo-something',
                                 side_effect=None))
    assert not match(Command(script="tsuru do-something",
                                 stderr='tsuru: "do-something" is not a tsuru command. See "tsuru help".',
                                 side_effect=None))

# Generated at 2022-06-14 11:04:17.561005
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('tsuru app-info -a appname',
                'tsuru: "app-info" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-info\n\t')) == 'tsuru app-info -a appname'

# Generated at 2022-06-14 11:04:31.911061
# Unit test for function match
def test_match():
    """
    Check if the function match work properly
    """
    output = "tsuru: \"team-add\" is not a tsuru command. See \"tsuru help\"."
    output += "\n\nDid you mean?\n\tteam-create\n"
    command = Command(script=output, stdout=output)
    assert match(command)
    assert get_all_matched_commands(command.output) == ["team-create"]



# Generated at 2022-06-14 11:04:37.475729
# Unit test for function get_new_command
def test_get_new_command():
    new_cmd = get_new_command('tsuru: "asdfg" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-add\n\tapp-remove\n\tapp-info')
    assert new_cmd == 'tsuru app-add'

# Generated at 2022-06-14 11:04:42.710772
# Unit test for function match
def test_match():
    assert ('tsuru: "abc" is not a tsuru command. See "tsuru help".\n'
            in match('tsuru: "abc" is not a tsuru command. See "tsuru help".\n'
                     'Did you mean?\n'
                     '  ab abc\n'
                     '  ac acb\n'))
    assert match('not a command') is None

# Generated at 2022-06-14 11:04:48.080867
# Unit test for function match
def test_match():
    assert match(Command('tsuru app-info', "tsuru: \"app-info\" is not a tsuru command. See \"tsuru help\".\n\nDid you mean?\n\tapp-info"))
    assert not match(Command('tsuru app-info', "tsuru app-info"))


# Generated at 2022-06-14 11:04:50.075941
# Unit test for function match
def test_match():
    for command in commands:
        assert match(command) == is_valid(command)


# Generated at 2022-06-14 11:05:45.346549
# Unit test for function match
def test_match():
    output = 'tsuru: "foo" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tfoo-bar\n'
    assert match(Command('tsuru foo',
                         '', output=output))

    output = 'tsuru: "foo" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tfoo-bar\n\tfoo-baz\n'
    assert match(Command('tsuru foo',
                         '', output=output))

    output = 'tsuru: "foo-bar" is not a tsuru command. See "tsuru help".\n'
    assert not match(Command('tsuru foo-bar',
                             '', output=output))



# Generated at 2022-06-14 11:05:48.375977
# Unit test for function match
def test_match():
    assert match(Command('tsuru app-create asdfasdf', 'tsuru: "app-create" is not a tsuru command. See "tsuru help".\n\nerror: command not found: app-create\n\nDid you mean?\n\tapp-remove'))


# Generated at 2022-06-14 11:05:53.091622
# Unit test for function match
def test_match():
    commands = ['tsuru aaa']
    suggestions = ['tsuru app-create']
    sugg = [s.script for s in match(commands, suggestions)]
    assert sugg == ['tsuru app-create']



# Generated at 2022-06-14 11:06:01.074135
# Unit test for function match
def test_match():
    assert(match(Command('tsuru app-list',
       '''tsuru: "app-list" is not a tsuru command. See "tsuru help".
Did you mean?
	app-create
	app-info
	app-log
	app-remove
	app-restart
	app-start''', 1)))
    assert not match(Command('tsuru app-list',
       '''tsuru: "app-list" is not a tsuru command. See "tsuru help".''', 1))


# Generated at 2022-06-14 11:06:04.680927
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('tsurur list-apps',
                      "tsuru: \"list-apps\" is not a tsuru command. See \"tsuru help\".\n\nDid you mean?\n\tlist-units",
                      '',0)
    assert get_new_command(command) == 'tsuru list-units'

# Generated at 2022-06-14 11:06:15.949545
# Unit test for function match
def test_match():
    assert match(Command('tsuru client rollback', 'tsuru: "client" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tcluster\n\tclusters\n\tcloud\n\ttarget\n')) == True
    assert match(Command('tsuru client rollback', 'tsuru: "client" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tcloud\n')) == False
    assert match(Command('tsuru client rollback', 'tsuru: "client" is not a tsuru command. See "tsuru help".\n\n')) == False


# Generated at 2022-06-14 11:06:25.240504
# Unit test for function get_new_command
def test_get_new_command():
    command_check_targets = Command('tsuru check-targets', 'Everything is ok!')
    assert get_new_command(command_check_targets) == 'tsuru check-target'

    command_node_add = Command('tsuru node-add', 'Everything is ok!')
    assert get_new_command(command_node_add) == 'tsuru node-add --register'

    command_node_remove = Command('tsuru node-remove', 'Everything is ok!')
    assert get_new_command(command_node_remove) == 'tsuru node-remove --deregister'

# Generated at 2022-06-14 11:06:32.494571
# Unit test for function match
def test_match():
    assert match(Command('tsuru app-list sd', 'tsuru: "sd" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-list'))
    assert match(Command('tsuru app-info sd', 'tsuru: "sd" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-info'))
    assert not match(Command('foo bar', 'tsuru: "tsuru" is not a tsuru command. See "tsuru help".\n'))


# Generated at 2022-06-14 11:06:37.340825
# Unit test for function match
def test_match():
    assert match(Command('tsuru target-list', '''tsuru: "target-list" is not a tsuru command. See "tsuru help".

Did you mean?
	target-add'''))
    assert not match(Command('tsuru target-list', '''tsuru: "target-list" is not a tsuru command. See "tsuru help".

Did you mean?
	target-add'''))
    assert not match(Command('cd tsuru', '''tsuru: "target-list" is not a tsuru command. See "tsuru help".

Did you mean?
	target-add'''))


# Generated at 2022-06-14 11:06:44.187977
# Unit test for function match
def test_match():
  assert match(Command('tsuru app-list',
    "tsuru: \"app-list\" is not a tsuru command. See \"tsuru help\".\n\nDid you mean?\n\tapp-list"))

