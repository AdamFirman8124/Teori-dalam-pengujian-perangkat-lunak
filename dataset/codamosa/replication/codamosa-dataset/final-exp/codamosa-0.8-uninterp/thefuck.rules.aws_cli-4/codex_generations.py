

# Generated at 2022-06-14 09:19:00.258525
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('aws ec2 describe-volumes --region eu-west-1') == ['aws ec2 describe-volumes --region us-east-1']


"""
Example terminal output:

$ aws ec2 describe-volumes --region eu-west-1
usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help
aws: error: argument --region: Invalid choice: 'eu-west-1', maybe you meant:
  us-east-1
us-west-1
us-west-2
"""

# Generated at 2022-06-14 09:19:09.498171
# Unit test for function match

# Generated at 2022-06-14 09:19:20.681352
# Unit test for function match
def test_match():
    command = Command('/tmp/aws s3api list-buckets')
    command.output = ("usage: aws [options] <command> <subcommand> [<subcommand> "
                      "...] [parameters]\n"
                      "\n"
                      "To see help text, you can run:\n"
                      "\n"
                      "  aws help\n"
                      "  aws <command> help\n"
                      "  aws <command> <subcommand> help\n"
                      "\n"
                      "Unknown options: s3api\n"
                      "Invalid choice: 's3api list-buckets', maybe you meant:\n"
                      "* list-bucket\n")
    assert match(command)


# Generated at 2022-06-14 09:19:26.251627
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("aws ec2 restart-instances --instance-ids $INSTANCE_ID", "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument instance-ids: Invalid choice: '$INSTANCE_ID', maybe you meant:\n* instance-id\n* --instance-id\n* --instance-ids\n", "")) == ["aws ec2 restart-instances --instance-id $INSTANCE_ID", "aws ec2 restart-instances --instance-ids $INSTANCE_ID"]

# Generated at 2022-06-14 09:19:31.101904
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script='./aws s3 ls',
                        output="Invalid choice: 's3e', maybe you meant:\n * s3, * ssm\nSee 'aws help' for descriptions of global parameters.\n")) == ["./aws s3 ls", "./aws ssm ls"]

# Generated at 2022-06-14 09:19:37.837015
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 describe-instances --output json',
    'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\nUnknown options: --output, json\nmaybe you meant:\n    --output-text')
    )



# Generated at 2022-06-14 09:19:49.436788
# Unit test for function get_new_command

# Generated at 2022-06-14 09:19:58.065206
# Unit test for function get_new_command
def test_get_new_command():
    script = 'aws ec2 run-instances --image-id ami-xxxxxxxx --count 1 --instance-type t2.micro'
    command = type('obj', (object,), {'script': script})
    assert(get_new_command(command) == [
        'aws ec2 run-instances --count 1 --instance-type t2.micro --image-id ami-xxxxxxxx',
        'aws ec2 run-instances --count 1 --image-id ami-xxxxxxxx --instance-type t2.micro'])

# Generated at 2022-06-14 09:20:09.621311
# Unit test for function match

# Generated at 2022-06-14 09:20:21.032712
# Unit test for function get_new_command

# Generated at 2022-06-14 09:20:34.374985
# Unit test for function match
def test_match():
    assert match(Command('aws s3 mb s3://bucket', 'usage: aws [options] <command> <subcommand> [parameters]\naws: error: argument subcommand: Invalid choice, maybe you meant:', ''))
    assert match(Command('aws sqs', 'usage: aws [options] <command> <subcommand> [parameters]\naws: error: argument subcommand: Invalid choice, maybe you meant:', ''))
    assert not match(Command('aws', 'usage: aws [options] <command> <subcommand> [parameters]\naws: error: argument subcommand: Invalid choice, maybe you meant:', ''))

# Generated at 2022-06-14 09:20:40.591927
# Unit test for function match
def test_match():
    assert match(
        Command('', 'aws usage:', 'aws: error: argument operation: Invalid choice: \'usage:\', maybe you meant:\n  * delete-function\n  * describe-function\n  * publish\n  * update-function-code\n  * invoke-async\nSee \'aws help\' for descriptions of global parameters.'))
    assert not match(Command('aws delete-function --function-name foo'))



# Generated at 2022-06-14 09:20:43.682911
# Unit test for function match
def test_match():
    assert not match(Command('tmux attach', '', '', 0))
    assert match(Command('aws', 'usage:', '', 0))
    assert match(Command('aws', 'usage:', 'maybe you meant:', 0))


# Generated at 2022-06-14 09:20:57.219692
# Unit test for function get_new_command
def test_get_new_command():
    some_command = "aws s3 sync --force test s3://some_bucket/some_directory"

# Generated at 2022-06-14 09:21:12.262658
# Unit test for function get_new_command

# Generated at 2022-06-14 09:21:18.250996
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    assert get_new_command(Command('aws s3 list', 'aws: error: argument command: Invalid choice: \'list\', maybe you meant:\n    la', None)) == [
        'aws s3 la']
    assert get_new_command(Command('aws s3 list', 'aws: error: argument command: Invalid choice: \'list\', maybe you meant:\ns3api\n\n', None)) == [
        'aws s3api']

# Generated at 2022-06-14 09:21:27.136397
# Unit test for function get_new_command
def test_get_new_command():
    assert(get_new_command(Command('aws',
                                   output="usage: awscli [options] <command> <subcommand> [parameters]\n"
                                          "awscli: error: Invalid choice: 'lalala', maybe you meant:\n"
                                          "\n* list-object-versions\n"
                                          "\n* list-objects-v2")) == ['aws s3api list-object-versions',
                                                                          'aws s3api list-objects-v2'])



# Generated at 2022-06-14 09:21:29.643737
# Unit test for function match
def test_match():
    assert match(Command('aws s3 help'))
    assert not match(Command('git ls-file'))


# Generated at 2022-06-14 09:21:31.283276
# Unit test for function get_new_command
def test_get_new_command():
    command = 'aws s3 --version'
    assert get_new_command(command) == ['aws s3api --version']

# Generated at 2022-06-14 09:21:42.433161
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('aws s3api invalid', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\n\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument invalid: Invalid choice, maybe you meant:\n\t* ls\n\t* ls-bucket\n\t* ls-objects\n\t* ls-object\n\t* ls-bucket-metadata\n', 'aws s3api invalid')
    assert get_new_command(command) == ['aws ls instance-profile']

# Generated at 2022-06-14 09:21:59.166831
# Unit test for function match

# Generated at 2022-06-14 09:22:04.737169
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 help', "", "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\n\naws: error: argument command: Invalid choice, maybe you meant:\n  lambda  (choose from a configuration set)"))


# Generated at 2022-06-14 09:22:17.133641
# Unit test for function get_new_command

# Generated at 2022-06-14 09:22:19.397830
# Unit test for function match
def test_match():
    assert (match(Command('aws foo help', 'usage: blah blah blah', '')))


# Generated at 2022-06-14 09:22:31.551698
# Unit test for function get_new_command
def test_get_new_command():
	command = Command("aws ec2 start-instances --instance-ids i-12345678", "")
	assert get_new_command(command) == ["aws ec2 start-instances --instance-ids i-12345678"]

	command = Command("aws ec2 start-instances --instance-ids i-12345678", "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\naws help\naws <command> help\naws <command> <subcommand> help\n\naws: error: argument --instance-ids: Invalid choice: 'i-12345678', maybe you meant: \n\n   * i-12345678 (a valid instance ID)")

# Generated at 2022-06-14 09:22:42.331454
# Unit test for function get_new_command

# Generated at 2022-06-14 09:22:48.952772
# Unit test for function get_new_command

# Generated at 2022-06-14 09:22:57.178320
# Unit test for function match
def test_match():
    output = '''
usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help
aws: error: argument operation: Invalid choice, maybe you meant:

  * s3api
  * cloudwatch
  * lambda
  * dynamodb
  * s3
  * configure
  * elasticloadbalancing
  * r53
  * rds
  * kms
  * cloudformation
  * logs
  * swf
  * route53
  * sts
  * iam
  * ec2
  * elb
  * s3-resource
  * sns
  * events

'''

# Generated at 2022-06-14 09:23:06.863782
# Unit test for function get_new_command

# Generated at 2022-06-14 09:23:10.101448
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws cloudformation create-stack apple',
                                   "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\naws: error: argument subcommand: Invalid choice: 'apple', maybe you meant:\n  * create-stack")) == \
                                   ['aws cloudformation create-stack']

# Generated at 2022-06-14 09:23:23.874133
# Unit test for function match

# Generated at 2022-06-14 09:23:33.879331
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws --configure', 'Invalid choice: \'--configure\', maybe you meant:\n * configure\n * configure-always')) == ['aws configure --configure']
    assert get_new_command(Command('aws --configure-always', 'Invalid choice: \'--configure-always\', maybe you meant:\n * configure\n * configure-always\n * describe-config')) == ['aws configure --configure-always', 'aws configure-always --configure-always', 'aws describe-config --configure-always']

# Generated at 2022-06-14 09:23:36.882075
# Unit test for function match
def test_match():
    assert not match(Command('asd', ""))
    assert match(Command('aws --version', ""))
    assert match(Command('aws help', ""))



# Generated at 2022-06-14 09:23:50.364921
# Unit test for function match

# Generated at 2022-06-14 09:24:02.552533
# Unit test for function match
def test_match():
    assert match(Command('aws --help', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\n\nInvalid choice: \'hellp\', maybe you meant:\n    help\n    help-config'))

# Generated at 2022-06-14 09:24:11.495174
# Unit test for function get_new_command
def test_get_new_command():
    app = Mock()
    app.which = lambda x: x
    script = 'aws ec2 take-snapshot --volume-id vol-45267ae2'
    output = "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument volume-id: Invalid choice: 'vol-45267ae2', maybe you meant:\n\n  volume-id-vol-45267ae2\n  volume-id-vol-e812af85\n  volume-id-vol-4d4af5b5"
    command = Command(script, output, app)
    assert get_new_command

# Generated at 2022-06-14 09:24:15.543794
# Unit test for function match
def test_match():
    assert match(Command('aws', '', ''))
    assert not match(Command('ls', '', ''))



# Generated at 2022-06-14 09:24:19.119458
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws s3 l', '')) == ['aws s3 ls']
    assert get_new_command(Command('aws s3 l', '')) != ['aws s3 cp']

# Generated at 2022-06-14 09:24:23.359545
# Unit test for function match
def test_match():
    wrong_command = Command('aws s3 help', 'aws: error: argument subcommand: Invalid choice: \'s3 help\', maybe you meant:* s3api* s3* s3control')
    assert match(wrong_command)


# Generated at 2022-06-14 09:24:28.142326
# Unit test for function match
def test_match():
    match_test = ('aws s3 ls --exclude "*" --include "*.jpg" \\\n'
                  '                             "s3://BUCKET" \\\n'
                  'usage: aws [options] <command> <subcommand> [parameters]\n'
                  'aws: error: argument subcommand: Invalid choice,'
                  ' maybe you meant:\n'
                  '\tls\n'
                  '\tmb\n'
                  '\tmv\n'
                  '\trm\n'
                  'See \'aws help\' for descriptions of global parameters.')

    assert match(match_test) == True



# Generated at 2022-06-14 09:24:37.017784
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws s3 ls', 'usage: aws [options] <command> <subcommand> [<subcommand> ...]\n'
                                   'aws: error: argument command: Invalid choice: '
                                   '"ls", maybe you meant:', 'aws s3 ls')) == ['aws s3 ls', 'aws s3 ls-bucket']

# Generated at 2022-06-14 09:24:40.048126
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("aws ec2 describe-instances --output table",
        "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\naws: error: argument operation: Invalid choice: 'describe-instances', maybe you meant:\n  * describe-identity-id-format\n  * describe-instances-status"
    )) == [
        "aws ec2 describe-identity-id-format --output table",
        "aws ec2 describe-instances-status --output table"
    ]


enabled_by_default = True

# Generated at 2022-06-14 09:24:43.079916
# Unit test for function match
def test_match():
    assert match(Command('aws --version',
                         "usage: aws [options] [parameters]\naws: error: argument command: Invalid choice: '--version', maybe you meant:\n* version\n  versions\n  versioning\n  versioning-migration\n  version-weight\n  vertical-scaling"))


# Generated at 2022-06-14 09:24:50.242441
# Unit test for function match
def test_match():
    assert match(Command('aws s3 help', 'usage: aws [options] <command> <subcommand> [<subcommand> ...]', 'aws: error: argument command: Invalid choice: \'help\', maybe you meant:', ''))
    assert not match(Command('aws s3 help', 'usage: aws [options] <command> <subcommand> [<subcommand> ...]', '', ''))


# Generated at 2022-06-14 09:25:02.359448
# Unit test for function get_new_command
def test_get_new_command():
    # Test when command is a one word string
    command = "aws ec2 help"
    assert get_new_command(command) == ["aws ec2 help"]

    # Test when command is a one word string in a list
    command = ["aws ec2 help"]
    assert get_new_command(command) == ["aws ec2 help"]

    # Test when command is a more than one word string
    command = "aws ec2 run-instances"
    assert get_new_command(command) == ["aws ec2 run-instances"]

    # Test when command is a more than one word string in a list
    command = ["aws ec2 run-instances"]
    assert get_new_command(command) == ["aws ec2 run-instances"]

    # Test when command is a one word string with a flag

# Generated at 2022-06-14 09:25:07.092424
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(["aws", "compute-optimizer", "GetAutoScalingGroupRecommendations", "--account-id", "123456789012", "--region", "us-east-1"]) == ["aws compute-optimizer get-auto-scaling-group-recommendations --account-id 123456789012 --region us-east-1"]

# Generated at 2022-06-14 09:25:16.350668
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws ec2 describe-instances --fasle', 
                        '')) == ['aws ec2 describe-instances --false']
    assert get_new_command(Command('aws ec2 describe-instances --fasle', 
                        'aws: error: argument --fasle: Invalid choice, maybe you meant:\n--instance-ids\n--filters\n--dry-run\n--output\n--profile')) == ['aws ec2 describe-instances --false', 'aws ec2 describe-instances --instance-ids', 'aws ec2 describe-instances --filters', 'aws ec2 describe-instances --dry-run', 'aws ec2 describe-instances --output', 'aws ec2 describe-instances --profile']


# Generated at 2022-06-14 09:25:24.857462
# Unit test for function match

# Generated at 2022-06-14 09:25:28.123154
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("aws ec2 help", "Invalid choice: 'hep', maybe you meant:\n\n* help", "")) == ["aws ec2 help"]

# Generated at 2022-06-14 09:25:36.785875
# Unit test for function match

# Generated at 2022-06-14 09:25:46.992474
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    output = "Invalid choice: 'llambda', maybe you meant:\n\n* lambda\n* ec2\n* logs\n"
    assert get_new_command(Command('aws llambda',
                                   output)) == ["aws lambda", "aws ec2", "aws logs"]

# Generated at 2022-06-14 09:25:55.224491
# Unit test for function get_new_command

# Generated at 2022-06-14 09:26:04.878941
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws s3 mb s3://my-bucet',
               'usage: aws [options] <command> <subcommand> [<subcommand> ...] '
               '[parameters]\n\naws: error: argument '
               'subcommand: Invalid choice, maybe you meant: \n  '
               'mb\n  rb\n\nTo see help text, you can run:\n\n  aws help\n  '
               'aws <command> help\n  aws <command> <subcommand> help\n',
               1)) == [u'aws s3 mb s3://my-bucet', u'aws s3 rb s3://my-bucet']

# Generated at 2022-06-14 09:26:18.334200
# Unit test for function get_new_command
def test_get_new_command():
    # Create a string for usage: and * options:
    awscli_error = """usage: aws [options] <command> <subcommand> [parameters]
aws: error: argument command: Invalid choice: 'ec2', maybe you meant:
    * ec2
    * ecr
    * ec2-instance-connect
    * elasticache"""
    command_script = "aws ec2"
    command = type("Command", (object,),
                   {"script": command_script, "output": awscli_error})
    new_cmd = get_new_command(command)
    assert new_cmd[0] == "aws ec2"
    assert new_cmd[1] == "aws ecr"
    assert new_cmd[2] == "aws ec2-instance-connect"

# Generated at 2022-06-14 09:26:32.443414
# Unit test for function get_new_command
def test_get_new_command():
    output = """
usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help
aws: error: argument <command>: Invalid choice, maybe you meant:
  ec2
  ec2-instance-connect
  ec2-instance-connect-settings"""

    command = Command(script="./aws ec2-instance-connect", output=output)
    assert get_new_command(command) == ["./aws ec2"]

# Generated at 2022-06-14 09:26:40.759187
# Unit test for function get_new_command
def test_get_new_command():
    output = """usage: aws [options] [ ...] [parameters]
To see help text, you can run:

  aws help
  aws help

Unknown options: --execute-api-request.
Invalid choice: '--execute-api-request', maybe you meant:
	--endpoint-url
	--query
	--execute-api
	--cli-auto-prompt
	--recursive
	--generate-cli-skeleton
	--paginate
	--debug
	--color
	--no-paginate
	--profile
	--no-color
"""
    command = "aws s3api list-buckets --execute-api-request"
    newcommand = get_new_command(Command(script=command, output=output))
    assert len(newcommand) == 9

# Generated at 2022-06-14 09:26:52.238546
# Unit test for function match

# Generated at 2022-06-14 09:26:56.007816
# Unit test for function match
def test_match():
    assert match(Command('aws --help', ''))
    assert match(Command('aws --help', 'usage: aws [options] [parameters]\n\nA mistake\n\n'
                                 'aws: error: argument --help: maybe you meant:  --help-all'))
    assert not match(Command('aws --help', 'A mistake'))

# Generated at 2022-06-14 09:27:00.838086
# Unit test for function match
def test_match():
    assert match(Command("aws s3 mb s3://test", "usage: aws [parameters] <command> <subcommand> [<subcommand> ...] [parameters]\n\nInvalid choice: 's3 mb', maybe you meant:\n\n* mb\n* mba\n* mbaas\n* mbp\n* s3api\n* s3control\n* s3m"))


# Generated at 2022-06-14 09:27:12.024249
# Unit test for function get_new_command
def test_get_new_command():
    script = "$ aws ec2 describe-instances --output=json"
    output = """usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help

Unknown options: --output=json
Invalid choice: 'ec2', maybe you meant:
            ecs
            acm
            ec
            ec2
            ec2-instance-connect
            lex
            codecommit
            apigateway
            acm
            ecr
            cloudfront
            es

"""

# Generated at 2022-06-14 09:27:33.590557
# Unit test for function match
def test_match():
    output = '''usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help

Invalid choice: 'ec2_describe', maybe you meant:
  * ec2 describe
  * ec2_instances_describe
'''
    assert match(Command(script='aws ec2_describe --output json', output=output))



# Generated at 2022-06-14 09:27:42.894797
# Unit test for function get_new_command

# Generated at 2022-06-14 09:27:51.782255
# Unit test for function match
def test_match():
    # Unit test for function match
    assert(match(Command(script="Not valid output of aws command", 
        output="usage:")) == False)
    assert(match(Command(script="aws help", 
        output="usage: aws [options] [ ...] [parameters] ")) == True)
    assert(match(Command(script="aws help", 
        output="usage: aws [options] [ ...] [parameters] \nInvalid choise: 'help', maybe you meant: ")) == True)


# Generated at 2022-06-14 09:28:00.816881
# Unit test for function match

# Generated at 2022-06-14 09:28:11.552485
# Unit test for function match
def test_match():
    command1 = "aws kms encrypt --key-id aa:bb:cc:11:22:33:44:55:66:77:88:99:00 --plaintext fileb://myfile --outputtext --query CiphertextBlob --output text"
    command2 = "aws kms encrypt --key-id aa:bb:cc:11:22:33:44:55:66:77:88:99:00 --plaintext fileb://myfile --outputtext --query CiphertextBlob --output text"

# Generated at 2022-06-14 09:28:20.570703
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command.__name__ == "get_new_command"
    # TODO write a test


enabled_by_default = True

# Generated at 2022-06-14 09:28:32.199424
# Unit test for function match
def test_match():
    output = """
Unknown options: --region eu-west-1, --profile default
usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help
aws: error: argument operation: Invalid choice: 'dynamodb', maybe you meant:
* dynamodbv2
"""
    command = Command('aws dynamodb', output)
    assert match(command)
    

# Generated at 2022-06-14 09:28:46.214419
# Unit test for function get_new_command
def test_get_new_command():
    command = type('Command', (), {
        'output': "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n  $ aws help\n  $ aws <command> help\n  $ aws <command> <subcommand> help\naws: error: argument subcommand: Invalid choice: 's3api', maybe you meant: \n* s3\n\nInvalid choice: 's3api', maybe you meant: \n* s3",
        'script': "aws s3api"
    })
    assert get_new_command(command) == ['aws s3']



# Generated at 2022-06-14 09:28:58.508930
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws ec2 get-console-output i-00000aa --region eu-west-1',
                                   'Invalid choice: \'--region\', maybe you meant:\n\n  '
                                   '* --region\n  * --regions')) == \
                                   ['aws ec2 get-console-output i-00000aa --region eu-west-1']
    assert get_new_command(Command('aws ec2 get-console-output i-00000aa --region eu-west-1',
                                   'Invalid choice: \'--region\', maybe you meant:\n\n  '
                                   '* --region\n  * --regions')) == \
                                   ['aws ec2 get-console-output i-00000aa --region eu-west-1']
