

# Generated at 2022-06-14 09:19:01.002631
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    command = Command('aws iam list-roles --profile development',
                      'An error occurred (InvalidClientTokenId) when calling the ListRoles operation: The security token included in the request is invalid.')
    assert get_new_command(command) == [
        'aws iam list-roles --profile develop']

# Generated at 2022-06-14 09:19:08.341852
# Unit test for function match
def test_match():
    assert match(Command(script='aws ec2', output='usage: aws [options] <command> <subcommand> [<subcommand> ...] ' \
                                                  '[parameters] To see help text, you can run: aws help aws ' \
                                                  'help <command> aws <command> help <subcommand> aws ' \
                                                  '<command> <subcommand> help Invalid choice: \'ec2\', maybe ' \
                                                  'you meant: * emr'))
    assert not match(Command(script='ls'))


# Generated at 2022-06-14 09:19:20.579399
# Unit test for function match

# Generated at 2022-06-14 09:19:30.840034
# Unit test for function match
def test_match():
    assert match(Command('aws s3 help', 'usage: aws [options] [ ...] [parameters]\n.....\nbad option: --help')) == True
    assert match(Command('aws s3 help', 'usage: aws [options] [ ...] [parameters]\n.....\nbad option: --help\nmaybe you meant: --a')) == True
    assert match(Command('aws s3 help', 'usage: aws [options] [ ...] [parameters]\n.....\nbad option: --help\nmaybe you meant: --a --b')) == True
    assert match(Command('ls', 'usage: ls')) == False


# Generated at 2022-06-14 09:19:36.835219
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

# Generated at 2022-06-14 09:19:48.930498
# Unit test for function match

# Generated at 2022-06-14 09:19:58.331275
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script='aws s3 bash', output='Invalid choice: \'bash\', maybe you meant:\n  * bash', stderr='usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument operation: Invalid choice, valid choices are:')) == ['aws s3 help']

# Generated at 2022-06-14 09:20:03.513484
# Unit test for function match
def test_match():
    assert match(Command('ls abc', "", "ls: cannot access 'abc': No such file or directory\nls: cannot access 'def': No such file or directory", 2, ""))
    assert not match(Command('ls', "", "", 0, ""))


# Generated at 2022-06-14 09:20:06.716215
# Unit test for function match
def test_match():
    assert match(Command('aws s3 lis', 'aws s3 ls\nusage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run: aws help\naws: error: argument subcommand: Invalid choice, valid choices are:\ncp\ncopy\nmb\nmove\nrb\nsync\n'))


# Generated at 2022-06-14 09:20:08.326264
# Unit test for function match
def test_match():
    assert match(Command('aws sts'))


# Generated at 2022-06-14 09:20:15.047144
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.aws_command_not_found import get_new_command
    assert get_new_command(Command('aws s3 mb s3://foo', 'aws: error: argument subcommand: Invalid choice', '')) == ['aws s3 mb s3://foo']
    


# Generated at 2022-06-14 09:20:18.969409
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 describe-images --owner 1234567', ''))
    assert not match(Command('aws ec2 describe-images', ''))



# Generated at 2022-06-14 09:20:30.436230
# Unit test for function match
def test_match():
    assert not match(Command('aws-e'))
    assert not match(Command('ls foo'))


# Generated at 2022-06-14 09:20:32.823427
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('aws ec2 describe-instances')
    assert get_new_command(command) == ['aws ec2 describe-images']



# Generated at 2022-06-14 09:20:40.888997
# Unit test for function match

# Generated at 2022-06-14 09:20:48.955323
# Unit test for function match
def test_match():
	assert match(Command("aws --help", "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument command: Invalid choice, valid choices are:\n\n  cloudformation\n  configure\n  ec2\n  help\n  iam\n  s3\n  sns\n  sqs\n\nMaybe you meant:\n\n  cloudformation\n  ec2\n  iam\n  s3\n  sns\n  sqs\n\n", "aws --help", 1)) == True

# Generated at 2022-06-14 09:20:52.437317
# Unit test for function get_new_command
def test_get_new_command():
    actions = ["fp", "deploy", "ge"]
    for action in actions:
        assert get_new_command(Command('aws ' + action, ""))


# Generated at 2022-06-14 09:21:01.701478
# Unit test for function match

# Generated at 2022-06-14 09:21:14.543227
# Unit test for function match
def test_match():
    """ match should be True when error is like "Invalid choice: '', maybe you meant: " """
    assert match(Command('aws', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters] \nTo see help text, you can run: \n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument subcommand: Invalid choice: \'\', maybe you meant: \n\tconfigure (choose from \'adm-list-devices\', \'adm-bulk-register-devices\', \'adm-create-platform-endpoint\', \'adm-get-endpoint-attribu\'...)\n'))


# Generated at 2022-06-14 09:21:23.487419
# Unit test for function match
def test_match():
    assert match(Command('aws s3 ls',
                         "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\n"
                         "To see help text, you can run:\n"
                         "aws help\n"
                         "aws <command> help\n"
                         "aws <command> <subcommand> help\n"
                         "unknown command: s3\n"
                         "maybe you meant:\n"
                         "* s3api",
                         ''))


# Generated at 2022-06-14 09:21:35.344555
# Unit test for function get_new_command
def test_get_new_command():
    script = 'aws ec2 describe-images --image-ids ami-12344444444444'

# Generated at 2022-06-14 09:21:43.714147
# Unit test for function match
def test_match():
    assert match(Command('aws help', 'aws: error: Invalid choice: "hellp"\n'
                                     'usage: aws [options] <command> <subcommand> [parameters]\n'
                                     "aws: error: the following arguments are required: command\n"
                                     "maybe you meant:\n'* help'\n'* ecs'\n'* ec2'\n"))
    assert not match(Command('ls /tmp', 'ls: cannot access /tmp: No such file or directory'))


# Generated at 2022-06-14 09:21:50.380604
# Unit test for function match

# Generated at 2022-06-14 09:21:56.289509
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws s3 ups',
                                   stderr='aws: error: invalid choice: s3 ups\naws: error: might you meant: s3 cp\n')) == ['aws s3 cp ups']

# Generated at 2022-06-14 09:22:04.977630
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 describe-volumes',
                         'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run: aws help\nUnknown options: ec2, describe-volumes\n',
                         'aws: error: argument subcommand: Invalid choice, valid choices are:\n\tcp\n\tls\n\n',
                         'aws: error: argument subcommand: Invalid choice, valid choices are:\n\tcp\n\tls\n\n',
                         'Invalid choice: \'ec2\', maybe you meant:\n\tcp\n\tls\n\tcp\n\tls\n\n'))

# Generated at 2022-06-14 09:22:16.872641
# Unit test for function get_new_command
def test_get_new_command():
    """
    Test function get_new_command with command line input of form:
    "aws ec2 describe-instances --instance-ids i-123456"
    """
    import subprocess
    p = subprocess.Popen("aws ec2 describe-instances --instance-ids i-123456", stdout=subprocess.PIPE, shell=True)
    (output, _) = p.communicate()
    cli = "aws ec2 describe-instances --instance-ids i-123456"
    command = type('obj', (object,), {'script': cli, 'output': output})
    new_command = get_new_command(command)
    assert(new_command[0] == "aws ec2 describe-instances --instance-id i-123456")

# Generated at 2022-06-14 09:22:20.120780
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws something', 'aws: error: Invalid choice: "something", maybe you meant:', 'aws something')) == ['aws something-something']



# Generated at 2022-06-14 09:22:32.186565
# Unit test for function match
def test_match():
    assert match(Command('aws s3 ls mybu', '', 'usage: aws [options] <command> <subcommand> [parameters]\naws: error: argument <command>: Invalid choice, maybe you meant:\n\tls\nSee \'aws help\'.'))
    assert not match(Command('ls mybu', '', 'usage: aws [options] <command> <subcommand> [parameters]\naws: error: argument <command>: Invalid choice: \'mybu\', maybe you meant:\n\tls\nSee \'aws help\'.'))

# Generated at 2022-06-14 09:22:36.225638
# Unit test for function match
def test_match():
    command = Command("aws s3 mb s3://foo", "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\n"
        "To see help text, you can run:\n"
        "aws help\n"
        "aws <command> help\n"
        "aws <command> <subcommand> help\n"
        "aws: error: argument command: Invalid choice, maybe you meant:\n"
        "\tmb\n"
        "\tmbox\n"
        "\tms\n"
        "\tmsi\n"
        "\tmv\n")
    assert match(command)



# Generated at 2022-06-14 09:22:40.593846
# Unit test for function match
def test_match():
    assert match(Command("aws ec2 describe-instance-attribute --instance-id i-12345678 --attribute blockDeviceMapping"))

# Generated at 2022-06-14 09:22:48.687556
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws ec2 describe-instances')) == ['aws ec2 describe-instances',
                                                                       'aws ec2 describe-instances --help']

# Generated at 2022-06-14 09:22:52.046890
# Unit test for function match
def test_match():
	assert match("usage: aws [options] [ ...] (see aws help topics)" in command.output) == True
	assert match("usage: aws [options] [ ...] (see aws help topics)" in command.output) == False

# Generated at 2022-06-14 09:22:57.817961
# Unit test for function match
def test_match():
    output = "usage: aws [options] &lt;command&gt; &lt;subcommand&gt; [parameters]\n\nTo see help text, you can run:\n\n  aws help\n  aws &lt;command&gt; help\n  aws &lt;comman"
    assert match(Command('', output))


# Generated at 2022-06-14 09:23:04.149877
# Unit test for function get_new_command
def test_get_new_command():
    command = type(
        'Command', (object,),
        {'script': 'aws ec2 describe-instances', 'output':
         """
         aws: error: argument operation: Invalid choice: 'describe-insances', maybe you meant:
          * describe-instance-status
          * describe-instances
         """})()
    new_command = get_new_command(command)
    assert new_command == ['aws ec2 describe-instance-status',
                           'aws ec2 describe-instances']

# Generated at 2022-06-14 09:23:06.291944
# Unit test for function match
def test_match():
    assert match(Command('aws s3 ls s3:///bucket/', 'aws: error: argument command: Invalid choice: \'ls\', maybe you meant:',
                         '~/aws/cli'))


# Generated at 2022-06-14 09:23:18.344886
# Unit test for function match
def test_match():
    assert match(Command(script='aws',
                         output='usage: aws [options] '
                                '<command> <subcommand> [<subcommand> ...] '
                                '[parameters]\n'
                                'To see help text, you can run:\n'
                                '\n'
                                '  aws help\n'
                                '  aws <command> help\n'
                                '  aws <command> <subcommand> help\n'
                                '\n'
                                'aws: error: argument command: Invalid choice: '
                                "'s3 cp', maybe you meant:\n"
                                '  * s3api\n'
                                '  * s3',
                         stderr='')) == True


# Generated at 2022-06-14 09:23:27.997121
# Unit test for function get_new_command

# Generated at 2022-06-14 09:23:36.442176
# Unit test for function match

# Generated at 2022-06-14 09:23:50.309549
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws cli', 'Invalid choice: \'cli\', maybe you meant:\n * create-alias\n * create-user')) == ['aws create-alias', 'aws create-user']
    assert get_new_command(Command('aws list', 'Invalid choice: \'list\', maybe you meant:\n * help\n * list-users')) == ['aws help', 'aws list-users']
    assert get_new_command(Command('aws alias', 'Invalid choice: \'alias\', maybe you meant:\n * create-alias\n * delete-alias')) == ['aws create-alias', 'aws delete-alias']
    assert get_new_command(Command('aws user-create', 'Invalid choice: \'user-create\', maybe you meant:\n * create-user')) == ['aws create-user']

# Generated at 2022-06-14 09:24:02.455803
# Unit test for function match
def test_match():
    assert match(Command('aws help --version',
        'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\n'
        'To see help text, you can run:\n'
        'aws help\n'
        'aws <command> help\n'
        'aws <command> <subcommand> help\n'
        'aws: error: argument --version: Invalid choice: "--version", maybe you meant: --version-name\n'
        '* --version-name\n'
        '  --versioning-state\n'
        '  --versioning\n'
        '  --versions'))

# Generated at 2022-06-14 09:24:25.065289
# Unit test for function match

# Generated at 2022-06-14 09:24:29.969155
# Unit test for function get_new_command
def test_get_new_command():
    output = "Invalid choice: 'usr', maybe you meant: \n\t* user"
    assert get_new_command(Command('aws usr', output)) == \
        ['aws user']

    output = ("*  amazon-linux-ami-2015.03.g-amazon-ecs-optimized\n"
              "   amazon-linux-ami-2015.03-al2-x86-64-s3-ebs")
    assert get_new_command(Command('aws commands', output)) == \
        ['aws amazon-linux-ami-2015.03.g-amazon-ecs-optimized',
         'aws amazon-linux-ami-2015.03-al2-x86-64-s3-ebs']


# Generated at 2022-06-14 09:24:41.054221
# Unit test for function get_new_command

# Generated at 2022-06-14 09:24:45.253846
# Unit test for function match
def test_match():
    assert match(Command('ls somedir', stderr='usage: ls [FILE]...'))
    assert not match(Command('ls somedir', stderr='somestring'))


# Generated at 2022-06-14 09:24:51.098728
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 stop-instances --instance-ids sg-00b6a8d4014f6ee02', '')) == True
    assert match(Command('aws ec2 stop-instances --instance-ids sg-00b6a8d4014f6ee02', 'usage:')) == False


# Generated at 2022-06-14 09:24:53.012198
# Unit test for function match
def test_match():
    assert match(Command(script='aws --version'))


# Generated at 2022-06-14 09:24:54.840731
# Unit test for function match
def test_match():
    assert match(Command('aws help'))


# Generated at 2022-06-14 09:25:01.534480
# Unit test for function match

# Generated at 2022-06-14 09:25:09.796576
# Unit test for function get_new_command
def test_get_new_command():
    command1 = type('Command', (object,), { 'script': "aws ec2 describe-instances --instance-ids i-123",
                                            'output': "Invalid choice: '--instance-ids', maybe you meant:\n\
* --instance-id" })
    assert get_new_command(command1) == ["aws ec2 describe-instances --instance-id i-123"]

    command2 = type('Command', (object,), { 'script': "aws ec2 describe-instances --instance-ids i-123 i-456",
                                            'output': "Invalid choice: '--instance-ids', maybe you meant:\n\
* --instance-id" })
    assert get_new_command(command2) == ["aws ec2 describe-instances --instance-id i-123 i-456"]

# Generated at 2022-06-14 09:25:16.518633
# Unit test for function match
def test_match():
    assert match(Command('aws iam delete-user --user-name ', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nto see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument operation: Invalid choice, valid choices are: \ndelete-login-profile\ndelete-user\n'))


# Generated at 2022-06-14 09:25:48.066538
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws --no-verify-s3-bucket-sig', 'usage: aws [options] <command> <subcommand> [<subcommand> ...]\naws: error: argument --no-verify-s3-bucket-sig: Invalid choice: \'--no-verify-s3-bucket-sig\', maybe you meant:\n\n  * verify-s3-bucket-signature\n\naws: error: the following arguments are required: command', 'aws --no-verify-s3-bucket-sig'))\
        == ['aws verify-s3-bucket-signature']


enabled_by_default = False

# Generated at 2022-06-14 09:26:01.276782
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws s3p help', "Invalid choice: 's3p', maybe you meant:\n        * s3api\n        * s3\n")) == ['aws s3api help', 'aws s3 help']
    assert get_new_command(Command('aws asd help', "Invalid choice: 'asd', maybe you meant:\n        * s3api\n        * s3\n")) == ['aws s3api help', 'aws s3 help']
    assert get_new_command(Command('aws s3 help', "Invalid choice: 's3', maybe you meant:\n        * s3api\n        * s3\n")) == ['aws s3api help', 'aws s3 help']

# Generated at 2022-06-14 09:26:09.485227
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws s3 ls', 'usage: aws [options] [parameters]\naws: error: argument operation: Invalid choice: \'s3 ls\', maybe you meant:\n\t        s3 ls\n\ts3 mb\n\ts3 cp\n\ts3 sync\n\ts3 rb\n\ts3 rm\n\ts3 mv\n\ts3 presign\n\ts3api ...\n', '')) == ['aws s3 ls']

# Generated at 2022-06-14 09:26:18.224963
# Unit test for function get_new_command
def test_get_new_command():
    output = """usage: aws [options] <command> <subcommand> [parameters]
aws: error: argument subcommand: Invalid choice, valid choices are:
\tsubcommand1
\tsubcommand2
\tsubcommand3
\tsubcommand4

See 'aws help' for descriptions of global parameters."""

    command = Command('aws subcommaand1')
    command.output = output
    assert get_new_command(command) == ['aws subcommand1', 'aws subcommand2', 'aws subcommand3', 'aws subcommand4']

# Generated at 2022-06-14 09:26:34.723911
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 help', ''))

# Generated at 2022-06-14 09:26:41.741398
# Unit test for function match
def test_match():
    assert match(Command('aws help', 'usage: aws [options] <command> <subcommand> [parameters]\nThe most widely used AWS CLI command\n'))
    assert match(Command('aws help', "usage: aws [options] <command> <subcommand> [parameters]\nThe most widely used AWS CLI command\n"))
    assert not match(Command(''))


# Generated at 2022-06-14 09:26:52.529008
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 describe-images', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters] To see help text, you can run:', 'aws help', 'aws <command> help', 'aws <command> <subcommand> help', 'aws: error: argument command: Invalid choice: \'ec2 describe-images\', maybe you meant:', '', '   ec2', '   describe-images'))

    assert not match(Command('aws --help', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]', 'To see help text, you can run:', 'aws help', 'aws <command> help', 'aws <command> <subcommand> help'))


# Generated at 2022-06-14 09:26:59.666952
# Unit test for function match
def test_match():
    assert match(Command('aws s3 mb s3://bucket',
                "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\n\n"
                "error: Invalid choice: 'mb', maybe you meant:\n"
                "    mb (move a local file to S3)\n"
                "    rb (remove a bucket)\n"
                "\n"
                "To see help text, you can run:\n"
                "  aws help\n"
                "  aws <command> help\n"
                "  aws <command> <subcommand> help\n\n"))


# Generated at 2022-06-14 09:27:10.804944
# Unit test for function get_new_command
def test_get_new_command():
    # Test for a command with aws-cli commands in second and third position
    output = """
usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help
aws: error: argument subcommand: Invalid choice: 'ec2', maybe you meant:
    configservice  ecs         et
"""
    script = 'aws ec2 ls'
    command = Command(script, output)
    assert get_new_command(command) == ['aws configservice ec2 ls', 'aws ecs ec2 ls', 'aws et ec2 ls']

    # Test for a command with aws-cli commands in the first position

# Generated at 2022-06-14 09:27:21.976359
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws ec2 start-instance i-1234', 'aws: error: argument instance: Invalid choice', 'aws: error: argument instance: Invalid choice: \'i-1234\', maybe you meant: * i-123456')) == ['aws ec2 start-instance i-123456']

# Generated at 2022-06-14 09:28:16.645255
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script='aws ec2 start-instances',
                      stdout='usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument instance: Invalid choice: "i-12f594e8", maybe you meant:\n  * i-12f594e\n* i-12f594f',
                      stderr='')

# Generated at 2022-06-14 09:28:26.436795
# Unit test for function match
def test_match():
    output = "Unknown options: --otions"
    assert (match(Command('aws ec2 describe-instances --otions', output)) ==
            "usage:" in output and "maybe you meant:" in output)

    output = "Unknown options: --otions"
    assert (match(Command('aws ec2 describe-instances', output)) !=
            "usage:" in output and "maybe you meant:" in output)


# Generated at 2022-06-14 09:28:38.801495
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

    command = Command('aws help', 'aws: error: argument subcommand: Invalid choice, valid choices are:\n'
                                 '  ec2                                 |  rds\n'
                                 '  dynamodb                            |  route53\n'
                                 '  cloudformation                      |  s3\n'
                                 '  elasticache                         |  ses\n'
                                 'aws: error: too few arguments\n')

    assert get_new_command(command) == ['aws ec2 help',
                                        'aws rds help',
                                        'aws dynamodb help',
                                        'aws route53 help',
                                        'aws cloudformation help',
                                        'aws elasticache help',
                                        'aws s3 help',
                                        'aws ses help']


enabled_by

# Generated at 2022-06-14 09:28:39.566641
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('aws --help') == ['aws --help']



# Generated at 2022-06-14 09:28:47.272012
# Unit test for function get_new_command
def test_get_new_command():
    output = ''
    expect = []
    with open('test_match_aws.output', 'rb') as f:
        output = f.read().decode('utf-8')
    with open('test_match_aws.expect', 'rb') as f:
        expect = f.read().decode('utf-8')
    expect = expect.rstrip()
    command = Command('aws --region us-west-1 ec2 describe-instances', output)
    assert get_new_command(command) == [expect]

# Generated at 2022-06-14 09:28:59.069004
# Unit test for function get_new_command
def test_get_new_command():
    # arg_1 should be replaced with arg_2, we will test this in our test cases below
    arg_1 = 's3'
    arg_2 = 's3api'

    # test_case_1: the output of the command is just the mistake, no options
    # the get_new_command funtion should return one command with the mistake replaced
    test_case_1_command = 'aws ' + arg_1