

# Generated at 2022-06-14 10:57:36.172129
# Unit test for function match
def test_match():
    assert match(Command('tsuru app-list', ''))
    assert not match(Command('tsuru app-list', 'my output'))


# Generated at 2022-06-14 10:57:40.341452
# Unit test for function match
def test_match():
    assert match(Command('tsurue', 'tsuru: "tsurue" is not a tsuru command. See "tsuru help".'))
    assert not match(Command('tsuru app-info', ''))



# Generated at 2022-06-14 10:57:53.231912
# Unit test for function match
def test_match():
  assert match(Command('tsuru help', 'tsuru: "tsuru help" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tlogin\n\tlogin-ssh\t\n\twhoami\t\n\tlogout\t\n\tversion\t\n\tconfig-get\n\tconfig-set\n')) == True
  assert match(Command('tsuru help', 'tsuru: "tsuru help" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tlogin')) == False
  assert match(Command('tsuru help', 'tsuru: "tsuru help" is not a tsuru command. See "tsuru help".')) == False

# Generated at 2022-06-14 10:57:59.292672
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.shells import Bash
    command = Command('tsuru help', 'tsuru: "help" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tlog\n\tlogin\n\ttarget-add', '', 0, Bash())
    assert get_new_command(command) == 'tsuru log'



# Generated at 2022-06-14 10:58:07.735677
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('tsuru target-add tsuru-production http://tsuru.io',
                      'tsuru: "target-add" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\ttarget-add \n\ttarget-remove\n\ttarget-set\n\ttarget-get\n\ttarget-list')
    assert get_new_command(command) == 'tsuru target-set tsuru-production http://tsuru.io'

# Generated at 2022-06-14 10:58:22.598873
# Unit test for function match
def test_match():
    output = ['tsuru: "im" is not a tsuru command. See "tsuru help"',
      '\nDid you mean?',
      '\tinfo',
      '\twm',
      '',
      '\t[Please press enter to continue]']
    assert match(Command('tsuru im 1', '', output))

    output = ['tsuru: "im" is not a tsuru command. See "tsuru help"',
      '\nDid you mean?',
      '\tinfo',
      '\twm',
      '',
      '\t[Please press enter to continue]',
      '\tThis is a test.',
      '\tThis is a test.']
    assert match(Command('tsuru im 1', '', output))


# Generated at 2022-06-14 10:58:28.453489
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('tsuru app-delelte app1',
                                   stderr='tsuru: "app-delelte" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tapp-delete\n\tapp-deploy\n\tapp-remove')) == 'tsuru app-delete app1'

# Generated at 2022-06-14 10:58:33.063656
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('tsuru s', 'tsuru: "s" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tstop')) == 'tsuru stop'

# Generated at 2022-06-14 10:58:41.848026
# Unit test for function match
def test_match():
    output = ("Woops, it appears that the command you are trying to run\n"
              "tsuru: \"some command\" is not a tsuru command. See "
              "\"tsuru help\".\n\n"
              "Did you mean?\n\tcommands\n\tversion\n\thelp\n")
    assert match(Command('some command', output))
    assert not match(Command('some command', "some command is not a tsuru command"))
    assert match(Command('some command',
                         ("tsuru: \"some command\" is not a tsuru command."
                          " See \"tsuru help\"")))


# Generated at 2022-06-14 10:58:44.767969
# Unit test for function get_new_command
def test_get_new_command():
    assert(get_new_command(Command('tsuru word',
                                   r"""tsuru: "word" is not a tsuru command. See "tsuru help".

Did you mean?
	web-word""", '')) == 'tsuru web-word')

# Generated at 2022-06-14 10:58:54.760334
# Unit test for function match
def test_match():
    assert match(Command('tsuru stop', 'tsuru: "stop" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tstop'))
    assert not match(Command('tsuru stop', ''))


# Generated at 2022-06-14 10:59:03.262886
# Unit test for function match
def test_match():
    assert match(Command(script='', output='tsuru: "app-create" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tapp-create-t'))
    assert not match(Command(script='', output='tsuru: "app-create" is not a tsuru command. See "tsuru help".'))
    assert not match(Command(script='', output='tsuru version 1.8.0'))


# Generated at 2022-06-14 10:59:10.910625
# Unit test for function match
def test_match():
    output1 = 'tsuru: "target-set" is not a tsuru command. See "targe-set help".\n\nDid you mean?\n\t\ntarget-set'
    output2 = 'tsuru:"target-set" is not a tsuru command. See "targe-set help".\n\nDid you mean?\n\t\ntarget-set'
    output3 = 'tsuru: "target-set" is not a tsuru command. See "targe-set help".\n\nDid you mean?\n\t\ntarget-set\n\ttarget-get'

# Generated at 2022-06-14 10:59:16.939501
# Unit test for function match
def test_match():
    command = Command('tsuru ps:list webapp', 'tsuru: "ps:list" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapps-list\n\tservice-info\n')
    assert match(command)

    command = Command('tsuru ps:list webapp', 'tsuru: "ps:list" is not a tsuru command. See "tsuru help".\n')
    assert not match(command)


# Generated at 2022-06-14 10:59:24.441238
# Unit test for function match
def test_match():
    command1 = Command('tsuru list', 'tsuru: "list" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tlist-apps\n\tlist-keys')
    assert match(command1)
    command2 = Command('tsuru list', 'tsuru: "list" is not a tsuru command. See "tsuru help". Did you mean?')
    assert not match(command2)


# Generated at 2022-06-14 10:59:36.326623
# Unit test for function match
def test_match():
    output1 = "tsuru: \"tsuru user-create\" is not a tsuru command. See \"tsuru help\".\n\nDid you mean?\n\tuser-create"
    output2 = "tsuru: \"tsuru user-create one\" is not a tsuru command. See \"tsuru help\".\n\nDid you mean?\n\tuser-create"
    output3 = "tsuru: \"tsuru user-create one\" is not a tsuru command. See \"tsuru help\".\n\nDid you mean?\n\tuser-create"
    output4 = "tsuru: \"tsuru user-create one\" is not a tsuru command. See \"tsuru help\".\n\nDid you mean?\n\tuser-create"
    from tests.utils import Command



# Generated at 2022-06-14 10:59:43.251754
# Unit test for function match
def test_match():
    output = ("tsuru: \"app-list\" is not a tsuru command. See \"tsuru help\"."
    "\n\nDid you mean?\n\tapp-create\n\tapp-deploy\n\tapp-remove\n\tapp-run\n")
    command = Command("tsuru app-list", output)
    assert match(command)



# Generated at 2022-06-14 10:59:47.431285
# Unit test for function match
def test_match():
    assert(match(Command('tsuru client', 'tsuru: "client" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tlog-load\n\tlog')))


# Generated at 2022-06-14 10:59:53.044413
# Unit test for function get_new_command
def test_get_new_command():
    command = types.Command('tsuru app-plan-change myapp free',
                            'tsuru: "app-plan-change" is not a tsuru command. See "tsuru help".\n\n\nDid you mean?\n\n\tapp-change-plan',
                            '')
    assert get_new_command(command) == command.script.replace('app-plan-change', 'app-change-plan')

# Generated at 2022-06-14 11:00:04.360497
# Unit test for function match
def test_match():
    assert match(Command('tsuru app-info', output='tsuru: "app-info" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tapp-info\n\tapp-list\n\tapp-remove\n\tapp-run'))
    assert match(Command('tsuru doc', output='tsuru: "doc" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tdocs-add\n\tdocs-remove'))
    assert not match(Command('tsuru help', output='tsuru: "help" is not a tsuru command. See "tsuru help".'))

# Generated at 2022-06-14 11:00:14.231585
# Unit test for function match
def test_match():
    assert match(Command('tsuru target-add localhost:8080 test', 'tsuru: "target-add" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tadd-key\n\tadd-unit\n\tadd-user\n\tadd-cname\n\tadd-permission\n\tadd-pool'))


# Generated at 2022-06-14 11:00:16.683937
# Unit test for function match
def test_match():
    assert match(Command('tsuru target-add api.localhost', "tsuru: \"target-add\" is not a tsuru command. See \"tsuru help\"."))


# Generated at 2022-06-14 11:00:22.956868
# Unit test for function match
def test_match():
    assert match(Command('tsur', 'tsur is not a tsuru command. See "tsuru help". Did you mean? tsuru target-add'))
    assert not match(Command('tsuru target-list', ''))
    assert not match(Command('tsuru target-list', 'tsuru: "foo" is not a tsuru command. See "tsuru help". Did you mean? tsuru target-add'))



# Generated at 2022-06-14 11:00:36.770903
# Unit test for function match

# Generated at 2022-06-14 11:00:41.793380
# Unit test for function match
def test_match():
    assert match(Command('tsuru app-list', 'tsuru: "app-list" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-list\n'))
    assert not match(Command('tsuru app-list', 'tsuru: "app-list" is not a tsuru command. See "tsuru help".'))
    assert not match(Command('tsuru app-list', 'tsuru: "app-list" is not a tsuru command. See "tsuru help".\n\nI don\'t know what your are talking abou you.\n'))


# Generated at 2022-06-14 11:00:48.369631
# Unit test for function get_new_command
def test_get_new_command():
    output = ("tsuru: \"git\" is not a tsuru command. See \"tsuru help\".\n"
              "Did you mean?\n\tgit-receive-pack\n\tgit-upload-pack")
    assert get_new_command(Command('tsuru git', output)) == (
        'tsuru git-receive-pack\n'
        'tsuru git-upload-pack')

# Generated at 2022-06-14 11:00:59.368357
# Unit test for function match
def test_match():
    match_output1 = "tsuru: \"echo\" is not a tsuru command. See \"tsuru help\"."
    match_output2 = "tsuru: \"procurar\" is not a tsuru command. See \"tsuru help\"."
    match_output3 = "tsuru: \"procura\" is not a tsuru command. See \"tsuru help\"."
    match_output4 = "tsuru: \"procura\" is not a tsuru command. See \"tsuru help\"."
    assert match(Command(script=match_output1)) == True
    assert match(Command(script=match_output2)) == True
    assert match(Command(script=match_output3)) == True
    assert match(Command(script=match_output4)) == True


# Generated at 2022-06-14 11:01:04.993057
# Unit test for function get_new_command
def test_get_new_command():
    command = type("Command", (object,), {"output": "tsuru: \"tsuru app-list\" is not a tsuru command. See \"tsuru help\".\n\nDid you mean?\n\tapp-list"})
    assert get_new_command(command) == "tsuru app-list"

# Generated at 2022-06-14 11:01:11.669754
# Unit test for function match
def test_match():
    assert match(Command('tsuru aaabbbccc is not a tsuru command. See "tsuru help".', ''))
    assert not match(Command('tsuru app-info is not a tsuru command. See "tsuru help".', ''))
    assert not match(Command('tsuru app-info target is not a tsuru command. See "tsuru help".', ''))
    assert not match(Command('', ''))


# Generated at 2022-06-14 11:01:22.435908
# Unit test for function match
def test_match():
    assert match(Command('tsur app-list', 'tsuru: "app-list" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-list\n'))
    assert match(Command('tsur list-app', 'tsuru: "list-app" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-list\n\tapp-restart\n\tapp-run\n'))
    assert not match(Command('tsur help', 'tsuru: "help" is not a tsuru command. See "tsuru help".\n'))


# Generated at 2022-06-14 11:01:32.951260
# Unit test for function get_new_command
def test_get_new_command():
    output1 = "tsuru: \"app-info\" is not a tsuru command. See \"tsuru help\".\nDid you mean?\n\tapp-create\n\tapp-remove\n\tapp-list\n\tapp-restart\n\tapp-start\n\tapp-stop"
    output2 = "tsuru: \"appnfo\" is not a tsuru command. See \"tsuru help\".\nDid you mean?\n\tapp-create\n\tapp-remove\n\tapp-list\n\tapp-restart\n\tapp-start\n\tapp-stop"
    assert get_new_command(MagicMock(output=output1)) == 'tsuru app-create'

# Generated at 2022-06-14 11:01:37.106361
# Unit test for function get_new_command
def test_get_new_command():
    # Comparing Strings to check if the the new command returned is equal to the
    # command in the output of the command.output
    new_command= get_new_command(
        Command('tsuru environmen-set -a myapp KEY=VALUE',
                'tsuru: "environmen-set" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tenvironment-set\n\n')
    )
    assert new_command == 'tsuru environment-set -a myapp KEY=VALUE'

# Generated at 2022-06-14 11:01:42.475181
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('tsuru asdasd', '')) == ['tsuru service-add']
    assert get_new_command(Command('tsuru asdasd', '2')) == ['tsuru service-bind']
    assert get_new_command(Command('tsuru asdasd', '3')) == ['tsuru service-list']

# Generated at 2022-06-14 11:01:47.464570
# Unit test for function get_new_command
def test_get_new_command():
    output = 'tsuru: "node" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tnode-get\n\tnode-list\n\tnode-remove'
    command = Command('node', output)
    assert get_new_command(command) == 'tsuru node-get'

priority = 1000
enabled_by_default = True

# Generated at 2022-06-14 11:01:57.133895
# Unit test for function get_new_command
def test_get_new_command():
    command = type('', (), {'output':
                            'ERROR: tsuru: "test" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tcreate-app\n\tdelete-app\n\thelp\n\tlist-apps\n\tlist-units\n\tremove-unit\n\trun-unit-tests\n\tstart\n\tstop\n\tupdate-app\n\tversion\n\t'})()
    assert get_new_command(command) == 'tsuru create-app'

# Generated at 2022-06-14 11:02:05.743195
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('tsuruuuu add-key',
        'tsuru: "tsuruuuu" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tadd-key\n')) == 'tsuru add-key'
    assert get_new_command(Command('tsuru add-new-key',
        'tsuru: "add-new-key" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tadd-key\n')) == 'tsuru add-key'
    assert get_new_command(Command('tsuru key-add',
        'tsuru: "key-add" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tadd-key\n'))

# Generated at 2022-06-14 11:02:18.148522
# Unit test for function match
def test_match():
    assert match(Command('tsuru hello', 'tsuru: "hello" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tcreate-app\n\tget', ''))
    assert not match(Command('tsuru hello create', 'tsuru: "hello" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tcreate-app\n\tget', ''))
    assert not match(Command('tsuru hello', 'tsuru: hello\nUsage: tsuru [--app appname] command [args ...]\ntsuru: See "tsuru help" for more information about a command.', ''))


# Generated at 2022-06-14 11:02:21.204726
# Unit test for function match
def test_match():
    command = Command('tsuru app-create helloworld go',
                      'tsuru: "app-create" is not a tsuru command. See "tsuru help".\nDid you mean?\n\t\tapp-create')
    assert match(command)


# Generated at 2022-06-14 11:02:31.655582
# Unit test for function get_new_command
def test_get_new_command():
    cmd = Command('tsuru app-list',
                  'tsuru: "app-list" is not a tsuru command. See "tsuru help"'
                  '\n\nDid you mean?\n\tapp-create\n\tapp-run\n\tapp-deploy'
                  '\n\tapp-remove\n\tapp-restart\n\tapp-list')
    assert get_new_command(cmd) == 'tsuru app-list'

# Generated at 2022-06-14 11:02:38.419134
# Unit test for function get_new_command
def test_get_new_command():
    from tests.helper import Command

    test_command = "tsuru: \"my-team-create\" is not a tsuru command. See \"tsuru help\"."
    test_command += "\n\nDid you mean?\n\tmy-team-add"
    command = Command(script=test_command)
    assert get_new_command(command) == 'tsuru my-team-add'

# Generated at 2022-06-14 11:02:50.913438
# Unit test for function match
def test_match():
    command = Command("tsuru user-list admin", "tsuru: \"user-list\" is not a tsuru command. See \"tsuru help\".\n\nDid you mean?\n\tsuru user-list\n")
    assert match(command)
    command = Command("tsuru userlist admin", "tsuru: \"userlist\" is not a tsuru command. See \"tsuru help\".")
    assert not match(command)
    command = Command("tsuru userlist admin", "tsuru: \"userlist\" is not a tsuru command. See \"tsuru help\".\n\nThe most similar commands are:\n\tuser-list")
    assert not match(command)


# Generated at 2022-06-14 11:03:03.878709
# Unit test for function match

# Generated at 2022-06-14 11:03:08.004676
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('tsuru app-info blah', "tsuru: \"app-info\" is not a tsuru command. See \"tsuru help\".\n\nDid you mean?\n\tapp-info")) == 'tsuru app-info'
    assert get_new_command(Command('tsuru app-info blah', "tsuru: \"app-info\" is not a tsuru command. See \"tsuru help\".\n\nDid you mean?\n\tapp-info\nanother-app-info")) == 'tsuru app-info'

# Generated at 2022-06-14 11:03:11.728745
# Unit test for function get_new_command
def test_get_new_command():
    output = 'tsuru: "tsuru environment-set" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tenvironment-add\n'
    assert (get_new_command(Command('tsuru environment-set', output))) == 'tsuru environment-add'


# Generated at 2022-06-14 11:03:16.634131
# Unit test for function match
def test_match():
    assert match(Command('tsuru app-create myapp',
                         'tsuru: "app-create" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-create'))
    assert not match(Command('', ''))

# Generated at 2022-06-14 11:03:23.219454
# Unit test for function match
def test_match():
    assert match(Command("tsuru fads", "tsuru: \"fads\" is not a tsuru command. See \"tsuru help\"."))
    assert not match(Command("tsuru fads", "tsuru: \"fads\" is not a tsuru command."))
    assert not match(Command("fads tsuru", "tsuru: \"fads\" is not a tsuru command. See \"tsuru help\"."))


# Generated at 2022-06-14 11:03:32.150267
# Unit test for function get_new_command
def test_get_new_command():
    # Example output:
    #     tsuru command-not-found: "version" is not a tsuru command. See "tsuru
    #     help".
    #
    #     Did you mean?
    #         app-version
    #         target-list
    #         app-info
    formated_output = 'tsuru: "command-not-found" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-version\ntarget-list\napp-info'

    command = "tsuru command-not-found"
    assert get_new_command(Command(command, formated_output)) == "tsuru app-version"

# Generated at 2022-06-14 11:03:39.698677
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('tsuru target-add', 'tsuru: "target-add" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tlogin-target', '')) == 'tsuru login-target'
    assert get_new_command(Command('tsuru target-add', 'tsuru: "target-add" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tlogin-target\n\tlogin-target-add', '')) == 'tsuru login-target'

# Generated at 2022-06-14 11:03:48.222362
# Unit test for function match
def test_match():
    output = ["tsuru: \"mytsuru\" is not a tsuru command. See \"tsuru help\".",
              "",
              "Did you mean?",
              "\ttsuru",
              ""]
    output = '\n'.join(output)
    assert match(Command('tsuru mytsuru', output=output))



# Generated at 2022-06-14 11:03:53.361836
# Unit test for function match
def test_match():
    assert(match(Command('tsuru servic', 'tsuru: "servic" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tservice-add\n\tservice-doc\n\tservice-instance-add\n\tservices-list', ''))
)


# Generated at 2022-06-14 11:03:59.667823
# Unit test for function match
def test_match():
    assert match(Command("tsuru app-list",
                         'tsuru: "app-list" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-list'))
    assert not match(Command("tsuru app-list", ""))


# Generated at 2022-06-14 11:04:08.987174
# Unit test for function get_new_command
def test_get_new_command():
    from tests.utils import Command

    output = 'tsuru: "docker-log" is not a tsuru command. See "tsuru help".\n' \
             '\n' \
             'Did you mean?\n' \
             '\tdocker-logs\n' \
             '\tdocker-login\n' \
             '\tdocker-logout\n' \
             '\tlist-unit-log\n' \
             '\tlist-unit-logs\n'

    assert get_new_command(Command('', output=output)) == 'tsuru docker-logs'

# Generated at 2022-06-14 11:04:18.680896
# Unit test for function get_new_command
def test_get_new_command():
	assert get_new_command('tsuru: "apppli" is not a tsuru command.'
		'See "tsuru help".\n\nDid you mean?\n\tapp-list'
		'\n\tapp-remove\n\tapp-run\n\tapp-info') == 'tsuru app-list'
	assert get_new_command('tsuru: "appli" is not a tsuru command.'
		'See "tsuru help".\n\nDid you mean?\n\tapp-list'
		'\n\tapp-remove\n\tapp-run\n\tapp-info') == 'tsuru app-list'

# Generated at 2022-06-14 11:04:30.488754
# Unit test for function get_new_command
def test_get_new_command():
    # command is a instance of Command class
    command = Command(script='', stdout='tsuru: "contatiner-move" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tcontainer-move\n')
    assert get_new_command(command) == 'tsuru container-move'

# Generated at 2022-06-14 11:04:32.068312
# Unit test for function match
def test_match():
    # Function get_new_command not mocked, so this test is skipped.
    pass

# Generated at 2022-06-14 11:04:41.376113
# Unit test for function get_new_command
def test_get_new_command():
    test_command = type('Command', (object,), {'output': 'tsuru: "applice" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp\n\tapply\n\tapp-create\n\tapp-delete\n\tapp-info\n\tapp-log\n\tapp-run\n\tapp-start\n\tapp-stop\n\tapp-swap'})

    assert get_new_command(test_command) == 'tsuru app-create'



enabled_by_default = True

# Generated at 2022-06-14 11:04:44.846836
# Unit test for function match
def test_match():
    output = """Did you mean?
    deploy-app
    cluster-info
    tsuru: "admin" is not a tsuru command. See "tsuru help".
"""
    assert match(Command('tsuru admi',output))



# Generated at 2022-06-14 11:04:54.146990
# Unit test for function match
def test_match():
    assert match(Command('tsuru app-create hello-world php', 'tsuru: "'
                         'app-create" is not a tsuru command. See "tsuru '
                         'help".\n\nDid you mean?\n\tapp-create', '', 1, ''))

    assert not match(Command('tsuru app-create hello-world php', 'tsuru: "'
                             'app-create" is not a tsuru command. See "tsuru '
                             'help".\n\nDid you mean?', '', 1, ''))


# Generated at 2022-06-14 11:05:05.128199
# Unit test for function match
def test_match():
    assert match(Command('tsuru app ', 'tsuru: "app" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapps', ''))
    assert match(Command('tsuru app-list', 'tsuru: "app-list" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapps-list', ''))
    assert not match(Command('ls', 'ls: missing operand\nTry \'ls --help\' for more information.\n', ''))
    assert not match(Command('tsuru apps-list', '', ''))


# Generated at 2022-06-14 11:05:07.564442
# Unit test for function match
def test_match():
    assert match(Command('tsuru help'))
    assert not match(Command('tsuru version'))


# Generated at 2022-06-14 11:05:12.957064
# Unit test for function get_new_command
def test_get_new_command():
    output = 'tsuru: "permiossion" is not a tsuru command. See "tsuru help".\n\n\nDid you mean?\n\tpermission'
    command = Command('permiossion list', output)
    assert get_new_command(command) == 'tsuru permission list'

# Generated at 2022-06-14 11:05:21.273417
# Unit test for function match
def test_match():
	assert match(Command('tsuru plataform-list', 'tsuru: "plataform-list" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tplatform-list')) != None
	assert match(Command('tsuru app-list', 'tsuru: "app-list" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-list')) != None


# Generated at 2022-06-14 11:05:25.018234
# Unit test for function match
def test_match():
    assert match(Command('tsuru app-info -a test', output='tsuru: "app-info" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-info'))


# Generated at 2022-06-14 11:05:27.615910
# Unit test for function get_new_command
def test_get_new_command():
    output = """tsuru: "ps" is not a tsuru command. See "tsuru help".

                  Did you mean?
                      ps
                      app-run"""
    command = Command("tsuru ps", output=output)
    assert get_new_command(command) == "tsuru app-run"

# Generated at 2022-06-14 11:05:32.996968
# Unit test for function match
def test_match():
    assert match(Command('tsuru bll',
                         'tsuru: "bll" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tbll',
                         ''))
    assert match(Command('tsuru bl',
                         'tsuru: "bl" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tbl',
                         ''))
    assert not match(Command('tsuru bll bla ',
                         'tsuru: "bll" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tbll',
                         ''))



# Generated at 2022-06-14 11:05:39.721472
# Unit test for function match
def test_match():
    output = 'tsuru: "hello" is not a tsuru command. See "tsuru help".\nDid you mean?\n\thelp\n\thook-add\n\thook-delete\n\thook-list\n'
    command = Command(script=None, stdout=None, stderr=None, output=output)
    
    assert match(command)



# Generated at 2022-06-14 11:05:44.413807
# Unit test for function match
def test_match():
    broken_cmd = ("tsuru: \"mycmd\" is not a tsuru command. See \"tsuru help\"."
                  "\n\nDid you mean?\n\tmycomand")
    assert match(Command('tsuru mycmd', broken_cmd))



# Generated at 2022-06-14 11:05:47.383819
# Unit test for function match
def test_match():
    assert match(Command('tsuru help', 'tsuru: "help" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\thelp-app', ''))
    assert not match(Command('tsuru app-create', ''))


# Generated at 2022-06-14 11:05:57.828913
# Unit test for function match
def test_match():
    command_output="tsuru app-list\n+--------------------------+--------+\n| app                      | units |\n+--------------------------+--------+\n| app-test                 | 1      |\n+--------------------------+--------+\n\nTotal: 0\ntsuru: tsuru config-set is not a tsuru command. See \"tsuru help\".\n\nDid you mean?\n\tapp-set-env\n\tapp-unset-env\n"
    assert match(Command('tsuru config-set', command_output))
    assert not match(Command('tsuru app-list', ''))


# Unit teat for function get_new_command

# Generated at 2022-06-14 11:06:01.766570
# Unit test for function get_new_command
def test_get_new_command():
    command = "tsuru: \"test\" is not a tsuru command. See \"tsuru help\"." \
              "\nDid you mean?\n\ttest-repository"
    assert(get_new_command(command) == "tsuru test-repository")

# Generated at 2022-06-14 11:06:09.797377
# Unit test for function match
def test_match():
    assert match(Command('tsuru node-list', 'tsuru: "node-list" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tnode-list'))
    assert not match(Command('git commit', ''))



# Generated at 2022-06-14 11:06:19.725958
# Unit test for function match
def test_match():
    command = Command("tsuru help",
                      "tsuru: \"help\" is not a tsuru command. See \"tsuru help\".\n"
                      "Did you mean?\n"
                      "\thelp-doc\n"
                      "\thelp-platform-add\n"
                      "\thelp-platform-remove\n"
                      "\thelp-remove\n"
                      "\thelp-team-create\n"
                      "\thelp-team-destroy\n"
                      "\thelp-team-list\n"
                      "\thelp-team-remove-user\n"
                      "\thelp-team-user-list\n"
                      "\thelp-user-add\n"
                      "\thelp-user-remove")

    assert match(command)


# Generated at 2022-06-14 11:06:30.689844
# Unit test for function match
def test_match():
    assert match(Command('tsuru app-info',
                         'tsuru: "app-info" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-list\n\tapp-migrate\n\tapp-info\n\tapp-update\n\tapp-remove\n\tswap\n\tswap-cancel\n\n'))
    assert match(Command('tsuru node-list',
                         'tsuru: "node-list" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tnode-add\n\tnode-remove\n\tnode-list\n\n'))

# Generated at 2022-06-14 11:06:44.769934
# Unit test for function match
def test_match():
    assert match(Command('tsuru help', "tsuru: \"help\" is not a tsuru command. See \"tsuru help\".\n\nDid you mean?\n\thelp-app\n\thelp-app-deploy\n\thelp-app-info\n\thelp-app-log\n\thelp-app-remove\n\thelp-app-run\n\thelp-app-start\n\thelp-app-stop\n\thelp-app-restart\n\thelp-app-grant\n\thelp-app-revoke\n\thelp-app-swap\n\thelp-app-deploy-list\n\thelp-app-spring\n"))



# Generated at 2022-06-14 11:06:48.662191
# Unit test for function match
def test_match():
    assert match(Command('tsuru status',
                         'tsuru: "status" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tstatus-app\n\tstatus-healer'))


# Generated at 2022-06-14 11:07:01.822221
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.main import Command

    assert get_new_command(Command("tsuru app-info", "tsuru: \"app-info\" is not a tsuru command. See \"tsuru help\".")) == ['tsuru app-info']
    assert get_new_command(Command("tsuru appInfo", "tsuru: \"appInfo\" is not a tsuru command.\nDid you mean?\n\tapp-info\n\tapp-log", output_stream="stderr")) == ['tsuru app-info']


# Generated at 2022-06-14 11:07:04.212526
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('tsurud fnord', '')
    new_command = get_new_command(command)
    assert new_command == 'tsurud target'


priority = 1000

# Generated at 2022-06-14 11:07:12.074431
# Unit test for function get_new_command
def test_get_new_command():
    test_command = Command('tsuru app-list', 'tsuru: "app-list" is not a tsuru command. See "tsuru help".\n\nDid you mean?\n\tapp-create\n\tapp-remove\n\tapp-run\t')
    assert get_new_command(test_command) == 'tsuru app-create'

# Generated at 2022-06-14 11:07:14.534794
# Unit test for function match
def test_match():
    assert match(Error('''tsuru: "deploy" is not a tsuru command. See "tsuru help"''', '', '', ''))
    assert not match(Error('not found', '', '', ''))


# Generated at 2022-06-14 11:07:17.537550
# Unit test for function match
def test_match():
	assert match("tsuru: \"tbla\" is not a tsuru command. See \"tsuru help\".\nDid you mean?\n\tbla")


# Generated at 2022-06-14 11:07:29.649741
# Unit test for function get_new_command
def test_get_new_command():
    output = 'tsuru: "team-create" is not a tsuru command. See "tsuru help".\nDid you mean?\n\tteam-add'
    command = type("Command", (object,), {"output": output})

    assert get_new_command(command) == "tsuru team-add"

