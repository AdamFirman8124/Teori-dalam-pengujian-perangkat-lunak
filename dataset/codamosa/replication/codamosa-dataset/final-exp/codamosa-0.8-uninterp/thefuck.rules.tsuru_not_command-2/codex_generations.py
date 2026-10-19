

# Generated at 2022-06-14 10:57:32.800856
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    assert get_new_command(Command('tsuru permission-list',
                                   'tsuru: "permission-list" is not a tsuru command. See "tsuru help".\n\n'
                                   'Did you mean?\n\tpermission-set\n\tpermission-remove\n\tpermission-create',
                                   '')) == 'tsuru permission-set'

# Generated at 2022-06-14 10:57:41.588675
# Unit test for function match
def test_match():
    assert match(Command('tsuru caramba', 'tsuru: "caramba" is not a tsuru \
command. See "tsuru help".\n\nDid you mean?\n\tapp-run, app-log, app-info, \
app-grant, app-plan-change, app-revoke'))
    assert not match(Command('tsuru caramba', 'tsuru: "caramba" is not a \
tsuru command. See "tsuru help".'))


# Generated at 2022-06-14 10:57:47.754801
# Unit test for function match
def test_match():
    assert match(Command('tsuru help', 'tsuru: "help" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\thelp-app\n\thelp-unit'))
    assert not match(Command('tsuru help', 'tsuru: "help" is not a tsuru command'))


# Generated at 2022-06-14 10:57:52.864804
# Unit test for function match
def test_match():
    assert match(Command('tsrur do-something', 'tsrur: "do-something" is not a tsuru command. See "tsru help".\n\nDid you mean?\n\tdo-something-else\n'))
    assert not match(Command('echo hello', ''))

# Generated at 2022-06-14 10:57:58.961825
# Unit test for function match
def test_match():
    assert not match(Command('tsuru app-create'))
    assert match(Command('tsuruu app-create', ''))
    assert match(Command('tsuruu app-create', 'tsuru: "tsuruu" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-create\n'))

# Generated at 2022-06-14 10:58:05.776629
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.tsuru_did_you_mean import get_new_command

    command = Command('tsuru permision-list',
                      'tsuru: "permision-list" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tpermission-list')
    assert get_new_command(command) == 'tsuru permission-list'

# Generated at 2022-06-14 10:58:08.668697
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('tsuru add-unit redis-server', '')) == 'tsuru app-add-unit redis-server'

# Generated at 2022-06-14 10:58:21.141629
# Unit test for function match
def test_match():
    assert match(Command('tsuru app-create tsuru-dashboard', 'tsuru: "tsuru-dashboard" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-create\n\tapp-info\n\tapp-list\n\tapp-remove\n\tapp-restart\n\tapp-start\n\tapp-stop\n\tapp-log'))
    assert match(Command('tsuru app-create tsuru-dashboard', '')) == False


# Generated at 2022-06-14 10:58:25.861730
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('tsuru someting',
                                  'tsuru: "someting" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tsomethin'))\
                                  == 'tsuru somethin'

# Generated at 2022-06-14 10:58:37.140643
# Unit test for function match
def test_match():
    assert match(Command('tsuru env-set -a asdf',
                         'tsuru: "env-set" is not a tsuru command. See "tsuru help".\n\n\tDid you mean?\n\t\tenv-get\tenv-unset\n'))
    assert not match(Command('tsuru env-set -a asdf', 'tsuru: "env-set" is not a tsuru command. See "tsuru help".\n'))
    assert not match(Command('tsuru env-set -a asdf', 'tsuru: "env-set" is not a tsuru command. See "tsuru help".\n\tDid you mean?\n'))
    

# Generated at 2022-06-14 10:58:44.283435
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('tsuru: "my-admin" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tadmin-list\n\tapp-grant\n') == "tsuru admin-list"

enabled_by_default = True

# Generated at 2022-06-14 10:58:54.657913
# Unit test for function get_new_command

# Generated at 2022-06-14 10:59:01.329282
# Unit test for function match
def test_match():
    broken_cmd1 = 'tsuru: "gola" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tgoal'
    broken_cmd2 = 'tsuru: "gola" is not a tsuru command. See "tsuru help"'
    assert match(Command('tsuru gola', broken_cmd1))
    assert not match(Command('tsuru gola', broken_cmd2))


# Generated at 2022-06-14 10:59:09.108293
# Unit test for function get_new_command
def test_get_new_command():
    command_output = ('tsuru: "test" is not a '
                      'tsuru command. See "tsuru help".\n\n'
                      'Did you mean?\n\t'
                      'target-add\n\ttarget-remove\n\t'
                      'target-set\n\ttarget-list')
    assert get_new_command(Command(script="tsuru",
                                   output=command_output)) == (
           'tsuru target-list')

# Generated at 2022-06-14 10:59:11.819615
# Unit test for function get_new_command
def test_get_new_command():
    command = tsuru_command('notasupercommand')
    assert get_new_command(command) == 'tsuru system-info'

# Generated at 2022-06-14 10:59:17.113226
# Unit test for function match
def test_match():
    from thefuck.types import Command

    output = '''tsuru: "myapp" is not a tsuru command. See "tsuru help".

Did you mean?
	target-list
	target-remove
	target-set
	team-create
	team-list
	team-remove
	team-rename
	team-user-add
	team-user-remove
	team-user-list
	token-add
	token-remove
	token-regenerate
	token-list
	user-create
	user-remove
	user-info
'''
    assert (match(Command('tsuru app-create myapp', output=output)) == True)



# Generated at 2022-06-14 10:59:21.223258
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('tsuru target-add foo bar'))
    assert get_new_command(Command('tsuru target-set foo bar'))
    assert get_new_command(Command('tsuru target-remove foo bar'))

# Generated at 2022-06-14 10:59:27.054930
# Unit test for function get_new_command
def test_get_new_command():
    output = u'''tsuru: "team-user" is not a tsuru command. See "tsuru help".

Did you mean?
	team-user-add
	team-user-remove'''

    assert get_new_command({'script': 'team-user', 'output': output}) == \
        'tsuru team-user-add team-user team-user'

# Generated at 2022-06-14 10:59:32.066465
# Unit test for function match
def test_match():
    output = 'tsuru: "login" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tlog-in\n\tsignin\n'
    assert match(Command('tsuru login', output))


# Generated at 2022-06-14 10:59:34.478882
# Unit test for function match
def test_match():
    assert match(Command('tsru target-list', ''))
    assert not match(Command('ls', ''))


# Generated at 2022-06-14 10:59:42.603142
# Unit test for function match
def test_match():
    broken_command = Command('tsuru givermigivemee', 'tsuru: "givermigivemee" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tgivermigiveme')
    assert match(broken_command)
    assert not match(Command('tsuru app-create', ''))


# Generated at 2022-06-14 10:59:52.614161
# Unit test for function match
def test_match():
    assert match(Command('tsuru target-list',
                                 'tsuru: "target-list" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\t' +
                                 'target-add\n\ttarget-remove\n\ttarget-set\n')
                         )
    assert  match(Command('tsuru target-list',
                          'tsuru: "target-list" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n' +
                            '\t' + 'target-add\n\ttarget-remove\n\ttarget-set\n'))


# Generated at 2022-06-14 11:00:01.069813
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.tsuru_did_you_mean import get_new_command

    output = 'tsuru: "command" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n	deploy'
    command = type('Command', (object,), {
        'script': 'tsuru command app',
        'output': output,
    })

    assert get_new_command(command) == 'tsuru deploy app'



# Generated at 2022-06-14 11:00:10.455895
# Unit test for function get_new_command
def test_get_new_command():
    # TODO: This test must use a mocked command
    output = 'tsuru: "app-create" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tapp-create\t\tCreate an app in tsuru\n\tapp-list\t\tList apps in tsuru'
    command = type('obj', (object,), {'output': output})()
    assert "app-create" == get_new_command(command)

# Generated at 2022-06-14 11:00:16.647468
# Unit test for function match
def test_match():
    command = "tsuru: \"myapp\" is not a tsuru command. See \"tsuru help\"." \
              "\n\nDid you mean?" \
              "\n\tapp-create\n\tapp-remove"
    assert not match(Command(script='tsuru app-register myapp',
                             output=command))
    assert match(Command(script='tsuru app-regisiter myapp',
                        output=command))



# Generated at 2022-06-14 11:00:27.444456
# Unit test for function match
def test_match():
    assert match(Command('tsuru token-add teste',
                 'tsuru: "token-add" is not a tsuru command. See "tsuru help".\ntsuru: Did you mean?\ntsuru token-add'))
    assert not match(Command('tsuru token-add teste',
                 'tsuru: "token-add" is not a tsuru command.'))
    assert not match(Command('tsuru token-add teste', 'command not found'))


# Generated at 2022-06-14 11:00:37.458877
# Unit test for function match
def test_match():
    message = 'tsuru: "platforms" is not a tsuru command. See "tsuru help".\n\nDid y\
ou mean?\n\tplatform-add\n\tplatfomr-remove\n\tplatform-list\n\t'
    assert match(Command('tsuru platforms', message, ''))

    message = 'tsuru: "pltorms" is not a tsuru command. See "tsuru help".\n\nDid y\
ou mean?\n\tplatform-add\n\tplatfomr-remove\n\tplatform-list\n\t'
    assert not match(Command('tsuru pltorms', message, ''))


# Generated at 2022-06-14 11:00:48.108080
# Unit test for function match
def test_match():
    command = Command(script='tsuru app-run',
                     stdout='tsuru: "app-run" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-start')
    assert match(command) is True

    command = Command(script='tsuru app-run',
                     stdout='tsuru: "app-run" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-start')
    assert match(command) is True

    command = Command(script='tsuru app-run',
                     stdout='tsuru: "app-run" is not a tsuru command. See "tsuru help".')
    assert match(command) is False


# Generated at 2022-06-14 11:00:53.819128
# Unit test for function match
def test_match():
    output_failed_command = "tsuru: \"create\" is not a tsuru command. See \"tsuru help\".\n\nDid you mean?\n\tadd-unit\n\tadd-key\n\tapp-create"
    command = Command("tsuru create", output_failed_command)

    assert(match(command))



# Generated at 2022-06-14 11:00:58.724228
# Unit test for function match
def test_match():
    assert match(Command('tsuru app-list foo',
        'tsuru: "app-list" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-list\n\tservice-list'))
    assert not match(Command('tsuru app-list', ''))


# Generated at 2022-06-14 11:01:13.469435
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('tsuru cookify')) == 'tsuru cookbook-add'
    assert get_new_command(Command('tsurun cookify')) == 'tsuru cookbook-add'
    assert get_new_command(Command('tsurun cookifyi')) == 'tsuru cookbook-add'
    assert get_new_command(Command('tsuru cookifi')) == 'tsuru cookbook-add'
    assert get_new_command(Command('tsurun cookifi')) == 'tsuru cookbook-add'
    assert get_new_command(Command('tsurun cookifo')) == 'tsuru cookbook-add'
    assert get_new_command(Command('tsurun cookif')) == 'tsuru cookbook-add'

# Generated at 2022-06-14 11:01:20.055002
# Unit test for function match
def test_match():
    assert match(Command('tsuru target', 'tsuru: "target" is not a tsuru command. See "tsuru help".\nDid you mean?\n\ttarget-remove\n\tapp-restart'))
    assert not match(Command('tsuru target', 'tsuru: "target" is not a tsuru command. See "tsuru help".'))


# Generated at 2022-06-14 11:01:22.712727
# Unit test for function match
def test_match():
	assert match('tsuru: "a" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-run\n')


# Generated at 2022-06-14 11:01:31.407164
# Unit test for function get_new_command
def test_get_new_command():
    # Case 1
    result = get_new_command(Command('tsu a',
                                     'Error: "tsu" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tapp-add'))
    assert result == 'tsuru app-add'

    # Case 2
    result = get_new_command(Command('tsu a',
                                     'Error: "tsu" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tapp-add\n\tapp-add-cname'))
    assert result == 'tsuru app-add'

# Generated at 2022-06-14 11:01:37.680078
# Unit test for function get_new_command
def test_get_new_command():
    command = type('fake_command', (), {'output': """tsuru: "bootstrap" is not a 
        tsuru command. See "tsuru help".
    
    Did you mean?
        target-add
        target-remove"""})
    assert get_new_command(command) == 'tsuru target-add'


# Generated at 2022-06-14 11:01:48.288551
# Unit test for function get_new_command

# Generated at 2022-06-14 11:01:53.482894
# Unit test for function match
def test_match():
    assert match(Command('tsuru delet -a myapp', 'tsuru: "delet" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tdelete\n'))
    assert not match(Command('tsuru delete', ''))
    assert not match(Command('ls', ''))


# Generated at 2022-06-14 11:01:59.725862
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('tsuru cron-update --service test-service', 'tsuru: "cron-update" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tcron-get\n\tcron-remove\n\tcron-set')) == 'tsuru cron-set --service test-service'

# Generated at 2022-06-14 11:02:03.758144
# Unit test for function match
def test_match():
    assert match(Command('tsuru add-key alexandre.piveteau@corp.globo.com -f ~/.ssh/id_rsa.pub',
                         'tsuru: "add-key" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tadd-key'))


# Generated at 2022-06-14 11:02:07.073983
# Unit test for function match
def test_match():
    assert match(Command('tsuru servicelist', 'tsuru: "servicelist" is not a tsuru command. See "tsuru help".\n'
                                              '\n'
                                              'Did you mean?\n'
                                              '\tservice-list'))



# Generated at 2022-06-14 11:02:16.417879
# Unit test for function match
def test_match():
    assert match(Command('tsuru sdsdd', ''))
    assert not match(Command('tsuru', ''))
    assert not match(Command('tsuru', 'Did not find any command'))


# Generated at 2022-06-14 11:02:23.828057
# Unit test for function match
def test_match():
    output = "tsuru: \"abc\" is not a tsuru command. See \"tsuru help\""
    output2 = "tsuru: \"abc\" is not a tsuru command. See \"tsuru help\"\nDid you mean?\n\tadd\n\tapp-change-units\n\tapp-create\n\tapp-remove\n\tapp-restart\n\tapp-run"
    output3 = "tsuru: \"abc\" is not a tsuru command. See \"tsuru help\"\nDid you mean?\n\tadd\n\tapp-change-units\n\tapp-create\n\tapp-remove\n\tapp-restart\n\tapp-run\n\tuser-create"
    assert match(Command('tsuru abc', output))


# Generated at 2022-06-14 11:02:30.770960
# Unit test for function match
def test_match():
    assert match(Command('tsuru'))
    assert match(Command('tsuru is not a tsuru command. See "tsuru help".'))
    assert not match(Command('tsuru app-list', 'tsuru app-list'))


# Generated at 2022-06-14 11:02:35.929773
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('tsuru app-list', 'tsuru: "app-list" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tapp-list\n\tapps-list')) == 'tsuru app-list'

# Generated at 2022-06-14 11:02:41.449321
# Unit test for function match
def test_match():
    assert match(Command("tsuru help app-list",
                         '"app-list" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-list\n\n'))
    assert not match(Command("tsuru help app-list", 'tsuru help: "app-list" is not a help topic. See "tsuru help".\n\n'))


# Generated at 2022-06-14 11:02:45.409727
# Unit test for function match
def test_match():
    assert match(Command('tsury mi', ''))
    assert not match(Command('tsuru mi', ''))
    assert not match(Command('tsuru mi', 'Error'))


# Generated at 2022-06-14 11:02:52.491095
# Unit test for function get_new_command
def test_get_new_command():
    # assert(get_new_command('tsuru hello\ntsuru: "hello" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\thelp\n') == 'tsuru help')
    assert(get_new_command('tsuru hello\ntsuru: "hello" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\thelp\n') == 'tsuru help')

# Generated at 2022-06-14 11:03:00.602675
# Unit test for function get_new_command
def test_get_new_command():
    broken_command = Command('tsuru app-list',
                             'tsuru: "app-list" is not a tsuru command. See "tsuru help". \nDid you mean?\n\tapp-create\n\tapp-remove\n\tapp-list-units\n')
    assert (get_new_command(broken_command) ==
            u'\x1b[0mtsuru\x1b[0m \x1b[32mapp-create\x1b[0m')

# Generated at 2022-06-14 11:03:11.185717
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('tsuru foo', 'tsuru: "foo" is not a tsuru command.')
    assert get_new_command(command) == 'tsuru foo-bar'

    command = Command('tsuru foo', 'tsuru: "foo" is not a tsuru command.\n'
                                   'Did you mean?\n\t'
                                   'foo-bar\n\tfoo-github-key\n')
    assert get_new_command(command) == 'tsuru foo-bar'

    assert not match(Command('tsuru foo', 'tsuru: invalid command: foo'))
    assert not match(Command('tsuru foo', 'Did you mean?\n\tfoo-bar\n\t'))

# Generated at 2022-06-14 11:03:16.080501
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('tsuru aaplication-log',
                                   "tsuru: \"aaplication-log\" is not a tsuru command. See \"tsuru help\".\nDid you mean?\n\tapplication-log")) == 'tsuru application-log'

# Generated at 2022-06-14 11:03:33.358636
# Unit test for function match
def test_match():
    cmd = 'test: "abcdefg" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\ttest\n\trest\n\n'
    output = Command('test', cmd)
    assert match(output)


# Generated at 2022-06-14 11:03:40.169979
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('tsuru a', 'tsuru: "a" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp\n\ttarget')
    assert get_new_command(command) == 'tsuru target'
    command = Command('tsuru', 'Did you mean\n\tapp')
    assert get_new_command(command) == 'tsuru app'

# Generated at 2022-06-14 11:03:47.922875
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("tsuru: \"apps\" is not a tsuru command. See \"tsuru help\".\n\nDid you mean?\n    add-key\n    app-info\n    app-remove\n    app-list") == 'tsuru app-info'

# Generated at 2022-06-14 11:03:53.534519
# Unit test for function get_new_command
def test_get_new_command():
    output = "tsuru: \"env-set\" is not a tsuru command. See \"tsuru help\".\n\n\tDid you mean?\n\t\tenv-get"
    command = type('obj', (object,), {'output': output})

    new_command = get_new_command(command)
    assert 'env-get' in new_command

# Generated at 2022-06-14 11:03:58.755889
# Unit test for function match
def test_match():
    assert match(Command('tsuru app-list', 'tsuru: "app-lis" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-list'))
    assert not match(Command('tsuru app-list', 'tsuru: "app-lis" is not a tsuru command.'))


# Generated at 2022-06-14 11:04:01.344493
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('tsuru node-list tsuru', '', '', '')) == "tsuru node-list"


# Generated at 2022-06-14 11:04:10.894432
# Unit test for function match
def test_match():
    assert match(Command('tsuru app-lis', 
                         'tsuru: "app-lis" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-list\n'))
    assert match(Command('tsuru appsssss', 
                         'tsuru: "appsssss" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapps\n'))
    assert not match(Command('tsuruuuu', 
                             'tsuru: "tsuruuuu" is not a tsuru command. See "tsuru help".'))


# Generated at 2022-06-14 11:04:19.315830
# Unit test for function match
def test_match():
    text1 = "tsuru: \"docker\" is not a tsuru command. See \"tsuru help\".\n\nDid you mean?\n\tdocker-get\n\tdocker-run"
    text2 = "tsuru: \"xyz\" is not a tsuru permission. See \"tsuru help permission\"."
    command1 = Command("docker", text1)
    command2 = Command("xyz", text2)
    assert not match(command1)
    assert not match(command2)


# Generated at 2022-06-14 11:04:32.269509
# Unit test for function match
def test_match():
    assert match(Command('tsaru help', 'tsaru: "tsaru" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapps\n\tauthorize\n\t'))
    assert not match(Command('tsuru help', 'tsuru: "tsuru" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapps\n\tauthorize\n\t'))

# Generated at 2022-06-14 11:04:38.948758
# Unit test for function match
def test_match():
    assert match(Command('tsuru app-create', 'tsuru: "app-create" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-create\n\tapp-del\n\tapp-list\n\tapp-remove\n'))
    assert not match(Command('tsuru app-create', 'tsuru app-create'))


# Generated at 2022-06-14 11:05:09.627597
# Unit test for function get_new_command
def test_get_new_command():
    output = """tsuru: "tsur" is not a tsuru command. See "tsuru help".

Did you mean?
	tsuru

See "tsuru help --help" for more information about a command."""
    test_command = Command('tsur', output=output)
    assert get_new_command(test_command) == "tsuru"

# Generated at 2022-06-14 11:05:17.410076
# Unit test for function match
def test_match():
    assert match(Command('tsuru blah blah blah', 'tsuru: "blah" is not a tsuru command.\nDid you mean?\n\tbuild-node\n\tpermission-list\n\tkey-add'))

    assert not match(Command('tsuru blah blah blah', 'command not found: tsuru'))
    assert not match(Command('tsuru blah blah blah', 'tsuru: "blah" is not a tsuru command.\nDid you mean?\n\tbuild-node\n\tpermission-list\n\tkey-add\n'))
    assert not match(Command('tsuru blah blah blah', 'tsuru: "blah" is not a tsuru command. See "tsuru help".'))



# Generated at 2022-06-14 11:05:20.905529
# Unit test for function match
def test_match():
    assert match(Command('tsuru app-log -app app', 'tsuru: "app-log" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tlog-app'))
    assert not match(Command('hello', 'tsuru: "app-log" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tlog-app'))


# Generated at 2022-06-14 11:05:29.572793
# Unit test for function match
def test_match():
    assert match(Command('tsuru app-row', 'tsuru: "app-row" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-run\n\tapp-log\n\tapp-list\n\tapp-create\n\tapp-info\n\tapp-deploy\n\tapp-remove\n\tapp-info'))
    assert not match(Command('tsuru app-row', 'tsuru: "app-row" is not a tsuru command. See "tsuru help".'))
    assert match(Command('tsuru app-row', 'tsuru: "app-row" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tapp-run'))

# Generated at 2022-06-14 11:05:30.066295
# Unit test for function match

# Generated at 2022-06-14 11:05:38.190094
# Unit test for function match
def test_match():
    assert match(Command('tsuru app-create', 'tsuru: "app-create" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-create\n'))
    assert not match(Command('tsuru app-deploy', 'tsuru: "app-deploy" is not a tsuru command. See "tsuru help".'))


# Generated at 2022-06-14 11:05:42.784234
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    assert get_new_command(Command('tsuru test', 'tsuru: "test" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\ttarget-list', '')) == 'tsuru target-list'

# Generated at 2022-06-14 11:05:48.214766
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

    command = Command(script='tsuru unit-add', stderr='tsuru: "unit-add" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tunit-add',
                      stdout='',
                      command='tsuru unit-add')
    assert get_new_command(command) == 'tsuru unit-add'

# Generated at 2022-06-14 11:05:52.919959
# Unit test for function match
def test_match():
    output='tsuru: "is" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tinfo'
    command = Command('tsuru is', output)
    assert match(command)



# Generated at 2022-06-14 11:05:57.344080
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('tsuru', 'tsuru: "a" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp\n\tapp-add\n\tapp-list')) == 'tsuru app'

# Generated at 2022-06-14 11:06:52.040789
# Unit test for function get_new_command
def test_get_new_command():
    def _test(old_text, new_text):
        old_cmd = Command('tsuru ' + old_text, '')
        new_cmd = get_new_command(old_cmd)
        assert new_cmd == 'tsuru ' + new_text

    _test('tsuru version', 'version')
    _test('target-set', 'target-add')
    _test('target-remove', 'target-add')

# Generated at 2022-06-14 11:07:01.828605
# Unit test for function match
def test_match():
    output = """tsuru: "login" is not a tsuru command. See "tsuru help".

Did you mean?
        logout
        app-add
        app-remove
        app-run"""

    assert(match(Command("tsuru login", "", output)) == True)

    output = """tsuru: "app-add" is not a tsuru command. See "tsuru help".

Did you mean?
        logout
        app-remove
        app-run"""
    assert(match(Command("tsuru app-add", "", output)) == True)



# Generated at 2022-06-14 11:07:16.435937
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

    assert get_new_command(Command('tsuru app-info',
    'tsuru: "app-info" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-assign',
    1)) == 'tsuru app-assign'

    assert get_new_command(Command('tsuru app-ip',
    'tsuru: "app-ip" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-add-cname',
    1)) == 'tsuru app-add-cname'


# Generated at 2022-06-14 11:07:20.223916
# Unit test for function match
def test_match():
	assert match("tsuru app-create: 'app-create' is not a tsuru command. See 'tsuru help'."
			+ '\nDid you mean?\n\tapp-create')

# Generated at 2022-06-14 11:07:26.406660
# Unit test for function match
def test_match():
    assert match(Command('tsuru app-info', 'tsuru: "app-info" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-info, app-log, app-log-reset, app-run'))
    assert not match(Command('tsuru app-info', ''))
    assert not match(Command('tsuru app-info', 'tsuru: "app-info" is not a tsuru command. See "tsuru help".'))
