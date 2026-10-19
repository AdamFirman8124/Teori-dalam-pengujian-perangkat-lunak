

# Generated at 2022-06-14 09:19:03.981892
# Unit test for function match
def test_match():
    assert match(Command('aws s3', 'aws: error: argument operation: Invalid choice: "s3", maybe you meant:', output = '''usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help
aws: error: argument operation: Invalid choice: "s3", maybe you meant:
   configure
   help
 * s3api'''))



# Generated at 2022-06-14 09:19:06.006108
# Unit test for function match
def test_match():
    """
        Function match
    """
    command = Command('aws help')
    assert match(command)


# Generated at 2022-06-14 09:19:09.703844
# Unit test for function match
def test_match():
    assert match(Command("aws s3 mb s3://", ""))
    assert not match(Command("aws s3 mb s3://test", ""))
    assert not match(Command("echo", ""))


# Generated at 2022-06-14 09:19:21.975323
# Unit test for function get_new_command

# Generated at 2022-06-14 09:19:28.880775
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    assert get_new_command(Command('aws ec2 start-indaances foobar',
                                   'usage: aws [options] <command> <subcommand> [parameters]\n'
                                   "\n"
                                   'aws: error: argument command: Invalid choice, maybe you meant:\n'
                                   '    start-instances\n'
            )) == ['aws ec2 start-instances foobar']

# Generated at 2022-06-14 09:19:34.965870
# Unit test for function match
def test_match():
    assert match(Command('aws help',
                         'usage: aws [options] [parameters]\n' +
                         'aws: error: argument operation: Invalid choice: \'help2\', maybe you meant: ' +
                         '\n    * help\n    * help-api\n    * help-synopsis', 1))



# Generated at 2022-06-14 09:19:41.073068
# Unit test for function match
def test_match():
    assert match(Command('aws s3api list-bucket-acls help'))
    assert match(Command('aws s3api list-bucket-acls help', '', '', '', '', ''))
    assert not match(Command('aws s3api create-bucket help', '', '', '', '', ''))



# Generated at 2022-06-14 09:19:43.725588
# Unit test for function match
def test_match():
    output = "Unknown options: --verion"
    assert match(Command("aws ec2 describe-instances --verion", output))


# Generated at 2022-06-14 09:19:48.183114
# Unit test for function match
def test_match():
    assert match(Command('aws s3 mb s3://test'))
    assert match(Command('aws s3 mb s3://test', 'InvalidChoice: error'))
    assert not match(Command('aws ec2 status'))

# Generated at 2022-06-14 09:19:55.459610
# Unit test for function get_new_command
def test_get_new_command():
	test_commands = [Command("aws s3 mb s3://testbucket111", "usage: aws [options] <command> <subcommand> [<subcommand> ..."), Command("aws s3 mb s3://testbucket111", "usage: aws [options] <command> <subcommand> [<subcommand> ...")]

# Generated at 2022-06-14 09:20:03.340247
# Unit test for function match
def test_match():
    command = Command("aws s3 ls", "usage: aws [options] <command> <subcommand> [parameters]\naws: error: argument command: Invalid choice, valid choices are:\n  configure | \n  help | \n  \nmaybe you meant:\n  s3 instead of s3")
    assert match(command)


# Generated at 2022-06-14 09:20:10.557734
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("aws ec2 help",
                                   "usage: aws [options]                           \n[ ...]\naws: error: argument operation: Invalid choice: 'help', maybe you meant:\n  * ec2\n  * elb\n  * s3\n",
                                   1)) == ['aws ec2 ', 'aws ec2 ', 'aws ec2 ']
    assert get_new_command(Command("aws ec2 help",
                                   "usage: aws [options]                           \n[ ...]\naws: error: argument operati: Invalid choice: 'help', maybe you meant:",
                                   1)) == []

# Generated at 2022-06-14 09:20:23.481961
# Unit test for function match
def test_match():
    output_1 = 'aws: error: argument command: Invalid choice, maybe you meant: '\
               '\n\n* receive-message\n* redrive-queue\n* remove-permission'
    output_2 = 'aws: error: argument command: Invalid choice, maybe you meant: '\
               '\n\n* receive-message\n* redrive-queue\n* remove-permission'
    output_3 = 'aws: error: argument command: Invalid choice'
    output_4 = 'Something else'
    output_5 = 'aws: error: argument command: Invalid choice, maybe you meant: '\
               '\n\n* receive-message\n* redrive-queue\n* remove-permission'
    command_1 = Command('aws', 'receive-message')
    command_1.output = output_

# Generated at 2022-06-14 09:20:27.855921
# Unit test for function match
def test_match():
    assert match(Command('aws',
        'aws: error: argument operation: Invalid choice: \'"e"\', maybe you meant: \n  * ecs \n  * ec2',
        'aws: error: Too few arguments.'))


# Generated at 2022-06-14 09:20:34.274564
# Unit test for function get_new_command
def test_get_new_command():
    command = type('', (), {})()
    command.script = 'aws ec2 (haha) (hoho) (hehe) (hihi)'
    command.output = 'aws: error: argument subnet-id: Invalid choice: \'haha\', maybe you meant: \n  \n  * ho'
    assert [replace_argument(command.script, 'haha', 'ho')] == get_new_command(command)

# Generated at 2022-06-14 09:20:37.865510
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('aws s3 --help')
    test_command = get_new_command(command)
    assert 'aws s3api --help' in str(test_command)

enabled_by_default = True

# Generated at 2022-06-14 09:20:39.151999
# Unit test for function match
def test_match():
    assert match(Command('aws help'))
    assert not match(Command('ls'))

# Generated at 2022-06-14 09:20:44.596503
# Unit test for function match
def test_match():
  assert match(Command("aws s3 ls", "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\n\nTo see help text,", ""));
  assert match(Command("aws s3 ls", "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\n\nTo see help text, Invalid choice: 'ham', maybe you meant:", ""));



# Generated at 2022-06-14 09:20:48.954985
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.aws import get_new_command

    command = Command('aws ec2', 'aws: error: argument command: Invalid choice: \'ce2\', maybe you meant:\n* ec2')
    assert get_new_command(command) == ['aws ec2']

    command = Command('aws ec2', 'aws: error: argument command: Invalid choice: \'ce2\', maybe you meant:')
    assert get_new_command(command) == []

# Generated at 2022-06-14 09:20:51.082847
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 help', 'usage: aws [options] <command> <subcommand> [parameters]'))
    assert not match(Command('aws something else', 'string'))


# Generated at 2022-06-14 09:21:01.841391
# Unit test for function get_new_command
def test_get_new_command():
    # Test for the short form of ec2 command
    script = "aws ec2 start-instance --region us-east-2 --instance-ids %s"
    command = "aws ec2 start-instance --region us-east-2 --instance-ids i-23423423423"

# Generated at 2022-06-14 09:21:14.739925
# Unit test for function match

# Generated at 2022-06-14 09:21:24.238632
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws s3 cp', "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument unknown: 'cp', maybe you meant:\n\n* cpane\n* cpan\n* cpanm\n")) == ['aws s3 cpane', 'aws s3 cpan', 'aws s3 cpanm']

# Generated at 2022-06-14 09:21:32.442919
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 help', 
    "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument subcommand: Invalid choice, maybe you meant: finished\n    finish\n    config\n    configures\n    conf\n    configure\n    configured\n    configuring\n    configures\n    "))
    assert not match(Command('aws ec2 help', 'usage: fur [options] <command> <subcommand>'))


# Generated at 2022-06-14 09:21:44.869728
# Unit test for function get_new_command

# Generated at 2022-06-14 09:21:59.799207
# Unit test for function match

# Generated at 2022-06-14 09:22:09.676540
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("aws ec2 describe-instances")

# Generated at 2022-06-14 09:22:19.480442
# Unit test for function get_new_command

# Generated at 2022-06-14 09:22:31.648640
# Unit test for function match

# Generated at 2022-06-14 09:22:34.151045
# Unit test for function match
def test_match():
    assert match(Command('aws help', 'usage:'))
    assert match(Command('aws help', 'usage:', None))
    assert match(Command('aws help', '', None))
    assert not match(Command('ls -al', '', None))


# Generated at 2022-06-14 09:22:44.217792
# Unit test for function match
def test_match():
    assert match(Command('aws --version', u'usage: aws [options] <command> '
            '<subcommand> [<subcommand> ...] [parameters]\nTo see help text, '
            'you can run:\n\n  aws help\n  aws <command> help\n  aws <command> '
            '<subcommand> help\naws: error: argument command: Invalid choice: '
            '"--version", maybe you meant:\n    verson'))



# Generated at 2022-06-14 09:22:50.601246
# Unit test for function match
def test_match():
    assert match(Command('aws s3p ls', 'usage: aws [options] <command> <subcommand> [parameters]'))
    assert not match(Command('aws s3 ls', 'usage: aws [options] <command> <subcommand> [parameters]'))
    assert not match(Command('ls', 'usage: aws [options] <command> <subcommand> [parameters]'))



# Generated at 2022-06-14 09:23:02.268195
# Unit test for function match

# Generated at 2022-06-14 09:23:10.017657
# Unit test for function get_new_command

# Generated at 2022-06-14 09:23:19.911340
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script="aws ec2 r", output="usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument subcommand: Invalid choice, maybe you meant:\n\n* run-instances\n* reboot-instances\n* describe-instances")
    assert get_new_command(command) == ["aws ec2 run-instances", "aws ec2 reboot-instances", "aws ec2 describe-instances"]

# Generated at 2022-06-14 09:23:30.281243
# Unit test for function get_new_command

# Generated at 2022-06-14 09:23:38.484918
# Unit test for function match
def test_match():
    from thefuck.rules.aws_cli import match
    assert match(Command('aws ec2 describe-instance',
        'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument subcommand: Invalid choice, maybe you meant:',
        'aws ec2 describe-instance'))

# Generated at 2022-06-14 09:23:45.781824
# Unit test for function match
def test_match():
    command = Command('aws ec2 run-instances --iamguration-file ./config.json ', 'usage: aws [options] <command> <subcommand> [parameters]\naws: error: argument instance-type: Invalid choice: \'config.json\', maybe you meant:\n  config  configuration\n')
    assert match(command)
    assert not match(Command('git commit', ''))


# Generated at 2022-06-14 09:23:47.980164
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws ec2 --help')) == [
        'aws ec2 help'
    ]

# Generated at 2022-06-14 09:23:51.475554
# Unit test for function match
def test_match():
    assert match(Command("aws help", "aws: error: argument operation: Invalid choice: '-h', maybe you meant:\n  * help\n  * help-config\n  * help-local"))



# Generated at 2022-06-14 09:23:57.401624
# Unit test for function match
def test_match():
    assert match(Command('aws s3api list', 'usage: aws [options] <command> <subcommand> [parameters]\naws: error: argument command: Invalid choice: ', 'aws')) != None

# Generated at 2022-06-14 09:24:01.936277
# Unit test for function get_new_command
def test_get_new_command():
    output = open('./unit_testing/aws_output.txt', 'r').read()
    command = MagicMock()
    command.output = output
    command.script = "aws sqs list-queues"
    print(get_new_command(command))

# Generated at 2022-06-14 09:24:11.339201
# Unit test for function get_new_command

# Generated at 2022-06-14 09:24:24.574728
# Unit test for function match
def test_match():
    assert match(Command('aws --help',
                         'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]'
                         '\naws: error: argument operation: Invalid choice: \'--help\', maybe you meant:'
                         '\n\t--help\n\t-h\n'))

    assert not match(Command('aws --help',
                             'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]'))
    assert not match(Command('aws --help',
                             'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]'
                             '\naws: error: argument operation: Invalid choice: \'--help\''))



# Generated at 2022-06-14 09:24:37.690143
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws ec2 describe-instances --instance-ids i-12345678')) == ['aws ec2 describe-instances --instance-id i-12345678']
    assert get_new_command(Command('aws ec2 describe_instances --instance-ids i-12345678')) == ['aws ec2 describe_instances --instance-id i-12345678']
    assert get_new_command(Command('aws ec2 describe-instances --instance-ids i-12345678 --profile prod')) == ['aws ec2 describe-instances --instance-id i-12345678 --profile prod']

# Generated at 2022-06-14 09:24:43.139027
# Unit test for function get_new_command
def test_get_new_command():
    command_input = mock.Mock(script='aws lambda list-functions',
                              output="usage: aws [options] <command> <subcommand> [parameters]\n\naws: error: argument subcommand: Invalid choice: 'subcommand', maybe you meant: *subcomand\n*subcomand2\n*subcommand\n\n")
    assert get_new_command(command_input) == ['aws lambda list-functions', 'aws lambda list-functions', 'aws lambda list-functions']

# Generated at 2022-06-14 09:24:53.109753
# Unit test for function get_new_command
def test_get_new_command():
    output = '''usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help
aws: error: argument subcommand: Invalid choice, maybe you meant:
* make
* take
* fak
  make
       Makes coffee.
'''
    command = 'aws fak make'
    assert get_new_command(Command(script=command,
                                          output=output,
                                          stderr=None)) == ['aws make make']

# Generated at 2022-06-14 09:25:03.393954
# Unit test for function get_new_command
def test_get_new_command():
    output = """usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help
aws: error: argument operation: Invalid choice, maybe you meant:
  autoscaling   ec2      elb      iam      rds
               s3       ses      sns      sqs

"""
    command = 'aws sumak'
    assert get_new_command(Command(command, output)) == [
        'aws autoscaling', 'aws ec2', 'aws elb', 'aws iam', 'aws rds',
        'aws s3', 'aws ses', 'aws sns', 'aws sqs']

# Generated at 2022-06-14 09:25:13.585846
# Unit test for function get_new_command

# Generated at 2022-06-14 09:25:19.238946
# Unit test for function match
def test_match():
    assert match(Command('aws s3 mv s3:\\foo \\bar',
                         'usage: aws [options] <command> '
                         '<subcommand> [<subcommand> ...] '
                         '[parameters] \nTo see help text, you can '
                         'run: \n\n  aws help \n  aws <command> '
                         'help \n  aws <command> <subcommand> '
                         'help \naws: error: argument '
                         'operation: Invalid choice, maybe you '
                         'meant: \n* mb \n* mv \n* presign \n* rb \n* '
                         'rb-iam \n* rm \n* sync\n',
                         '', 1))


# Generated at 2022-06-14 09:25:34.431469
# Unit test for function match

# Generated at 2022-06-14 09:25:47.201020
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    command = Command('aws ec2d start  --instance-ids 1223', 'Invalid choice: "ec2d", maybe you meant:\n* ec2\n* ec2-macro\n* ec2-net\n* ec2-pegasus\n* ec2-run-instances\n* ec2-signature\n* ec2-unsafe\n')

# Generated at 2022-06-14 09:25:49.876580
# Unit test for function match
def test_match():
    assert re.search(INVALID_CHOICE, command.output)
    assert re.findall(OPTIONS, command.output, flags=re.MULTILINE)


# Generated at 2022-06-14 09:25:52.847899
# Unit test for function get_new_command
def test_get_new_command():
    assert ['aws ec2 describe-instances'], get_new_command(
                                                    Command('aws ec2 describe-instanses'))

# Generated at 2022-06-14 09:26:03.751211
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws ec2 describe-instances --region us-west-1',
                                   'usage: aws [options] <command> <subcommand> [<subcommand> ...]\n'
                                   '[...]\n'
                                   'Invalid choice: \'describe-insances\', maybe you meant:\n'
                                   '\n'
                                   '   * describe-instances\n'
                                   '   * describe-instance-status\n'
                                   '\n'
                                   '[...]')) == ['aws ec2 describe-instances --region us-west-1',
                                                 'aws ec2 describe-instance-status --region us-west-1']

# Generated at 2022-06-14 09:26:09.056781
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("aws --version", "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters] \n\nTo see help text, you can run:\n\n  aws help\n\nUnknown options: --versiorn\n\nAvailable services:\n* ec2\n* elasticbeanstalk\n* iam\n* opsworks\n* route53\n\nUnknown options: --versiorn\nAn error occurred (InvalidParameterValue) when calling the operation: Invalid choice: '--version', maybe you meant: \n* version", "aws")

    assert get_new_command(command) == ["aws version"]

# Generated at 2022-06-14 09:26:20.036684
# Unit test for function match
def test_match():
    command = Command('aws foo', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\n'
                                 'To see help text, you can run:\n'
                                 '\n'
                                 '  aws help\n'
                                 '  aws <command> help\n'
                                 '  aws <command> <subcommand> help\n'
                                 '\n'
                                 'Unknown options: foo\n'
                                 'maybe you meant:\n'
                                 '	* foobar\n'
                                 '\n'
                                 'aws: error: argument subcommand: Invalid choice, valid choices are:\n'
                                 '	* foobar')
    assert match(command)


# Generated at 2022-06-14 09:26:34.111373
# Unit test for function get_new_command
def test_get_new_command():
    commands = ['ok', 'aws rds describe-db-instances']
    # New script for command 'aws rds describe-db-instances'
    new_command = 'aws rds describe-db-instances'
    assert get_new_command(commands[1])[0] == new_command
    # New script for command 'aws rds describe-db-instances --query'
    new_command = 'aws rds describe-db-instances --query'
    commands = ['ok', 'aws rds describe-db-instances --query']
    assert get_new_command(commands[1])[0] == new_command


enabled_by_default = True

# Generated at 2022-06-14 09:26:39.574917
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('aws configure --profile=test', 'aws: error: argument --profile: invalid choice: \'test\', maybe you meant: \n* test\n  test \'hi\'')
    assert get_new_command(command) == ['aws configure --profile=test', 'aws configure --profile=\'test hi\'']

# Generated at 2022-06-14 09:26:50.214785
# Unit test for function get_new_command
def test_get_new_command():
    script = "aws ec2 update-tags"
    output = """usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help

Unknown options: ec2, update-tags
aws: error: invalid choice: 'ec2 update-tags' (maybe you meant: 'ec2 update-tags-for-resource')"""
    command = Command(script, output)

    assert get_new_command(command) == ["aws ec2 update-tags-for-resource"]

# Generated at 2022-06-14 09:26:59.558107
# Unit test for function match
def test_match():
    assert match(Command("aws ec2 help", "usage: aws [options] <command> <subcommand> [parameters]\nInvalid choice: 'ec2', maybe you meant: \n    * elb\n    * ebs", "aws ec2 help"))
    assert not match(Command("aws ec2 help", "usage: aws [options] <command> <subcommand> [parameters]\nInvalid choice: 'ec2', maybe you meant: \n    * elb\n    * ebs", "aws ec2 help"))


# Generated at 2022-06-14 09:27:05.757818
# Unit test for function match

# Generated at 2022-06-14 09:27:13.540373
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('aws s3 ls --profile',
                      'usage: aws [options] \
                      <command> <subcommand> [<subcommand> ...] [parameters]\n\nTo see help text, you can run:\naws help\naws <command> help\naws <command> <subcommand> help\naws: error: argument operation: Invalid choice, \
                      maybe you meant: ls\nls\n* ls\n* mb\n* rb\n* cp\n* sync\n* mv\n* rm\n* rq\n* setacl\n* getacl\n* presign\n* wait\n* restore\n* toil\n* ls-queue\n* get-queue-url\n* sqs')

# Generated at 2022-06-14 09:27:21.668545
# Unit test for function match
def test_match():
    assert match(Command('aws help', 'usage: aws [options] <command> <subcomand> ' +
                                    '[<subcommand> ...] [parameters] ' +
                                    'To see help text, you can run: ' +
                                    'aws help <command> <subcommand> ... ' +
                                    'aws: error: argument subcommand: Invalid choice: ' +
                                    "'helper', maybe you meant: 'help' 'help' 'shell'"))


# Generated at 2022-06-14 09:27:27.456201
# Unit test for function get_new_command
def test_get_new_command():
    new_cmd = get_new_command("aws unknown usage: aws [options] <command> <subcommand> [<subcommand> ...]")
    assert new_cmd == ["aws unknown"]

    assert get_new_command("aws --unknown usage: aws [options] <command> <subcommand> [<subcommand> ...]") == ["aws"]

    new_cmd = get_new_command("aws s3 --unknown usage: aws [options] <command> <subcommand> [<subcommand> ...]")
    assert new_cmd == ["aws s3"]

    new_cmd = get_new_command("aws s3 ls --unknown usage: aws [options] <command> <subcommand> [<subcommand> ...]")
    assert new_cmd == ["aws s3 ls"]

    new_cmd = get_new_command

# Generated at 2022-06-14 09:27:31.754179
# Unit test for function get_new_command
def test_get_new_command():
    # For command.output "Invalid choice: 'no', maybe you meant:
    #  * node\n  * now",
    assert get_new_command(command) == [
        'aws s3 ls no', 'aws s3 ls now']


enabled_by_default = True

# Generated at 2022-06-14 09:27:42.392068
# Unit test for function get_new_command

# Generated at 2022-06-14 09:27:46.446230
# Unit test for function match
def test_match():
    assert match(Command('aws s3 ls', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] ... maybe you meant: ', False))


# Generated at 2022-06-14 09:27:56.249691
# Unit test for function match
def test_match():
    assert match(Command('dir log', output='usage: aws COMMAND [PARAMETERS] \
        [JSON-INPUT] [JSON-OUTPUT]\naws: error: argument command: Invalid choice: \
        \'./log.txt\', maybe you meant: logs'))
assert match(Command('pwd', output='usage: aws COMMAND [PARAMETERS] \
        [JSON-INPUT] [JSON-OUTPUT]\naws: error: argument pwd: Invalid choice: \
        \'pwd\', maybe you meant: pwds'))



# Generated at 2022-06-14 09:28:00.749878
# Unit test for function get_new_command
def test_get_new_command():
    result = get_new_command(command)
    assert result[0] == "['aws', 's3', 'ls']"
    assert result[1] == result[0]



# Generated at 2022-06-14 09:28:13.280451
# Unit test for function match
def test_match():
	assert  match(Command('aws command --help', 'usage: aws [options] <command> <subcommand> [<subcommand> ...]\n\n[aws cli v2]\naws: error: argument command: Invalid choice: \'command\', maybe you meant:')).output == "usage:"

# Generated at 2022-06-14 09:28:21.233325
# Unit test for function get_new_command
def test_get_new_command():
    c = ut.Command('aws s3 lisst bucket',
                   'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: Invalid choice: "s3", maybe you meant:\n  * s3api\n    s3-outposts\n\n')
    assert get_new_command(c) == ['aws s3api lisst bucket', 'aws s3-outposts lisst bucket']

# Generated at 2022-06-14 09:28:32.394079
# Unit test for function match
def test_match():
    assert match(Command('aws s3 ls', ''))
    assert match(Command('aws s3 ls', 'usage: aws [options] <command> <subcommand> [parameters]'))
    assert match(Command('aws s3 ls', 'usage: aws [options] <command> <subcommand> [parameters]\naws: error: argument command: Invalid choice: \'s3\'\n\nValid choices are:\n  *  -\n  *  iam\n  *  rds\n  *  ssm\n  *  maybe you meant: ec2'))
    assert not match(Command('aws s3 ls', 'usage: aws [options] <command> <subcommand> [parameters]\naws: error: argument command: Invalid choice: \'s3\''))

# Generated at 2022-06-14 09:28:44.281975
# Unit test for function get_new_command

# Generated at 2022-06-14 09:28:54.382375
# Unit test for function match