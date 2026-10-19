

# Generated at 2022-06-14 09:18:55.748056
# Unit test for function get_new_command
def test_get_new_command():
    output = '\naws: error: argument subcommand: Invalid choice: \u0027ec2\u0027, maybe you meant:  \n  * lambda\n'
    assert get_new_command(Command('aws ec2', output)) == ['aws lambda']

# Generated at 2022-06-14 09:19:03.923134
# Unit test for function get_new_command
def test_get_new_command():
    script = '$ aws cloudformation deploy --stack-name test --template-file test.json'
    command = MagicMock(script=script, output='Invalid choice: \'deploy\', maybe you meant: * delete')
    expected = [
        'aws cloudformation delete --stack-name test --template-file test.json',
        'aws cloudformation deploy --stack-name test --template-file test.json'
    ]
    assert get_new_command(command) == expected

# Generated at 2022-06-14 09:19:05.521673
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 error'))


# Generated at 2022-06-14 09:19:16.192914
# Unit test for function match
def test_match():
    command1 = Command('aws foo bar')
    command2 = Command('aws s3 bar')
    command3 = Command('aws')
    command4 = Command('aws s3')
    command5 = Command('aws s3 cp')
    command6 = Command('aws s3 cp foo bar')
    
    # test 1
    assert match(command1) == False
    # test 2
    assert match(command2) == True
    # test 3
    assert match(command3) == False
    # test 4
    assert match(command4) == False
    # test 5
    assert match(command5) == True
    # test 6
    assert match(command6) == True


# Generated at 2022-06-14 09:19:16.693764
# Unit test for function match
def test_match():
    assert match(Command('aws s3 ls sse'))


# Generated at 2022-06-14 09:19:25.379316
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 describe-instances', output='usage: aws [options] <command> <subcommand> [parameters]'))
    assert not match(Command('aws ec2 describe-instances', output='Invalid choice: \'ec2d\', maybe you meant: ec2d'))

# Generated at 2022-06-14 09:19:37.496674
# Unit test for function match
def test_match():
    output = """usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
           To see help text, you can run:

           aws help
           aws <command> help
           aws <command> <subcommand> help
           aws: error: argument command: Invalid choice, valid choices are:
           cloudformation   | cloudfront        | cloudhsm           | cloudsearch       | cloudsearchdomain | cloudtrail
           cloudwatch       | cognito-identity  | cognito-sync       | configservice     | datapipeline      | directconnect
           dynamodb         | ec2               | ecs                | elasticache       | elasticbeanstalk  | elastictranscoder
           elb              | emr               | glacier
           maybe you meant: ec2"""


# Generated at 2022-06-14 09:19:49.088607
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 help launch-instances', 'usage: launch-instances [-h] [--debug | --no-debug] [--profile PROFILE] [--region REGION] [--endpoint-url ENDPOINT_URL] [--cli-input-json JSON] [--generate-cli-skeleton JSON] [--cli-auto-prompt] [--query-cli-formatter QUERY_CLI_FORMATTER] [--cli-full-response] [--cli-read-timeout CLI_READ_TIMEOUT] [--cli-connect-timeout CLI_CONNECT_TIMEOUT] (--cli-input-json | --generate-cli-skeleton | --cli-auto-prompt)')) == True


# Generated at 2022-06-14 09:19:51.442322
# Unit test for function match
def test_match():
    command = Command('aws sdb')
    assert match(command)


# Generated at 2022-06-14 09:20:03.286627
# Unit test for function get_new_command
def test_get_new_command():
    print("Testing aws.py...")
    expected = [
        u'aws ec2 describe-snapshots --region us-west-2 --owner-ids 123456789012',
        u'aws ec2 describe-snapshots --region us-west-2',
        u'aws ec2 describe-snapshots --region us-west-2 --snapshot-id snap-1234567890abcdef0'
    ]

    class MockCommand:
        def __init__(self, script, output):
            self.script = script
            self.output = output

        # TODO: For some reason, t.o() crashes on Windows
        def __repr__(self):
            return self.output


# Generated at 2022-06-14 09:20:09.180017
# Unit test for function get_new_command
def test_get_new_command():
	assert get_new_command(Command('aws --help')) == "aws help"
	assert get_new_command(Command('aws ec2 --help')) == "aws ec2 help"


# Generated at 2022-06-14 09:20:20.832790
# Unit test for function match

# Generated at 2022-06-14 09:20:33.316523
# Unit test for function get_new_command
def test_get_new_command():
	Command = namedtuple('Command', ['script', 'output'])

# Generated at 2022-06-14 09:20:43.878490
# Unit test for function get_new_command

# Generated at 2022-06-14 09:20:56.895792
# Unit test for function match
def test_match():
    assert match(Command('aws help', output='usage: aws [options] <command> <subcommand> [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument subcommand: Invalid choice, valid choices are:\n  help',
                          stderr=''))
    assert not match(Command('aws help', output='usage: aws [options] <command> <subcommand> [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help',
                             stderr=''))


# Generated at 2022-06-14 09:21:12.028495
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws', 'aws s3 ls\nusage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run: aws help\naws: error: argument subcommand: Invalid choice, valid choices are:\n  cp\n  ls\n  mb\n  mv\n  rb\n  rsync\n  s3api\n  sync\n  website\n\nMaybe you meant:\n  s3\n')) == ['aws s3 ls']

# Generated at 2022-06-14 09:21:15.173393
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws', 'aws ec2 describe-instances --filter "Name=instance-state-name,Values=running"')) == ['aws ec2 describe-instances --filters "Name=instance-state-name,Values=running"']


# Generated at 2022-06-14 09:21:19.483805
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("aws ec2 start-instance --instance-ids blah blah")
    assert([replace_argument(command.script, "start-instance", o) for o in ["start-instances"]] == \
           get_new_command(command))

# Generated at 2022-06-14 09:21:22.397145
# Unit test for function match
def test_match():
    command = Command('aws ec2 describe-instances --instance-id --region us-east-1')
    assert match(command)


# Generated at 2022-06-14 09:21:31.081848
# Unit test for function get_new_command
def test_get_new_command():
    script = 'aws <command> [<subcommand> [<subcommand> ...]] [parameters] [options]\n'
    output = 'Invalid choice: \'foobar\', maybe you meant:\n' \
             '    * foo\n' \
             '    * bar'
    command = type('obj', (object,), {'script': script, 'output': output})
    assert get_new_command(command) == ['aws <command> [<subcommand> [<subcommand> ...]] [parameters] [options]', 'aws <command> [<subcommand> [<subcommand> ...]] [parameters] [options]']

# Generated at 2022-06-14 09:21:45.025096
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('aws ec2 start-instances --instance-ids i-55555') == [
        'aws ec2 start-instances --instance-ids i-55555'
    ]
    assert get_new_command('aws ec2 start-instances --instance-id i-55555') == [
        'aws ec2 start-instances --instance-ids i-55555'
    ]
    assert get_new_command('aws ec2 start-instance --instance-ids i-55555') == [
        'aws ec2 start-instances --instance-ids i-55555'
    ]
    assert get_new_command('aws ec2 start-instance --instance-id i-55555') == [
        'aws ec2 start-instances --instance-ids i-55555'
    ]

# Generated at 2022-06-14 09:21:56.209962
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('aws ec2 describe-something --filters Name=instance-type,Values=t2.medium')
    assert get_new_command(command) == ['aws ec2 describe-something --filters Name=instance-type,Values=t2.micro', 'aws ec2 describe-something --filters Name=instance-type,Values=t2.small', 'aws ec2 describe-something --filters Name=instance-type,Values=t2.large']

# Generated at 2022-06-14 09:21:58.761451
# Unit test for function match
def test_match():
    def test_match():
        assert (match(Command('aws --bad option', '')))
        assert not (match(Command('aws --good option', '')))



# Generated at 2022-06-14 09:22:04.818579
# Unit test for function match
def test_match():
    assert match(Command('aws',
                         output="usage: aws [options] [ ...] [parameters]\naws: error: Invalid choice: 'non', maybe you meant:\n\tnone\n\tnon-current\n\tnot-null\n\tnoncurrent\n\tnonzero\n\tnon-null\n\ttrue\n\tnull\n\tfalse\n\tnot-null\n\tnone\n\tnon-current\n"))


# Generated at 2022-06-14 09:22:13.258547
# Unit test for function match
def test_match():
    assert match({
        'command': None,
        'exit_code': 0,
        'output': 'Invalid choice: \'version\', maybe you meant: \n  * command\n  * configure\n  * create-alternate-name\n  * help\n  * info\n  * maint\n  * man\n  * network\n  * options\n  * subcommands\n  * update\n  * upgrade\n  * version-info\n'
    }) is True


# Generated at 2022-06-14 09:22:18.736043
# Unit test for function get_new_command
def test_get_new_command():
    output = '''usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help

Invalid choice: 's3/bucket/put', maybe you meant:
  * s3/bucket/acl
  * s3/bucket/cors
  * s3/bucket/delete
  * s3/bucket/location
  * s3/bucket/policy
  * s3/bucket/put
  * s3/bucket/website
'''
    command = Mock(output=output, script='aws s3/bucket/put')

# Generated at 2022-06-14 09:22:24.558890
# Unit test for function match
def test_match():
    from tests.utils import Command
    assert match(Command('aws iam make-me-a-sandwich'))
    assert match(Command('aws iam make-me-a-sandwich foo bar baz'))
    assert not match(Command("echo 'aws iam make-me-a-sandwich'"))



# Generated at 2022-06-14 09:22:28.853629
# Unit test for function match
def test_match():
    assert match(Command('aws help', ''))
    assert match(Command('aws s3 help', ''))
    assert not match(Command('aws s3 ls', ''))



# Generated at 2022-06-14 09:22:40.863843
# Unit test for function match

# Generated at 2022-06-14 09:22:46.003796
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('aws ec2 describe-vpcs --filters Name=cidr,Valuse=10.0.0.0/16')
    assert get_new_command(command) == ["aws ec2 describe-vpcs --filters Name=cidr,Values=10.0.0.0/16"]

# Generated at 2022-06-14 09:22:52.727352
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    
    result = get_new_command(Command(script='aws --version',
                                     stdout='aws: error: argument --version: Invalid choice: \'--version\', maybe you meant:\n  * --version\n  * console\n  * configure',
                                     stderr='')
                            )
    assert ['aws --version', 'aws console', 'aws configure'] == result

# Generated at 2022-06-14 09:23:04.078919
# Unit test for function get_new_command
def test_get_new_command():
    script = "aws s3 ls s3://bucket"

# Generated at 2022-06-14 09:23:08.834138
# Unit test for function match
def test_match():
    command = Command('aws ec2 help',
            """usage: aws [options] <command> <subcommand> [parameters]
    To see help text, you can run:

      aws help
      aws <command> help
      aws <command> <subcommand> help
    aws: error: argument command: Invalid choice: 'ec2 help', maybe you meant:
    * elbv2
    * elb
    * ec2
    * emr
    * s3api
    * s3
    * dynamodbstreams
    * dynamodb
    * kinesis
    """)
    assert match(command)


# Generated at 2022-06-14 09:23:19.975569
# Unit test for function match
def test_match():
    output_true = '''usage: aws [options] <command> <subcommand> [parameters]
aws: error: argument command: Invalid choice, valid choices are:

maybe you meant:
  ec2
  ses
  iam


aws: error: argument command: Invalid choice, valid choices are:

'''
    output_false = '''usage: aws [options] <command> <subcommand> [parameters]
aws: error: argument command: Invalid choice, valid choices are:

'''

    assert_true = match(Command(script = 'aws [options] <command> <subcommand> [parameters]', output = output_true))
    assert_false = match(Command(script = 'aws [options] <command> <subcommand> [parameters]', output = output_false))
    

# Generated at 2022-06-14 09:23:24.564129
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws autoscaling describe-a')) == \
       ['aws autoscaling describe-account-limits']
    assert get_new_command(Command('aws autoscaling describe-a --region us-east-1')) == \
       ['aws autoscaling describe-account-limits --region us-east-1']

# Generated at 2022-06-14 09:23:26.737156
# Unit test for function match
def test_match():
    # Assert that function match returns true if the output has the error message
    assert match(Command('aws ec2 describe', ''))


# Generated at 2022-06-14 09:23:33.543536
# Unit test for function match
def test_match():
    assert match(Command('aws s3 mb s3://aws-logs-760158085601-us-west-2/home/ec2-user/aws/s3/', '', 'usage: aws [options] <command> <subcommand> [<subcommand> ...]\naws: error: argument subcommand: Invalid choice, maybe you meant:', 1))
    assert not match(Command('git status', '', 'On branch master\nYour branch is up-to-date with \'origin/master\'.\n\nnothing to commit, working directory clean', 1))



# Generated at 2022-06-14 09:23:38.310683
# Unit test for function match
def test_match():
    cmd = Command('aws ec2 describe-instances',
                  'usage: aws [options] &lt;command&gt; &lt;subcommand&gt; '
                  '[parameters]\naws: error: argument &lt;command&gt;: '
                  'Invalid choice: \'ec2\', maybe you meant:\n'
                  '        events\n        ecr\n        ec2\n'
                  '        ecs\n        efs\n        eks')
    assert match(cmd)


# Generated at 2022-06-14 09:23:40.278107
# Unit test for function match
def test_match():
    command = Command('aws')
    assert match(command)


# Generated at 2022-06-14 09:23:47.858132
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 help', 'aws: error: argument command: Invalid choice: \'ec2 help\', maybe you meant:\n  * describe-instances\n  * describe-reserved-instances\n  * describe-reserved-instances-offerings\n  * describe-vpcs\n  * describe-security-groups\n'))
    assert not match(Command('aws ec2 help', ''))



# Generated at 2022-06-14 09:23:55.647518
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws', 'aws s3 mb s3://test-bucket/', 'usage: aws [options] <command> <subcommand> [parameters]\naws: error: argument subcommand: Invalid choice, maybe you meant:', '')) == ['aws s3 mb s3://test-bucket']

# Generated at 2022-06-14 09:24:01.714038
# Unit test for function match
def test_match():
    new_command = get_new_command()
    # Test for aws commands that returns error
    command = Command('aws ec2 terminate-instances --instance-ids i1')
    assert match(command)

    # Test for aws commands that doesn't returns error
    command = Command('aws ec2 describe-instances')
    assert not match(command)

# Generated at 2022-06-14 09:24:05.903837
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("aws ec2 describe-instances", "Invalid choice: 'ec2', maybe you meant:\n  * ec2\n  * cf", "")
    assert get_new_command(command) == ['aws ec2 describe-instances']

# Generated at 2022-06-14 09:24:12.872297
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws ec2 help', 'aws: error: too few arguments')) == ['aws help ec2']

# Generated at 2022-06-14 09:24:24.942537
# Unit test for function get_new_command

# Generated at 2022-06-14 09:24:27.329286
# Unit test for function match
def test_match():
	cmd = Command('aws ec2 describe-real')
	assert match(cmd)



# Generated at 2022-06-14 09:24:28.643576
# Unit test for function match
def test_match():
    assert match(Command('aws'))


# Generated at 2022-06-14 09:24:38.862539
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    assert get_new_command(Command('aws s3 rb s3://bucket', '', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\naws: error: argument subcommand: Invalid choice: \'rb\', maybe you meant:\n\tcp\n\tsync\nTo see help text, you can run:\naws help\naws <command> help\naws <command> <subcommand> help\n	* cp\n	* sync')) == ['aws s3 cp s3://bucket', 'aws s3 sync s3://bucket']

# Generated at 2022-06-14 09:24:43.776748
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script = 'aws ec2 describe-regions',
                      output = """usage: aws [options] <command> <subcommand> [parameters]
aws: error: argument subcommand: Invalid choice, valid choices are:
        describe-regions
        describe-regions-v2
        endpoints

maybe you meant:
        describe-regions-v2
        describe-regions
        endpoints""")
    assert get_new_command(command) == ['aws ec2 describe-regions-v2', 'aws ec2 describe-regions', 'aws ec2 endpoints']

# Generated at 2022-06-14 09:24:55.578647
# Unit test for function match
def test_match():
    match_case = [
        ('Invalid choice: \'e2ee\', maybe you meant:', True),
        ('aws e2ee', False),
        ('aws', False),
        ('aws e2ee', False),
        ('aws', False),
        ('aws s3', False),
        ('aws', False),
        ('aws s3', False),
        ('aws', False),
        ('aws e2ee', False),
        ('aws', False),
        ('aws s3', False),
        ('aws', False),
        ('aws e2ee', False),
        ('', False),
        ('aws s3', False),
        ('', False),
        ('aws e2ee', False),
        ('', False),
        ('aws s3', False),
        ('', False)
    ]

# Generated at 2022-06-14 09:25:00.674566
# Unit test for function match
def test_match():
    assert match(Command('aws --version', 'usage: aws [options] [parameters]', ''))
    assert not match(Command('echo foo', '', ''))


# Generated at 2022-06-14 09:25:13.985384
# Unit test for function match
def test_match():
    # Mistake made in 'aws help' command
    assert(match(Command('aws help', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\n\naws: error: Invalid choice: \'help\', maybe you meant:', None)) is True)
    # Mistake made in 'aws s3 help' command

# Generated at 2022-06-14 09:25:18.140927
# Unit test for function get_new_command
def test_get_new_command():
    command = 'aws ec2'
    mistake = 'ec2'
    options = ['ecr']
    assert get_new_command(command) == [replace_argument(command, mistake, o) for o in options]


# Generated at 2022-06-14 09:25:27.678944
# Unit test for function get_new_command
def test_get_new_command():
    command = make_command("aws s3 ls", "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\n\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\n\nUnknown options: s3", "aws s3 ls")
    assert get_new_command(command) == ["aws service list", "aws s3 ls"]

# Generated at 2022-06-14 09:25:34.283279
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws s3 ls --region us-east-1', ''))\
        == ['aws s3 ls --region us-east-2']
    assert get_new_command(Command('aws iam add-role-to-instance-profile --profile my-profile', ''))\
        == ['aws iam add-instance-profile-to-role --instance-profile my-profile']
    assert get_new_command(Command('aws iam attach-role-policy --policy-name S3Access --role-name S3Role --profile myprofile', ''))\
        == ['aws iam attach-role-policy --policy-arn "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess" --role-name S3Role --profile myprofile']

# Generated at 2022-06-14 09:25:47.148122
# Unit test for function match

# Generated at 2022-06-14 09:25:54.201784
# Unit test for function match
def test_match():
    command = Command('aws ec2 describe-instances --region us-east-1', 'aws: error: argument operation: Invalid choice, maybe you meant:\n\tdisconnect-vpn-gateway\n\tattach-vpn-gateway\n\tdescribe-vpn-gateways\n\tdetach-vpn-gateway\n\tcreate-vpn-gateway\n\tdescribe-vpn-connections\n\tdescribe-customer-gateways\n\tdescribe-vpn-gateway-attachments\n\tcreate-customer-gateway\n\n', 'aws')
    assert match(command)


# Generated at 2022-06-14 09:25:55.881389
# Unit test for function get_new_command
def test_get_new_command():
    new_command = get_new_command(Command('aws ec2 --stop'))
    assert new_command == ['aws ec2 --start']

enabled_by_default = True

# Generated at 2022-06-14 09:26:04.727455
# Unit test for function match
def test_match():
    assert match(Command("aws help",
        """usage: aws [options] &lt;command&gt; &lt;subcommand&gt; &lt;subcommand&gt; ... [parameters]
    To see help text, you can run:

      aws help
      aws &lt;command&gt; help
      aws &lt;command&gt; &lt;subcommand&gt; help
    aws: error: Invalid choice: 'not-a-valid-command', maybe you meant:
      cloudformation
      cloudwatch
      configure
      deploy
      dynamodb
      ec2
      help
      iam
      s3cmd""", ""))


# Generated at 2022-06-14 09:26:17.341703
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    output = """
usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help
aws: error: argument subcommand: Invalid choice, maybe you meant:
* ec2
* rds
* s3
    """
    command = Command("aws sqs listqueues", output)
    new_command = get_new_command(command)
    assert new_command == 'aws ec2 listqueues'
    assert get_new_command(Command("aws sqs listqueues", "Shit")) == None

enabled_by_default = True

# Generated at 2022-06-14 09:26:35.198347
# Unit test for function match
def test_match():
    output1 = "Unknown options: --term, --sport"
    output2 = "usage: aws [options] <command> <subcommand> [parameters]\nTo see help text, you can run:\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument operation: Invalid choice, maybe you meant: describe"
    output3 = "usage: aws [options] <command> <subcommand> [parameters]\nTo see help text, you can run:\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument operation: Invalid choice, maybe you meant: list-function"

    command1 = Command('aws s3 ls --term --sport', output1)
   

# Generated at 2022-06-14 09:26:38.078342
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws ec2 instacne-type')) == ['aws ec2 instance-type']


# Generated at 2022-06-14 09:26:48.710928
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 ls Error',
                         'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\n\n',
                         'aws: error: argument subcommand: Invalid choice, maybe you meant:\n',
                         '\n',
                         '* ls       (p. 135)\n',
                         '* mls      (p. 140)\n',
                         '* lls      (p. 136)\n',
                         '* ms       (p. 141)\n',
                         '* mv       (p. 141)\n'))



# Generated at 2022-06-14 09:26:54.005800
# Unit test for function match
def test_match():
    assert match(Command('aws', output='usage: blah, maybe you meant:'))
    assert not match(Command('aws', output='usage: blah, maybe you did not mean:'))
    assert match(Command('aws', output='''aws: error: argument command: Invalid choice, valid choices are:
* modify-image-attribute
usage: aws [options] <command> <subcommand> [parameters]
aws: error: argument command: Invalid choice: 'blah', maybe you meant:
* modify-image-attribute
'''))


# Generated at 2022-06-14 09:26:59.594966
# Unit test for function get_new_command
def test_get_new_command():
    command_output_example = ("usage: aws [options] <command> <subcommand> [parameters]\n"
                              "aws: error: argument command: Invalid choice: 'ssssssss'\n"
                              "maybe you meant: sg")
    command_example = type('cmd', (object,), {
        'output': command_output_example,
        'script': "aws ssssssss"
    })
    assert get_new_command(command_example) == ["aws sg"]

# Generated at 2022-06-14 09:27:01.643224
# Unit test for function match
def test_match():
    assert match(Command('aws s3 ls'))
    assert not match(Command(''))
    assert not match(Command('ls s3'))
    assert match(Command('aws s3 ls', ''))


# Generated at 2022-06-14 09:27:12.388830
# Unit test for function match
def test_match():
    assert match(Command('aws ec2', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument subcommand: Invalid choice, valid choices are:\n\n* ec2\n* ecs\n* efs\n* rds\n* iam\n* elasticache\n* ecr\n* lambda\n* opsworks\n* emr\n*\nmaybe you meant:\n\n* ecr\n* ecs\n* efs\n* emr\n* ec2'))



# Generated at 2022-06-14 09:27:25.711715
# Unit test for function match
def test_match():
    assert match(Command('aws s3 cp --options foo', '', 'usage: aws [options] <command> <subcommand> [<subcommand> ...]'))
    assert match(Command('aws s3 cp --options foo', '', 'Invalid choice: \'--options\', maybe you meant:\n    --profile'))
    assert not match(Command('aws s3 cp --options foo', '', 'usage: aws [options] <command> <subcommand> [<subcommand> ...]\n\naws: error: argument command: Invalid choice'))


# Generated at 2022-06-14 09:27:32.680100
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws ec2 describe-images --output text')) == ['aws ec2 describe-images --output text']
    assert get_new_command(Command('aws ec2 describe-images --output json')) == ['aws ec2 describe-images --output json']
    assert get_new_command(Command('aws ec2 describe-images --output text')) == ['aws ec2 describe-images --output text']


enabled_by_default = True

# Generated at 2022-06-14 09:27:42.649819
# Unit test for function match

# Generated at 2022-06-14 09:27:47.388081
# Unit test for function match
def test_match():
    assert match(Command('aws s3 ls', "usage:"))
    assert not match(Command('aws s3 ls', "Listing bucket"))



# Generated at 2022-06-14 09:27:53.940563
# Unit test for function match
def test_match():
    assert not match(Command(script='', output=''))
    assert match(Command(script='', output='usage: '))
    assert match(Command(script='', output='maybe you meant:'))
    assert match(Command(script='', output='usage: \nmaybe you meant:'))
    assert not match(Command(script='', output='usage: maybe you meant:'))
    assert match(Command(script='', output='usage: maybe you meant:\n* CMD'))


# Generated at 2022-06-14 09:28:01.881342
# Unit test for function match

# Generated at 2022-06-14 09:28:07.663399
# Unit test for function match
def test_match():
    assert match(Command('aws s3mv s3://bucket1/file1 s3://bucket2/file1',
                         'usage: aws [options]                                                                                                                             \naws: error: argument command: Invalid choice, maybe you meant:                                                                                           \n  configure     \tConfigure the AWS Command Line Interface',
                         1))

# Generated at 2022-06-14 09:28:13.435574
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("aws ec2 describe-key-pairs --filters Name=key-name,Values=foooo") == [
        "aws ec2 describe-key-pairs --filters Name=key-name,Values=foo",
        "aws ec2 describe-key-pairs --filters Name=key-name,Values=foos"]

# Generated at 2022-06-14 09:28:23.781581
# Unit test for function match

# Generated at 2022-06-14 09:28:30.139223
# Unit test for function match
def test_match():
    output = """usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help
aws: error: argument --profile: Invalid choice: 'profil', maybe you meant:
  * profile"""
    assert match(Command('aws', output=output))


# Generated at 2022-06-14 09:28:46.434707
# Unit test for function match
def test_match():
    assert match(Command('aws help', 'Invalid choice: "kms", maybe you meant:', 'aws'))
    assert match(Command('aws help', 'Invalid choice: "s3", maybe you meant:', 'aws'))
    assert match(Command('aws help', 'Invalid choice: "kms", maybe you meant:', 'aws'))
    assert match(Command('aws help', 'Invalid choice: "dynamodb", maybe you meant:', 'aws'))
    assert not match(Command('aws help', 'Invalid choice: "kms", maybe you meant:', ''))
    assert not match(Command('aws help', 'Invalid choice: "s3", maybe you meant:', ''))
    assert not match(Command('aws help', 'Invalid choice: "kms", maybe you meant:', ''))

# Generated at 2022-06-14 09:28:58.749799
# Unit test for function get_new_command
def test_get_new_command():
    output = u"""usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help
aws: error: argument subcommand: Invalid choice, maybe you meant:
* subcommand
* subcommand
* subcommand
   * subcommand
   * subcommand
   * subcommand
   * subcommand
   * subcommand
   * subcommand
See 'aws help' for descriptions of global parameters.
"""
    command = Command("aws s3", "", "", output)