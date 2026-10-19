

# Generated at 2022-06-14 09:19:06.916442
# Unit test for function get_new_command
def test_get_new_command():
    command = "aws s3api list-objects --bukets test"
    output = "s3api is a sub-command of s3. You must use the --bucket parameter.\n"\
             "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\n"\
             "To see help text, you can run:\n"\
             "  aws help\n"\
             "  aws <command> help\n"\
             "  aws <command> <subcommand> help\n"\
             "aws: error: argument operation: Invalid choice, valid choices are:\n"\
             "* list-buckets\n"\
             "* list-multipart-uploads\n"\
             "* list-object-versions\n"\
            

# Generated at 2022-06-14 09:19:18.634340
# Unit test for function match
def test_match():
    assert match(Command('aws configure',
        output='usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters] \nTo see help text, you can run:\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help'))
    assert not match(Command('aws configure',
        output='usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters] \nTo see help text, you can run:\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help',
        stderr='Unable to locate credentials'))


# Generated at 2022-06-14 09:19:27.503933
# Unit test for function match
def test_match():
    assert match(Command('aws --version',
                         '/usr/bin/aws: error: argument --version: ' \
                         'expected one argument\nusage: aws [options] ' \
                         '<command> <subcommand> [<subcommand> ...] [parameters]\n\n'
                         'To see help text, you can run: \n\n  ' \
                         'aws help\n  aws <command> help\n  aws <command> <subcommand> help\n\n',
                         2))


# Generated at 2022-06-14 09:19:35.818202
# Unit test for function get_new_command
def test_get_new_command():
    import collections
    Command = collections.namedtuple('Command', ['script', 'output'])
    command = Command(script = "aws ec2 run-instances", output = "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\n  aws: error: argument operation: Invalid choice, valid choices are:\n    request-spot-fleet\n    run-instances\n    start-instances\n    stop-instances\n    terminate-instances",)
    command = get_new_command(command)
    print(command)

# Generated at 2022-06-14 09:19:41.642548
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws ec2 rn --pofiles', 'Invalid choice: \'-pofiles\' (choose from \'rename-instances\', \'reboot-instances\')\n')) == ['aws ec2 rename-instances --pofiles', 'aws ec2 reboot-instances --pofiles']



# Generated at 2022-06-14 09:19:45.414216
# Unit test for function match
def test_match():
    command = "aws s3 mb s3://mybucket"
    output = "Error: s3: argument subcommand: Invalid choice, valid choices are:"
    assert match(Command(command, output))


# Generated at 2022-06-14 09:19:52.429006
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 describe-security-groups', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\naws: error: argument subcommand: Invalid choice, maybe you meant:\n  describe-snapshots   Describe an EC2 snapshot\n* describe-security-groups  Describe an EC2 security-groups\n  describe-instances   Describe an EC2 instancess'))
    assert not match(Command('ls'))

# Generated at 2022-06-14 09:19:54.784677
# Unit test for function get_new_command
def test_get_new_command():
    command = "aws ec2 --region us-west-2"
    new_command = get_new_command(command)
        
    assert new_command == "aws ec2 --region us-west-2"

# Generated at 2022-06-14 09:20:05.164118
# Unit test for function match
def test_match():
    assert match(Command('aws s3 mb s3://somebucket',
                         'The bucket name you requested is not available'
                         '\n'
                         'Bucket names must contain lowercase letters, numbers,'
                         ' periods, and dashes.'))

    assert match(Command('aws ec2 describe-images --owner self',
                         'usage: aws [options] &lt;command&gt; '
                         '[parameters]\n'
                         'aws: error: argument --owner: Invalid choice'
                         ' \'self\', maybe you meant:',))


# Generated at 2022-06-14 09:20:17.263410
# Unit test for function match
def test_match():
    # Simple match test
    assert match(Command(script="aws s3 ls", output="usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\n\nMaybe you meant:\n    ls"))
    # Checking to make sure the function doesn't match on a different aws command
    assert not match(Command(script="aws ec2 run-instances --image-id ami-e444444d --count 1 --instance-type t1.micro --key-name MyKeyPair --security-groups MySecurityGroup", output="usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\n\nMaybe you meant:\n    run-instances"))


# Generated at 2022-06-14 09:20:23.164667
# Unit test for function match
def test_match():
    assert match(Command(script='aws ec2 describe-instances', output='usage:'))
    assert match(Command(script='aws ec2 describe-instanceZs', output='usage:'))
    assert not match(Command(script='aws ec2 describe-instances', output='debug:'))


# Generated at 2022-06-14 09:20:30.616362
# Unit test for function match
def test_match():
    assert match(Command('aws help', ''))
    assert match(Command('aws help', "usage:"))
    assert match(Command('aws help', "maybe you meant:"))
    assert not match(Command('ls', ''))

if __name__ == '__main__':
    print(get_new_command(Command("aws help", "'aws2' is not a valid AWS CLI command.\nMaybe you meant:\n  cloudsearch")))

# Generated at 2022-06-14 09:20:40.065165
# Unit test for function get_new_command
def test_get_new_command():
    command = apply_alias(Command('aws help', 'aws: Invalid choice: \'h\', maybe you meant:\n  help\n  ...'))
    assert get_new_command(command) == ['aws help']

    command = apply_alias(Command('aws help', 'aws: Invalid choice: \'h\', maybe you meant:\n  help\n  ...'))
    assert get_new_command(command) == ['aws help']

    command = apply_alias(Command('aws help', 'aws: Invalid choice: \'h\', maybe you meant:\n  help\n  ...'))
    assert get_new_command(command) == ['aws help']

    command = apply_alias(Command('aws help', 'aws: Invalid choice: \'h\', maybe you meant:\n  help\n  ...'))
    assert get_new_command

# Generated at 2022-06-14 09:20:52.505061
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws ec2 stop --syntax',
                                   'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\n'
                                   'aws: error: argument subcommand: Invalid choice: \'ec2 stop --syntax\', '
                                   'maybe you meant:\n\n'
                                   '* --syntax\n  * help\n'
                                   'See \'aws help\' for descriptions of global parameters.\n')) == \
           ['aws --syntax ec2 stop', 'aws ec2 help stop']

# Generated at 2022-06-14 09:21:01.340645
# Unit test for function match
def test_match():
    assert(match(Command("aws", "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]", "Invalid choice: 'hey', maybe you meant:\n\t* hey1\n\t* hey2\n\t* hey3\n\t* hey4")) == True)
    assert(match(Command("aws", "", "Invalid choice: 'hey', maybe you meant:\n\t* hey1\n\t* hey2\n\t* hey3\n\t* hey4")) == False)

# Generated at 2022-06-14 09:21:14.749638
# Unit test for function match

# Generated at 2022-06-14 09:21:27.683034
# Unit test for function get_new_command

# Generated at 2022-06-14 09:21:33.428194
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 start-instances --instance-ids foo', '',
                         'usage: aws [options]  <command>  '
                         '<subcommand> [<subcommand> ...] [parameters]\n'
                         'aws: error: argument instance-ids: '
                         "Invalid choice: 'foo', maybe you meant:\n"
                         '* i\n'
                         '* id\n'
                         '* --instance-id'))



# Generated at 2022-06-14 09:21:45.997458
# Unit test for function match
def test_match():
    assert(match(Command(script='aws', output='usage: aws [options] <command> <subcommand> [parameters]\naws: error: argument <command> is required\nmaybe you meant: cloudformation\ns3api\n',
        stderr='usage: aws [options] <command> <subcommand> [parameters]\naws: error: argument <command> is required\nmaybe you meant: cloudformation\ns3api\n',
        exit_code=2)) == True)

# Generated at 2022-06-14 09:21:59.557026
# Unit test for function match
def test_match():
    assert match(Command('aws s3 ls', '', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument subcommand: Invalid choice, maybe you meant:\n  command\n  configure\n  help\n  iam\n  s3'))

# Generated at 2022-06-14 09:22:05.435197
# Unit test for function match
def test_match():
    invalid_output = "aws: error: argument subcommand: Invalid choice, valid choices are: \n* foo\n* bar"
    assert match(Command('aws subcommand --some-args', invalid_output))
    assert not match(Command('aws subcommand --some-args', 'aws: error: argument subcommand: invalid choice: foo'))

# Generated at 2022-06-14 09:22:17.594546
# Unit test for function get_new_command

# Generated at 2022-06-14 09:22:25.409772
# Unit test for function get_new_command
def test_get_new_command():
    # test case 1: invalid choice is the last argument
    output = "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\n\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\n\nUnknown options: --foo\n\nInvalid choice: '--foobar', maybe you meant:\n\n  * --foo\n  * --force\n  * --foreground\n"
    script = "aws --foobar"
    command = collections.namedtuple('Command', ['script', 'output'])(script, output)
    new_commands = get_new_command(command)

# Generated at 2022-06-14 09:22:32.894842
# Unit test for function match
def test_match():
    command = Command("aws s3 rb s3://bucket", "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument command: Invalid choice, valid choices are:\n        mb | rb | cp | ls | mv | rm | sync | website | ")
    assert match(command)


# Generated at 2022-06-14 09:22:42.933599
# Unit test for function match
def test_match():
    assert match(Command('aws', output="usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument subcommand: Invalid choice: '', maybe you meant:configure\n"))
    assert not match(Command('aws', output="usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument subcommand: Invalid choice: '', maybe you meant:"))

#

# Generated at 2022-06-14 09:22:44.593524
# Unit test for function match
def test_match():
    assert match(Command('aws --version'))


# Generated at 2022-06-14 09:22:54.119531
# Unit test for function match

# Generated at 2022-06-14 09:23:05.213521
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

    script = "aws ec2 start-instances --instance-ids i-0123456789abcdef0"

# Generated at 2022-06-14 09:23:16.500345
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command(Command("aws s3 ls s3://mybucket", "usage: aws [options] <command> <subcommand> [<subcommand> ...]\n\n  error: argument subcommand: Invalid choice, valid choices are:\n\n  cp\n  ls\n  mb\n  mv\n  rb\n  rm\n  sync\n  website\n\nmaybe you meant: s3 cp, s3 mv, s3 rm\n")) == 
            ['aws s3 cp s3://mybucket', 'aws s3 mv s3://mybucket', 'aws s3 rm s3://mybucket'])

# Generated at 2022-06-14 09:23:28.226265
# Unit test for function get_new_command

# Generated at 2022-06-14 09:23:33.107955
# Unit test for function match
def test_match():
    assert match(Command('aws sts get-session-token', "Unknown options: '--foo'", ''))
    assert not match(Command('aws sts get-session-token', "", ''))


# Generated at 2022-06-14 09:23:40.012521
# Unit test for function match
def test_match():
    assert match(Command('aws --version', 'usage: aws [options] <command> <subcommand> [parameters]\naws: error: argument subcommand: Invalid choice: "--version"\n(maybe you meant: --color, --version, --output, --profile, --debug)\n'))
    assert match(Command('aws s3 ls', 'usage: aws [options] <command> <subcommand> [parameters]\naws: error: argument subcommand: Invalid choice: "s3"\n(maybe you meant: --color, --version, --output, --profile, --debug)\n'))

# Generated at 2022-06-14 09:23:50.982823
# Unit test for function get_new_command
def test_get_new_command():
   log = '''
usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help
aws: error: argument subcommand: Invalid choice, maybe you meant:
  config
  kms
  s3
  s3api
  sts
'''
   command = type('', (), {
       'output': log,
       'script': 'aws config ls --recursive'
   })
   command.script = command()
   assert get_new_command(command) == ['aws config ls --recursive']

# Generated at 2022-06-14 09:23:58.224322
# Unit test for function match
def test_match():
    assert match(Command('aws s3 ls', 'usage: aws [options] <command> <subcommand> [parameters]\n\naws: error: argument command: Invalid choice, maybe you meant: ...', ''))
    assert not match(Command('ls',
                             'usage: aws [options] <command> <subcommand> [parameters]',
                             ''))


# Generated at 2022-06-14 09:24:03.876161
# Unit test for function match
def test_match():
    """Test if function `match` behaves as expected."""
    result = match(Command('aws ec2 run-instances'))
    assert result is True
    result = match(Command('aws ec2 run-insts'))
    assert result is False
    result = match(Command('ls -al'))
    assert result is False


# Generated at 2022-06-14 09:24:11.959891
# Unit test for function match

# Generated at 2022-06-14 09:24:18.109295
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script='aws help foo',
                      output="Invalid choice: 'foo', maybe you meant:\n  * bar\n  * baz\n  * foobar")
    assert get_new_command(command) == ['aws help bar', 'aws help baz', 'aws help foobar']



# Generated at 2022-06-14 09:24:20.454079
# Unit test for function match
def test_match():
    assert match(Command('aws help'))
    assert not match(Command('help aws'))

# Generated at 2022-06-14 09:24:29.863937
# Unit test for function get_new_command
def test_get_new_command():
	command_output = """
usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help
aws: error: argument subcommand: Invalid choice, maybe you meant:
  lint          Validate CloudFormation templates.
  lint-template Validate CloudFormation templates.
See 'aws help' for descriptions of global parameters.
"""
	command_script = 'aws list-categories'
	command = namedtuple('Command', 'script output')(command_script, command_output)
	new_command_list = get_new_command(command)

	assert(new_command_list[0] == 'aws lint list-categories')

# Generated at 2022-06-14 09:24:38.294584
# Unit test for function match
def test_match():
    assert match(Command('aws --help', 'aws: error: unknown option: --help\nusage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\naws help\naws <command> help\naws <command> <subcommand> help\naws: error: argument command: Invalid choice, valid choices are:\n\tconfigure\n\t* help\n\t\n\tmaybe you meant: * help'))


# Generated at 2022-06-14 09:24:53.619230
# Unit test for function get_new_command
def test_get_new_command():
    output = "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument subcommand: Invalid choice: 's.3', maybe you meant:\n  s3\n  s3api"
    script = ["aws", "ec", "s.3", "help"]
    command = Command(script, output)
    new_command = get_new_command(command)
    assert new_command == [["aws", "ec", "s3", "help"], ["aws", "ec", "s3api", "help"]]

# Generated at 2022-06-14 09:24:57.240189
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws s3 ls', 'Invalid choice: \'s3\', maybe you meant:\n  ls\n')) == ['aws ls s3']

# Generated at 2022-06-14 09:25:11.125113
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 describe-volumes',
                         "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\n"
                         "To see help text, you can run:\n"
                         "\n"
                         "  aws help\n"
                         "  aws <command> help\n"
                         "  aws <command> <subcommand> help\n"
                         "\n"
                         "aws: error: argument subcommand: Invalid choice, maybe you meant:\n"
                         "* describe-volumes\n"
                         "  describe-snapshots\n"
                         "  create-volume\n"
                         "  delete-volume\n"
                         "  attach-volume\n"))

# Generated at 2022-06-14 09:25:18.148571
# Unit test for function get_new_command
def test_get_new_command():
    script = 'aws ec2 desscribe-activities --profile dev --region ap-south-1'
    output = '''
usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help
aws: error: argument subcommand: Invalid choice, maybe you meant:
                      * describe-activities
                      * describe-attribute
                      * describe-classification-jobs
                      * '''
    new = 'aws ec2 describe-activities --profile dev --region ap-south-1'

    command = Command(script, output)
    assert get_new_command(command)[0] == new

# Generated at 2022-06-14 09:25:31.694497
# Unit test for function match

# Generated at 2022-06-14 09:25:45.740649
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    assert get_new_command(Command('aws --version', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\n\ninvalid choice: ', '')) == ['aws version']

# Generated at 2022-06-14 09:25:54.131027
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 describe-price',
        'A client error (InvalidParameterValue) occurred when calling the DescribePrice operation: Unexpected parameter \'ec2 describe-price\'\nusage: aws [options] <command> <subcommand> [parameters]\naws: error: argument command: Invalid choice, valid choices are:\nconfigure\neb\necr\nelasticache\nelasticbeanstalk\nelb\nelbv2\nemr\niam\nkms\nlambda\nom\ns3api\ns3control\ns3\nsts\nsns\n', 1, None))
    assert match(Command('aws help', '')) is False
    assert match(Command('aws help describe-price', '')) is False

# Generated at 2022-06-14 09:25:59.651289
# Unit test for function match
def test_match():
    for cmd in [
        Command('aws ec2 start-instances --instance-ids i-1234567'),
        Command('aws ec2 stop-instances --instance-ids i-1234567'),
        Command('aws ec2 reboot-instances --instance-ids i-1234567')
    ]:
        assert match(cmd)


# Generated at 2022-06-14 09:26:07.063600
# Unit test for function match
def test_match():
    from thefuck.types import Command

    assert match(Command('aws ec2 help', 'Invalid choice: \'ec2\', maybe you meant:\n  * ec3'))
    assert match(Command('aws help', 'Invalid choice: \'help\', maybe you meant:\n  * help'))
    assert not match(Command('aws help ec2', 'Invalid choice: \'help\', maybe you meant:\n  * help'))


# Generated at 2022-06-14 09:26:18.538062
# Unit test for function get_new_command
def test_get_new_command():
	assert(get_new_command(Command('aws s3 ls', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [...]')) == [['aws', 's3', 'ls']])
	assert(get_new_command(Command('aws s3 ls', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [...]\naws: error: argument subcommand: Invalid choice: \'ls\', maybe you meant:\n\n* ls\n* mb\n* rb\n\n')) == [['aws', 's3', 'ls'], ['aws', 's3', 'mb'], ['aws', 's3', 'rb']])

# Generated at 2022-06-14 09:26:30.975702
# Unit test for function match
def test_match():
    assert match(Command(script="aws help", output="Invalid choice: 'help', maybe you meant:* blah blah blah"))
    assert not match(Command(script="aws", output="some other output"))
    assert not match(Command(script="", output="some other output"))
    assert not match(Command(script="", output=""))


# Generated at 2022-06-14 09:26:39.821317
# Unit test for function match
def test_match():
    assert match(Command('aws ec2', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]', '', 1))
    assert match(Command('aws ec2', 'Error: argument command: Invalid choice, valid choices are:', '', 1))
    assert not match(Command('asd ec2', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]', '', 1))

test = [
    Command('aws ec2', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]', '', 1),
    Command('aws ec2', 'Error: argument command: Invalid choice, valid choices are:', '', 1)
    ]


# Generated at 2022-06-14 09:26:42.637093
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 describe-volumes --volume-id vol-12345 --output text --query Stacks'))


# Generated at 2022-06-14 09:26:53.232948
# Unit test for function get_new_command

# Generated at 2022-06-14 09:26:54.644696
# Unit test for function match
def test_match():
    assert match(Command('aws', ''))
    assert not match(Command('ls', ''))


# Generated at 2022-06-14 09:26:56.427878
# Unit test for function match
def test_match():
    assert match(Command('aws ec2 help', ''))
    assert match(Command('aws ec2 stop-instances a b c', ''))



# Generated at 2022-06-14 09:27:01.198345
# Unit test for function match
def test_match():
    for command in [
        Command("aws --help"),
        Command("aws foo.txt"),
        Command("aws new --region --help")
    ]:
        assert not match(command)

    for command in [
        Command("aws --non-existing-argument"),
        Command("aws help --non-existing-command"),
        Command("aws non-existing-group --non-existing-command")
    ]:
        assert match(command)



# Generated at 2022-06-14 09:27:04.978149
# Unit test for function match
def test_match():
    assert match(Command('aws iam list-users',
                         'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\naws: error: argument command: Invalid choice, maybe you meant:\n  list-users       \n* help            \n\nTo see help text, you can run:\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\n',1))



# Generated at 2022-06-14 09:27:09.122695
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws s3 ls notexists', "Invalid choice: 'notexists', maybe you meant:\n  * ls")) == ["aws s3 ls"]



# vim:expandtab:shiftwidth=4:tabstop=4:softtabstop=4:textwidth=80

# Generated at 2022-06-14 09:27:14.042834
# Unit test for function match
def test_match():
    assert match(Command('aws --help', '', 'Invalid choice: \'A\', maybe you meant: B\n  * A'))
    assert not match(Command('echo --help', '', 'usage: echo [-n] [string ...]'))



# Generated at 2022-06-14 09:27:27.011585
# Unit test for function match
def test_match():
    assert match(Command('aws s3 ls', 'usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n\n  aws help\n  aws <command> help\n  aws <command> <subcommand> help\naws: error: argument command: Invalid choice, valid choices are:\n\nconfigure\nhelp\n\n', 1))
    assert not match(Command('aws s3 ls', '', 0))




# Generated at 2022-06-14 09:27:29.275919
# Unit test for function get_new_command
def test_get_new_command():
	assert get_new_command("aws ec2 describe-instances") == 'aws ec2 describe-instances'

# Generated at 2022-06-14 09:27:41.973790
# Unit test for function match

# Generated at 2022-06-14 09:27:47.387900
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('aws ec2 describe-instances --output text --query Reservations[*].Instances[*].[PublicIpAddress]')) == ['aws ec2 describe-instances --query Reservations[*].Instances[*].Tags[*].[Key,Value]' ]

# Generated at 2022-06-14 09:27:49.682782
# Unit test for function match
def test_match():
    assert match(Command('awshelp\t'))
    assert not match(Command('aws'))



# Generated at 2022-06-14 09:27:56.052896
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('aws ec2 listinstances', 'aws: error: argument command: Invalid choice: \'listinstances\', maybe you meant: \n  * list-instances\n  * list-jobs\n\nSee \'aws help\' for descriptions of global parameters.')

    assert get_new_command(command) == ['aws ec2 list-instances', 'aws ec2 list-jobs']

# Generated at 2022-06-14 09:27:58.441332
# Unit test for function match
def test_match():
    assert match(Command('aws', 'usage:'))
    assert not match(Command('ls', ''))


# Generated at 2022-06-14 09:28:10.632875
# Unit test for function get_new_command

# Generated at 2022-06-14 09:28:17.775172
# Unit test for function match

# Generated at 2022-06-14 09:28:28.061717
# Unit test for function get_new_command

# Generated at 2022-06-14 09:28:47.106652
# Unit test for function get_new_command
def test_get_new_command():
    test_output = "usage: aws [options] [ ...] \n\n" \
                  "  --just-a-test                this is just a test\n" \
                  "  --just-another-test          just another test\n" \
                  "  --just-yet-another-test      just yet another test\n" \
                  "Invalid choice: 'just-a-test', maybe you meant:\n" \
                  "  --just-another-test          just another test\n" \
                  "  --just-yet-another-test      just yet another test\n"
    test_command = Command("aws --just-a-test", test_output)
    assert get_new_command(test_command) == [
        "aws --just-another-test", "aws --just-yet-another-test"]

# Generated at 2022-06-14 09:28:49.592636
# Unit test for function match
def test_match():
    assert match(Command('aws acc', ''))
    assert not match(Command('perl acc', ''))


# Generated at 2022-06-14 09:28:55.086704
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('aws ec2 describe-instance --filters Name=instance-state-name,Values=running Name=tag:test,Values=test') == \
           ['aws ec2 describe-instance --filters Name=instance-state-name,Values=running Name=tag:test,Values=test']



enabled_by_default = False