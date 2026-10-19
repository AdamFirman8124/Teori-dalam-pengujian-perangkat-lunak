

# Generated at 2022-06-14 09:19:01.267306
# Unit test for function get_new_command
def test_get_new_command():
    script = 'aws ec2 describe-instances'

# Generated at 2022-06-14 09:19:05.365246
# Unit test for function match
def test_match():
    assert match(Command('aws', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]'))
    assert not match(Command('aws', 'there is no typo'))


# Generated at 2022-06-14 09:19:14.939149
# Unit test for function get_new_command
def test_get_new_command():
    script = "aws ec2"
    output = "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument subcommand: Invalid choice, maybe you meant:\n  subnet"
    command = type('obj', (object,), {'script': script, 'output': output})
    error = get_new_command(command)
    assert "aws ec2 subnet" in error

# Generated at 2022-06-14 09:19:24.465913
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('aws iam users')
    output = ("usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\n"
              "   or: aws [options] <command> <subcommand> [<subcommand> ..."
              " ...] <action> <arg> [<arg> ...]\n"
              "To see help text, you can run:\n"
              "aws help\n"
              "aws <command> help\n"
              "aws <command> <subcommand> help\n"
              "aws: error: argument command: Invalid choice: 'iam users',"
              " maybe you meant: users")
    command.output = output
    assert get_new_command(command) == ['aws users']

# Generated at 2022-06-14 09:19:29.913006
# Unit test for function match
def test_match():
    assert match(Command('aws s3 cp s3://somebucket/somefile.txt .',
                         "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\n\n...",
                         123))
    assert not match(Command('some command', 'some output', 123))



# Generated at 2022-06-14 09:19:33.800215
# Unit test for function get_new_command
def test_get_new_command():
    command = 'aws help'
    assert get_new_command(command)[0] == 'aws'
    command = 'aws'
    assert get_new_command(command)[0] == 'aws'

# Generated at 2022-06-14 09:19:38.753144
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('aws s3 mb s3://test --region eu-west-1') == ['aws s3 mb s3://test --region eu-west-1', 'aws s3 mb s3://test --region eu-west-2']

# Generated at 2022-06-14 09:19:49.881417
# Unit test for function match

# Generated at 2022-06-14 09:19:55.678769
# Unit test for function match
def test_match():
    example = """usage: aws [options] <command> <subcommand> [parameters]
aws: error: argument operation: Invalid choice, valid choices are:
* create
* delete
* list
* modify
* describe
maybe you meant: delete"""
    assert match(Command(example, ""))



# Generated at 2022-06-14 09:20:04.721405
# Unit test for function get_new_command
def test_get_new_command():
    command = type('Command', (object,), {'script': 'aws ec2 help', 'output': 'usage: aws [options] <command> <subcommand> [parameters]\naws: error: argument command: Invalid choice: \'help\', maybe you meant:\n        * ec2\n        * ecs\n        * ecr\n        * ecr-login'})
    assert ['aws ec2 help', 'aws ecs help', 'aws ecr help', 'aws ecr-login help'] == get_new_command(command)

# Generated at 2022-06-14 09:20:14.504539
# Unit test for function get_new_command
def test_get_new_command():
    command = "aws ec2 describe-security-groups"
    options = ['ec2', 's3', 'sns', 'sqs', 'cloudfront', 'describe-security-groups', 'describe-snapshots', 'describe-snapshots', 'snapshots', 'describe-snapshots', 's3', 's3', 's3', 's3', 's3', 's3', 's3']
    matched = [(command, options)]

    assert get_new_command(command) == matched


# Generated at 2022-06-14 09:20:23.790990
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws s3 ls',
        "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument subcommand: Invalid choice: 's3', maybe you meant: \n* services\n",
        0)) == ['aws services ls']


enabled_by_default = True

# Generated at 2022-06-14 09:20:25.490110
# Unit test for function match
def test_match():
    assert match(Command('aws --elasticmapreduce'))


# Generated at 2022-06-14 09:20:35.799778
# Unit test for function get_new_command
def test_get_new_command():

    # Generic test case
    command_sample = Command('aws ec2 create-tags --resources vol-32159 --tag Name=test-volume --tag Env=prod --tag Role=splunk', 'aws: error: argument --tag: Invalid choice: \'Name=test-volume\', maybe you meant:\n  --tags')
    expected_output = [
        'aws ec2 create-tags --resources vol-32159 --tags Name=test-volume --tag Env=prod --tag Role=splunk',
        'aws ec2 create-tags --resources vol-32159 --tags Name=test-volume --tags Env=prod --tag Role=splunk']

    assert get_new_command(command_sample) == expected_output

    # Test case for when the mistake is the 2nd parameter

# Generated at 2022-06-14 09:20:39.050111
# Unit test for function get_new_command
def test_get_new_command():
    match = mock.Mock(output="Invalid choice: 'abc', maybe you meant:\n  * def")
    assert get_new_command(match) == ["aws def"]

# Generated at 2022-06-14 09:20:40.366128
# Unit test for function match
def test_match():
    assert match(Command('aws s3 lss', ''))


# Generated at 2022-06-14 09:20:42.118994
# Unit test for function match
def test_match():
    assert match(Command('aws s3 ls', ''))
    assert not match(Command('ls', ''))


# Generated at 2022-06-14 09:20:48.900262
# Unit test for function match
def test_match():
    assert match(Command("aws s3cp s3://foo s3://bar", "usage: aws [options] <command> <subcommand> [parameters]\nError: Invalid choice: 's3cp', maybe you meant: \n* s3", ""))
    assert not match(Command("aws s3 ls s3://bucket_name", "", ""))

# Generated at 2022-06-14 09:21:00.319612
# Unit test for function match
def test_match():
    assert match(Command('aws --help',
                         'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\n'
                         'To see help text, you can run:\n'
                         '\n'
                         '  aws help\n'
                         '  aws <command> help\n'
                         '  aws <command> <subcommand> help\n'
                         'aws: error: argument --help: Invalid choice, maybe you meant:\n'
                         '                 help\n'
                         '                 help \n'
                         '                 CLOUDFORMATION',
                         None, 123))


# Generated at 2022-06-14 09:21:11.377867
# Unit test for function get_new_command
def test_get_new_command():
    args = ['aws', 'ec2', 'create-qoute-request']
    cmd = Command(script=' '.join(args), stdout="usage: aws [options] <command> <subcommand>\n[...]\n\ncommands:\n* create-qoute-request\n* [...]\n\nInvalid choice: 'create-qoute-request', maybe you meant:\n* create-quote-request", stderr='', env={})
    print(get_new_command(cmd))


enabled_by_default = True

# Generated at 2022-06-14 09:21:21.018804
# Unit test for function match

# Generated at 2022-06-14 09:21:24.012358
# Unit test for function match
def test_match():
    assert not match(Command("foo", "", "usage:"))
    assert not match(Command("foo", "", "maybe you meant:"))
    assert match(Command("foo", "", "usage:\nmaybe you meant:"))


# Generated at 2022-06-14 09:21:33.950187
# Unit test for function get_new_command

# Generated at 2022-06-14 09:21:39.801093
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws s3 ls', """(aws: error: argument subcommand: Invalid choice: 's3', maybe you meant:
  * s3api
    s3
See 'aws help' for descriptions of global parameters.
)""")) == ['aws s3api ls', 'aws s3 ls']

# Generated at 2022-06-14 09:21:48.459301
# Unit test for function get_new_command
def test_get_new_command():
    output = """
usage: aws [options] <command> <subcommand> [parameters]
aws: error: option --s3 (expected at most 1 argument)

aws: error: unexpected argument s3://aws-logs-298926889618-eu-west-1/elasticloadbalancing/eu-west-1/2017/05/27/
        maybe you meant:
            --s3
Try 'aws help' for more information.
    """
    assert get_new_command(type('', (), {'script': 'aws --s3', 'output': output})) == ['aws --s3']


# Generated at 2022-06-14 09:22:00.637146
# Unit test for function get_new_command

# Generated at 2022-06-14 09:22:07.218429
# Unit test for function get_new_command
def test_get_new_command():
    def check_command(command):
        assert get_new_command(command) == ['aws sqs', 'aws s3']

    # Uses the example of the aws --help command
    command = Command('aws', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\n'
                             'aws: error: argument command: Invalid choice, maybe you meant:\n'
                             '   * sqs\n'
                             '   * s3\n'
                             'See \'aws help\' for descriptions of global parameters.')

    check_command(command)

# Generated at 2022-06-14 09:22:14.434651
# Unit test for function match

# Generated at 2022-06-14 09:22:23.313344
# Unit test for function get_new_command
def test_get_new_command():
    output = """
    usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
    To see help text, you can run:

      aws help
      aws <command> help
      aws <command> <subcommand> help

    aws: error: argument subcommand: Invalid choice, maybe you meant:
            ecs | es | iam | rds | s3* | sdb | ses | sts | support

    """
    command=Command("aws s3 --version",output)
    assert get_new_command(command) == ["aws s3 --version"]

# Generated at 2022-06-14 09:22:30.632304
# Unit test for function match
def test_match():
    assert match(Command('aws lambda list-event-source-mappings --function-name myfunction', 'usage: aws [options] <command> <subcommand> [parameters]\naws: error: argument --function-name: Invalid choice: \'myfunction\', maybe you meant:', 'aws lambda list-event-source-mappings --function-name myfunction'))



# Generated at 2022-06-14 09:22:47.061543
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("aws help")
    command.output = """usage: aws [options] <command> <subcommand> [parameters]
aws: error: argument command: Invalid choice, valid choices are:

configure       Configure the AWS Command Line Interface
ec2             Amazon Elastic Compute Cloud
help            Display help text
iam             AWS Identity and Access Management
s3              Amazon Simple Storage Service
sns             Amazon Simple Notification Service
sqs             Amazon Simple Queue Service

Maybe you meant: ec2

To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help
"""
    assert [replace_argument(command.script, "help", "ec2")] == get_new_command(command)

# Generated at 2022-06-14 09:22:55.786369
# Unit test for function match
def test_match():
    assert match(command=Command(script='aws', output='usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument command: Invalid choice, valid choices are:\n\n      configure  |  help  |  help-cancel  |  help-command  |  help-list  |\n      help-topics  |  iam  |  rds  |  redshift  |  route53  |\n      sns  |  sqs  |\n\n'))

# Generated at 2022-06-14 09:23:05.514883
# Unit test for function get_new_command

# Generated at 2022-06-14 09:23:18.634016
# Unit test for function match
def test_match():
    command1 = Command('aws cloudformation create-stack --template-body file://my_template.json --stack-name my_stack',
                       'usage: aws [options] <command> <subcommand> [<subcommand> ...]\n'
                       '       To see help text, you can run:\n'
                       '       \n'
                       '       aws help\n'
                       '       aws <command> help\n'
                       '       aws <command> <subcommand> help\n'
                       '       \n'
                       'aws: error: argument command: Invalid choice: '
                       "'create-stack', maybe you meant:\n"
                       '    * cloud-formation\n'
                       '    * cloudformation\n',
                       1)
    assert match(command1)


# Generated at 2022-06-14 09:23:28.464571
# Unit test for function match

# Generated at 2022-06-14 09:23:30.365984
# Unit test for function match
def test_match():
    command = Command('aws ec2 create-snapshot')
    assert match(command)



# Generated at 2022-06-14 09:23:32.586299
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("aws ec2 describe-instances --region us-east-1") == ['aws ec2 describe-regions --region us-east-1']

# Generated at 2022-06-14 09:23:39.629558
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 start-instances i-123456', 
    r'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument subcommand: Invalid choice, maybe you meant:\n  ssh\n  scp\n  s3\n  ec2'))

# Generated at 2022-06-14 09:23:51.206670
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('aws ec2 describe-instances --ramdom') == ['aws ec2 describe-instances --region']
    assert get_new_command('aws ec2 describe-instances --ramdom --boom') == ['aws ec2 describe-instances --region --boom']
    assert get_new_command('aws ec2 describe-instances --ramdom --boom --bam') == ['aws ec2 describe-instances --region --boom --bam']
    assert get_new_command('aws ec2 describe-instances --ramdom --boom --bam --bap') == ['aws ec2 describe-instances --region --boom --bam --bap']


# Generated at 2022-06-14 09:23:57.455270
# Unit test for function match
def test_match():
    assert match(Command(script="aws help", output="usage: aws [options] [parameters]\n\nA help maybe you meant: foo."))
    assert not match(Command(script="aws help", output="usage: aws [options] [parameters]\n\nA help maybe you meant: foo."))



# Generated at 2022-06-14 09:24:01.770123
# Unit test for function match
def test_match():
    pass


# Generated at 2022-06-14 09:24:08.780661
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws foo bar', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] ...', 'Invalid choice: \'foo\', maybe you meant:\n  * foo\n  * moo')) == [Command('aws foo bar', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] ...', 'Invalid choice: \'foo\', maybe you meant:\n  * foo\n  * moo')]

# Generated at 2022-06-14 09:24:20.264176
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('aws help')
    command.output = 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument command: Invalid choice, maybe you meant: \n  configure\n* help\n\n'
    assert get_new_command(command) == ['aws help']

# Generated at 2022-06-14 09:24:29.754771
# Unit test for function get_new_command
def test_get_new_command():
    command = type('Command', (object,), {
        'script':'aws s3 mv folder/subfolder s3://bucket/subfolder-mv',
        'output':'''Invalid choice: 'mv', maybe you meant:
        * cp
        * mb
        * rb
        * rm
        * sync
        '''})

# Generated at 2022-06-14 09:24:41.813491
# Unit test for function get_new_command
def test_get_new_command():
	# Test with 1 option
    new_command = get_new_command(Command(script='aws ec2 start-instances --foobar',
					output="usage: aws [options] <command> <subcommand> [parameters]\naws: error: argument --foobar: Invalid choice: '--foobar', maybe you meant: \n* --filter\n* --filters\n* --force\n* --force-stop"))
    assert len(new_command) == 3
    assert new_command[0] == 'aws ec2 start-instances --filter'
    assert new_command[1] == 'aws ec2 start-instances --filters'
    assert new_command[2] == 'aws ec2 start-instances --force'

	# Test with 2 options containing the same text at different indexes in the output


# Generated at 2022-06-14 09:24:47.969568
# Unit test for function match
def test_match():
    assert match(Command("aws ec2 start-instances --instance-ids i-1234567 --region us-east-1", "Invalid choice: '--instance-ids', maybe you meant:\n  --instance-id\n  --instance-ids\n\nSee 'aws help' for descriptions of global parameters.\n"))



# Generated at 2022-06-14 09:24:57.782978
# Unit test for function match
def test_match():
    assert match(Command('aws s3 ls foobarbaz', 'Invalid choice: \'foobarbaz\', maybe you meant:\n  * ls\n  * mb\n  * rb\n  * sync\n\nSee \'aws help\' for descriptions of global parameters.\n'))

# Generated at 2022-06-14 09:25:06.000299
# Unit test for function get_new_command
def test_get_new_command():
    new_command = get_new_command(Command("aws s3 ls s3://bucket_name",
                                          "usage: aws [options] <command> <subcommand> [<subcommand> ...]\n"
                                          "[<subcommand> ...] is not a valid choice for this command.\n"
                                          "Maybe you meant:\n"
                                          "    mb\n"
                                          "    mv\n"
                                          "    rb\n"
                                          "    rm\n"
                                          "    website"))

# Generated at 2022-06-14 09:25:11.918951
# Unit test for function get_new_command
def test_get_new_command():
    import os
    import glob

    f = glob.glob('tests/fixtures/aws/*')
    for filename in f:
        script = 'aws' + os.path.splitext(filename)[0].split('aws')[1]
        output = open(filename).read()

        c = Command(script, output)
        result = get_new_command(c)

        assert result != None
        assert len(result) == 4


# Generated at 2022-06-14 09:25:23.000156
# Unit test for function get_new_command
def test_get_new_command():
    script = "aws s3api delet-bucket --bucket my-bucket"

# Generated at 2022-06-14 09:25:28.848047
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 describe-instances'))
    assert not match(Command('ls'))


# Generated at 2022-06-14 09:25:33.686834
# Unit test for function match
def test_match():
    assert match(Command('aws', output='usage: error'))
    assert match(Command('aws', output='usage: bad'))
    assert not match(Command('aws', output='usage: good'))
    assert match(Command('aws', output='usage: Invalid choice: \'bad\', maybe you meant:\n* good'))


# Generated at 2022-06-14 09:25:46.785313
# Unit test for function match

# Generated at 2022-06-14 09:25:48.261608
# Unit test for function match
def test_match():
    assert match(Command('aws s3 ls', ''))


# Generated at 2022-06-14 09:25:55.291687
# Unit test for function match
def test_match():

    # test if the command matches the output
    assert match(Command('aws', 'usage: aws [options] <command> <subcommand> [parameters]', 'Invalid choice: ', 'maybe you meant:', ''))

    # test if the command does not match the output
    assert not match(Command('aws', 'Invalid choice: ', 'maybe you meant:', ''))


# Generated at 2022-06-14 09:26:05.338885
# Unit test for function match
def test_match():
    err = "aws: error: argument subcommand: Invalid choice: 'ec2', maybe you meant: \n\n* ecr"
    output = Command("aws help", err)
    assert match(output)

    output = Command("aws help", "aws: error: argument subcommand: Invalid choice: 'ec2', maybe you meant: ")
    assert not match(output)

    output = Command("aws help", "aws: error: argument subcommand: Invalid choice: 'ec2'")
    assert not match(output)

    output = Command("aws help", "aws: error: argument subcommand: Invalid choice: 'ec2', maybe you meant: \n\n* ecrdd")
    assert not match(output)



# Generated at 2022-06-14 09:26:10.123281
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(parse('aws sts get-caller-identity')) == \
           [u'aws sts get-caller-identify', u'aws sts get-caller-identity']

# Generated at 2022-06-14 09:26:11.882431
# Unit test for function match
def test_match():
    assert match(Command('aws --help'))


# Generated at 2022-06-14 09:26:21.279021
# Unit test for function match
def test_match():
    assert(match(Command('aws --help',
                         'usage: aws [options] [parameters]\nInvalid choice: "--help", maybe you meant:\n  * --version\n  * --endpoint-url',
                         '/dev/null')) == True)

    assert(match(Command('aws --help',
                         'usage: aws [options] [parameters]\nInvalid choice: "--help", maybe you meant:\n  * --version\n  * --endpoint-url\n',
                         '/dev/null')) == True)


# Generated at 2022-06-14 09:26:27.849514
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 help',
                         'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument subcommand: Invalid choice, maybe you meant:\n  service\n  configure\n  help\n\n'))


# Generated at 2022-06-14 09:26:39.827585
# Unit test for function match
def test_match():
    assert match(Command('aws --help'))

# Generated at 2022-06-14 09:26:47.945427
# Unit test for function get_new_command
def test_get_new_command():
    output = ("usage: aws [options] [params] [param_value]\n"
              "aws: error: argument [command]: Invalid choice: ''\n"
              "maybe you meant: [command]\n"
              " * cloudfront\n"
              " * cloudformation\n")
    command = Command('aws', output)
    assert get_new_command(command) == [
        "aws cloudfront",
        "aws cloudformation"]


enabled_by_default = True

# Generated at 2022-06-14 09:26:52.092653
# Unit test for function get_new_command
def test_get_new_command():
    test1 = Command("aws cloudformation deploy", "usage: aws [options]\naws: error: argument CLOUDFORMATION: Invalid choice, maybe you meant:", "aws cloudformation deploy")
    assert get_new_command(test1) == ["aws cloudformation deploy"]

# Generated at 2022-06-14 09:26:54.352655
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("aws 'codepipeline','get-pipeline'")) == \
        ["aws codepipeline get-pipeline"]

# Generated at 2022-06-14 09:27:02.375786
# Unit test for function match
def test_match():
    # Failure case
    assert not match(Command('aws', ''))

    # Success cases
    assert match(Command('aws', 'usage: aws [options] <command> <subcommand> [parameters]',
                         'Invalid choice: \'abc\', maybe you meant:',
                         '* aaa',
                         '* bbb',
                         '* ccc'))
    assert match(Command('aws', 'usage: aws [options] <command> <subcommand> [parameters]',
                         'Invalid choice: \'abc\', maybe you meant:',
                         '* aaa'))
    assert match(Command('aws', 'usage: aws [options] <command> <subcommand> [parameters]',
                         'Invalid choice: \'abc\', maybe you meant:',
                         '* aaa',
                         '* bbb'))


# Generated at 2022-06-14 09:27:03.269305
# Unit test for function match
def test_match():
    assert match(Command('aws s3 lis', ''))



# Generated at 2022-06-14 09:27:12.296923
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Mock(
        script='aws s3 ls',
        output="aws: error: argument subcommand: Invalid choice: 'ls'\n"
        "aws: error: argument subcommand: maybe you meant: \n"
        "ls\n"
        "name (string)  -- The name of the new bucket.\n"
        "* s3api\n"
        "s3control\n"
        "s3\n"
        "s3api\n"
        "s3control\n"
        "s3",
        stderr='',
        stdout='')) == ['aws s3api ls', 'aws s3control ls']

# Generated at 2022-06-14 09:27:24.928141
# Unit test for function get_new_command

# Generated at 2022-06-14 09:27:35.490910
# Unit test for function get_new_command
def test_get_new_command():
    # Invalid choice: 'publish', maybe you meant:
    #     * push
    #     * pull
    output = """usage: aws [options] [ ...] [parameters]
To see help text, you can run:

  aws help
  aws  help
  aws   help

Unknown options: aws, [options], [, ...], [parameters]
Invalid choice: 'publish', maybe you meant:
    * push
    * pull
"""
    command = type('Command', (), {'script': 'aws', 'output': output})
    new_commands = get_new_command(command)
    assert new_commands == ['aws  push', 'aws  pull']

# Generated at 2022-06-14 09:27:42.625545
# Unit test for function get_new_command
def test_get_new_command():
    output = """usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help
aws: error: argument command: Invalid choice, valid choices are:

cloudformation   | configure       | configure help

Unknown options: b, l
(Expected: i, f, g, x, z, y)
"""
    new_command = get_new_command("aws b l", output)
    assert "aws cloudformation" in new_command
    assert "aws configure" in new_command

# Generated at 2022-06-14 09:27:52.479712
# Unit test for function match
def test_match():
    assert match(Command('', '', 'usage: aws [options] <command> <subcommand> [parameters]\nTo see help text, you can run:\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument command: Invalid choice, maybe you meant:', ''))


# Generated at 2022-06-14 09:27:54.240491
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 help'))


# Generated at 2022-06-14 09:27:57.463695
# Unit test for function match
def test_match():
    assert match(Command('aws s3um cp s3://foo/bar/baz /tmp/', ''))
    assert not match(Command('aws s3 cp s3://foo/bar/baz /tmp/', ''))


# Generated at 2022-06-14 09:28:06.220664
# Unit test for function match
def test_match():
    output = "aws: error: argument subcommand: Invalid choice, valid choices are:\ns3api     | s3sync\n"
    assert match(Command(script='aws', output=output))
    output = "aws: error: argument subcommand: Invalid choice: 's3', maybe you meant:\n* s3api\n* s3sync\n"
    assert match(Command(script='aws', output=output))
    assert not match(Command(script='aws', output='aws subcommand'))



# Generated at 2022-06-14 09:28:11.209565
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 stop-instances --instance-ids i-12345678')).is_success
    assert match(Command('aws ec2 stop-instances --instance-ids i-12345678')).is_fail
    assert match(Command('aws ec2 stop-instances --instance-ids i-12345678')).is_fail


# Generated at 2022-06-14 09:28:23.181478
# Unit test for function match
def test_match():
    assert match(Command('aws', 'Invalid choice: "ec2", maybe you meant: ec2\n* ec2\n* ec2-instance-connect\n* ec2-ssh'))
    assert not match(Command('aws', 'Invalid choice: "ec2", maybe you meant: ec2'))

# Generated at 2022-06-14 09:28:32.842030
# Unit test for function match

# Generated at 2022-06-14 09:28:47.521680
# Unit test for function match
def test_match():
    output = '''usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help
aws: error: argument subcommand: Invalid choice, maybe you meant:
  --debug                              turn on debug logging
  --endpoint-url                       override command's default URL with the given URL
  --no-verify-ssl                      override command's default SSL verification behavior
  --profile                            use a specific profile from your credential file
  --region                             override command's default region with the given region
  --version                            show the version of aws-cli you are using
See 'aws help' for descriptions of global parameters.
'''

# Generated at 2022-06-14 09:28:59.074642
# Unit test for function match