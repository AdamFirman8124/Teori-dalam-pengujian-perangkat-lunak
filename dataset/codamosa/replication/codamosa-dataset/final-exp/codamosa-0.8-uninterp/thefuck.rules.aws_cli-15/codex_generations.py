

# Generated at 2022-06-14 09:19:01.388646
# Unit test for function match

# Generated at 2022-06-14 09:19:05.039890
# Unit test for function match
def test_match():
    command = Command('aws help')
    assert match(command)

    command = Command('aws hlp')
    assert match(command)
    assert 'usage:' in command.output
    assert "maybe you meant:" in command.output


# Generated at 2022-06-14 09:19:10.095038
# Unit test for function get_new_command
def test_get_new_command():
    run = lambda x: Match(script=x, output='')
    assert get_new_command(run('aws s3 create')) == ['aws s3api create-bucket']
    assert get_new_command(run('aws s3 create-buket')) == ['aws s3api create-bucket']

# Generated at 2022-06-14 09:19:22.241894
# Unit test for function get_new_command
def test_get_new_command():
    input_1 = Command('aws ec2 describe-regions --region us-east-1', 'aws: error: argument --region: Invalid choice',
    'usage: aws [options] &lt;command&gt; &lt;subcommand&gt; [parameters]')
    assert get_new_command(input_1) == ['aws ec2 describe-regions --region us-east-2', 'aws ec2 describe-regions --region us-east-3']

    input_2 = Command('aws ec2 describe-regions --region uus-east-1', 'aws: error: argument --region: Invalid choice',
    'usage: aws [options] &lt;command&gt; &lt;subcommand&gt; [parameters]')

# Generated at 2022-06-14 09:19:28.203880
# Unit test for function match
def test_match():
    match_command = Command('aws ec2 descibe-instances', '', 'usage: aws [options] <command> <subcommand> [parameters]')
    assert match(match_command)
    not_match_command = Command('aws ec2 describe-instances', '', 'Could not connect to the endpoint URL')
    assert not match(not_match_command)


# Generated at 2022-06-14 09:19:37.070161
# Unit test for function match
def test_match():
    import mock

    output = 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument subcommand: Invalid choice, maybe you meant:\n    configure\n    help\n\n'
    result = match(mock.Mock(output=output))

    assert bool(result) == True


# Generated at 2022-06-14 09:19:49.055806
# Unit test for function get_new_command
def test_get_new_command():
    script = 'aws ec2 --help'

# Generated at 2022-06-14 09:19:57.009596
# Unit test for function match
def test_match():
    assert match(Command('aws pu', "usage: aws [options] [ ...] \
                                    [parameters] [ ...] To see help text, you can run: aws help \
                                    Invalid choice: 'pu', maybe you meant: \
                                    * put\n\n", ''))
    assert not match(Command('aws put 1 2', '', ''))
    assert not match(Command('test.sh', '', ''))


# Generated at 2022-06-14 09:20:05.327008
# Unit test for function get_new_command
def test_get_new_command():
    cmd = "aws --help"
    output = """
usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help

aws: error: argument operation: Invalid choice, maybe you meant:
...
    * configure"""
    assert get_new_command(Command(cmd, output)) == ["aws configure"]


enabled_by_default = True

# Generated at 2022-06-14 09:20:18.130184
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command


# Generated at 2022-06-14 09:20:21.547806
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws he', 'Unknown options: he\n')) == ['aws help']

# Generated at 2022-06-14 09:20:33.783325
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("aws ssss ec2 describe-instances --region us-east-1", "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument subcommand: Invalid choice, maybe you meant:\n  ec2             Work with Amazon Elastic Compute Cloud (EC2).\n  events          Work with Amazon CloudWatch Events.\n  cloudwatch      Work with Amazon CloudWatch.\n  organizations   Work with AWS Organizations.\n  ssm             Work with Amazon EC2 Simple Systems Manager.")

# Generated at 2022-06-14 09:20:44.105187
# Unit test for function get_new_command
def test_get_new_command():
    script = "aws ec2 restore-instance-defau"
    output = "usage: aws [options]   [parameters]\n\na2 restore-instance-defau\n\nInvalid choice: 'a2 restore-instance-defau', maybe you meant:\n    * authorize-security-group-ingress\n    * create-security-group\n    * describe-security-groups\n    * describe-key-pairs\n    * describe-instances\n    * create-image\n    * terminate-instances\n    * run-instances"

# Generated at 2022-06-14 09:20:55.291929
# Unit test for function get_new_command
def test_get_new_command():
    script = 'aws cloudformation list-stack-resources --stack-name foo'
    output = "usage: aws [options] <command> <subcommand> [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument operation: Invalid choice: 'cloudformation list-stack-resources', maybe you meant:\n* cloudformation-list-stack-resources"
    cmd = Command(script, output)
    assert get_new_command(cmd) == [u'aws cloudformation-list-stack-resources --stack-name foo']

# Generated at 2022-06-14 09:20:59.577736
# Unit test for function get_new_command

# Generated at 2022-06-14 09:21:12.262504
# Unit test for function get_new_command
def test_get_new_command():
    """Test function get_new_command"""
    input_command = "aws s3 mv foo s3://bucket/bar/baz A client error (403) occurred when calling the HeadObject operation: Forbidden An error occurred (403) when calling the HeadObject operation: Forbidden"
    input_output = "An error occurred (403) when calling the HeadObject operation: Forbidden"
    input_mistake = "mv"
    input_options = ["mb", "mirror", "move"]
    output = [replace_argument(input_command, input_mistake, o) for o in input_options]

    get_new_command(input_command, input_output, input_mistake, input_options) == output

# Generated at 2022-06-14 09:21:18.536366
# Unit test for function get_new_command
def test_get_new_command():
    command = type('', (), {'output': "usage: aws [options] [parameters]\n\naws: error: argument command: Invalid choice: 'emr', maybe you meant:\n * ems\n * emr\n * ems-console\n * emr-console", 'script': 'aws emr'})()
    new_command = get_new_command(command)
    assert new_command == ['aws ems', 'aws emr', 'aws ems-console', 'aws emr-console']

# Generated at 2022-06-14 09:21:30.992333
# Unit test for function match

# Generated at 2022-06-14 09:21:33.857839
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 run-instance --instance-type=m1.small'))
    assert not match(Command('git branch'))

# Generated at 2022-06-14 09:21:46.143057
# Unit test for function get_new_command
def test_get_new_command():
    import sys
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--version')
    parser.add_argument('--endpoint-url')
    parser.add_argument('--no-verify-ssl')
    parser.add_argument('--region')
    parser.add_argument('--output')
    parser.add_argument('--profile')
    parser.add_argument('--ca-bundle')
    parser.add_argument('--debug')
    cmd = ['aws', '--region=', '--endpoint-url=', '--no-verify-ssl', '--strict-ssl', '--verify-ssl']
    cmd.extend(parser.parse_args(sys.argv[1:]).__dict__.keys())


# Generated at 2022-06-14 09:21:54.810295
# Unit test for function match
def test_match():
    assert match(Command('aws ec2-describe-instances --region us-west-2',
                         'Invalid choice: \'--region\', maybe you meant:\n  --color\n  --json\n  --no-color\n  --outline\n  --profile\n  --query\n  --region\n  --version',
                         '', 1, None))


# Generated at 2022-06-14 09:22:03.703551
# Unit test for function get_new_command
def test_get_new_command():
    script = "aws ec2 help"
    output = "usage: aws [options] <command> <subcommand> [parameters]" \
             "\naws: error: argument <command>: Invalid choice: '<subcommand>', maybe you meant:" \
             "\n  * <subcommand>" \
             "\n  * <subcommand>" \
             "\n  * <subcommand>" \
             "\n  * <subcommand>"
    command = Command(script, output)
    assert get_new_command(command) == [
        'aws ec2 <subcommand>',
        'aws ec2 <subcommand>',
        'aws ec2 <subcommand>'
    ]

# Generated at 2022-06-14 09:22:11.280845
# Unit test for function match
def test_match():
    assert for_app('aws')(Command(script='aws stuff --query something',
                                 output='usage: aws [options] <command> <subcommand> [parameters]\n'+
                                        'aws: error: argument --query: Invalid choice: \' something\'\n'+
                                        '       (maybe you meant: --query-string)', stderr='error',))


# Generated at 2022-06-14 09:22:13.157879
# Unit test for function match
def test_match():
    assert not match(Command())
    assert match(Command('aws s3', ''))


# Generated at 2022-06-14 09:22:21.419750
# Unit test for function match
def test_match():
    from thefuck.types import Command
    assert match(Command('aws s3 mb s3://bucket_name/',
            'usage: aws [options] <command> <subcommand> [parameters]\naws: error: argument subcommand: Invalid choice, valid choices are:\n* make_bucket\n* mb',
            ''))


# Generated at 2022-06-14 09:22:30.677860
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(
        Command("aws ec2 describe-regions us-east-1",
                "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\n"
                "aws: error: argument subcommand: Invalid choice, maybe you meant:\n"
                "   --version                  Show the version number and exit\n"
                "   describe-regions\n"
                "   ec2\n")) == ["aws ec2 describe-regions --version",
                                 "aws ec2 describe-regions describe-regions",
                                 "aws ec2 describe-regions ec2"]



# Generated at 2022-06-14 09:22:41.953608
# Unit test for function match
def test_match():
    assert match(Command('aws --help', 'usage: aws [options] <command> <subcommand> '
        '[<subcommand> ...] [parameters]\n'
        'To see help text, you can run:\n'
        '\n'
        '  aws help\n'
        '  aws <command> help\n'
        '  aws <command> <subcommand> help\n'
        'aws: error: argument command: Invalid choice, maybe you meant: '
        'configure\n', ''))

# Generated at 2022-06-14 09:22:45.119385
# Unit test for function match
def test_match():
    assert match(Command(script='aws s3 ls',
        output='Invalid choice: \'s3\', maybe you meant:\n        s3api\n        s3api\n'))

# Generated at 2022-06-14 09:22:52.922627
# Unit test for function get_new_command
def test_get_new_command():
    assert (
        get_new_command(Command('aws ec2 vpc-describe',
                                '\n'.join([
                                    'usage: aws [options] <command> <subcommand> [parameters]',
                                    'aws: error: argument command: Invalid choice: \'ec2\'',
                                    'maybe you meant:',
                                    '    * ec2-describe-vpcs',
                                    '    * ec2-describe-volumes']))) == [
                                        'aws ec2-describe-vpcs',
                                        'aws ec2-describe-volumes'])

# Generated at 2022-06-14 09:22:55.950689
# Unit test for function match
def test_match():
    assert match(check_output("aws ec2 describe-instances", stderr=True))
    assert not match(check_output("aws ec2 describe-instances", stderr=False))

# Generated at 2022-06-14 09:23:01.675048
# Unit test for function match
def test_match():
    pass

# Generated at 2022-06-14 09:23:03.795996
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 describe-regions some_garbage'))
    assert not match(Command('ls'))


# Generated at 2022-06-14 09:23:09.813501
# Unit test for function get_new_command
def test_get_new_command():
    print("Unit test for get_new_command(command)")
    print("Command: aws s3 ls ")

    command = "aws s3 ls "
    script = "aws s3 ls"
    output = "Invalid choice: 's3', maybe you meant:\n  * s3api\n  * ssm\n  * sts"
    my_command = Command(script, output)
    output_command = get_new_command(my_command)[0]

    print("Output:")
    print(output_command)
    print("\n")

if __name__ == "__main__":
    test_get_new_command()

# Generated at 2022-06-14 09:23:14.070250
# Unit test for function get_new_command
def test_get_new_command():
    command = type("Command", (object,), {'script': "foo", 'output': "Invalid choice: 'foobar', maybe you meant:\n  foo1\n  foo2\n"})
    assert(get_new_command(command) == ["foo1", "foo2"])

# Generated at 2022-06-14 09:23:20.897488
# Unit test for function match
def test_match():
    assert match(Command('aws help',
        'usage: aws [options] <command> <subcommand> [parameters]\n'
        'aws: error: argument command: Invalid choice: \'hell\' (choose '
        'from \'acm\', \'apigateway\', \'application-autoscaling\', '
        '\'autoscaling\', \'batch\', \'cloudformation\''
        ', maybe you meant: api))'))


# Generated at 2022-06-14 09:23:31.904382
# Unit test for function match
def test_match():
    command = Command('aws --help', '') 
    assert not match(command)
    command = Command('aws help', 'usage: aws [options] [parameters]\naws: error: argument operation: Invalid choice, maybe you meant:\n  help\n  * --help\n  * info')
    assert match(command)
    command = Command('aws help', 'usage: aws [options] [parameters]\naws: error: argument operation: Invalid choice, maybe you meant:\n  help\n  * --help\n  * info\n  * init')
    assert match(command)

# Generated at 2022-06-14 09:23:41.877423
# Unit test for function get_new_command

# Generated at 2022-06-14 09:23:49.951284
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws s3 mb --region eu-central-1 s3://test-bucket-name-v2')) == ['aws s3 mb --region eu-central-1 s3://test-bucket-name-v2']
    assert get_new_command(Command('aws eks update-kubeconfig --name cluster-name')) == ['aws eks update-kubeconfig --name cluster-name']

# Generated at 2022-06-14 09:24:01.761112
# Unit test for function get_new_command
def test_get_new_command():
    output = '''aws: error: argument subcommand: Invalid choice, maybe you meant:
  * s3
  * route53
  * r53
  * elb
  * rds
  * cloudwatch
  * s3api
  * cloudtrail
See 'aws help' for descriptions of global parameters.'''
    script = "aws ec2 --help"
    command = Command(script, output)
    assert get_new_command(command) == ['aws s3 --help',
                                        'aws route53 --help',
                                        'aws r53 --help',
                                        'aws elb --help',
                                        'aws rds --help',
                                        'aws cloudwatch --help',
                                        'aws s3api --help',
                                        'aws cloudtrail --help']

# Generated at 2022-06-14 09:24:06.802308
# Unit test for function match
def test_match():
    print("Testing match")
    result = match(Command('aws configure --profile=default'))
    assert result == False
    result = match(Command('aws help'))
    assert result == False
    result = match(Command('aws configure --set --profile=default'))
    assert result == True


# Generated at 2022-06-14 09:24:21.307365
# Unit test for function match
def test_match():
    correct_cmd = u'aws ec2 --version'
    wrong_cmd = u'aws ec2 --ver XXXXX'
    assert match(Command(script=correct_cmd)) != match(Command(script=wrong_cmd))

# unit test for function get_new_command

# Generated at 2022-06-14 09:24:27.759775
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

    command = Command('aws s3 ls',
                      'usage: aws [options] <command> '
                      '<subcommand> [<subcommand> ...] [parameters]\n'
                      'aws: error: argument operation: Invalid value '
                      '\'ls\': Invalid choice:'
                      ' \'ls\', maybe you meant: * ls * list * mls',
                      '', 1)

    assert get_new_command(command) == ['aws s3 ls', 'aws s3 list', 'aws s3 mls']

# Generated at 2022-06-14 09:24:40.568231
# Unit test for function get_new_command
def test_get_new_command():
    script = "aws s3api ls xxaa"

# Generated at 2022-06-14 09:24:45.963738
# Unit test for function match

# Generated at 2022-06-14 09:24:47.907553
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("ls -l") == ['ls -l']

# Generated at 2022-06-14 09:24:57.760622
# Unit test for function get_new_command

# Generated at 2022-06-14 09:25:11.427744
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("aws help", "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\n\naws: error: argument command: Invalid choice, maybe you meant: \n\tautoscaling\n\tcloudwatch\n\tconfig\n\tecs\n\telasticache\n\telasticbeanstalk\n\nSee 'aws help' for descriptions of global parameters. \n")
    assert get_new_command(command) == ['aws autoscaling help', 'aws cloudwatch help', 'aws config help', 'aws ecs help', 'aws elasticache help', 'aws elasticbeanstalk help']



# Generated at 2022-06-14 09:25:14.861031
# Unit test for function get_new_command
def test_get_new_command():
    command = type('obj', (object,), {'output': "Invalid choice: 'k'.\nMaybe you meant:\n  key\n  kill", 'script': 'aws cmd key'})
    assert get_new_command(command) == ['aws cmd key', 'aws cmd kill']

# Generated at 2022-06-14 09:25:26.859623
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.shells import Bash
    correct_command = Bash().and_('aws help')
    wrong_command = correct_command.copy()

# Generated at 2022-06-14 09:25:30.557666
# Unit test for function match
def test_match():
    assert not match(Command('aws ec2 describe-regions', ''))
    assert match(Command('aws ec2 desribe-regions', ''))
    assert match(Command('aws ec2 describe-regions', ''))

# Generated at 2022-06-14 09:26:03.647583
# Unit test for function match

# Generated at 2022-06-14 09:26:09.786355
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.aws_typo import get_new_command
    assert get_new_command(Command('aws configu', '', 'usage: aws [options] <command> <subcommand> [parameters]\n\naws: error: argument command: Invalid choice, maybe you meant:\n    configure  \n    configure  \n    configure  \n\n')) == ['aws configure', 'aws configure', 'aws configure']

# Generated at 2022-06-14 09:26:20.542230
# Unit test for function match
def test_match():
    assert match(Command('aws s3 mb s3://bucket',
                         output='usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument subcommand: Invalid choice, maybe you meant:\n\n  mb                      make-bucket\n  rb                      rm-bucket\n  ls                      list-objects\n  presign                 presign-url\n'))
    assert match(Command('aws s3 rb s3://bucket',
                         output='An error occurred (BucketNotEmpty) when calling the DeleteBucket operation: The bucket you tried to delete is not empty')) is False


# Generated at 2022-06-14 09:26:31.666696
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws s3 ls', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\naws: error: argument <command>: Invalid choice: \'s3\', maybe you meant:\n\t\tsts\n\t\tssm')) == [
        'aws sts ls', 'aws ssm ls']
    assert get_new_command(Command('aws kinesis ls', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\naws: error: argument <command>: Invalid choice: \'kinesis\', maybe you meant:\n\t\tsts\n\t\tssm')) == [
        'aws sts ls', 'aws ssm ls']

# Generated at 2022-06-14 09:26:35.056761
# Unit test for function match
def test_match():
    assert match(Command('aws (ddd)', 'usage: aws [options] \n*\n*\n', stderr='Invalid choice: \'(ddd)\', maybe you meant:\n*\n*\n'))


# Generated at 2022-06-14 09:26:46.365056
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 describe-instances',
                         "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument subcommand: Invalid choice, maybe you meant:\n    delete-tags    delete-tagsets\n    describe-tags  describe-tagsets\nSee 'aws help' for descriptions of global parameters.\n"))
    assert not match(Command('ls'))
    assert not match(Command('ls', ''))


# Generated at 2022-06-14 09:26:50.872105
# Unit test for function match
def test_match():
    command = Command('aws ec2 describe-vpcs')
    assert match(command)
    command = Command('aws ec2 describe-volumes --volume-ids vol-049df61146c4d7901')
    assert match(command) is False


# Generated at 2022-06-14 09:26:52.627796
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 describe-instances --output table'))
    

# Generated at 2022-06-14 09:26:56.575886
# Unit test for function get_new_command
def test_get_new_command():
    command = "aws cloudformation update-stack --template-body ./config/base.json --parameters ./config/production.json --stack-name production --region us-east-1"
    assert get_new_command(command) == ["aws cloudformation update-stack --template-body ./config/base.json --parameters ./config/production.json --stack-name production --region us-east-1"]

# Generated at 2022-06-14 09:27:04.071424
# Unit test for function get_new_command
def test_get_new_command():

    # Test case 1
    command = Command("aws dynamodb describe-table --table-name testTable1 --region eu-west-1")

# Generated at 2022-06-14 09:27:55.454821
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('aws ec2 run-instances --image-id ami-5189a661 --count 1 --instance-type t1.micro --key-name MyKeyPair --security-groups MySecurityGroup')
    assert ['aws ec2 run-instances --image-id ami-5189a661 --count 1 --instance-type t1.micro --key-name MyKeyPair --security-groups MySecurityGroup',
            'aws ec2 run-instances --image-id ami-5189a661 --count 1 --instance-type t1.micro --key-name MyKeyPair --security-groups mysecuritygroup'] == get_new_command(command)

# Generated at 2022-06-14 09:28:08.372183
# Unit test for function get_new_command

# Generated at 2022-06-14 09:28:13.737641
# Unit test for function match
def test_match():
	script1 = 'aws usage'
	script2 = 'aws ec2'
	script3 = 'aws ec2 run-instances --image-id ami-78a54011 --count 1 --instance-type t1.micro'
	assert (match(script1) and match(script2) and match(script3)) == False


# Generated at 2022-06-14 09:28:24.189601
# Unit test for function match

# Generated at 2022-06-14 09:28:29.297343
# Unit test for function get_new_command
def test_get_new_command():
    script_example = 'aws ec2 describe-instances'

# Generated at 2022-06-14 09:28:46.034253
# Unit test for function match

# Generated at 2022-06-14 09:28:54.067058
# Unit test for function get_new_command
def test_get_new_command():
    command = type('Command', (object,), {
        'output': 'usage: aws [options] &lt;command&gt; &lt;subcommand&gt; [parameters]\n\naws: error: argument command: Invalid choice: "mycommand", maybe you meant:\n    help    List all commands\n    list    List all commands\n',
        'script': "aws mycommand"
        })
    assert get_new_command(command) == ['aws help', 'aws list']