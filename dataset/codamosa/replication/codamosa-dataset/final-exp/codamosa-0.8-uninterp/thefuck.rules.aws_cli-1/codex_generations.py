

# Generated at 2022-06-14 09:19:05.476893
# Unit test for function match
def test_match():
    # Test 1
    command = Command('aws', 'aws: error: argument --region: Invalid choice: "us-west-3", maybe you meant:')
    assert match(command) == True
    # Test 2
    command = Command('aws', 'aws: error: argument --region: Invalid choice: "us-west-3", maybe you meant:')
    assert match(command) == True
    # Test 3
    command = Command('aws', 'aws: error: argument --region: Invalid choice: "us-west-3", maybe you meant:')
    assert match(command) == True


# Generated at 2022-06-14 09:19:17.698799
# Unit test for function get_new_command
def test_get_new_command():
    test_invalid_choice = "aws s3api get-bucket-versioni"

# Generated at 2022-06-14 09:19:22.969357
# Unit test for function get_new_command
def test_get_new_command():
    new_command = get_new_command(type('obj', (object,), {'script': 'aws --version', 'output': 'usage: aws [options] <command> <subcommand> [<subcommand> ...]'}))
    assert new_command == ['aws --help']

# Generated at 2022-06-14 09:19:34.003555
# Unit test for function get_new_command

# Generated at 2022-06-14 09:19:40.020126
# Unit test for function match
def test_match():
    assert not match(Command('aws'))
    assert match(Command('aws', stderr='...\naws: error: Invalid choice: "wtf", maybe you meant: ...'))
    assert match(Command('aws', stderr='error: Invalid choice: "wtf", maybe you meant: "wtf"\n...'))


# Generated at 2022-06-14 09:19:48.041044
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script='aws s3 cp 5.txt s3://bucket/',
                                   output='usage: aws [options]\n'
                                          'aws: error: argument command: Invalid choice: \'5.txt\', maybe you meant:\n'
                                          '\tcloudfront\n'
                                          '\ts3cp\n')) == ['aws s3 cp cloudfront s3://bucket/', 'aws s3 cp s3cp s3://bucket/']

# Generated at 2022-06-14 09:19:53.778686
# Unit test for function get_new_command
def test_get_new_command():
    examples = [
        ('aws ec2 descibe-instances',
         ['aws ec2 describe-instances']),

        ('aws ec2 stop-instances --instance-ids i-0e8e7cd5f5d5d788d --force',
         ['aws ec2 stop-instances'])
    ]

    for example in examples:
        command, output = example
        assert get_new_command(Command(command, '', '', output, output)) == output

enabled_by_default = True

# Generated at 2022-06-14 09:19:57.113313
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 describe-instances --region us-east-1', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\n\nUnknown options: --region, us-east-1\nInvalid choice: \'--region, us-east-1\', maybe you meant:', ''))

# Generated at 2022-06-14 09:20:09.067394
# Unit test for function get_new_command

# Generated at 2022-06-14 09:20:15.340399
# Unit test for function get_new_command
def test_get_new_command():
    get_new_command_TEST = get_new_command('aws s3 ls s3:/bucket/object --profile testprofile1')
    assert get_new_command_TEST == [
                                    'aws s3 ls s3:/bucket/object --profile testprofile2',
                                    'aws s3 ls s3:/bucket/object --profile testprofile3'
                                    ]

# Generated at 2022-06-14 09:20:25.535013
# Unit test for function get_new_command
def test_get_new_command():
    script = "aws ec2 deetach-instance-from-load-balancer"
    output = "aws: error: argument operation: Invalid choice: 'deetach-instance-from-load-balancer', maybe you meant:\n" + \
             "  * detach-instance-from-load-balancer  \n" + \
             "  * describe-instance-attribute-value"
    result = ['aws ec2 detach-instance-from-load-balancer', 'aws ec2 describe-instance-attribute-value']
    assert get_new_command(Command(script, output)) == result

# Generated at 2022-06-14 09:20:35.208936
# Unit test for function match
def test_match():
    assert match(Command(script='aws s3 ls bucket', output='usage: aws [...)', stderr='usage: aws [...)'))
    assert match(Command(script='aws s3 cp localdir s3://bucket', output='usage: aws [...)', stderr='usage: aws [...)'))
    assert not match(Command(script='aws s3 ls bucket', output='aws: command not found', stderr='aws: command not found'))
    assert not match(Command(script='aws s3 cp localdir s3://bucket', output='usage: some-command [...)', stderr='usage: some-command [...)'))


# Generated at 2022-06-14 09:20:42.555345
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('aws ec2 describe-instances --filter Name=ip-address,Values=123.123.123.123', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] \n\naws: error: argument filter: Invalid choice: \'ip-address\', maybe you meant: \n* ip-address-type \n')
    assert get_new_command(command) == ['aws ec2 describe-instances --filter Name=ip-address-type,Values=123.123.123.123']

# Generated at 2022-06-14 09:20:46.533184
# Unit test for function match
def test_match():
    command1 = 'aws ec2 describe-instances'
    command2 = 'aws ec2 describe-instances --hash'
    assert match(command1)
    assert not match(command2)

# Generated at 2022-06-14 09:20:58.131515
# Unit test for function match
def test_match():
    assert not match(Command(script='aws ec2',
                             stderr='usage: aws [options] [parameters]\naws: error: argument command: Invalid choice')
                 )
    assert match(Command(script='aws ec2',
                         stderr='''usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help
aws: error: argument command: Invalid choice 'ec2', maybe you meant:
* ec21
* ec22
'''
                         )
                 )



# Generated at 2022-06-14 09:21:13.331477
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.aws_cli import get_new_command

# Generated at 2022-06-14 09:21:21.202560
# Unit test for function match
def test_match():
    assert match(Command(script='', output='usage: aws [options] <command> <subcommand> [parameters] ...'))
    assert match(Command(script='', output='usage: fk [options] <command> <subcommand> [parameters] ...'))
    assert match(Command(
        script='',
        output='''usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]

To see help text, you can run:
aws help
aws <command> help
aws <command> <subcommand> help
aws: error: argument command: Invalid choice, maybe you meant:
* help
* ec2
* s3
'''))

# Generated at 2022-06-14 09:21:28.564310
# Unit test for function match
def test_match():
    output = "usage: aws [options] [ ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws help cli error: Invalid choice: 'testing', maybe you meant: * cli\n  elb\n  dynamodb\n  rds\n  r53\n  sns\n  s3\n  sqs\n  sts\n  cloudformation\n\n  (aws) "
    assert match(Command('aws testing', output))


# Generated at 2022-06-14 09:21:32.259276
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws ec2 start_instances --instance-ids i-007')) == ['aws ec2 start-instances --instance-ids i-007']
    assert get_new_command(Command('aws ec2 retriev-instances --instance-ids i-007')) == ['aws ec2 retrieve-instances --instance-ids i-007']



# Generated at 2022-06-14 09:21:41.581608
# Unit test for function get_new_command
def test_get_new_command():
    output = '''usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help
aws: error: argument subcommand: Invalid choice: 'coomand', maybe you meant:
    * command
    * commands'''
    command = Command('aws coomand --help', output=output)
    assert get_new_command(command) == ['aws command --help', 'aws commands --help']

# Generated at 2022-06-14 09:21:46.541136
# Unit test for function match
def test_match():
    assert match(Command('aws s3', output='usage: aws [options] <command> <subcommand> [parameters]\naws: error: argument subcommand: Invalid choice: "s3"\n'));


# Generated at 2022-06-14 09:21:53.138018
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws s3 ls', 'Invalid choice: \'s3\', maybe you meant:\ns3api\n')) == ['aws s3api ls']
    assert get_new_command(Command('aws s3 ls', 'Invalid choice: \'s3\', maybe you meant:\ns3api\ns3api\n')) == ['aws s3api ls', 'aws s3api ls']



# Generated at 2022-06-14 09:22:03.991717
# Unit test for function get_new_command
def test_get_new_command():
    command = "aws ec2 delete-volume --volume-id vol-123bece5"
    output = "\nusage: aws [options] &lt;command&gt; &lt;subcommand&gt; [parameters]\naws: error: argument operation: Invalid choice, valid choices are:\n        attach-volume | attach-vpn-gateway | create-volume | create-vpc | create-vpn-gateway\n        delete-volume | delete-vpc | delete-vpn-gateway | detach-volume | detach-vpn-gateway\n        describe-volume | describe-volumes | describe-vpc | describe-vpcs | describe-vpn-gateway\n        describe-vpn-gateways\n        (maybe you meant: delete-volume)\n"

# Generated at 2022-06-14 09:22:07.079185
# Unit test for function match
def test_match():
    command = Command('aws "ec2" "describe-instances"')
    assert match(command)


# Generated at 2022-06-14 09:22:13.308467
# Unit test for function get_new_command
def test_get_new_command():
    old = Command('aws ec2 describe-instances --profile dev')
    new = [Command('aws ec2 describe-instances --query \'Reservations[*].Instances[*].[Tags[?Key==`Name`].Value | [0],InstanceId,PublicIpAddress,State.Name,InstanceType,LaunchTime]\' --output text --profile dev')]
    assert get_new_command(old) == new

# Generated at 2022-06-14 09:22:18.785879
# Unit test for function match

# Generated at 2022-06-14 09:22:20.082462
# Unit test for function match
def test_match():
    assert match(Command("aws ec2 brazil-south-1"))


# Generated at 2022-06-14 09:22:28.057303
# Unit test for function get_new_command
def test_get_new_command():
    command_output = "usage: aws [options] <command> <subcommand> [parameters]\naws: error: argument command: Invalid choice: 'configure', maybe you meant:\n\tconfigure\n* create\n\tdeveloper-guide\n"
    command = Command(script='aws configure', output=command_output, stderr='')
    assert get_new_command(command) == ['aws configure', 'aws create', 'aws developer-guide']

# Generated at 2022-06-14 09:22:38.381978
# Unit test for function match
def test_match():
        assert match(Command('aws s3 mb --dry-', 'usage: aws [options] <command> <subcommand> [parameters]\naws: error: unrecognized arguments: --dry-\n', 'aws s3 mb --dry-run s3://test.bucket'))
        assert not match(Command('aws s3 mb --dry-run s3://test.bucket', 'usage: aws [options] <command> <subcommand> [parameters]\naws: error: unrecognized arguments: --dry-\n', 'aws s3 mb --dry-run s3://test.bucket'))


# Generated at 2022-06-14 09:22:52.047148
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('aws --endpoint-url https://blah.com s3api create-bucket --bucket 1234567-twice-a-day --region us-east-1', 'aws: error: argument --bucket: Invalid choice: "1234567-twice-a-day". Maybe you meant:\n  * abcdefghi\n  * jklmnopqr\n  * stuvwxyz\n\nUnknown options: --bucket\nusage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:')

# Generated at 2022-06-14 09:22:58.041985
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws cloudfornctaion vlalidate', '')) == ['aws cloudformation validate']


enabled_by_default = False

# Generated at 2022-06-14 09:23:06.697740
# Unit test for function get_new_command

# Generated at 2022-06-14 09:23:18.874295
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('aws ec2 --reboot-instances --instance-ids i-0b263912') == ['aws ec2 reboot-instances --instance-ids i-0b263912']
    assert get_new_command('aws ec2 --stop-instances --instance-ids i-0b263912') == ['aws ec2 stop-instances --instance-ids i-0b263912']
    assert get_new_command('aws ec2 --start-instances --instance-ids i-0b263912') == ['aws ec2 start-instances --instance-ids i-0b263912']

# Generated at 2022-06-14 09:23:27.134474
# Unit test for function get_new_command
def test_get_new_command():
    output = "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument subcommand: Invalid choice, maybe you meant:\n    ses\n    sdb\n    s3\n    swf\n    sqs\n    sns\n    sts\n    ses"
    script = "aws s3"
    command = get_new_command(Command(script, output))
    assert command[0] == "aws sqs"

# Generated at 2022-06-14 09:23:34.679527
# Unit test for function get_new_command
def test_get_new_command():
    commands = ['aws help']
    fixed_command = 'aws help'
    assert get_new_command(Command(commands, 'The AWS CLI is the official command line interface for AWS.\nusage: aws [options] <command> <subcommand> [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument --output: Invalid choice: \'test_option\' (choose from json, text, table)\n\nUnknown options: --output, (test_option)\n', '')) == [fixed_command]


# Generated at 2022-06-14 09:23:41.087864
# Unit test for function get_new_command
def test_get_new_command():
    command = MagicMock()
    command.output = "usage: aws [options] <command> <subcommand> [parameters]\naws: error: argument command: Invalid choice: 'mytest', maybe you meant:\n        * mytest\n"
    command.script = "aws mytest"
    assert get_new_command(command) == [
        "$ aws mytest",
        "$ aws mytest"]

enabled_by_default = True

# Generated at 2022-06-14 09:23:48.161550
# Unit test for function match

# Generated at 2022-06-14 09:23:56.463050
# Unit test for function match

# Generated at 2022-06-14 09:24:03.933345
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("aws cli", output = """usage: aws [options] <command> <subcommand> [parameters]
aws: error: argument command: Invalid choice, maybe you meant:
    cloudformation
    cloudwatch
    events
    lambda
    s3api

See 'aws help' for descriptions of global parameters.
""")).startswith("aws cloudformation")
    print("Unit test for function get_new_command completed.")

# Generated at 2022-06-14 09:24:09.760061
# Unit test for function match
def test_match():
    # test case 1
    output = '''
usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help
aws: error: argument command: Invalid choice, valid choices are:'''

    assert match(Command('aws', output=output))


# Generated at 2022-06-14 09:24:24.746299
# Unit test for function match
def test_match():
    command = Command('aws ec2 run-instances', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument command: Invalid choice, maybe you meant:  ec2\n\nUnknown options: run-instances')
    assert match(command)


# Generated at 2022-06-14 09:24:33.868175
# Unit test for function match
def test_match():
    assert (match(Command('aws ec2',
                          'usage: aws [options] <command> <subcommand> [parameters]\nTo see help text, you can run:\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument command: Invalid choice, maybe you meant:',
                          'aws: error: argument command: Invalid choice, maybe you meant:\n  config\n  configure\n  iam')).group())


# Generated at 2022-06-14 09:24:42.300101
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 start-instances --instance-ids i-12345678',
            'aws: error: argument --instance-ids: Invalid choice: \'i-12345678\', maybe you meant:', ''))

    assert not match(Command('aws ec2 start-instances --instance-ids i-12345678', '', ''))

    assert match(Command('aws ec2 stop-instances --instance-ids i-12345678',
            'aws: error: argument --instance-ids: Invalid choice: \'i-12345678\', maybe you meant:', ''))


# Generated at 2022-06-14 09:24:53.010302
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 run-instances --help',
        'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument operation: Invalid choice, maybe you meant:\n  run-instances  (this is acommand)\n  stop-instances  (this is a different command)\nSee \'aws help\' for descriptions of global parameters.'))
    assert not match(Command('aws ec2 run-instances --help', ''))


# Generated at 2022-06-14 09:25:03.615393
# Unit test for function match
def test_match():

    # create a Command object with outputs that are commonly seen when
    # running `aws help`
    test_command = Command("aws --help", "aws: error: argument command: Invalid choice: '--help', maybe you meant:  \n* help\n* help-topic \n\nUnknown options: --help\n")

    # assert that the match function returns true when `command.output`
    # contains `maybe you meant:`
    assert match(test_command) is True

    # declare a new Command that does not return any output that matches
    # the pattern that our match function is looking for
    test_command2 = Command("aws --help", "")

    # assert that the match function returns False when the `command.output`
    # does not contain the pattern that the match function is looking for
    assert match(test_command2) is False


# Generated at 2022-06-14 09:25:14.446216
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 start-instance i-1234567', 'usage: aws [options] \n\
        <command> <subcommand> [<subcommand> ...] [parameters]\n\
        To see help text, you can run:\n\
        \n\
        aws help\n\
        aws <command> help\n\
        aws <command> <subcommand> help\n\
        \n\
        Unknown options: i-1234567\n\
        \n\
        Unknown options:\n\
        \n\
            i-1234567\n\
        \n\
        ', ''))



# Generated at 2022-06-14 09:25:23.904406
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script='aws ec2 describe-instances --filter',
                          output='usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument --filter: Invalid choice: \'someNonExistentParameter\', maybe you meant:* filter\n\nUnknown options: --filter\n'
                          )) == ['aws ec2 describe-instances * filter']


# Generated at 2022-06-14 09:25:34.889533
# Unit test for function get_new_command
def test_get_new_command():
    command = "aws ec2 stop-instances --instance-ids i-12345678"

# Generated at 2022-06-14 09:25:43.817030
# Unit test for function match
def test_match():
    output_sample = "usage: aws [options] [ ...] [parameters]\n\
            To see help text, you can run:\n\n\
                aws help\n\n\
                aws help\n\n\
                aws help\n\n\
            Unknown options: --i, maybe you meant: --no-paginate, --profile\n"
    command_sample = "aws --i "
    assert match(command=Command(script=command_sample, output=output_sample))



# Generated at 2022-06-14 09:25:51.460902
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script=script, output=output)
    get_new_command(command)


# Generated at 2022-06-14 09:26:15.476758
# Unit test for function match
def test_match():
    command = Command("", "usage:: aws [options] <command> <subcommand> [parameters]\naws: error: argument command: Invalid choice, maybe you meant:\n  * configure\n  * help\n  * ec2\n  * iam\n  * opsworks\n  * s3\n  * sqs\n  * ecs\n  * elb\n  * cloudsearch\n  * route53\n  * cloudformation\n  * cloudfront\n  * cloudhsm")
    assert match(command)


# Generated at 2022-06-14 09:26:28.709276
# Unit test for function match
def test_match():
    assert not match(Command(script="aws", output=""))
    assert not match(Command(script="aws", output="usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]"))
    assert match(Command(script="aws", output="usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\naws: error: argument command: Invalid choice: 'list-keys', maybe you meant:\n\n* list-keypairs\n* list-keypairs\n"))


# Generated at 2022-06-14 09:26:31.456231
# Unit test for function match
def test_match():
    assert match(Command('aws help',
                                   "aws: error: argument --output: Invalid choice: '', maybe you meant: \n* json\n* text\n* table"))

# Generated at 2022-06-14 09:26:35.862764
# Unit test for function match
def test_match():
    command = Command('aws help',
                      "usage: aws [options] <command> <subcommand> [parameters]\naws: error: argument command: Invalid choice: 'help', maybe you meant:\n'help-api'\n'help-command-list'\n'help'\nTry 'aws help' for more information.\n")
    assert match(command) is True



# Generated at 2022-06-14 09:26:45.861379
# Unit test for function match
def test_match():
    # test match
    command = Command('aws ec2 help --help', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nto see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\n\nUnknown options: --help', 'aws ec2 help --help')
    assert match(command)
    # test no match
    command = Command('aws ec2', '', 'aws ec2')
    assert not match(command)


# Generated at 2022-06-14 09:26:52.020813
# Unit test for function match
def test_match():
    assert match(Command(script="aws cli",
                         output="usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\n\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\n\naws: error: Invalid choice: 'cli', maybe you meant:\n  logs\n  cloudtrail\n  cloudsearch\n  cloudwatch\n  cloudsearchdomain\n  cloudformation\n  cloudfront\n  cloudhsm\n  cloudhsmv2\n  cloudsearchdomain\n  cloudtrail\n  cloudwatch\n\n"))

# Generated at 2022-06-14 09:26:56.586093
# Unit test for function match
def test_match():
	cmd = Command("aws ec2 start-instances --cluster foo", "aws: error: argument --instance-ids: Invalid choice: 'foo', maybe you meant:   --instance-id")
	assert match(cmd)


# Generated at 2022-06-14 09:27:07.243304
# Unit test for function get_new_command

# Generated at 2022-06-14 09:27:09.588249
# Unit test for function get_new_command
def test_get_new_command():
    script = "aws ec2 help"
    output = "Invalid choice: 'help', maybe you meant:\n  * help\n  * hex"
    additional_info = ""
    command = thefuck.shells.and_('', script, output, additional_info)
    assert get_new_command(command) == ['aws ec2 help']

enabled_by_default = True

# Generated at 2022-06-14 09:27:22.883498
# Unit test for function get_new_command

# Generated at 2022-06-14 09:27:53.462663
# Unit test for function match
def test_match():
    command = Command("aws s3 ls bucketname --recursive")
    assert match(command)



# Generated at 2022-06-14 09:27:56.651255
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("aws ec2 terminate-instances --instance-ids i-0123456789") == [("aws ec2 terminate-instances --instance-ids i-012345678",)]

# Generated at 2022-06-14 09:28:01.661614
# Unit test for function match
def test_match():
    assert match(Command('aws invalidoption', 'wrong', 'Invalid choice: \'invalidoption\', maybe you meant:\
\n* invalidaction\n* invalidcommand\n\nSee \'aws help\' for descriptions of global parameters.'))


# Generated at 2022-06-14 09:28:11.907661
# Unit test for function get_new_command
def test_get_new_command():
    test_command1 = "aws ec2 describe-instance --invalid-parameter --instance-ids i-12345678 > output"
    test_command2 = "aws ec2 describe-instance --invalid-parameter --instance-ids i-12345678"
    test_command3 = "aws ec2 describe-instances --instance-ids i-12345678 > output"
    test_command4 = "aws ec2 describe-instances --instance-ids i-12345678"
    test_command5 = "aws ec2 describe-instance --instance-ids i-12345678 > output"
    test_command6 = "aws ec2 describe-instance --instance-ids i-12345678"


# Generated at 2022-06-14 09:28:30.141288
# Unit test for function match
def test_match():
    assert match(Command('aws --help', 'aws: error: unrecognized arguments: --help\nusage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: Invalid choice: "--help", maybe you meant:* help\n')) == True

# Generated at 2022-06-14 09:28:39.837025
# Unit test for function get_new_command
def test_get_new_command():
    command = type('obj', (object,), {'script': "aws help", 'output': "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\naws help\naws <command> help\naws <command> <subcommand> help\naws: error: argument subcommand: Invalid choice: 'help', maybe you meant: \n    helo\n    help\n    health\n    hosting"})
    assert get_new_command(command) == ['aws helo']

# Generated at 2022-06-14 09:28:47.454978
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

    command = Command('aws ec2 describe-instances --instance-ids',
                      'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\n'
                      'aws: error: argument instance-ids: Invalid choice: \'-\', maybe you meant:\n'
                      '    * --instance-id',
                      '')

    assert get_new_command(command) == [
        'aws ec2 describe-instances --instance-id']

# Generated at 2022-06-14 09:28:57.738915
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command('''usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help

Unknown options: '--help'
''') ==
    ['''usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help

Unknown options: 'help'
'''])