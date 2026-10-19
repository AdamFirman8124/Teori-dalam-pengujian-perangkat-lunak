

# Generated at 2022-06-14 09:19:00.393668
# Unit test for function match

# Generated at 2022-06-14 09:19:04.605309
# Unit test for function match
def test_match():
    assert match(Command("aws help", "usage: aws [....] Invalid choice: 'help', maybe you meant: 's3'"))
    assert not match(Command("aws", "usage: aws [....]"))


# Generated at 2022-06-14 09:19:15.709249
# Unit test for function match
def test_match():
    assert match(Command('aws --help', ''))
    assert match(Command('aws s3', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]'))
    assert match(Command('aws invalid', "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\n\n"
                                        + "error: argument command: Invalid choice, maybe you meant:\n"
                                        + "        support\n"
                                        + "   *\ts3\n"
                                        + "        sqs\n"
                                        + "        sts\n"))
    assert not match(Command('aws s3', ''))


# Generated at 2022-06-14 09:19:25.005863
# Unit test for function get_new_command
def test_get_new_command():
    output = """
                usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
                To see help text, you can run:

                aws help
                aws <command> help
                aws <command> <subcommand> help
                UnrecognizedClientException: The security token included in the request is invalid.
                A client error (UnrecognizedClientException) occurred when calling the DescribeInstances operation: The security token included in the request is invalid.
                    \tstatus code: 400, request id: d8be0c23-7cd7-11e9-8bed-5f5ee5a5a5ba
                Unknown options: --verify-ssl, --endpoint-url
                \tawscli.clidriver.main()
          """


# Generated at 2022-06-14 09:19:34.907151
# Unit test for function match

# Generated at 2022-06-14 09:19:42.016946
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws ec2 delete-security-gruoups --group-id sec-1 --dry-run', "Invalid choice: 'delete-security-gruoups', maybe you meant:  delete-security-group\nerror: argument --group-id: expected one argument\n")) == ['aws ec2 delete-security-group --group-id sec-1 --dry-run']



# Generated at 2022-06-14 09:19:45.766854
# Unit test for function match
def test_match():
    assert match(Command('aws s3 ls', 'Invalid choice: \'/s3\', maybe you meant:', ''))
    assert not match(Command('aws', 'Aws is not a command', ''))


# Generated at 2022-06-14 09:19:47.771031
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 describe-instances --region us-east-1'))



# Generated at 2022-06-14 09:19:50.650895
# Unit test for function match
def test_match():
    assert match(Command('aws', 25))
    assert not match(Command('aws', 34))
    assert not match(Command('foobar', 25))



# Generated at 2022-06-14 09:20:02.797799
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('aws ec2 describe-instances')

# Generated at 2022-06-14 09:20:10.789891
# Unit test for function get_new_command
def test_get_new_command():
    a = 'aws --help'
    b = 'aws ec2 describe-instances --help'
    c = 'aws ec2 describe-instances --help'

    assert(get_new_command(a) == [])
    assert(get_new_command(b) == [])
    assert(get_new_command(c) == [])

# Generated at 2022-06-14 09:20:21.513723
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.aws_command_not_found import get_new_command, INVALID_CHOICE, OPTIONS

# Generated at 2022-06-14 09:20:33.783358
# Unit test for function match
def test_match():
    assert match(Command(script="aws ec2 describe-instance --instance-ids i-12345678", output="usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]")) == False
    assert match(Command(script="aws ec2 describe-instance-ids i-12345678", output="usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]")) == False

# Generated at 2022-06-14 09:20:40.226416
# Unit test for function match
def test_match():
    command = Command('aws', 'usage: aws [--version] [--help] <command> <subcommand> [<subcommand> ...] [parameters]', 'aws: error: argument subcommand: Invalid choice: \'foo\', maybe you meant: \n  * foo-bar\n  * foo-baz\naws: error: the following arguments are required: subcommand', 'aws')
    assert match(command)


# Generated at 2022-06-14 09:20:49.779334
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script='aws ec2 describe-intstances --instance-ids 2234234234234')) ==\
           ['aws ec2 describe-instances --instance-ids 2234234234234']
    assert get_new_command(Command(script='aws ec2 describe-intstances --instance-ids 2234234234234',
                                   output='aws: error: argument ')) == []

# Generated at 2022-06-14 09:21:00.692447
# Unit test for function get_new_command

# Generated at 2022-06-14 09:21:09.269565
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws s3 cp s3://mybucket/myfile.txt .', 'aws: error: argument --recursive: Invalid choice: (-r --recursive), maybe you meant:\\n* --recursive')) == ['aws s3 cp s3://mybucket/myfile.txt . --recursive']

# Generated at 2022-06-14 09:21:14.339191
# Unit test for function get_new_command
def test_get_new_command():
    output = '''aws: error: argument subcommand: Invalid choice: 'a', maybe you meant:
    * subset
    * push
'''
    assert(get_new_command(Command('aws --subcommand', output=output)) == ['aws --subset', 'aws --push'])

# Generated at 2022-06-14 09:21:25.632447
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('aws', u"""usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help
aws: error: argument command: Invalid choice, valid choices are:

ops  
s3  
s3api 
s3-signer 
sns  
sqs  
sts  
maybe you meant:

s3api   
s3-signer

""")

    assert get_new_command(command) == [Command('aws', 's3api'), Command('aws', 's3-signer')]



# Generated at 2022-06-14 09:21:29.402561
# Unit test for function match
def test_match():
    import subprocess
    output = subprocess.check_output('aws help', shell=True).decode('utf-8')
    assert match(Command('aws help', output))



# Generated at 2022-06-14 09:21:34.311215
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 describe-instances foo bar'))
    assert not match(Command('aws ec2 describe-instances'))


# Generated at 2022-06-14 09:21:46.444885
# Unit test for function match
def test_match():
    assert match(Command('aws s3',
    'usage: aws [options] <command> <subcommand> [parameters]\n\
aws: error: argument <command>: Invalid choice, maybe you meant:\n\
\t   cloudformation   \tWork with AWS CloudFormation templates\n\
\t   cloudfront       \tConfigure Amazon CloudFront distributions\n\
\t   cloudsearch      \tManage Amazon CloudSearch domains\n\
\t   cloudsearchdomain\tSearch Amazon CloudSearch domains',
    ''))
    assert not match(Command('aws s3',
    'usage: aws [options] <command> <subcommand> [parameters]',
    ''))

# Generated at 2022-06-14 09:21:54.991712
# Unit test for function match
def test_match():
    assert match(Command('aws s3 ls', 'usage: aws [options] <command> <subcommand> [parameters]\naws: error: argument operation: Invalid choice, maybe you meant:\n        mv\n        cp\n        rb\n        rm\n        presign\n        ls\n        mb\n        sync\n        website\n        rsync\n        set-acl\n        facilitie'))
    assert not match(Command('ls', ''))

# Test function get_new_command

# Generated at 2022-06-14 09:22:05.093370
# Unit test for function get_new_command
def test_get_new_command():
    test_get_new_command.command = type("Command", (object,), {})()
    test_get_new_command.command.script = "aws s3api list-buckets"

# Generated at 2022-06-14 09:22:17.388664
# Unit test for function get_new_command

# Generated at 2022-06-14 09:22:25.339792
# Unit test for function get_new_command
def test_get_new_command():
    script = 'aws s3 ls s3://my-bucket/dir --region us-east-1'

# Generated at 2022-06-14 09:22:38.802285
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.aws_maybe_you_meant import get_new_command
    assert get_new_command(
        Command("aws ec2 desribe-instances", "", "usage: aws [options] <command> <subcommand> [parameters]\naws: error: argument subcommand: Invalid choice, maybe you meant:\n\n\t* describe-instances\n\t* describe-images\n\t* describe-snapshots\n\nSee 'aws help' for descriptions of global parameters.\n", 0)) == [
            "aws ec2 describe-instances"]

# Generated at 2022-06-14 09:22:45.584205
# Unit test for function match
def test_match():
	# test valid input
	cmd = 'aws --profile=profile s3 ls s3://bucket/folder --endpoint-url=http://localhost:2380 --recursive'

# Generated at 2022-06-14 09:22:55.014223
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    command = Command('aws s3 ls', 'usage: aws [options] <command> <subcommand> [parameters]\naws: error: argument subcommand: Invalid choice: \'ls\', maybe you meant:\n    * rb\n    * mb\n    * ls\n    * cp\n    * rm\n    * rsync\n    * sync\n    * website\n    * presign\n    * accelerate\n    * controls\n    * events\n    * inventory\n    * metrics\n    * policy\n    * replica\n    * report\n    * requestpayment\n    * restore\n    * tagging\n    * usage\n    * wait\n    * multipart\n    * presignedurl')

# Generated at 2022-06-14 09:23:05.696508
# Unit test for function get_new_command
def test_get_new_command():
    script = "aws ec2 help"

# Generated at 2022-06-14 09:23:20.021342
# Unit test for function get_new_command
def test_get_new_command():
    new_commands = get_new_command(Command("aws s3 ls --recursive", "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument operation: Invalid choice, maybe you meant: \n* cp\n* ls \n* mb\n* rb", stderr="aws: error: argument operation: Invalid choice, maybe you meant: \n* cp\n* ls \n* mb\n* rb"))

# Generated at 2022-06-14 09:23:25.414686
# Unit test for function match
def test_match():
    assert match(Command('aws ec2', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument <command> is required'))



# Generated at 2022-06-14 09:23:31.848284
# Unit test for function match
def test_match():
    assert match(Command('aws s3 ls', 'usage: aws [options] <command> <subcommand> [<subcommand> ...]\nError: Invalid choice: "s3"', '', 0, None))

if __name__ == '__main__':
    print(get_new_command(Command('aws s3 ls', 'usage: aws [options] <command> <subcommand> [<subcommand> ...]\nError: Invalid choice: "s3"', '', 0, None)))

# Generated at 2022-06-14 09:23:36.881760
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 describe-instances --region us-east-1',
                         "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run: aws help\nUnknown options: --region, us-east-1\nMaybe you meant:\n    instances\n    regions\n    instance-ids\n"))



# Generated at 2022-06-14 09:23:39.469373
# Unit test for function match

# Generated at 2022-06-14 09:23:52.308636
# Unit test for function get_new_command

# Generated at 2022-06-14 09:24:01.810690
# Unit test for function match
def test_match():
	assert match(Command('aws ec2 describe-instances --instance-id i-12345678', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\n\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\n\nerror: Invalid choice: "--instance-id", maybe you meant:\n  --instance-ids\n  --instance-initiated-shutdown-behavior\nSee "aws help" for descriptions of global parameters.'))


# Generated at 2022-06-14 09:24:09.996042
# Unit test for function match
def test_match():
    assert match(Command('aws s3 ls', 'usage: aws [options] <command> <subcommand> [parameters]', 'aws: error: argument command: Invalid choice: \'s3\', maybe you meant:\n  * ssm\n  * sts\n  * sqs'))
    assert not match(Command('aws s3 ls', ''))
    assert not match(Command('aws s3 ls', 'aws: error: argument command: Invalid choice: \'s4\', maybe you meant:\n  * s3\n  * ssm\n  * sts\n  * sqs'))


# Generated at 2022-06-14 09:24:24.574951
# Unit test for function get_new_command

# Generated at 2022-06-14 09:24:37.762407
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    script = "aws ec2 describe-sns"

# Generated at 2022-06-14 09:24:51.368561
# Unit test for function match
def test_match():
    assert match(Command('aws --help',
                         'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run: aws help\naws: error: argument operation: Invalid choice, valid choices are:\n  --version\n  cloudformation\nmaybe you meant:\n  codepipeline'))

# Integration test for function get_new_command

# Generated at 2022-06-14 09:25:02.816582
# Unit test for function get_new_command

# Generated at 2022-06-14 09:25:14.849625
# Unit test for function get_new_command
def test_get_new_command():
    script = 'aws: command not found'

# Generated at 2022-06-14 09:25:26.803979
# Unit test for function match

# Generated at 2022-06-14 09:25:36.256418
# Unit test for function match

# Generated at 2022-06-14 09:25:41.050539
# Unit test for function match
def test_match():
    assert match(Command('ls --help', ''))
    assert match(Command('ls --help', 'usage: ls [options] [target]\nmaybe you meant: ls'))
    assert not match(Command('ls --help', 'usage: ls [options] [target]'))


# Generated at 2022-06-14 09:25:49.184093
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.aws import get_new_command
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--foo')
    import io
    output = io.StringIO('aws: error: argument -f/--foo: Invalid choice: \'baz\', maybe you meant:\n * bar\n * foo\n')
    command = parser.parse_args(['aws', '-f', 'baz'])
    new_commands = get_new_command(command)
    assert len(new_commands) == 2
    assert new_commands[0] == 'aws -f bar'
    assert new_commands[1] == 'aws -f foo'


# Generated at 2022-06-14 09:26:02.127918
# Unit test for function get_new_command

# Generated at 2022-06-14 09:26:10.214328
# Unit test for function match
def test_match():
    assert match({'script': 'aws --help', 'output': 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument subcommand: Invalid choice, maybe you meant:\n  es        elasticache\n  ec2       elasticloadbalancing\n  elb      '})


# Generated at 2022-06-14 09:26:12.928737
# Unit test for function match
def test_match():
    command = Command('aws blah blah blah', 'usage: blah blah blah maybe you meant: blah')
    assert match(command)



# Generated at 2022-06-14 09:26:28.379111
# Unit test for function match
def test_match():
    assert match(Command('aws'))
    assert match(Command('aws s3'))
    assert not match(Command('aws ec2'))



# Generated at 2022-06-14 09:26:35.373660
# Unit test for function match
def test_match():
    output = """usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help
aws: error: argument subcommand: Invalid choice, maybe you meant:
    setup
    events
    logs
    configure

"""
    assert match(Command('aws', output))
    assert not match(Command('aws', ''))
    assert not match(Command('git', 'status'))


# Generated at 2022-06-14 09:26:47.016589
# Unit test for function match

# Generated at 2022-06-14 09:26:54.896825
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws cloudfront list-distributions --marker "12345"',
                                   'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:  aws help\naws: error: argument subcommand: Invalid choice: \'"12345"\', maybe you meant:  ls?\n* list\n* ls\n\n',3)) == ['aws cloudfront list-distributions --marker list', 'aws cloudfront list-distributions --marker ls']

# Generated at 2022-06-14 09:27:08.069616
# Unit test for function match
def test_match():
    incorrect_cmd = Command('aws dynamoDB ListTables')

# Generated at 2022-06-14 09:27:13.468769
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws ec2 describe-instances foo bar')) == ['aws ec2 describe-instances foo', 'aws ec2 describe-instances bar']
    assert get_new_command(Command('aws ec2 describe-instances foobar')) == ['aws ec2 describe-instances foo']

# Generated at 2022-06-14 09:27:21.609021
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 describe-regions --region us-east-1',
        "Invalid choice: 'describe-regions', maybe you meant:\n  * describe-regions\n"))
    assert not match(Command('aws ec2 describe-regions --region us-east-1',
        "usage: aws [options] [parameters]\naws: error: argument operation: Invalid choice (\"describe-regions\"), maybe you meant:"))


# Generated at 2022-06-14 09:27:28.496419
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

    script = 'aws ec2 help'
    output = """usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help
aws: error: argument subcommand: Invalid choice: 'help', maybe you meant:
    create-flow-logs
    delete-flow-logs"""
    new_command = [
        'aws ec2 create-flow-logs',
        'aws ec2 delete-flow-logs']
    assert get_new_command(Command(script, output)) == new_command

# Generated at 2022-06-14 09:27:39.782415
# Unit test for function get_new_command

# Generated at 2022-06-14 09:27:51.831436
# Unit test for function get_new_command

# Generated at 2022-06-14 09:28:22.530257
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("aws ec2 describe-instances") == ["aws ec2 describe-instances"]

# Generated at 2022-06-14 09:28:32.691927
# Unit test for function match
def test_match():
    assert match(Command("aws s3 help", "usage: aws [options] <command> <subcommand> [parameters]\naws: error: argument command: Invalid choice: 's3 help', maybe you meant:\n        s3api\n        s3\n        ssm\n        service\n        sqs\n        serverlessrepo\n        sdb\n        sns"))

    assert match(Command("aws s3 help", "usage: awscli [options] <command> <subcommand> [<subcommand> ...] [parameters]\nawscli: error: argument --output: Invalid choice: 'json', maybe you meant:\n        json-input\n        table"))


# Generated at 2022-06-14 09:28:44.503210
# Unit test for function get_new_command
def test_get_new_command():
    from collections import namedtuple
    Command = namedtuple('Command', ['script', 'output'])

# Generated at 2022-06-14 09:28:46.373505
# Unit test for function match
def test_match():
    test = thefuck.utils.Test()

    assert match(test.script('aws'))
    assert not match(test.script('ssh'))
    assert not match(test.script('ls'))



# Generated at 2022-06-14 09:28:58.700352
# Unit test for function get_new_command
def test_get_new_command():
    script = "aws dynamodb create-table"
    output = "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument command: Invalid choice, maybe you meant: table\n    config\n    configure\n    console\n    events\n    inf\n    info\n    secretsmanager\n    secretsmanagerrecover\n    trim\n    zzz\n    zzzz\n\n"
