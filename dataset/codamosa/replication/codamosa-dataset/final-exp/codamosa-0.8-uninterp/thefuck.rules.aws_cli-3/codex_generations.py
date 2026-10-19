

# Generated at 2022-06-14 09:18:53.923913
# Unit test for function get_new_command
def test_get_new_command():
    new_command_list = get_new_command(Command('aws ec2 describe-foo', None))
    assert new_command_list == ['aws ec2 describe-fq',
                                'aws ec2 describe-fz'
                                ]

# Generated at 2022-06-14 09:18:55.818523
# Unit test for function get_new_command
def test_get_new_command():
    retour = get_new_command(Command('aws ec2 --help', ''))
    assert retour == 0

# Generated at 2022-06-14 09:19:07.761186
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command


# Generated at 2022-06-14 09:19:18.933622
# Unit test for function match

# Generated at 2022-06-14 09:19:31.424097
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('aws ec2 describe-instances --filter Name=instance-state-code,Values=16', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument --filter: Invalid choice: \'instance-state-code,Values=16\', maybe you meant:\n* filter\n* --filter-name\n* --filter-value\n* --group-id\n\n')

# Generated at 2022-06-14 09:19:35.128415
# Unit test for function match
def test_match():
    assert match(Command('aws ec2', ''))
    assert match(Command('aws --ec2', ''))
    assert not match(Command('aws ec2 --help', ''))


# Generated at 2022-06-14 09:19:42.624392
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 run-instances',
            output="usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument subcommand: Invalid choice, maybe you meant: "))


# Generated at 2022-06-14 09:19:48.794676
# Unit test for function match
def test_match():
    assert match(Command('aws s3 ls s3://foo/ --endpoint', 'aws: error: argument operation: Invalid choice'))
    assert match(Command('aws s3 ls s2://foo/ --endpoint', 'aws: error: argument operation: Invalid choice'))
    assert not match(Command('aws s3 ls s2://foo/ --endpoint', 'aws: error: argument service: Invalid choice'))


# Generated at 2022-06-14 09:19:55.120074
# Unit test for function match
def test_match():
    assert match(Command('aws s3','''usage: aws [options] [ ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help

Unknown options: s3
'''))



# Generated at 2022-06-14 09:20:06.823963
# Unit test for function match
def test_match():
    assert match(Command('aws sqs', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\nerror: Invalid choice: \'sqs\', maybe you meant:', 'aws sqs'))
    assert not match(Command('aws', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help', 'aws'))


# Generated at 2022-06-14 09:20:08.909584
# Unit test for function get_new_command
def test_get_new_command():
    pass

# Generated at 2022-06-14 09:20:14.203146
# Unit test for function match
def test_match():
    assert match(Command('aws s3 help', 'aws: error: argument command: Invalid choice: \'help\', maybe you meant:\n  ls\n  mb\n  rb\n  rsync\n  s3api\n  sync\nUse "aws help" for more information about a command.'
))

# Generated at 2022-06-14 09:20:20.536680
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.scripts import aws
    assert aws.get_new_command(
        'aws s3api list-buckets --query\nUnknown options: --querty') == [
            "aws s3api list-buckets --query 'Buckets[*].Name'",
            "aws s3api list-buckets --query 'Owner.DisplayName'",
            "aws s3api list-buckets --query 'Owner.ID'"]

# Generated at 2022-06-14 09:20:33.026826
# Unit test for function match
def test_match():
    output = "usage: aws [options] \n\
    \t<service> <subcommand> [<subcommand> ...] [parameters]\n\
    \n\
    To see help text, you can run:\n\
    \n\
    \taws help\n\
    \taws <service> help\n\
    \taws <service> <subcommand> help\n\
    \n\
    aws: error: argument <subcommand>: Invalid choice: '--s3', maybe you meant:\n\
    \t* s3api\n\
    \t* s3control\n\
    \t* s3"
    assert match(Command("aws --s3", output=output))
    assert not match(Command("aws s3", output=output))

# Generated at 2022-06-14 09:20:39.097371
# Unit test for function match
def test_match():
    assert match(Command('aws help'))
    assert match(Command('aws help', 'usage:\nmaybe you meant:'))
    assert not match(Command('aws help', 'usage:'))
    assert not match(Command('aws help', 'unknown command'))
    assert not match(Command('aws help'))
    assert not match(Command('aws help', 'usage:'))


# Generated at 2022-06-14 09:20:45.267575
# Unit test for function match
def test_match():
    if test_match.__name__ != 'test_match':
        return
    print("TEST: function match")
    assert not match(Command('ls'))
    assert match(Command(
        'aws s3 lol', 'usage: aws [options] <command> <subcomman> [parameters]\n\naws: error: argument command: Invalid choice: \'lol\', maybe you meant: list\n  * list\n  * create\n  * mb\n  * rb\n'))



# Generated at 2022-06-14 09:20:49.060730
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('aws ec2 help',
                      "Invalid choice: 'ec2h', maybe you meant:\n  * ec2help\n  * ec2instanceconnect\n  * ec2instanceconnecthelp")
    assert get_new_command(command) == ['aws ec2help help',
                                        'aws ec2instanceconnect help',
                                        'aws ec2instanceconnecthelp help']

# Generated at 2022-06-14 09:20:57.091940
# Unit test for function get_new_command

# Generated at 2022-06-14 09:21:10.648396
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("aws help", "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument subcommand: Invalid choice: 'help', maybe you meant: \n\n    help\n    --help\n    --help-command\n    --help-syntax\n    ", "")
    assert get_new_command(command) == ['aws --help "--help" "--help" "--help" "--help" "help"']

# Generated at 2022-06-14 09:21:18.251747
# Unit test for function get_new_command
def test_get_new_command():
    script = "aws s3 ls --regio"
    output = "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument --regio has multiple spellings, which one did you mean?\n* --region"
    assert get_new_command(Command(script=script, output=output)) == ["aws s3 ls --region"]

# Generated at 2022-06-14 09:21:31.519287
# Unit test for function get_new_command
def test_get_new_command():
    # 1
    command1 = Command('aws ec2 start-instances --instance-ids i-1234567890abcdef0',
                       "Invalid choice: 'start-instances', maybe you meant:\n"
                       "  status \n"
                       "  start-stop-instances \n"
                       "  stop-instances",
                       '')
    assert get_new_command(command1) == ['aws ec2 status --instance-ids i-1234567890abcdef0',
                                         'aws ec2 start-stop-instances --instance-ids i-1234567890abcdef0',
                                         'aws ec2 stop-instances --instance-ids i-1234567890abcdef0']
    # 2

# Generated at 2022-06-14 09:21:44.258853
# Unit test for function match

# Generated at 2022-06-14 09:21:55.458510
# Unit test for function match
def test_match():
    assert match(Command("aws help", "usage: aws [options] <command> <subcommand> [parameters]", ""))
    assert not match(Command("aws help", "usage: aws [options] <command> <subcommand> [parameters]", ""))
    assert not match(Command("aws help", "usage: aws [options] <command> <subcommand> [parameters]", ""))



# Generated at 2022-06-14 09:21:59.571611
# Unit test for function match
def test_match():
    command = Command("aws o")
    command.output = """
Usage: aws [options] [ ...]

aws: error: argument operation: Invalid choice, maybe you meant:
* operations
* operation
"""
    assert match(command)


# Generated at 2022-06-14 09:22:09.494966
# Unit test for function get_new_command

# Generated at 2022-06-14 09:22:19.404886
# Unit test for function get_new_command
def test_get_new_command():
    command = type('Command', (), {
        'script': 'aws help',
        'output': "Invalid choice: 'help', maybe you meant:   * help\n"
        })
    assert get_new_command(command) == \
        ['aws * help']

    command = type('Command', (), {
        'script': 'aws elb help',
        'output': "Invalid choice: 'help', maybe you meant:   add-tags           create-load-balancer      disable-zones-for-lb    describe-instance-health\n"
        })
    assert get_new_command(command) == \
        ['aws elb add-tags',
        'aws elb create-load-balancer',
        'aws elb disable-zones-for-lb',
        'aws elb describe-instance-health']

# Generated at 2022-06-14 09:22:31.552541
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("aws ec2 run-instance ", "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\n\nInvalid choice: 'run-instance', maybe you meant:\n        remove-tags-from-resource\n   *   run-instances", "", 0, "aws ec2 run-instance ")) == ['aws ec2 remove-tags-from-resource ', 'aws ec2 run-instances ']

# Generated at 2022-06-14 09:22:42.331875
# Unit test for function get_new_command

# Generated at 2022-06-14 09:22:48.953709
# Unit test for function match

# Generated at 2022-06-14 09:22:54.847220
# Unit test for function match
def test_match():
    assert match(Command('aws s3 mb s3://acme-logs/ --region us-east-1', 'usage: aws [options] <command> <subcommand> [parameters]\naws: error: argument subcommand: Invalid choice, maybe you meant:\n\n\tmb\t\t\tMake a bucket\n\ts3cp\tCopies data from and to Amazon S3\n\ts3ls\t\tList S3 objects and common prefixes under a prefix or all S3 buckets\n'))
    assert not match(Command('cd /tmp', ''))


# Generated at 2022-06-14 09:23:06.816744
# Unit test for function match
def test_match():
    assert match(Command("aws configure", "", "usage: aws [options] [parameters]", 1))

# Generated at 2022-06-14 09:23:12.571355
# Unit test for function match
def test_match():
    output = "usage: aws [options] <command> <subcommand> [<subcommand> ...]"\
            "[parameters]\nTo see help text, you can run:\n\t"\
            "aws help\n\taws <command> help\n\taws <command> <subcommand> "\
            "help\naws: error: argument <command>: Invalid choice: 'ec2e',"\
            "maybe you meant: encapsulate\n\t\tencrypted\n\t\tencryptor\n\t\t"\
            "encode\n\t\tec2\n\t\tact"\
            "aws: error: argument <command>: Invalid value: 'ec2e'"
    assert(match(Command(script = "", output = output)))


# Generated at 2022-06-14 09:23:16.109870
# Unit test for function match
def test_match():
    assert match(Command('aws', '--help'))
    assert match(Command('aws', 's3 ls'))
    assert not match(Command('aws', 's3 ls --parameter'))


# Generated at 2022-06-14 09:23:27.896435
# Unit test for function get_new_command

# Generated at 2022-06-14 09:23:36.371576
# Unit test for function match

# Generated at 2022-06-14 09:23:50.307853
# Unit test for function get_new_command

# Generated at 2022-06-14 09:24:01.709958
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 stop-instances', 'usage: aws [options] <command> <subcommand>', 'aws: error: argument subcommand: Invalid choice: \'sop-instances\', maybe you meant:\n  * start-instances\n  * stop-instances-by-instance-id', 'aws ec2 sop-instances'))
    assert match(Command('aws ec2 stop-instances', 'usage: aws [options] <command> <subcommand>', 'aws: error: argument subcommand: Invalid choice: \'sop-instances\', maybe you meant:\n  * start-instances\n  * stop-instances-by-instance-id', 'aws ec2 sop-instances')) == True

# Generated at 2022-06-14 09:24:06.749295
# Unit test for function get_new_command
def test_get_new_command():
    new_cmd = get_new_command(Command(script='aws s3 help', output="A sample output"))
    assert new_cmd[0] == 'aws s3 help'
    assert new_cmd[1] == 'aws s3 help'
    assert new_cmd[2] == 'aws s3 help'

# Generated at 2022-06-14 09:24:22.883691
# Unit test for function match

# Generated at 2022-06-14 09:24:31.415553
# Unit test for function match
def test_match():
    assert not match(Command('aws'))
    assert match(Command('aws ec2', "usage: aws [options] <command> <subcommand> [parameters]\n\
aws: error: argument subcommand: Invalid choice, maybe you meant:\n\
    ec2         Work with Amazon Elastic Compute Cloud (EC2) instances"))
    assert not match(Command('aws -V', "aws-cli/1.9.19 Python/2.6.6 Linux/2.6.18-164.el5 botocore/1.2.26"))
    assert not match(Command('aws ec2 run-instances --image-id ami-00000001', "aws: error: argument --image-id: Invalid AMI ID: 'ami-00000001'"))

# Generated at 2022-06-14 09:24:42.039420
# Unit test for function match
def test_match():
    assert match(Command('aws', '', 'usage: Unknown command'))
    assert match(Command('aws', '', 'usage: Invalid command'))
    assert match(Command('aws', '', 'usage: Invalid command\nmaybe you meant:'))
    assert not match(Command('aws', '', 'Unknown command'))
    assert not match(Command('aws', '', 'usage: Unknown command\nmaybe you meant:'))
    assert not match(Command('aws', '', 'Invalid command'))


# Generated at 2022-06-14 09:24:49.695780
# Unit test for function match
def test_match():
    output = "Unknown options: --filters.    See 'aws ec2 describe-instances help'".split()
    assert match(Command(script = "aws ec2 describe-instances", output = output))
    output = "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]".split()
    assert not match(Command(script = "aws ec2 describe-instances", output = output))


# Generated at 2022-06-14 09:25:01.027248
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('aws ec2 describe-instances')
    assert get_new_command(command) == ['aws ec2 describe-instances']
    command = Command('aws ec2 describe-instsnces')
    assert get_new_command(command) == ['aws ec2 describe-instances']
    command = Command('aws ec2 describe-instances --output json --color auto')
    assert get_new_command(command) == ['aws ec2 describe-instances --color auto --output json']
    command = Command('aws ec2 describe-instance --output json --color auto')
    assert get_new_command(command) == ['aws ec2 describe-instances --color auto --output json']

# Generated at 2022-06-14 09:25:09.355108
# Unit test for function get_new_command

# Generated at 2022-06-14 09:25:14.566177
# Unit test for function match
def test_match():
    command = Command("aws --version", "")
    assert match(command) is False
    command = Command("aws ec2 describe-instances", "")
    assert match(command) is False
    command = Command("aws", "usage:\n .* maybe you meant:")
    assert match(command) is True



# Generated at 2022-06-14 09:25:26.520947
# Unit test for function match

# Generated at 2022-06-14 09:25:35.900694
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command(Command('aws s3 ls', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]', 'aws: error: argument subcommand: Invalid choice, maybe you meant:', '* s3')) == ['aws s3 ls'])
    assert (get_new_command(Command('aws s3 ls', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]', 'aws: error: argument subcommand: Invalid choice, maybe you meant:', '* s3', '* cloudformation')) == ['aws s3 ls', 'aws cloudformation ls'])

# Generated at 2022-06-14 09:25:44.610311
# Unit test for function match
def test_match():
    assert match(Command("aws s3 ls",
                         "usage: aws [options] <command> <subcommand> [parameters]\naws: error: argument command: Invalid choice, valid choices are:\n* cp\n* ls\n* mb\n* mv\n* rb\n* rm\n* rsync\n* sync\n* website\nmaybe you meant: s3ls\n"))
    assert not match(Command("aws s3 ls", "bot@warbyparker.com's password: "))


# Generated at 2022-06-14 09:25:53.414074
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 --help', 'Invalid choice: "e"\nmaybe you meant:\n  ec2\n  ec2-instance-connect\n  ec2-instance-connect (truncated)...\n\nusage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\n  To see help text, you can run:\n  ...\n  For more information on a specific command, run:\n  ...'))

# Generated at 2022-06-14 09:25:55.127594
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 ran'))
    assert not match(Command('aws ec2 run'))


# Generated at 2022-06-14 09:26:09.650842
# Unit test for function match

# Generated at 2022-06-14 09:26:20.491213
# Unit test for function match
def test_match():
    assert match(Command('aws iam list-users', '', 'usage: aws [options] <command> <subcommand> [<subcommand> ...]\n\naws: error: argument subcommand: Invalid choice, maybe you meant:')).script == 'aws iam list-users'
    assert match(Command('aws iam list-users', '', 'usage: aws [options] <command> <subcommand> [<subcommand> ...]\n\naws: error: argument subcommand: Invalid choice, maybe you meant:\n\n* list-users')).script == 'aws iam list-users'

# Generated at 2022-06-14 09:26:33.495824
# Unit test for function match
def test_match():
    assert match(Command("", "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\n\nTo see help text, you can run: aws help\n\nUnknown options: --command\n"))
    assert not match(Command("", ""))
    assert not match(Command("", "invalid choice '--commant'\nusage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\n\nTo see help text, you can run: aws help\n\nUnknown options: --command\n"))



# Generated at 2022-06-14 09:26:38.026987
# Unit test for function match

# Generated at 2022-06-14 09:26:48.191267
# Unit test for function match
def test_match():
    assert match(Command('aws s3 ls', 'usage: aws [options] <command> <subcommand> [parameters]\naws: error: argument operation: Invalid choice: \'s3\', maybe you meant:\n        service\n        service-quotas\n        s3api\n        secretsmanager\n        securityhub\n        serverlessrepo\n        servicecatalog\n        ses\n        shield\n        signer\n        sms\n        snowball\n        sns\n        sqs\n\n'))
    assert not match(Command('aws s3 ls', ''))



# Generated at 2022-06-14 09:26:56.956072
# Unit test for function match
def test_match():
    output = ("usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\n"
              "aws: error: argument command: Invalid choice, valid choices are:\n"
              "  *  autoscaling  (maybe you meant: configservice)\n"
              "    cloudformation\n"
              "    cloudfront\n"
              "    cloudsearch\n"
              "    cloudtrail\n"
              "    cloudwatch\n"
              "    directoryservice\n"
              "    dynamodb\n"
              "    ec2\n")

    command = Command("aws s3 ls", output)
    assert match(command)
    assert get_new_command(command) == ['aws configservice ls']


# Generated at 2022-06-14 09:26:59.133607
# Unit test for function match
def test_match():
    assert match(Command('aws help', "usage:"))
    assert not match(Command('aws help', ""))


# Generated at 2022-06-14 09:27:05.504144
# Unit test for function match

# Generated at 2022-06-14 09:27:09.883334
# Unit test for function match
def test_match():
    assert(match(Command('aws s3 mb s3://abc', 'usage: aws [options] <command> <subcommand> [parameters]\naws: error: argument subcommand: Invalid choice, maybe you meant:\n\tmb\n\tmb-leg\n\tmB\n')))\
    == True


# Generated at 2022-06-14 09:27:23.139919
# Unit test for function match

# Generated at 2022-06-14 09:27:42.556878
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 describe-instances --filter Name=instance-state-code,Values=80,16', 'aws: error: argument --filter: Invalid choice: \'80,16\', maybe you meant:', '', 3))


# Generated at 2022-06-14 09:27:45.052057
# Unit test for function match
def test_match():
    assert match(Command('aws ec2'))


# Generated at 2022-06-14 09:27:54.425494
# Unit test for function match
def test_match():
    # Set up mock aws output
    wrong_command = "aws ec2 terminate-instances -i i-12345678"
    output = """usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help
aws: error: argument subcommand: Invalid choice, maybe you meant:
  instance
  instances

"""
    assert match(Command(wrong_command, output))
    # Test for false positive
    assert not match(Command(wrong_command, ""))


# Generated at 2022-06-14 09:27:58.410144
# Unit test for function match
def test_match():
    command = Command("aws ec2", "Invalid choice: 'ec2', maybe you meant:")
    assert match(command)
    command = Command("aws", "Invalid choice: 'ec2', maybe you meant:")
    assert match(command)
    command = Command("aws", "No such file or directory")
    assert not match(command)


# Generated at 2022-06-14 09:28:10.630633
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 start-instance --instance-ids i-12345678'))

# Generated at 2022-06-14 09:28:15.278037
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 describe-class-b',
                         "usage: aws [options] 'describe-class' [command_options] [ | 'describe-class']\n\n"
                         "aws: error: 'describe-class-b' is not a valid command.\n"
                         "See 'aws help' (maybe you meant: 'describe-class')\n")) is True


# Generated at 2022-06-14 09:28:23.119002
# Unit test for function get_new_command
def test_get_new_command():
    script = "aws ec2 ls"
    assert get_new_command(Command(script, "")) == ["aws ec2 list-instances"]
    assert get_new_command(Command(script, "Wrong ...")) == ["aws ec2 list-instances"]

# Generated at 2022-06-14 09:28:31.913163
# Unit test for function match
def test_match():
    command = Command("aws clouds", "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument command: Invalid choice, maybe you meant:\n  client-vpce-associate\n  client-vpn-associate\n  client-vpn-connect\n  describe-client-vpn-authorization-rules\n  describe-client-vpn-target-networks")
    assert match(command)



# Generated at 2022-06-14 09:28:38.653014
# Unit test for function match
def test_match():
	output = '''usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help
aws: error: argument command: Invalid choice, maybe you meant:
  config
'''
	assert match(Command(script='aws', output=output))


# Generated at 2022-06-14 09:28:49.407832
# Unit test for function match