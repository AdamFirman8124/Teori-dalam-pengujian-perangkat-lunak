

# Generated at 2022-06-14 10:24:59.110008
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.lein_is_not_a_task import get_new_command

    command = Command('lein rla', 'Project not found', 'lein rla')
    assert get_new_command(command) == 'lein repl'



# Generated at 2022-06-14 10:25:06.358584
# Unit test for function match
def test_match():
    assert match(Command('lein foo : bar', 'lein foo : bar \n\
          "{A command task}" is not a task. See "lein help". \n\
          Did you mean this? \n\
          foo-bar'))
    assert not match(Command('lein foo', 'lein foo \n\
          "{A command task}" is not a task. See "lein help".'))


# Generated at 2022-06-14 10:25:17.003782
# Unit test for function match
def test_match():
    """
    Unit test for function match. The function verifies if the output of the 
    command is correct to be replaced. Match() must return True.
    """
    command = Command('lein umbrealla status', 'Error: Unknown task "umbrealla". See "lein help".\nDid you mean this?\n  update\n  utils\n  test\n  repl\n  run\n  release\n  new\n  install\n  help\n  jar\n  module\n  install-for-emacs\n  clean\n  classpath\n  check\n  do\n  test-refresh\n  jar-uberjar\n  with-profile')
    command.script = 'lein umbrealla status'
    assert(match(command) == True)



# Generated at 2022-06-14 10:25:24.693586
# Unit test for function match
def test_match():
    assert match(Command('lein repl',
                         'Could not find task or namespaces '
                         'repl.\nDid you mean this?\n'
                         '\trelease'))
    assert not match(Command('lein repl', 'Could not find task or namespaces'))
    assert not match(Command('lein repl',
                             'Could not find task or namespaces '
                             'repl.\nDid you mean this?\n'
                             '\trelease'))


# Generated at 2022-06-14 10:25:31.239623
# Unit test for function match
def test_match():
    new_command = Command('lein midje', '''
Did you mean this?
         lein midje
    ''')
    assert match(new_command)



# Generated at 2022-06-14 10:25:40.308989
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.lein_did_you_mean import get_new_command
    right_cmd = {'output': "lein foo\n'foo' is not a task. See 'lein help'."
                           "\nDid you mean this?\n         foo"}
    wrong_cmd = {'output': 'lein foos\nERROR: Invalid task, terminating...'}
    assert get_new_command(right_cmd) == 'lein foo '
    assert get_new_command(wrong_cmd) is None

# Generated at 2022-06-14 10:25:42.333380
# Unit test for function get_new_command
def test_get_new_command():
    new_command = get_new_command('lein doo node')
    assert new_command == "lein do node"

# Generated at 2022-06-14 10:25:48.112236
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('lein deps ', '')
    assert get_new_command(command) == 'lein deps :tree'

# Generated at 2022-06-14 10:25:52.223696
# Unit test for function match
def test_match():
    assert match(Command('lein', stderr='Could not find task or (did you mean "dev/test?"?)'))
    assert not match(Command('lein', stderr='Could not find task or (did you mean "dev/test?")'))


# Generated at 2022-06-14 10:25:57.431977
# Unit test for function match
def test_match():
    command = 'lein foo bar'
    output = '''
[smana@smana-arch lein-app]$ lein foo bar
'foo' is not a task. See 'lein help'.
Did you mean this?
         foo
'''
    assert match(Command(script=command, output=output))


# Generated at 2022-06-14 10:26:06.448728
# Unit test for function get_new_command
def test_get_new_command():
    cmd = 'lein test-watcher'
    out = ("task 'test-whatched' is not a task. See 'lein help'.\n"
           "Did you mean this?\n"
           "    test-watcher")
    new_cmd = str(get_new_command(Command(cmd, out)))
    assert new_cmd == 'sudo lein test-watcher'

# Generated at 2022-06-14 10:26:08.206820
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

# Generated at 2022-06-14 10:26:13.949202
# Unit test for function get_new_command
def test_get_new_command():
    test_lines = ['lein repl\n', '"repl" is not a task. See "lein help".\n',
        '\n', 'Did you mean this?\n', '     repl\n']
    test_command = type('', (),
        {'script': 'lein repl', 'output': ''.join(test_lines)})
    assert get_new_command(test_command) == "lein repl"

# Generated at 2022-06-14 10:26:20.862866
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('lein cljsbuid auto')
    command.output = """
'cljsbuid' is not a task. See 'lein help'.
Did you mean this?
        cljsbuild

Run `lein help $TASK` for details.
"""
    assert get_new_command(command) == 'lein cljsbuild auto'


# Generated at 2022-06-14 10:26:24.283466
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('lein foo bar', '"foo" is not a task. See "lein help".\nDid you mean this?\n\trun')
    assert get_new_command(command) == "lein run bar"

# Generated at 2022-06-14 10:26:30.229075
# Unit test for function match
def test_match():
    assert match(Command(script='lein run'))
    assert match(Command(script='lein config'))
    assert not match(Command(script='lein',
        stderr='Could not find task \'run\'. Did you mean this?\n'
               '         run-all-tests',
       ))
    assert not match(Command(script='lein',
        stderr='Could not find task \'config\'. Did you mean this?\n'
               '         clean-config',
        ))


# Generated at 2022-06-14 10:26:35.574864
# Unit test for function match
def test_match():
    assert match(Command('lein test', 'lein test\n'
                         '"test" is not a task. See "lein help".\n'
                         'Did you mean this?\n'
                         '         test\n'
                         '         test-in-project'))


# Generated at 2022-06-14 10:26:46.172265
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

    assert get_new_command(Command('lein test',
                                   'lein test is not a task.\nDid you mean this?\n         test')) == 'lein test'

    assert get_new_command(Command('lein test',
                                   'lein test is not a task.  Did you mean this?\n         test-all')) == 'lein test-all'

    assert get_new_command(Command('lein test',
                                   'lein test is not a task.  Did you mean one of these?\n         test-all\n         test-refresh')) == 'lein test-all'


# Generated at 2022-06-14 10:26:55.847571
# Unit test for function get_new_command
def test_get_new_command():
    import sys
    from thefuck.rules.lein_not_task import get_new_command
    script = "lein run"
    output = ("'runn' is not a task. See 'lein help'.\n" 
              "Did you mean this?\nrun")
    command = type('Command', (object,), {
        'script': script,
        'output': output,
        'stdout': sys.stdout,
        'stderr': sys.stderr})
    assert get_new_command(command) == 'lein run'

# Generated at 2022-06-14 10:27:00.489807
# Unit test for function get_new_command
def test_get_new_command():
    output = """
    'z' is not a task. See 'lein help'.
    Did you mean this?
    :z

    """
    command = Command('lein z', output)
    assert get_new_command(command) == "lein :z"


# Generated at 2022-06-14 10:27:07.281628
# Unit test for function get_new_command
def test_get_new_command():
    command = 'lein ids'
    output = ''''ids' is not a task. See 'lein help'.
Did you mean this?
         jar'''

    command = Mock(script='lein ids', output=output)
    assert get_new_command(command) == 'lein jar'

# Generated at 2022-06-14 10:27:07.994320
# Unit test for function get_new_command
def test_get_new_command():
    pass

# Generated at 2022-06-14 10:27:17.138036
# Unit test for function get_new_command

# Generated at 2022-06-14 10:27:22.487313
# Unit test for function get_new_command
def test_get_new_command():
    test_command = "lein test"
    test_output = """
Could not find task or a macro or a namespace named 'test'.
Did you mean this?
         test-refresh
    """
    assert get_new_command({'script': test_command, 'output': test_output}) == "lein test-refresh"

# Generated at 2022-06-14 10:27:30.561690
# Unit test for function match
def test_match():
    assert match(Command('lein run',
                         "lein run: 'run' is not a task. See 'lein help'.\nDid you mean this?\n<TAB> test\n",
                         ''))
    assert not match(Command('lein',
                             "lein: 'run' is not a task. See 'lein help'.\nDid you mean tis?\n<TAB> test\n",
                             ''))


# Generated at 2022-06-14 10:27:32.815976
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.lein_no_task import get_new_command
    assert get_new_command('lein whatsthis') == 'lein thisisatask'

# Generated at 2022-06-14 10:27:34.926954
# Unit test for function match
def test_match():
    assert match("lein foo")
    assert not match("lein help")


# Generated at 2022-06-14 10:27:37.271528
# Unit test for function match
def test_match():
    # match function should return a bool
    assert type(match(Command())) == bool


# Generated at 2022-06-14 10:27:41.616923
# Unit test for function match
def test_match():
    assert not match(Command('lein help'))
    assert not match(Command('lein help', 'lein: task not found: help'))
    assert match(Command('lein helo', 'lein: task not found: hello\n Did you mean this?\n  help'))

# Generated at 2022-06-14 10:27:45.098717
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    script = 'lein'
    stdout = "Could not find task 'grep'.\n\nDid you mean this?\n        help\n        exec\n        release\n\nBUILD SUCCESSFUL"
    stderr = ''
    command = Command(script, stdout, stderr)
    newCommand = get_new_command(command)
    assert newCommand.script == 'lein help'


# Generated at 2022-06-14 10:27:58.407470
# Unit test for function get_new_command
def test_get_new_command():
    print("get_new_command")
    # Arrange
    from thefuck.types import Command
    from thefuck.rules.lein_command_not_found import get_new_command
    command = Command('lein teste',
                      "Could not find task 'teste'\nDid you mean this?\n  test")

    # Act
    actual = get_new_command(command)

    # Assert
    expected = "lein test"
    assert (actual == expected)


# Generated at 2022-06-14 10:28:03.600358
# Unit test for function match
def test_match():
    command_true = Command(script='lein something', stdout='some_output'
                , output='\'something\' is not a task. See \'lein help\'.\nDid you mean this?\nsomething-else')
    command_false = Command(script='lein something', stdout='some_output'
                , output='Did you mean this?\nsomething-else')
    assert match(command_true)
    assert not match(command_false)



# Generated at 2022-06-14 10:28:12.769962
# Unit test for function match
def test_match():
    assert match(Command('lein rpl 5 10', 'lein rpl is not a task. See \'lein help\'.'))
    assert match(Command('lein rpls 5 10', 'lein rpls is not a task. See \'lein help\'.'))
    assert not match(Command('lein rpls 5 10', 'lein rpls is not a task'))
    assert not match(Command('lein rpls 5 10', 'lein is not a task'))


# Generated at 2022-06-14 10:28:21.440350
# Unit test for function get_new_command
def test_get_new_command():
    # Test 1
    output=""" 'foobar' is not a task. See 'lein help'.
Did you mean this?
         :foo
         :foobar
         :foobarbaz
    """

    command='lein run'
    new_cmd = get_new_command(Command(script=command, output=output))

    assert new_cmd == "lein run :foo"

    # Test 2
    output=""" 'test' is not a task. See 'lein help'.
Did you mean one of these?
         task-foo
         task-bar
         task-baz
    """

    command='lein test'
    new_cmd = get_new_command(Command(script=command, output=output))

    assert new_cmd == "lein test task-foo"

# Generated at 2022-06-14 10:28:33.139178
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("lein doo node",
                                   "lein doo node' is not a task. See 'lein help'.\n\nDid you mean this?\n         node")) == "lein doo node"
    assert get_new_command(Command("lein doo node",
                                   "lein doo node' is not a task. See 'lein help'.\n\nDid you mean this?\n         do")) == "lein do"
    assert  get_new_command(Command("lein dummy",
                                    "lein dummy' is not a task. See 'lein help'.\n\nDid you mean one of these?\n         dummy-aot\n         dummy-rebel-readline\n         dummy-uberjar\n         dummy-war")) == "lein dummy-aot"

# Generated at 2022-06-14 10:28:45.856060
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('lein run clean', 'lein run clean\n\nlein run		Runs user-defined \'startup\' function.\n\n\n\'clean\' is not a task. See \'lein help\'.')).script == 'lein run'
    assert get_new_command(Command('lein cljsbuild clean', 'lein cljsbuild clean\n\nlein cljsbuild/build	Compile a ClojureScript build once.\nlein cljsbuild/clean	Clean compiled files in stages.\nlein cljsbuild/help	Display help summary.\n\nDid you mean this?\nlein cljsbuild/clean\n\n\'clean\' is not a task. See \'lein help\'.')).script == 'lein cljsbuild clean'

# Generated at 2022-06-14 10:28:52.560926
# Unit test for function match
def test_match():
    # Test for `lein` command
    assert match(Command('lein run clean', '', '', 1, None))
    assert match(Command('lein run clean', '', '', 1, None))
    assert match(Command('lein run clean', '', '', 1, None))

    # Test for `sudo lein` command
    assert match(Command('sudo lein run clean', '', '', 1, None))
    assert match(Command('sudo lein run clean', '', '', 1, None))
    assert match(Command('sudo lein run clean', '', '', 1, None))

    # Test for `sudo su -c lein run clean` command
    assert match(Command('sudo su -c lein run clean', '', '', 1, None))

# Generated at 2022-06-14 10:29:05.119588
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.shells import Bash

    assert get_new_command(Command(script='lein',
                                   output=("'project' is not a task. See 'lein help'.\n"
                                           "Did you mean this?\n"
                                           "         project\n"),
                                   settings=Bash())) == 'lein project'

    assert get_new_command(Command(script='lein',
                                   output=("'compile' is not a task. See 'lein help'.\n"
                                           "Did you mean this?\n"
                                           "         compile\n"
                                           "         uberjar\n"),
                                   settings=Bash())) == 'lein compile'


# Generated at 2022-06-14 10:29:09.502754
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    assert get_new_command(Command("lein run somfoo", "lein foo is not a task. See 'lein help'.\nDid you mean this?\n\trun", "")) == "lein run somfoo"

# Generated at 2022-06-14 10:29:10.686772
# Unit test for function match
def test_match():
    assert match(Command('lein'))


# Generated at 2022-06-14 10:29:23.413301
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

    assert get_new_command(Command("lein foo", "foo is not a task...Did you mean this?\nrun")) == 'lein run'

# Generated at 2022-06-14 10:29:28.984459
# Unit test for function match
def test_match():
    assert match(Command('lein clein'))
    assert match(Command('sudo lein clein'))
    assert not match(Command('lein help'))
    assert not match(Command('lein clein help'))
    assert not match(Command('sudo lein help'))
    assert not match(Command('sudo lein clein help'))


# Generated at 2022-06-14 10:29:38.133990
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('lein clojure', output='''\
`clojure` is not a task. See 'lein help'.

Did you mean this?

         compile
    ''')) == 'lein compile'

    assert get_new_command(Command('lein clojure', output='''\
`clojure` is not a task. See 'lein help'.

Did you mean one of these?

        clean
        clean,
        cljsbuild
    ''')) == 'lein clean'

# Generated at 2022-06-14 10:29:43.152503
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command({'script': 'lein terminal', 'output': '''
Exception in thread "main" java.lang.RuntimeException: terminal is not a task. See 'lein help'.
Did you mean this?
         trampoline'''}) == 'lein trampoline'

# Generated at 2022-06-14 10:29:48.210683
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('lein runn', '''
[WARNING] lein runn is not a task. See 'lein help'.
Run `lein tasks` for a list of tasks.
Did you mean this?
                run
''', None, '', '')) == "lein run"

# Generated at 2022-06-14 10:29:53.738418
# Unit test for function get_new_command
def test_get_new_command():
    import re

    command = MagicMock(output='\'help\' is not a lein task. See \'lein help\'.\nDid you mean this?\n\trun\n\nRun a subset of the default tasks.')
    broken_cmd = re.findall(r"'([^']*)' is not a task",
                            command.output)[0]
    new_cmds = get_all_matched_commands(command.output, 'Did you mean this?')

    new_command = get_new_command(command)

    assert broken_cmd == 'help'
    assert new_cmds == ['run']
    assert "lein run" == new_command



# Generated at 2022-06-14 10:30:05.105945
# Unit test for function match
def test_match():
	assert match(Command("lein test", "ERROR: 'test' is not a task. See 'lein help'.\nCould not find tasks.lisp, project.clj, or leiningen/tasks.clj on the classpath.\nDid you mean this?\n  teest\n  te", "lein"))
	assert not match(Command("lein testasd", "Couldn't find project.clj, which is needed for testing\nDid you mean this?\n  teest\n  te", "lein"))
	assert not match(Command("lein test asd", "Couldn't find project.clj, which is needed for testing\nDid you mean this?\n  teest\n  te", "lein"))


# Generated at 2022-06-14 10:30:08.614718
# Unit test for function match
def test_match():
    assert match(Command('lein ina toast', ''))
    assert match(Command('lein ina toast', '', stderr='oups'))
    assert not match(Command('lein ina toast', 'No oups'))

# Generated at 2022-06-14 10:30:23.066759
# Unit test for function match

# Generated at 2022-06-14 10:30:26.063443
# Unit test for function match
def test_match():
    assert not match(Command("lein", stderr='lein run'))
    assert match(Command("lein help", stderr='lein: Command not found'))


# Generated at 2022-06-14 10:30:49.730542
# Unit test for function get_new_command
def test_get_new_command():
    output = "Could not find task or namespaces 'wowow'. Did you mean this?\n - woah\n - whoa"
    command = Command('lein wowow', '', output)
    assert get_new_command(command) == 'lein woah'

# Generated at 2022-06-14 10:30:55.396173
# Unit test for function match
def test_match():
    correct_match = "Command 'lein plz' is not a task. See 'lein help'.\nDid you mean this?\n    help\n"
    assert match(Command(script='lein plz'))
    assert match(Command(script='lein plz', output=correct_match))
    assert 'Did you mean this?' not in match.stderr


# Generated at 2022-06-14 10:31:00.198353
# Unit test for function get_new_command
def test_get_new_command():
    output = "Error: Unknown task 'test'\n\nDid you mean this?\n         test\n         test-refresh\n         test-verbose\n\nRun `lein help` for a list of tasks."
    command = Command('lein test', output=output)
    assert get_new_command(command).script == 'lein test'

# Generated at 2022-06-14 10:31:10.879334
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('lein cljd',
                                   output='\'cljd\' is not a task. See \'lein help\'.\nDid you mean this?\nrjh')) == 'lein rjh'
    assert get_new_command(Command('lein jure',
                                   output='\'jure\' is not a task. See \'lein help\'.\nDid you mean this?\nrepl')) == 'lein repl'
    assert get_new_command(Command('lein jar',
                                   output='\'jar\' is not a task. See \'lein help\'.\nDid you mean this?\njar!\ndepstar\nuberjar')) == 'lein jar!'

# Generated at 2022-06-14 10:31:15.401284
# Unit test for function get_new_command
def test_get_new_command():
    output = ''''leimn help' is not a task. See 'lein help'.
Did you mean this?
         run
'''
    assert get_new_command(Command('lein leimn help', output)) == 'lein run'



# Generated at 2022-06-14 10:31:18.333731
# Unit test for function match
def test_match():
    assert match(Command('lein deploy', ''))
    assert not match(Command('lein deploy', 'lein help'))


# Generated at 2022-06-14 10:31:23.493247
# Unit test for function match
def test_match():
    assert match(Command('lein foo', '''Leiningen: 'foo' is not a task. See 'lein help'.
Did you mean this?
         repl
         run
         jar
         uberjar
         pom
         install
         deploy
         release
         help
         test'''))



# Generated at 2022-06-14 10:31:35.915905
# Unit test for function get_new_command
def test_get_new_command():
    script = 'lein build'
    output = '''
lein: 'build' is not a task. See 'lein help'.

Did you mean this?
         uberjar
    '''
    command = Command(script, output)
    new_command = get_new_command(command)
    assert new_command == 'lein uberjar'

# Generated at 2022-06-14 10:31:44.268046
# Unit test for function match

# Generated at 2022-06-14 10:31:53.071339
# Unit test for function match
def test_match():
    assert match(Command('lein foo', 'lein foo is not a task. See "lein help".\n\nDid you mean this?\n     foo-bar'))
    assert not match(Command('lein foo', 'Could not find artifact org.clojure:clojure:jar:1.6.0 in central (http://repo1.maven.org/maven2/)\n'))
    assert not match(Command('lein foo', 'lein foo is not a task. See "lein help".'))

# Unit tests for function get_new_command

# Generated at 2022-06-14 10:32:32.437209
# Unit test for function match
def test_match():
    command = 'lein uberjar'
    assert match(command)


# Generated at 2022-06-14 10:32:36.880002
# Unit test for function get_new_command
def test_get_new_command():
    command = 'lein test'
    output = 'lein: "' + command + '" is not a task. See \'lein help\'.\nDid you mean this?\n  run'
    command = Command(command, output)
    assert get_new_command(command) == 'lein run' + sudo_support()

# Generated at 2022-06-14 10:32:39.776807
# Unit test for function get_new_command
def test_get_new_command():
    command = "lein foo"
    print(get_new_command(command))
    
# test_get_new_command()

# Generated at 2022-06-14 10:32:42.542709
# Unit test for function match

# Generated at 2022-06-14 10:32:48.824517
# Unit test for function match
def test_match():
    # Valid case
    assert match(Command('lein run'))

    # Invalid case
    assert not match(Command('git run'))


# Generated at 2022-06-14 10:32:55.542194
# Unit test for function match
def test_match():
    command = Command('lein trampoline run', 'lein: Command not found.')
    assert not match(command)

    command = Command('lein test', 'test is not a taske. See lein help')
    assert not match(command)

    command = Command(
        'lein test',
        'test is not a task. See lein help\nDid you mean this?  trampoline')
    assert match(command)



# Generated at 2022-06-14 10:33:00.652317
# Unit test for function match
def test_match():
    assert match(Command('lein run foo', 'run is not a task. See \'lein help\'\nDid you mean this?\n    run\n    run-\n'))
    assert not match(Command('lein run', 'lein run\nfoo\n'))
    assert not match(Command('lein repl', 'lein repl\nfoo\n'))


# Generated at 2022-06-14 10:33:08.628000
# Unit test for function match
def test_match():
    assert match(Command('lein run',
                         'run is not a task. See `lein help`.\nDid you mean this?'))

    assert match(Command('lein test',
                         "test is not a task. See 'lein help'.\nDid you mean this?"))

    assert not match(Command('lein test', "test is not a task. See 'lein help'."))
    assert not match(Command('lein', 'lein is not a task. See `lein help`.'))

# Generated at 2022-06-14 10:33:14.651023
# Unit test for function get_new_command
def test_get_new_command():
    output = (
        u"Command not found.\n"
        u'Did you mean this?\n'
        u'         :test-refresh\n'
        u'         :nREPL        \n'
        u'Run "lein help" for a list of available tasks.')
    assert get_new_command(Command('lein kom', output)) == 'lein :test-refresh'

# Generated at 2022-06-14 10:33:23.318344
# Unit test for function get_new_command
def test_get_new_command():
    original_cmd = "lein ci-test"
    output = "`ci-test` is not a task. See 'lein help'.\nDid you mean this?\n         test"
    assert(get_new_command(Command(original_cmd, output)) == "lein test")

# Generated at 2022-06-14 10:34:51.002428
# Unit test for function match
def test_match():
    assert match(Command('lein abc',
                         '''Could not find tasks matching pattern:
                            abc
                            [:a :b :c] is not a task. See 'lein help'.''',
                         '''Did you mean this?
                            :c'''))

    assert not match(Command('lein abc', 'Could not find tasks matching pattern: abc'))
    assert not match(Command('lein abc', 'abc is not a task'))
    assert not match(Command('lein abc', 'abc is not a task. See "lein help"'))
    assert not match(Command('lein abc', 'abc is not a task. See "lein help"', 'Did you mean this?'))



# Generated at 2022-06-14 10:34:58.595227
# Unit test for function get_new_command