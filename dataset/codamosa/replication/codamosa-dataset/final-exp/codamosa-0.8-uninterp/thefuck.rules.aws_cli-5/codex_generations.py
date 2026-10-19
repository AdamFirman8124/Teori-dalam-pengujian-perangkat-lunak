

# Generated at 2022-06-14 09:19:05.310523
# Unit test for function get_new_command

# Generated at 2022-06-14 09:19:14.081947
# Unit test for function match
def test_match():
    output = '''usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help
aws: error: argument subcommand: Invalid choice, valid choices are:

An error occurred (InvalidParameterValue) when calling the DescribeSubnets operation: The subnet ID 'subnet-1' does not exist'''
    assert match(Command('aws s3', output=output))



# Generated at 2022-06-14 09:19:24.261284
# Unit test for function get_new_command
def test_get_new_command():
    script_command = "aws s3 mb s3://foo/"

# Generated at 2022-06-14 09:19:34.618676
# Unit test for function get_new_command
def test_get_new_command():
    test_script = 'aws lambda get-policy'

# Generated at 2022-06-14 09:19:47.509753
# Unit test for function match
def test_match():
    assert match(Command('aws --request-payer requests help',
                         'usage: aws [options] <command> <subcommand> [parameters]\naws: error: argument --request-payer: Invalid choice: \'requests\', maybe you meant: \'requester\'\n* requester\n'))

    assert not match(Command('aws --request-payer requests help', 'usage: aws [options] <command> <subcommand> [parameters]\n'))
    assert not match(Command('aws --request-payer requests help', 'usage: aws [options] <command> <subcommand> [parameters]'))

# Generated at 2022-06-14 09:19:55.230605
# Unit test for function match
def test_match():
    assert match(Command('aws s3 ls', ''))
    assert match(Command('aws s3 ls', 'aws: error: argument subcommand: Invalid choice', ''))
    assert match(Command('aws s3 ls', 'aws: error: argument subcommand: Invalid choice', 'usage: aws [options] <command> <subcommand> [parameters]', 'aws: error: argument subcommand: Invalid choice, maybe you meant:', '* subnets '))
    assert not match(Command('aws s3 ls', 'usage: aws [options] <command> <subcommand> [parameters]', 'aws: error: argument subcommand: Invalid choice, maybe you meant:', '* subnets '))
    assert not match(Command('aws', ''))

# Generated at 2022-06-14 09:20:07.736844
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.aws_cli import get_new_command

# Generated at 2022-06-14 09:20:11.898365
# Unit test for function match
def test_match():
    output = 'aws: error: argument operation: Invalid choice: \'yasin\' (choose from \'deregister, describe, list, register\')'
    assert match(Command(script='', output=output))



# Generated at 2022-06-14 09:20:15.682474
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws ec2 stop-instance --instance-ids i-12345678')) == [
        'aws ec2 stop-instances --instance-ids i-12345678'
    ]

# Generated at 2022-06-14 09:20:21.328475
# Unit test for function get_new_command
def test_get_new_command():
  assert get_new_command("aws ec2 describe-instances --filter 'Name=instance-state-name,Values=running' --output text --region us-east-1") == ["aws ec2 describe-instances --filter Name=instance-state-name,Values=running --output text --region us-east-1"]

# Generated at 2022-06-14 09:20:27.798695
# Unit test for function match
def test_match():
    assert match(Command('aws configure'))
    assert match(Command('aws ec2'))
    assert not match(Command('aws ecs'))
    assert not match(Command('aws'))
    assert not match(Command('git commit'))


# Generated at 2022-06-14 09:20:30.328408
# Unit test for function match
def test_match():
    assert match(Command('aws', 'usage: foo', 'Error: Incorrect usage'))
    assert not match(Command('aws', 'usage: foo', ''))

# Generated at 2022-06-14 09:20:37.329542
# Unit test for function match

# Generated at 2022-06-14 09:20:41.915353
# Unit test for function match
def test_match():
    command = 'aws'
    old_output = 'aws: error: argument command: Invalid choice: \'blah\', maybe you meant: * s3\n* usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\n\n'
    assert match(Command(command, old_output))


# Generated at 2022-06-14 09:20:51.088463
# Unit test for function match
def test_match():
    assert match(Command('aws help', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument operation: Invalid choice, valid choices are:\n', 123))
    assert not match(Command('aws ec2 describe-instance', '', 0))

# Generated at 2022-06-14 09:20:58.699771
# Unit test for function get_new_command
def test_get_new_command():
    # Given
    from thefuck.types import Command

    output = '''usage: aws [options] [ ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help
aws: error: argument command: Invalid choice, valid choices are:

commands are:
   sns            | Manage Simple Notification Service (SNS) topics, subscriptions, and messages
   help           | Shows a list of commands or help for one command
aws: error: argument command: Invalid choice, maybe you meant:
        sns

See 'aws help' for descriptions of global parameters.
'''
    # When
    new_command = get_new_command(Command('aws mo', output=output))

    # Then

# Generated at 2022-06-14 09:20:59.482268
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 describe-instances'))


# Generated at 2022-06-14 09:21:06.847707
# Unit test for function match
def test_match():
    assert match(Command('aws confi ', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]', ''))
    assert not match(Command('command', '', ''))


# Generated at 2022-06-14 09:21:15.072782
# Unit test for function match
def test_match():
    """
    Test the correctness of function match
    """
    assert match(Command('aws --help',
                         'usage: aws [options] <command> <subcommand> [parameters]\naws: error: argument operation: Invalid choice: \'help\', maybe you meant:',
                         'aws --help'))
    assert not match(Command('aws --help',
                             'usage: aws [options] <command> <subcommand> [parameters]'))
    
    

# Generated at 2022-06-14 09:21:17.316408
# Unit test for function match
def test_match():
    assert match(Command('aws --help'))
    assert not match(Command('pwd'))



# Generated at 2022-06-14 09:21:28.139852
# Unit test for function get_new_command
def test_get_new_command():
    from .helper import Command

    script = 'command --foobar'
    output = """
usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help

aws: error: argument --foobar: Invalid choice, maybe you meant:
  --foo-bar

aws <command> <subcommand> <subcommand> 

"""
    assert get_new_command(Command(script, output)) == ['command --foo-bar']

# Generated at 2022-06-14 09:21:31.244069
# Unit test for function match
def test_match():
    output = "Invalid choice: 's3', maybe you meant:\n\n\t* s3api"
    command = Command("aws s3 ls", output)
    assert match(command)



# Generated at 2022-06-14 09:21:38.827098
# Unit test for function match
def test_match():
    assert match(Command('aws --help', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\n\nerror: Invalid choice: \'hellp\', maybe you meant:\n\n* help\n'))

#Unit test for function get_new_command

# Generated at 2022-06-14 09:21:43.713866
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("aws help moom") == ['aws help miem']
    assert get_new_command("aws help moom --verbose") == ['aws help miem --verbose']
    assert get_new_command("aws help moom --verbose --help") == ['aws help miem --verbose --help']

# Generated at 2022-06-14 09:21:48.905777
# Unit test for function match
def test_match():
    assert match(Command('aws', output='usage: aws [options] <command> <subcommand> [parameters]\n\
            To see help text, you can run:\n\
            \n\
            aws help\n\
            aws <command> help\n\
            aws <command> <subcommand> help\n\
            \n\
            Unknown options: --region, us-east-1\n\
            Unknown options: --region, us-west-2\n\
            Invalid choice: \'--regions\', maybe you meant:\n\
                * --region'))


# Generated at 2022-06-14 09:22:01.361752
# Unit test for function match
def test_match():
    assert match(Command('aws config', ''))

# Generated at 2022-06-14 09:22:09.965820
# Unit test for function match

# Generated at 2022-06-14 09:22:18.844413
# Unit test for function match
def test_match():
    assert not match(Command('aws'))
    assert not match(Command('aws help configure'))
    assert match(Command('aws help configre',
                         "usage: aws [options] <command>\n\nA mistake of configre\nmaybe you meant: configure\n"))



# Generated at 2022-06-14 09:22:25.063441
# Unit test for function match
def test_match():
    assert match(Command('aws s3 sync s3://source s3://destination --delete --grants read=uri=http://acs.amazonaws.com/groups/global/AllUsers full=emailaddress=owner@example.com full=emailaddress=owner2@example.com', 'Invalid choice: \'--grants\', maybe you meant:', '', 1, False))


# Generated at 2022-06-14 09:22:38.647986
# Unit test for function get_new_command

# Generated at 2022-06-14 09:22:54.119841
# Unit test for function get_new_command

# Generated at 2022-06-14 09:23:02.111707
# Unit test for function get_new_command
def test_get_new_command():
    # Test for exact match
    command = Command('aws sqs list',
        """
usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help

Unknown options: sq
botocore.exceptions.UnknownArgumentError: Unknown options: sq\n"""
    )

    assert get_new_command(command) == ['aws s3 list']



# Generated at 2022-06-14 09:23:04.814651
# Unit test for function match
def test_match():
    assert bool(match(Command('aws ec2 nope', ''))) is True
    assert bool(match(Command('aws lalala', ''))) is False



# Generated at 2022-06-14 09:23:09.872511
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws nop', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nto see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\ninvalid choice: \'nop\', maybe you meant:\n  --no-paginate', '')) == \
               [replace_argument('aws nop', 'nop', o) for o in ['--no-paginate']]

# Generated at 2022-06-14 09:23:11.693655
# Unit test for function match
def test_match():
    assert match(Command('aws route53'))


# Generated at 2022-06-14 09:23:23.938425
# Unit test for function get_new_command
def test_get_new_command():
    command = namedtuple('Command', 'script output')

# Generated at 2022-06-14 09:23:29.932988
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.main import Command

# Generated at 2022-06-14 09:23:38.311380
# Unit test for function get_new_command
def test_get_new_command():
    # Test 1: Invalid choice and suggest solution
    command = type('obj', (object,), {
        'script': 'aws iam list-u',
        'output': ("usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\n",
                   "aws: error: argument subcommand: Invalid choice: 'list-u', maybe you meant: \n",
                   "   list-users\n",
                   "   list-virtual-mfa-devices\n",
                   "   list-mfa-devices\n")})

    expected = [
        "aws iam list-users",
        "aws iam list-virtual-mfa-devices",
        "aws iam list-mfa-devices"
    ]

    assert get_new_command(command) == expected

    # Test 2

# Generated at 2022-06-14 09:23:51.370275
# Unit test for function match
def test_match():
    assert match(Command('aws s3 mb s3://foo',
                         'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\n'
                         'aws: error: argument <command>: Invalid choice, maybe you meant:\n'
                         '\tmb\n'
                         '\tmb\n'
                         '\tmb\n'
                         '\tmb\n'
                         '\tmb\n'
                         '\tmb\n'
                         '\tmb\n'
                         '\tmb\n'
                         '\tmb\n'
                         '\tmb\n', 1))

# Generated at 2022-06-14 09:23:58.170324
# Unit test for function match
def test_match():
    assert match(Command(script='', output='usage: aws [options]'))
    assert match(Command(script='', output='usage: aws [options] maybe you meant: aws'))
    assert not match(Command(script='', output='usage: aws'))
    assert not match(Command(script='', output='usage: aws [options]'))


# Generated at 2022-06-14 09:24:21.095998
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 list-instances --profile prod --region us-east-1',
                         "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\nerror: Invalid choice: 'ec2', maybe you meant:",
                         3)) == True


#Unit test for function get_new_command

# Generated at 2022-06-14 09:24:28.728309
# Unit test for function get_new_command
def test_get_new_command():
    output = '''
usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help
aws: error: argument operation: Invalid choice, valid choices are:

describe-account-attributes
get-account-summary

An error occurred (UnrecognizedClientException) when calling the
DescribeAccountAttributes operation: The security token included in the request
is invalid.'''
    command = Command("aws account operational", output)
    assert get_new_command(command) == ['aws describe-account-attributes']

# Generated at 2022-06-14 09:24:33.377907
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("aws ec2 --list\nUnknown options: --list\nMaybe you meant:\n  terminate-instances\n  describe-instances\n  reboot-instances") == ["aws ec2 terminate-instances", "aws ec2 describe-instances", "aws ec2 reboot-instances"]

# Generated at 2022-06-14 09:24:41.915833
# Unit test for function match
def test_match():
    command = Command('aws ec2 describe-instances', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument subcommand: Invalid choice, valid choices are:\nrun-instances          | start-instances         | stop-instances          | reboot-instances        | terminate-instances     | describe-instances      | report-instances-status | start-instances-enabled | reboot-instances-enabled\n', 1)


# Generated at 2022-06-14 09:24:54.378781
# Unit test for function match

# Generated at 2022-06-14 09:25:04.239626
# Unit test for function match

# Generated at 2022-06-14 09:25:14.304437
# Unit test for function get_new_command
def test_get_new_command():
    script1 = "aws ec2 describe-images"
    script2 = "aws s3 mb s3://test"
    output1 = """usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help

Unknown options: describe-images, --filters, Name=architecture,Values=x86_64, Name=root-device-type,Values=ebs
Invalid choice: 'describe-images', maybe you meant:  
    * ec2
    * route53
    * dynamodb
    * iam
    * rds
    * s3
    * cloudformation
"""

# Generated at 2022-06-14 09:25:26.197875
# Unit test for function match

# Generated at 2022-06-14 09:25:32.827176
# Unit test for function match
def test_match():
    # Empty case
    assert(match(Command('', '')) == False)
    
    # No match case
    assert(match(Command('git', 'git help')) == False)
    
    # Match case
    command = Command('aws s3 ls', 'aws: error: argument command: Invalid choice: `ls`, maybe you meant:  \n* ls-buckets')
    assert(match(command) == True)



# Generated at 2022-06-14 09:25:46.294110
# Unit test for function get_new_command

# Generated at 2022-06-14 09:26:20.890916
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("aws ec2 describe-regions --region us-east-2")

# Generated at 2022-06-14 09:26:25.557462
# Unit test for function match
def test_match():
    from thefuck.types import Command
    assert match(Command('aws key', '')) is False
    assert match(Command('aws key', 'usage: aws [options] <command> <subcommand> [parameters]\naws: error: argument operation: Invalid choice', 'aws key', ''))



# Generated at 2022-06-14 09:26:35.425712
# Unit test for function get_new_command

# Generated at 2022-06-14 09:26:38.378953
# Unit test for function get_new_command
def test_get_new_command():
    command = 'aws s3 mb s3:///bucket_name/folder/ --fail'
    assert get_new_command(command) == 'aws s3 mb s3:///bucket_name/folder --fail'

# Generated at 2022-06-14 09:26:50.382828
# Unit test for function get_new_command
def test_get_new_command():
    output = """usage: aws [options] <command> <subcommand> [parameters]
aws: error: argument command: Invalid choice, valid choices are:
        autoscaling | cloudformation | cloudfront | cloudhsm | cloudsearch | cloudsearchdomain | cloudtrail | cloudwatch | command_not_found | datapipeline | directconnect | dynamodb | ec2 | elasticache | elasticbeanstalk | elasticloadbalancing | elastictranscoder | elasticmapreduce | iam | importexport | kinesis | opsworks | rds | redshift | route53 | s3 | ses | ses | simpledb | sns | sqs | storagegateway | sts | support | swf
        maybe you meant: command_not_found"""

# Generated at 2022-06-14 09:26:59.133193
# Unit test for function get_new_command
def test_get_new_command():
    script = 'aws ec2 help'

# Generated at 2022-06-14 09:27:06.945213
# Unit test for function get_new_command
def test_get_new_command():
    output = "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument <command>: Invalid choice: 's3lsit', maybe you meant:* s3"
    script = "aws s3lsit /"
    assert get_new_command(Command(script, output)) == ["aws s3 /"]

# Generated at 2022-06-14 09:27:13.886955
# Unit test for function get_new_command

# Generated at 2022-06-14 09:27:25.411410
# Unit test for function match

# Generated at 2022-06-14 09:27:35.541800
# Unit test for function match
def test_match():
	assert match(Command('aws --version',
						 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument --version: Invalid choice: \'--version\', maybe you meant:\n    --version\n    --vpc\n    --execute-api\n    --endpoint\n    --endpoint-url',
						 '/usr/local/bin/aws', 'aws'))


# Generated at 2022-06-14 09:28:31.322742
# Unit test for function match
def test_match():
    # What the function should output
    output = 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument command: Invalid choice: "Asd", maybe you meant: as-attach-load-balancers\naws: error: argument command: Invalid choice: "Asd", maybe you meant: as-attach-load-balancers\naws: error: argument command: Invalid choice: "Asd", maybe you meant: as-attach-load-balancers'
    # What the function should output
    should_output = True
    # The function output

# Generated at 2022-06-14 09:28:45.474657
# Unit test for function match
def test_match():
    assert match(Command("aws ec2 describe-regions", "No such file or directory\nusage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\nerror: Invalid choice: 'ec2', maybe you meant:", error_code=127))
    assert not match(Command("aws ec2 describe-regions", "export AWS_SECRET_ACCESS_KEY=xxx\nexport AWS_ACCESS_KEY_ID=xxx", error_code=127))


# Generated at 2022-06-14 09:28:48.675180
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws s3 ls --region us-west-2')) == \
        ['aws s3 ls --region us-west-1', 'aws s3 ls --region us-west-2']

# Generated at 2022-06-14 09:29:00.129244
# Unit test for function match