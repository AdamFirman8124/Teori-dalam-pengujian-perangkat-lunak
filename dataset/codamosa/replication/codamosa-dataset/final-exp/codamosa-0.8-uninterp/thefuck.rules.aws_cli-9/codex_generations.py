

# Generated at 2022-06-14 09:19:02.098692
# Unit test for function match
def test_match():
    assert match(Command('aws', 'aws: error: argument command: Invalid choice: "ec2", '
                                 'maybe you meant: \n* instance'))
    assert not match(Command('aws', ''))
    assert not match(Command('aws', 'aws: error: argument command: Invalid choice: "ec2", '
                                      'yoyoyoyoyo'))

# Generated at 2022-06-14 09:19:04.577587
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 start-instances --instance-ids i-123456 --region myregion'))


# Generated at 2022-06-14 09:19:07.804038
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws --foo', 'aws: error: invalid choice: --foo\n                                 * --bar'))\
        == ['aws --bar']

# Generated at 2022-06-14 09:19:12.054799
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("aws ec2 describe-instances --filters Name=instance-name,Values=blabla")
    assert get_new_command(command) == ["aws ec2 describe-instances --filters Name=instance-name,Values=blahblah"]

# Generated at 2022-06-14 09:19:23.260380
# Unit test for function match
def test_match():
    command = Command('aws s3 ls s3://bucket', "usage: aws [options] <command> <subcommand> [parameters] \nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\nInvalid choice: 's3', maybe you meant:\n\n* s3api\n* s3api\n")
    assert not match(command)



# Generated at 2022-06-14 09:19:34.146197
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 describe-instances --regio ap-southeast-1', 'aws: error: argument --region: Invalid choice: \'ap-southeast-1\', maybe you meant: us-east-1, us-west-1, us-west-2, eu-west-1, ap-northeast-1, sa-east-1, ap-southeast-2.'))
    assert not match(Command('ls', 'Usage: ls [OPTION]... [FILE]...'))

# Generated at 2022-06-14 09:19:47.069162
# Unit test for function match
def test_match():
    output = "Error: usage: aws [options] <command> <subcommand> [parameters]\n" \
             "To see help text, you can run:\n" \
             "aws help\n" \
             "aws <command> help\n" \
             "aws <command> <subcommand> help\n" \
             "Unknown options: --client-config, s3.\n" \
             "Maybe you meant:\n" \
             "* cf\n" \
             "* s3api\n" \
             "* ssm\n" \
             "* add\n" \
             "* rds\n" \
             "* es\n" \
             "* s3\n" \
             "* cloudhsm\n" \
             "* redshift\n" \
            

# Generated at 2022-06-14 09:19:55.084370
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 doesnotexists', 'usage: aws [options] <command> <subcommand> [parameters]\n\naws: error: argument command: Invalid choice, maybe you meant:\n    configure   Create a default credential/config file\n    ec2         Describe and configure Amazon EC2 instances and more\n    help        Describe AWS services, configure and manage them', ''))
    assert not match(Command('aws2 ec2 doesnotexists', 'usage: aws [options] <command> <subcommand> [parameters]\n\naws: error: argument command: Invalid choice, maybe you meant:\n    configure   Create a default credential/config file\n    ec2         Describe and configure Amazon EC2 instances and more\n    help        Describe AWS services, configure and manage them', ''))


# Generated at 2022-06-14 09:20:05.293806
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 describe-instance-status', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\n\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\n\nUnknown options: e, s'))
    assert not match(Command('aws ec2 describe-instance-status', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\n\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\n\nUnknown options: e, s', ''))


# Generated at 2022-06-14 09:20:18.129797
# Unit test for function get_new_command

# Generated at 2022-06-14 09:20:24.410120
# Unit test for function match

# Generated at 2022-06-14 09:20:35.479674
# Unit test for function match
def test_match():
    assert match(Command('aws s3 ls', '', 'usage: aws [options] <command> <subcommand> [parameters]\naws: error: argument subcommand: Invalid choice: \'"ls"\', maybe you meant: \n    list-buckets\n    list-objects-v2\n\n'))
    assert not match(Command('aws s3 ls', '', 'usage: aws [options] <command> <subcommand> [parameters]\n'))
    assert not match(Command('aws s3 ls', '', 'usage: aws [options] <command> <subcommand> [parameters]\naws: error: argument subcommand: Invalid choice: \'"ls"\', maybe you meant: \n    list-buckets\n    list-objects-v2\n\n'))

# Unit test

# Generated at 2022-06-14 09:20:43.801278
# Unit test for function get_new_command
def test_get_new_command():
    script = "['aws', 'ec2', 'describe-instances']"
    output = "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument subcommand: Invalid choice, maybe you meant:\n\n* describe-instance"
    command = Command(script, output)
    assert get_new_command(command) == [['aws', 'ec2', 'describe-instance']]

# Generated at 2022-06-14 09:20:47.416081
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("aws sts get-service-identity-validation --selector include-account-aliases")) == ["aws sts get-service-identity-validation"]

# Generated at 2022-06-14 09:20:52.504308
# Unit test for function get_new_command
def test_get_new_command():
    command = type('Command', (object,), {'script': 'test invalid-value', 'output': "invalid-value usage: something\nmaybe you meant: valid-value\n* valid-value\n"})
    assert get_new_command(command) == ['test valid-value']

# Generated at 2022-06-14 09:20:56.400446
# Unit test for function get_new_command
def test_get_new_command():
    assert(get_new_command("aws ec2 describe-instances --filters 'Name=foo,Values=bar'")
           == ['aws ec2 describe-instances --filter Name=foo,Values=bar'])

# Generated at 2022-06-14 09:21:09.269809
# Unit test for function get_new_command
def test_get_new_command():

    # Command with Invalid choice:
    command = Command('aws ec2 run-instances')
    assert get_new_command(command) == ['aws ec2 run-instances']

    # Command with Invalid choice and maybe you meant
    command = Command('aws ec2 stop-insatnces', 'stop-insatnces --help\nusage: aws [options] <service-name> <operation> [parameters]\naws: error: argument operation: Invalid choice: \'stop-insatnces\', maybe you meant:')
    assert get_new_command(command) == ['aws ec2 stop-instances']

# Generated at 2022-06-14 09:21:14.339618
# Unit test for function match
def test_match():
    assert match({'output': 'usage: aws [options]\nInvalid choice: \'wrong\', maybe you meant:\n\t* right\n\t* right2\'', 'script':''})
    assert not match({'output': '', 'script':''})


# Generated at 2022-06-14 09:21:17.963357
# Unit test for function match
def test_match():
    assert match(Command(script='aws something', output='Invalid choice: ' \
                                                       '"something", valid values' \
                                                       ' are: \n\n* list\n'))


# Generated at 2022-06-14 09:21:20.414504
# Unit test for function match
def test_match():
    assert match(Command("aws", "Invalid choice: 'xyz', maybe you meant:", ""))


# Generated at 2022-06-14 09:21:32.089385
# Unit test for function get_new_command

# Generated at 2022-06-14 09:21:43.300383
# Unit test for function match

# Generated at 2022-06-14 09:21:49.640778
# Unit test for function match
def test_match():
    examples = [
        'aws: error: argument command: Invalid choice, maybe you meant:',
        'aws: error: argument subcommand: Invalid choice, maybe you meant:',
        'aws: error: argument resource: Invalid choice, maybe you meant:',
        'aws: error: argument action: Invalid choice, maybe you meant:'
    ]
    assert all(match(Command('aws', examples[0])) for example in examples)
    assert not match(Command('aws', 'aws', '--help'))
    assert match(Command('aws', 'aws', 'cloudfront', 'usage:', 'aws', 'cloudfront', 'help'))
    assert match(Command('aws', 'aws', 'cloudfront', 'usage:', 'aws', 'cloudfront', 'COMMAND'))

# Generated at 2022-06-14 09:22:01.034057
# Unit test for function get_new_command
def test_get_new_command():
    output = """aws: error: argument command: Invalid choice: 'create-invalid', maybe you meant:
        create-access-key
        create-alias
        create-batch-prediction
        create-data-source-from-rds
        create-data-source-from-redshift
        create-data-source-from-s3
        create-data-source-from-sql-server
        create-data-source-from-tracker
        create-datasource
        create-evaluation
        create-ml-db-credential
        create-realtime-endpoint
        create-s3-data-source
        create-tag

    See 'aws help' for descriptions of global parameters."""
    command = Command("aws create-invalid", "", output)

# Generated at 2022-06-14 09:22:03.090675
# Unit test for function get_new_command
def test_get_new_command():
    test_command = "aws iam list-instance-profiles"

# Generated at 2022-06-14 09:22:11.242413
# Unit test for function match

# Generated at 2022-06-14 09:22:11.878047
# Unit test for function match
def test_match():
    pass

# Generated at 2022-06-14 09:22:24.180866
# Unit test for function match
def test_match():
    assert match(create_mock_command('aws', 'usage: aws [options] <command> <subcommand> [parameters]\naws: error: argument command: Invalid choice: \'iam\', maybe you meant:\n  instance-store  Manage storage for EC2 instances\n  transactions     Manage transactions for Amazon EC2 reservations\n\n'))
    assert not match(create_mock_command('aws', 'usage: aws [options] <command> <subcommand> [parameters]\naws: error: argument command: Invalid choice: \'iam\', maybe you meant:\n  instance-store  Manage storage for EC2 instances\n  transactions     Manage transactions for Amazon EC2 reservations\n\n'))


# Generated at 2022-06-14 09:22:37.947141
# Unit test for function match

# Generated at 2022-06-14 09:22:41.829483
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 describe-instances --query "" --instance-ids "'))

# Generated at 2022-06-14 09:22:49.885061
# Unit test for function match
def test_match():
    assert match(Command('aws s3 ls --region eu-west-1', 'aws: error: argument --region: Invalid choice: '
    '\'eu-west-1\', maybe you meant: \n  * eu-central-1\n  * eu-west-2\n  * us-east-1\n  * us-west-1\n  * us-west-2'))

# Generated at 2022-06-14 09:22:59.240971
# Unit test for function match
def test_match():
    assert match(Command(script="aws help", output="Invalid choice: 'help', maybe you meant: \r\n* configure"))
    assert match(Command(script="aws help", output="Invalid choice: 'help', maybe you meant: \r\n* configure"))
    assert not match(Command(script="aws help", output="Invalid choice: 'help', maybe you meant: \r\n* configure", stderr="UsageError: need to configure"))
    assert not match(Command(script="aws help", output="Invalid choice: 'help', maybe you meant: \r\n* configure", stderr="Invalid choice: 'help', maybe you meant: \r\n* configure"))

# Generated at 2022-06-14 09:23:06.375677
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('aws ec2 describe-spot-instance-requests', 'aws: error: argument --max-price: Invalid choice: \'10e\', maybe you meant:\n\n  * --max-price\n  * --max-results\n\naws: error: argument --filters: Invalid choice: \'instance-id=i-0fe2db0432c8b99f7\', maybe you meant:\n\n  * --filters\n')
    options = get_new_command(command)
    assert ['aws ec2 describe-spot-instance-requests --max-price'] == options


# Generated at 2022-06-14 09:23:18.732484
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('aws elb describe-load-balancers --load-balancer-name=error', "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument --load-balancer-name: Invalid choice: 'error', maybe you meant:\n\t* elb-error\n\telb-error-2\n", '', 0)
    assert get_new_command(command) == ['aws elb describe-load-balancers --load-balancer-name=elb-error', 'aws elb describe-load-balancers --load-balancer-name=elb-error-2']

# Generated at 2022-06-14 09:23:28.602627
# Unit test for function match
def test_match():
    """
    Verifies that the function match runs correctly
    """
    assert match(Command('aws ecs list-clusters --region eu-west-1',
                         'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument subcommand: Invalid choice: "list-clusters"\naws: error: argument region: Invalid choice: "eu-west-1"\n',
                         'aws ecs list-clusters --region eu-west-1', 1))

# Generated at 2022-06-14 09:23:32.166267
# Unit test for function match
def test_match():
    assert(match(Command('aws s3 ls s3://my-test-bucket-doesntexist', '', "Unknown options: 's3://my-test-bucket-doesntexist', maybe you meant:  get-object")) == True)


# Generated at 2022-06-14 09:23:33.551367
# Unit test for function match
def test_match():
    assert match(Command("aws cloudformation create-stack --stack-name my-new-stack --template-body file://mytemplate.json"))


# Generated at 2022-06-14 09:23:40.373602
# Unit test for function match
def test_match():
    """Check that the function match is correct"""

# Generated at 2022-06-14 09:23:43.918200
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("aws s3 ls bucket --recursive") == ['aws s3 ls bucke --recursive', 'aws s3 ls buckei --recursive']


# Generated at 2022-06-14 09:23:54.845063
# Unit test for function match
def test_match():
    assert not match(Command("apt-get update", "", ""))

# Generated at 2022-06-14 09:24:02.230223
# Unit test for function match
def test_match():
    assert match(Command('aws s3 mb s3://bucket-name', 'The program \'aws\' is currently not installed. To run \'aws\' please ask your administrator to install the package \'awscli\''))
    assert not match(Command('ls', ''))


# Generated at 2022-06-14 09:24:11.447859
# Unit test for function match

# Generated at 2022-06-14 09:24:24.575577
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.aws_cli import get_new_command
    script = 'aws ec2 create-volume --size 5'
    output = '''usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help

aws: error: argument subcommand: Invalid choice, valid choices are:

create-snapshot
create-volume
delete-snapshot
delete-volume
describe-snapshots
describe-volumes
describe-volume-attribute
describe-volume-status
modify-snapshot-attribute
modify-volume-attribute
report-volume-status

Unknown options: create-volume
'''

# Generated at 2022-06-14 09:24:37.687872
# Unit test for function match
def test_match():

    # Valid command
    command = Command("aws ec2 describe-instances", "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument operation: Invalid choice, maybe you meant:\n  configuration-template   describe-configuration-options   describe-configurations   \n                          list-available-solution-stacks   validate-template", "aws ec2 describe-instances")
    matchInfo = match(command)
    expected = True
    assert matchInfo == expected

    # Invalid command

# Generated at 2022-06-14 09:24:44.427357
# Unit test for function get_new_command

# Generated at 2022-06-14 09:24:56.122564
# Unit test for function match
def test_match():
    output = "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\n\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument operation: Invalid choice, maybe you meant: create?\n    * create\n    * destroy\n    * list\n    * modify\n    * describe\n    * delete\n    * update"
    assert match(Command(script="aws test", output=output))


# Generated at 2022-06-14 09:25:00.252618
# Unit test for function get_new_command
def test_get_new_command():
    # TODO Find a way to stub the output
    command = Command('aws help', 'aws: error: argument subcommand: Invalid choice: \'help\', maybe you meant:\n  * help-cmd\n')
    assert get_new_command(command) == ['aws help-cmd']

# Generated at 2022-06-14 09:25:05.469177
# Unit test for function get_new_command
def test_get_new_command():
    command = 'aws cli:aws: error: argument subcommand: Invalid choice: ' \
        "'s3-params', maybe you meant: \n" \
        "  * s3-objects\n" \
        "  * s3-buckets\n" \
        "  * s3-source"

    expected = ['aws cli:aws s3-objects',
        'aws cli:aws s3-buckets',
        'aws cli:aws s3-source']

    assert get_new_command(command) == expected

# Generated at 2022-06-14 09:25:08.401495
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws ec2 list-instance')) == \
            ['aws ec2 list-instances']



# Generated at 2022-06-14 09:25:16.246592
# Unit test for function match
def test_match():
    # Test output with no invalid choice or maybe you meant:
    assert not match(Command('aws s3 cp foo bar', ''))

    # Test output with no invalid choice but with maybe you meant:
    assert not match(Command('aws s3 cp foo bar', '', 'usage: aws [options] [ ...] [parameters] \nmaybe you meant: foo'))

    # Test output with invalid choice but no maybe you meant:
    assert not match(Command('aws s3 cp foo bar', '', 'usage: aws [options] [ ...] [ paramet ers] \ninvalid choice: \'foo\', maybe you meant: bar'))

    # Test output with invalid choice and with maybe you meant:

# Generated at 2022-06-14 09:25:32.215599
# Unit test for function get_new_command
def test_get_new_command():
    script = "aws s3 ls --mybucket"
    output = """usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help
aws: error: argument --mybucket: Invalid choice, valid choices are:

* s2
* s3a
* s3w"""
    command = Command(script, output)
    assert get_new_command(command) == ['aws s3 ls --s2', 'aws s3 ls --s3a', 'aws s3 ls --s3w']

# Generated at 2022-06-14 09:25:41.421004
# Unit test for function match
def test_match():
    assert match(Command(
        script="aws --help",
        output="usage: aws [options] <command> <subcommand> [parameters]"
    ))
    assert match(Command(
        script="aws --help",
        output="usage: aws [options] <command> <subcommand> [parameters]"
    ))
    assert not match(Command(
        script="aws --help",
        output="Command aws"
    ))


# Generated at 2022-06-14 09:25:50.499302
# Unit test for function match

# Generated at 2022-06-14 09:26:03.037612
# Unit test for function get_new_command
def test_get_new_command():
    import tempfile
    import execute
    with tempfile.NamedTemporaryFile(mode='wt') as temp:
        temp.write('''
usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help
aws: error: argument command: Invalid choice, maybe you meant:
* ec2
* ecr
* ecs
See 'aws help' for descriptions of global parameters.
''')
        temp.seek(0)
        output = execute.Popen(["tac", temp.name], stdout=execute.PIPE).stdout.read()

# Generated at 2022-06-14 09:26:04.728137
# Unit test for function match
def test_match():
    assert match(Command('aws', output='usage'))
    assert not match(Command('aws', output='foo'))


# Generated at 2022-06-14 09:26:09.691689
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    assert get_new_command(Command('aws cloudformation create-stack --stack-name', 'usage: ... maybe you meant:...')) == ['aws cloudformation create-stack stack-name']

# Generated at 2022-06-14 09:26:17.564203
# Unit test for function match
def test_match():
    output = "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument subcommand: Invalid choice, maybe you meant:\n  commands\n  completion\n  configure\n\n"
    assert match(Command('aws s3', output))


# Generated at 2022-06-14 09:26:34.306607
# Unit test for function match
def test_match():
    command = "aws s3 rb s3://BUCKET/ --force An error occurred (InvalidArgument) when calling the DeleteObjects operation: Error parsing XML: Premature end of data in tag KeySet line 1"
    assert match(command)
    command = "aws iam login"
    assert match(command)
    command = "aws s3 ls"
    assert match(command)
    command = "aws s3 mb"
    assert match(command)
    command = "aws s3 ls s3://bucket"
    assert match(command)
    command = "aws s3 ls s3://bucket/folder"
    assert match(command)
    command = "aws dynamodb create-table s3://bucket/folder"
    assert match(command)
    assert not match("aws help")

# Generated at 2022-06-14 09:26:47.644367
# Unit test for function match
def test_match():
    assert match(Command('aws s3 ls', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\n\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\n\ninvalid choice: \'s3\' (choose from help, configure, iam, rds, ses, sns, sqs, iam)', 'aws s3 ls'))

# Generated at 2022-06-14 09:26:54.128026
# Unit test for function get_new_command
def test_get_new_command():
    m = Mock()
    m.script = 'aws ec2 sart-instances'
    m.output = """Invalid choice: 'sart-instances', maybe you meant:
                 * start-instances
                 * stop-instances
                 * describe-instances
                 * describe-instance-attribute"""
    assert get_new_command(m) == ['aws ec2 start-instances', 'aws ec2 stop-instances', 'aws ec2 describe-instance-attribute']

# Generated at 2022-06-14 09:27:10.350234
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws ec2 describe-images --owner self')) == \
        ['aws ec2 describe-images --owner self']

# Generated at 2022-06-14 09:27:23.577765
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

# Generated at 2022-06-14 09:27:31.134872
# Unit test for function get_new_command
def test_get_new_command():
    # setup
    command = type("obj", (object,), {'output': "Invalid choice: 'invalid', maybe you meant:\n  * init\n  * info\n"})()
    # invoke
    result = get_new_command(command)
    # assert
    assert result == ['aws init', 'aws info']



# Generated at 2022-06-14 09:27:42.192254
# Unit test for function match

# Generated at 2022-06-14 09:27:49.052585
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    assert get_new_command(Command('aws ec2')) == ['aws ec2 --help']
    assert get_new_command(Command('aws ec2 stop')) == ['aws ec2 stop-instances --help']
    assert get_new_command(Command('aws ec2 run-instances')) == ['aws ec2 run-instances --help']

# Generated at 2022-06-14 09:27:59.451091
# Unit test for function get_new_command
def test_get_new_command():
    script = 'aws ec2 run-instances --image-id ami-1234 --instance-type t1.micro'
    output = '''usage: aws [options] <command> <subcommand> [<subcommand> ...] [options] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help
aws: error: argument --instance-type: Invalid choice: 't1.micro', maybe you meant:
    t1.micro'''

# Generated at 2022-06-14 09:28:10.958164
# Unit test for function get_new_command
def test_get_new_command():
    assert ["aws configure set default.region us-east-1"] == get_new_command(Command('aws configure set default.region us-east-1', 'aw: error: argument region: Invalid choice: \'us-east-1\', maybe you meant:\n* us-gov-east-1\n* us-gov-west-1\n* us-east-2\n* us-west-1\n* us-west-2\nUSAGE', '', 1))


# Generated at 2022-06-14 09:28:13.629171
# Unit test for function match
def test_match():
    assert match(Command("aws s3 lls s3://bucket/", "Invalid choice: 'lls', maybe you meant:\n* ls"))


# Generated at 2022-06-14 09:28:22.121026
# Unit test for function get_new_command

# Generated at 2022-06-14 09:28:27.233956
# Unit test for function get_new_command
def test_get_new_command():
    run = lambda x: command_from_output(x, 'aws')
    assert get_new_command(run('aws asdf')) == ['aws as-delete-stack', 'aws as-describe-adjustment-types', 'aws as-describe-auto-scaling-groups']



# Generated at 2022-06-14 09:28:54.937342
# Unit test for function get_new_command
def test_get_new_command():
    command = make_command('aws --version', 'usage: aws [options] [parameters]\ns3 = s3api *\nInvalid choice: \'s3\', maybe you meant:\n        * s3api\n')
    assert get_new_command(command) == ['aws --version s3api']