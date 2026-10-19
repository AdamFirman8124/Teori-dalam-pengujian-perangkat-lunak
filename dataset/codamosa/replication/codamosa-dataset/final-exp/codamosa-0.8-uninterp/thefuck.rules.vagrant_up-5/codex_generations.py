

# Generated at 2022-06-14 10:57:42.813949
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('vagrant', '', 'The domain was not found, but can be added with: vagrant up')) == 'vagrant up'
    assert get_new_command(Command('vagrant', '', 'you must first update your vagrant box')) == 'vagrant box update'
    assert get_new_command(Command('vagrant', '', 'VM must be running to open SSH connection')) == ['vagrant up', 'vagrant up']
    assert get_new_command(Command('vagrant', '', 'VM must be running to open SSH connection')) != 'vagrant up'

# Generated at 2022-06-14 10:57:48.810581
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

    assert get_new_command(Command("vagrant ssh", "", "")) == \
        'vagrant up && vagrant ssh'
    assert get_new_command(Command("vagrant ssh ccc", "", "")) == \
        ['vagrant up ccc && vagrant ssh ccc', 'vagrant up && vagrant ssh ccc']

# Generated at 2022-06-14 10:57:57.291671
# Unit test for function match
def test_match():
    command = Command('vagrant foo',
                      'The environment has not yet been created. '
                      'Run `vagrant up` to create the environment. '
                      'If a machine is not created, only the default'
                      ' provider will be shown. So if you\'re using a '
                      'non-default provider, make sure to create the '
                      'machine first by running `vagrant up`.')
    assert match(command)
    command = Command('vagrant foo', 'FOO')
    assert not match(command)



# Generated at 2022-06-14 10:58:00.814849
# Unit test for function match
def test_match():
    assert match(Command('vagrant up', '', "The host path of the shared folder is missing: /home/vagrant/sync"))
    assert match(Command('vagrant up', '', "Please initialize your environment to use this command"))
    assert not match(Command('vagrant up', '', "There are errors in the configuration of this machine"))

# Generated at 2022-06-14 10:58:13.824366
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('vagrant plugin install vagrant-berkshelf',
                                   'The installed version of Vagrant is too old '
                                   'for the installed version of the Vagrant '
                                   'Berkshelf plugin. Please ensure you are '
                                   'using Vagrant 1.2.2 or later and then run '
                                   '`vagrant up` to run Vagrant.')) == \
            'vagrant plugin install vagrant-berkshelf && vagrant up'

# Generated at 2022-06-14 10:58:21.667400
# Unit test for function get_new_command
def test_get_new_command():
    script = '''vagrant ssh'''
    cmd = Command(script, '')
    assert get_new_command(cmd) == [u'vagrant up', script]

    script = '''vagrant ssh web'''
    cmd = Command(script, '')
    assert (get_new_command(cmd) == [u'vagrant up web', 'vagrant up && ' + script])

# Generated at 2022-06-14 10:58:27.491120
# Unit test for function match
def test_match():
    assert match(Command(script='vagrant up',
                         output="""The environment has been instructed to "
                         "always run `vagrant up` in a new directory. Run
                         `vagrant up` to create a new environment.
                         """)
                 )
    assert not match(Command(script='vagrant up',
                             output='No output'))



# Generated at 2022-06-14 10:58:32.027909
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.vagrant_up import get_new_command
    assert get_new_command(Command('vagrant up', '', 'The machine name(s) were not specified')) == ['vagrant up', 'vagrant up && vagrant ssh']

# Generated at 2022-06-14 10:58:42.385230
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(
        'vagrant status', '', 'The VM is in an inaccessible directory. Run `vagrant up` to create and start the VM.\n')) == ['vagrant up', 'vagrant up && vagrant status']
    assert get_new_command(Command(
        'vagrant status machine1', '', 'The VM is in an inaccessible directory. Run `vagrant up` to create and start the VM.\n')) == ['vagrant up machine1', 'vagrant up && vagrant status machine1']
    assert get_new_command(Command(
        'vagrant status machine1 machine2', '', 'The VM is in an inaccessible directory. Run `vagrant up` to create and start the VM.\n')) == ['vagrant up machine2', 'vagrant up && vagrant status machine1 machine2']

# Generated at 2022-06-14 10:58:48.031949
# Unit test for function match
def test_match():
    assert match(Command('vagrant ssh', '==> default: Machine is not running. Check current state with `vagrant status` (this can take a while) ==> default: Machine is not running. Check current state with `vagrant status` (this can take a while) The machine you\'re attempting to SSH into is not running. Please start the machine, either by running `vagrant up` or using the VirtualBox GUI.'))
    assert not match(Command('vagrant ssh', 'The machine you\'re attempting to SSH into is not running. Please start the machine, either by running `vagrant up` or using the VirtualBox GUI.'))
    assert not match(Command('vagrant ssh', ''))


# Generated at 2022-06-14 10:59:04.183994
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('vagrant ssh')) == u'vagrant up && vagrant ssh'
    assert get_new_command(Command('vagrant ssh -h')) == u'vagrant up && vagrant ssh -h'
    assert get_new_command(Command('vagrant ssh machine')) == [u'vagrant up machine && vagrant ssh machine',
                                                               u'vagrant up && vagrant ssh machine']
    assert get_new_command(Command('vagrant ssh machine -h')) == [u'vagrant up machine && vagrant ssh machine -h',
                                                                  u'vagrant up && vagrant ssh machine -h']

# Generated at 2022-06-14 10:59:08.448159
# Unit test for function get_new_command
def test_get_new_command():
    assert(get_new_command(Command("vagrant ssh not-started", "", "")) == [shell.and_(u"vagrant up not-started", u"vagrant ssh not-started"), shell.and_(u"vagrant up", u"vagrant ssh not-started")])
    assert(get_new_command(Command("vagrant ssh", "", "")) == shell.and_(u"vagrant up", u"vagrant ssh"))

# Generated at 2022-06-14 10:59:16.184641
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script='vagrant ssh',
                      stderr='default: The VM is not running. To start the VM, run `vagrant up`')
    assert get_new_command(command) == "vagrant up ; vagrant ssh"

    command = Command(script='vagrant ssh machine1',
                      stderr='machine1: The VM is not running. To start the VM, run `vagrant up`')
    assert get_new_command(command) == "vagrant up machine1 ; vagrant ssh machine1"

# Generated at 2022-06-14 10:59:23.346675
# Unit test for function match
def test_match():
    command = Command('vagrant up',
                      '--provider vmware_fusion',
                      ['vagrant up', '--provider', 'vmware_fusion'],
                      "The VMware provider requires the \u001b[31mVMware\u001b[0m \u001b[31mDesktop\u001b[0m installation. Please run `vagrant up` again and include the flag `--provider vmware_desktop`.\n\nAlternatively, you can install the \u001b[31m`vagrant-vmware-fusion`\u001b[0m plugin for this provider, which is installed separately from Vagrant. This will allow you to use the `vmware_fusion` provider without the official VMware installation.\n\nMake sure you have the necessary plugins installed and then run `vagrant up` again.\n")

# Generated at 2022-06-14 10:59:36.085339
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

    vagrant_up = 'vagrant up'
    vagrant_up_with_vm = 'vagrant up {}'
    command = Command('vagrant up vm1', vagrant_up)
    assert get_new_command(command) == [vagrant_up_with_vm.format('vm1'), vagrant_up]
    command = Command('vagrant up vm1 --provider=openstack', vagrant_up)
    assert get_new_command(command) == [vagrant_up_with_vm.format('vm1'),
                                        vagrant_up_with_vm.format('vm1 --provider=openstack'), vagrant_up]
    command = Command('vagrant up', vagrant_up)
    assert get_new_command(command) == vagrant_up

# Generated at 2022-06-14 10:59:42.665134
# Unit test for function match
def test_match():
    assert match(Command('vagrant up',
                         "There are errors in the configuration of this machine. Please fix\nthe following errors and try again:\n\nvm:vm:* The following settings shouldn't exist: private_network"))
    assert not match(Command('vagrant up', 'Running provisioner: Vagrant::Provisioners::Puppet...'))



# Generated at 2022-06-14 10:59:46.816374
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('vagrant ssh') == 'vagrant up && vagrant ssh'
    assert get_new_command('vagrant ssh machine') == ['vagrant up machine && vagrant ssh machine', 'vagrant up && vagrant ssh machine']

# Generated at 2022-06-14 10:59:50.086672
# Unit test for function get_new_command
def test_get_new_command():
    from tests.utils import Command

    assert get_new_command(Command('vagrant ssh app1',
                                   'The machine with the name \'app1\' was not found configured for this Vagrant environment. Run `vagrant up` to create the machine.')) == 'vagrant up app1 && vagrant ssh app1'

    assert get_new_command(Command('vagrant ssh',
                                   'The machine with the name \'default\' was not found configured for this Vagrant environment. Run `vagrant up` to create the machine.')) == 'vagrant up && vagrant ssh'

# Generated at 2022-06-14 10:59:59.981927
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('vagrant ssh', '', '==> default: Machine is not up-to-date. Run `vagrant provision` to update it.')) == shell.and_(u"vagrant provision", u"vagrant ssh") # noqa
    assert get_new_command(Command('vagrant reload', '', '==> default: Machine is not up-to-date. Run `vagrant provision` to update it.')) == shell.and_(u"vagrant provision", u"vagrant reload") # noqa
    assert get_new_command(Command('vagrant status', '', 'The environment has not yet been created. Run `vagrant up` to create the environment.')) == [shell.and_(u"vagrant up", u"vagrant status")] # noqa

# Generated at 2022-06-14 11:00:07.647638
# Unit test for function get_new_command
def test_get_new_command():
    command_normal = Command('vagrant ssh', '')
    assert get_new_command(command_normal) == ['vagrant up; vagrant ssh',
                                               'vagrant up; vagrant ssh']

    command_with_machine = Command('vagrant ssh machine-name', '')
    assert get_new_command(command_with_machine) == ['vagrant up machine-name; vagrant ssh machine-name',
                                                     'vagrant up; vagrant ssh machine-name']

# Generated at 2022-06-14 11:00:14.408481
# Unit test for function get_new_command
def test_get_new_command():
    assert_equals("vagrant up && vagrant ssh", get_new_command("vagrant ssh"))
    assert_equals("vagrant up m1 && vagrant ssh m1", get_new_command("vagrant ssh m1"))

# Generated at 2022-06-14 11:00:19.706475
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('vagrant ssh', '')) == shell.and_(u"vagrant up", 'vagrant ssh')
    assert get_new_command(Command('vagrant ssh machine_name', '')) == [shell.and_(u"vagrant up machine_name", 'vagrant ssh machine_name'), shell.and_(u"vagrant up", 'vagrant ssh machine_name')]

# Generated at 2022-06-14 11:00:33.637709
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('vagrant ssh', "The machine with the name 'foo' was not found configured for this Vagrant environment. Run `vagrant up` to start this virtual machine.")) == "vagrant up && vagrant ssh"
    assert get_new_command(Command('vagrant ssh foo', "The machine with the name 'foo' was not found configured for this Vagrant environment. Run `vagrant up` to start this virtual machine.")) == ['vagrant up foo && vagrant ssh foo', 'vagrant up && vagrant ssh foo']
    assert get_new_command(Command('vagrant ssh bar', "The machine with the name 'bar' was not found configured for this Vagrant environment. Run `vagrant up` to start this virtual machine.")) == ['vagrant up bar && vagrant ssh bar', 'vagrant up && vagrant ssh bar']

# Generated at 2022-06-14 11:00:39.055920
# Unit test for function get_new_command
def test_get_new_command():
    # no machine name
    command_no_machine = Command('vagrant')
    assert get_new_command(command_no_machine) == [u'vagrant up && vagrant']

    # machine name
    command_machine = Command('vagrant ssh master')
    resulting_command = get_new_command(command_machine)
    assert resulting_command == [u'vagrant up master && vagrant ssh master',
                                 u'vagrant up && vagrant ssh master']

# Generated at 2022-06-14 11:00:48.741855
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("vagrant ssh default", "The virtual machine is not running. To start the machine, run `vagrant up`")
    assert get_new_command(command) == ['vagrant up', shell.and_("vagrant up", command.script)]

    command = Command("vagrant ssh", "The virtual machine is not running. To start the machine, run `vagrant up`")
    assert get_new_command(command) == ['vagrant up', shell.and_("vagrant up", command.script)]

    command = Command("vagrant ssh", "A `vagrant up` is required for use of this command.")
    assert get_new_command(command) == [shell.and_("vagrant up", command.script)]

# Generated at 2022-06-14 11:00:50.974693
# Unit test for function match

# Generated at 2022-06-14 11:00:57.213434
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.vagrant_up import get_new_command
    assert get_new_command("vagrant global-status") == 'vagrant global-status && vagrant up'
    assert get_new_command("vagrant global-status running") == ['vagrant global-status running && vagrant up running',
                                                                'vagrant global-status running && vagrant up']

# Generated at 2022-06-14 11:01:08.178314
# Unit test for function match
def test_match():
    output = (u'Vagrant could not detect VirtualBox! Make sure VirtualBox is'
              u' properly installed.\nVagrant uses the VBoxManage binary that'
              u' ships with VirtualBox, and requires this to be available on'
              u' the PATH. If VirtualBox is installed, please find the VBox'
              u'Manage binary and add it to the PATH environmental variable.'
              u'\n\nvagrant up\n\n')
    assert match((u'vagrant up', Command(u'vagrant up', output)))
    assert not match((u'vagrant ssh', Command(u'vagrant ssh', output)))


# Generated at 2022-06-14 11:01:11.553939
# Unit test for function get_new_command
def test_get_new_command():
    cmd = 'vagrant up foo'
    assert get_new_command(Command(cmd, '')) == ['vagrant up foo', 'vagrant up && vagrant up foo']



# Generated at 2022-06-14 11:01:17.722252
# Unit test for function get_new_command
def test_get_new_command():
    # test no machine
    assert get_new_command(Command("echo not_a_machine", "echo not_a_machine", "echo not_a_machine")) == ["vagrant up"]
    # test machine given
    assert get_new_command(Command("echo machine_test", "echo machine_test", "echo machine_test")) == ["vagrant up machine_test", "vagrant up"]

# Generated at 2022-06-14 11:01:30.909819
# Unit test for function match
def test_match():
    assert match(Command("vagrant ssh default",
                         "The SSH command responded with a non-zero exit status. Vagrant\nassumes that this means the command failed.\n\nStdout from the command:\n\n\nStderr from the command:\n\nssh_exchange_identification: read: Connection reset by peer\n\nA Vagrant environment or target machine is required to run this\ncommand. Run \"vagrant init\" to create a new Vagrant environment. Or,\nget an ID of a target machine from \"vagrant global-status\" to run\nthis command on. A final option is to change to a directory with a\nVagrantfile and to try again.\n")) is True


# Generated at 2022-06-14 11:01:37.680142
# Unit test for function get_new_command
def test_get_new_command():
    # Without machine argument
    assert get_new_command(u'vagrant ssh') == u'vagrant up && vagrant ssh'
    # With machine argument
    assert get_new_command(u'vagrant ssh machine1') == \
           [u'vagrant up machine1 && vagrant ssh machine1',
            u'vagrant up && vagrant ssh machine1']

# Generated at 2022-06-14 11:01:42.174319
# Unit test for function match
def test_match():
    script = Script(command='vagrant ssh', output='please run `vagrant up`')
    with patch('thefuck.rules.vagrant.is_enabled', return_value=True):
        assert match(script)



# Generated at 2022-06-14 11:01:46.539708
# Unit test for function match
def test_match():

    output = "The following SSH command responded with a non-zero exit status.\n\n"\
             "Vagrant assumes that this means the command failed!"

    assert match(Command('vagrant ssh', output))
    assert not match(Command('vagrant halt', output))



# Generated at 2022-06-14 11:01:58.942456
# Unit test for function get_new_command
def test_get_new_command():
    command = type('test', (object,), {'script_parts': ['vagrant', 'ssh', 'test1', 'test2'], 'script': 'test'})
    cmds = get_new_command(command)
    assert cmds == ['vagrant up test1; test', 'vagrant up; test']
    command = type('test', (object,), {'script_parts': ['vagrant', 'ssh', 'test1', 'test2'], 'script': 'test'})
    cmds = get_new_command(command)
    assert cmds == ['vagrant up test1; test', 'vagrant up; test']
    command = type('test', (object,), {'script_parts': ['vagrant', 'ssh', 'test1', 'test2', 'test3'], 'script': 'test'})
    cmd

# Generated at 2022-06-14 11:02:04.858581
# Unit test for function get_new_command
def test_get_new_command():
    cmd = Command('vagrant ssh', '', 'The VM is currently not running.')
    assert get_new_command(cmd) == 'vagrant up && vagrant ssh'
    cmd = Command('vagrant ssh node-1', '', 'The VM is currently not running.')
    assert get_new_command(cmd) == [u'vagrant up node-1 && vagrant ssh node-1', 'vagrant up && vagrant ssh node-1']

# Generated at 2022-06-14 11:02:09.371483
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("vagrant ssh") == [shell.and_(u"vagrant up", "vagrant ssh")]
    assert get_new_command("vagrant ssh mssql") == [shell.and_(u"vagrant up mssql", "vagrant ssh mssql"),
                                                    shell.and_(u"vagrant up", "vagrant ssh mssql")]

# Generated at 2022-06-14 11:02:17.324800
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("vagrant up",
        "The VM is currently powered off. To restart the VM, "
        "simply run `vagrant up`",
        "")) == shell.and_("vagrant up", "vagrant up")

    assert get_new_command(Command("vagrant up myvm",
        "The VM is currently powered off. To restart the VM, "
        "simply run `vagrant up`",
        "")) == ["vagrant up myvm && vagrant up myvm", "vagrant up && vagrant up"]


enabled_by_default = True

# Generated at 2022-06-14 11:02:18.954274
# Unit test for function match
def test_match():
    check_match(match, "vagrant up")



# Generated at 2022-06-14 11:02:22.899352
# Unit test for function match
def test_match():
    command = Command(script="",
        output="'default' machine doesn't exist. Please run `vagrant up` to create it.")
    assert match(command)



# Generated at 2022-06-14 11:02:35.140810
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('vagrant ssh', '')) == 'vagrant up && vagrant ssh'
    assert get_new_command(Command('vagrant ssh machine', '')) == ['vagrant up machine && vagrant ssh machine', 'vagrant up && vagrant ssh machine']
    assert get_new_command(Command('vagrant global-status', '')) == 'vagrant up && vagrant global-status'

# Generated at 2022-06-14 11:02:41.022546
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(u"vagrant ssh -c 'echo \"Hello\"' default") == [u'vagrant up default && vagrant ssh -c \'echo "Hello"\' default', u'vagrant up && vagrant ssh -c \'echo "Hello"\' default']
    assert get_new_command(u"vagrant ssh -c 'echo \"Hello\"'") == [u'vagrant up && vagrant ssh -c \'echo "Hello"\'']

# Generated at 2022-06-14 11:02:46.850117
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    assert get_new_command(Command('vagrant taint', '')) == [u"vagrant up && vagrant taint"]
    assert get_new_command(Command('vagrant taint machine', '')) == [u"vagrant up machine && vagrant taint machine", u"vagrant up && vagrant taint machine"]

# Generated at 2022-06-14 11:02:52.120388
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("vagrant ssh vagrant") == "vagrant up && vagrant ssh vagrant"
    assert get_new_command("vagrant ssh")[0] == "vagrant up vagrant && vagrant ssh"
    assert get_new_command("vagrant ssh")[1] == "vagrant up && vagrant ssh"


# Generated at 2022-06-14 11:02:58.059205
# Unit test for function match
def test_match():
	assert match(Command('vagrant ssh machine1', 'The virtual machine asked to be started for machine1, but it is not running and cannot be started because the provider does not support it. To fix this, use \"vagrant up\" to start this virtual machine.'))
	assert not match(Command('vagrant ssh machine1', 'stdin: is not a tty'))

# Generated at 2022-06-14 11:03:10.159958
# Unit test for function match
def test_match():
    assert (match(Command('vagrant ssh', '', '', '', None)))
    assert (match(Command('vagrant up', '', '', '', None)))
    assert (match(Command('vagrant status', '', '', '', None)))
    assert (match(Command('vagrant ssh master1', '', '', '', None)))
    assert (not match(Command('vagrant dest', '', '', '', None)))
    assert (not match(Command('vagrant not vagrant', '', '', '', None)))
    assert (not match(Command('vagrant ', '', '', '', None)))
    assert (not match(Command('vagrant', '', '', '', None)))
    assert (not match(Command('', '', '', '', None)))

# Generated at 2022-06-14 11:03:14.133540
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script = "vagrant destroy -f")
    assert get_new_command(command) == [u'vagrant up && vagrant destroy -f', u'vagrant up && vagrant destroy -f']


# Generated at 2022-06-14 11:03:18.428306
# Unit test for function get_new_command
def test_get_new_command():
    command = u"vagrant ssh --gui machine"
    assert get_new_command(Command(command, "")) == [u"vagrant up machine && vagrant ssh --gui machine",
                                               u"vagrant up && vagrant ssh --gui machine"]

# Generated at 2022-06-14 11:03:21.613589
# Unit test for function match
def test_match():
    assert match(Command('vagrant sh-config testbox',
                         ''))
    assert not match(Command('vagrant status',
                         ''))



# Generated at 2022-06-14 11:03:27.866968
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("vagrant ssh-config",
                      "The environment has not yet been created. Run \"vagrant up\" to create the environment.")
    assert get_new_command(command) == "vagrant up && vagrant ssh-config"

    command = Command("vagrant ssh-config app",
                      "The environment has not yet been created. Run \"vagrant up\" to create the environment.")
    assert get_new_command(command) == "vagrant up app && vagrant ssh-config app"

# Generated at 2022-06-14 11:03:36.689724
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('vagrant ssh', '', 'The VM must be running to open SSH connections.')) == 'vagrant up && vagrant ssh'
    assert get_new_command(Command('vagrant ssh machine', '', 'The VM must be running to open SSH connections.')) == ['vagrant up machine && vagrant ssh machine', 'vagrant up && vagrant ssh machine']

# Generated at 2022-06-14 11:03:42.144600
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.vagrant_up import get_new_command
    assert get_new_command(Command('vagrant ssh app1', '')) == [u'vagrant up app1 && vagrant ssh app1', u'vagrant up && vagrant ssh app1']
    assert get_new_command(Command('vagrant ssh', '')) == [u'vagrant up', u'vagrant ssh']

# Generated at 2022-06-14 11:03:44.996625
# Unit test for function match
def test_match():
    assert match(Command('vagrant ssh'))
    assert match(Command('vagrant rdp'))
    assert not match(Command('vagrant up'))


# Generated at 2022-06-14 11:03:49.967595
# Unit test for function get_new_command
def test_get_new_command():
    assert(get_new_command(Command('vagrant ssh host1', '', '', '', '')) ==
           [shell.and_(u"vagrant up host1", "vagrant ssh host1"),
            shell.and_(u"vagrant up ", "vagrant ssh host1")])


# Generated at 2022-06-14 11:03:55.131904
# Unit test for function match
def test_match():
    assert match(Command(script='vagrant init local/trusty',
                         stderr='The current directory is not a Vagrant-managed directory. Run `vagrant init` to create a new Vagrant environment for the current directory, or `vagrant up` to launch an environment for this project. Run `vagrant help` for more general help.'))



# Generated at 2022-06-14 11:04:06.949936
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('vagrant ssh box1', 'The box1 instance is not running. '
                                                 'Please run `vagrant up`')) == 'vagrant up && vagrant ssh box1'
    assert get_new_command(Command('vagrant ssh', 'The box1 instance is not running. '
                                                 'Please run `vagrant up`')) == 'vagrant up && vagrant ssh'
    assert get_new_command(Command('vagrant ssh box1', 'The box1 instance is not running. '
                                                 'Please run `vagrant up`')) == 'vagrant up && vagrant ssh box1'

# Generated at 2022-06-14 11:04:10.848822
# Unit test for function match
def test_match():
    assert match(Command("vagrant status",
                         u"==> default: VM not created. "
                         u"Run `vagrant up` to create it."))



# Generated at 2022-06-14 11:04:13.129375
# Unit test for function match
def test_match():
	cmd = Command('vagrant up', '')
	assert match(cmd)


# Generated at 2022-06-14 11:04:24.782691
# Unit test for function get_new_command
def test_get_new_command():
    from tests.utils import Command

    assert get_new_command(Command('vagrant status', output='some output')) \
           == u'vagrant up && vagrant status'
    assert get_new_command(Command('vagrant status', output='')) \
           == u'vagrant up && vagrant status'
    assert get_new_command(Command('vagrant status', output='some output')) \
           == u'vagrant up && vagrant status'
    assert get_new_command(Command('vagrant status machine', output='some output')) \
           == [u'vagrant up machine && vagrant status machine', u'vagrant up && vagrant status machine']

# Generated at 2022-06-14 11:04:28.435701
# Unit test for function get_new_command
def test_get_new_command():
    cmd = Command('vagrant ssh',
        'Machine does not appear to be running. Run `vagrant up` to start the machine if it is stopped.`',
        '', 1)

    assert get_new_command(cmd) == ['vagrant up && vagrant ssh',
        'vagrant up vm && vagrant ssh vm']


enabled_by_default = True

# Generated at 2022-06-14 11:04:43.423526
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('vagrant reload', 'The VM must be running to open SSH '
                      'connections. Run `vagrant up` to start the virtual '
                      'machine.')
    assert get_new_command(command) == ["vagrant up && vagrant reload",
                                        "vagrant up && vagrant reload"]

    command = Command('vagrant reload mach1', 'The VM must be running to open '
                      'SSH connections. Run `vagrant up` to start the '
                      'virtual machine.')
    assert get_new_command(command) == ['vagrant up mach1 && vagrant reload mach1',
                                        'vagrant up && vagrant reload mach1']


# Generated at 2022-06-14 11:04:51.738479
# Unit test for function match
def test_match():
    assert match(Command('vagrant provision', '', 'There are no active machines to run.\n\nRun `vagrant up` to create VMs.\n'))
    assert match(Command('vagrant provision', '', 'The machine is reported as not running.\n\nRun `vagrant up` to start the machine.'))
    assert match(Command('vagrant provision', '', 'There are no active machines to run.\n\nRun `vagrant up` to create VMs.'))


# Generated at 2022-06-14 11:04:59.968441
# Unit test for function get_new_command
def test_get_new_command():
    def run_match(match_input, expected, app_name="vagrant"):
        output = Command(match_input, "")
        output.app_name = app_name
        assert (get_new_command(output) == expected)

    run_match("vagrant ssh", "vagrant up && vagrant ssh")
    run_match("vagrant ssh www\"'1", "vagrant up www\"'1 && vagrant ssh www\"'1")
    run_match("vagrant ssh www1", [
        "vagrant up www1 && vagrant ssh www1",
        "vagrant up && vagrant ssh www1"])

# Generated at 2022-06-14 11:05:00.690693
# Unit test for function get_new_command

# Generated at 2022-06-14 11:05:07.380318
# Unit test for function get_new_command
def test_get_new_command():
    check_output = lambda x: 'thefuck: Did not detect \'vagrant up\' from the output'
    assert get_new_command(Command('vagrant ssh manchine',
                                   stderr=check_output)) == ['vagrant up manchine', 'vagrant ssh manchine']
    assert get_new_command(Command('vagrant ssh',
                                   stderr=check_output)) == ['vagrant up', 'vagrant ssh']

# Generated at 2022-06-14 11:05:10.957049
# Unit test for function match
def test_match():
    assert match(Command('vagrant ssh', '', 'There are no active machines for this project.')) == True
    assert match(Command('vagrant ssh', '', 'Active machines')) == False


# Generated at 2022-06-14 11:05:12.892605
# Unit test for function get_new_command
def test_get_new_command():
    assert shell.and_("vagrant up", "vagrant halt").script == "vagrant up && vagrant halt"


enabled_by_default = True

# Generated at 2022-06-14 11:05:17.967146
# Unit test for function match
def test_match():
    assert (match(
        Command('vagrant ssh machine -c "cd /vagrant/ && ls foo"',
                'The beginner needs to run `vagrant up` remastered to start this machine.')) ==
            True)



# Generated at 2022-06-14 11:05:23.702997
# Unit test for function match
def test_match():
    match_output = subprocess.Popen(['vagrant', 'reload', 'test-vm'], stdout=subprocess.PIPE)
    result = subprocess.check_output(['vagrant', 'status', 'test-vm'], stdin=match_output.stdout)
    assert match(Command("vagrant status test-vm", result))


# Generated at 2022-06-14 11:05:25.422455
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    assert (get_new_command(Command("vagrant ssh test", "", ""))
            == 'vagrant up test && vagrant ssh test')



# Generated at 2022-06-14 11:05:38.908114
# Unit test for function match
def test_match():
    assert match(Command('vagrant up',
                         'The following SSH command responded with a non-zero exit status.'))



# Generated at 2022-06-14 11:05:45.814808
# Unit test for function get_new_command
def test_get_new_command():
    output1 = 'The environment has not yet been created. Run `vagrant up` to create the environment.'
    output2 = 'The default provider (virtualbox) is not available for the current system.'

    # Test for 'vagrant ssh'
    command1 = Command('vagrant ssh', output1)
    assert get_new_command(command1) == 'vagrant up && vagrant ssh'

    # Test for 'vagrant ssh -h'
    command2 = Command('vagrant ssh -h', output1)
    assert get_new_command(command2) == 'vagrant up && vagrant ssh -h'

    # Test for 'vagrant ssh machine'
    command3 = Command('vagrant ssh machine', output1)

# Generated at 2022-06-14 11:05:48.936702
# Unit test for function get_new_command

# Generated at 2022-06-14 11:06:01.230038
# Unit test for function match

# Generated at 2022-06-14 11:06:03.444573
# Unit test for function match
def test_match():
    assert match(Command(script="vagrant ssh", stdout='no instance'))


# Generated at 2022-06-14 11:06:11.487536
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('vagrant ssh master', '')) == shell.and_(u"vagrant up", "vagrant ssh master")
    assert get_new_command(Command('vagrant ssh master -v', '')) == shell.and_(u"vagrant up", "vagrant ssh master -v")
    assert get_new_command(Command('vagrant ssh', '')) == [shell.and_(u"vagrant up", "vagrant ssh"), shell.and_(u"vagrant up", "vagrant ssh")]

# Generated at 2022-06-14 11:06:19.709899
# Unit test for function match
def test_match():
    assert match(Command('vagrant status', output='The maachind is not running'))
    assert match(Command('vagrant status', output="To create this machine, run `vagrant up`"))
    assert match(Command('vagrant status', output="To start this machine, run `vagrant up`"))
    assert match(Command('vagrant status', output="To resume this machine, run `vagrant up`"))
    assert match(Command('vagrant status', output="To initialize this machine's host-only network, run `vagrant up`"))
    assert match(Command('vagrant status', output="To reinitialize this machine's network, run `vagrant up`"))



# Generated at 2022-06-14 11:06:30.690984
# Unit test for function match
def test_match():
    assert match(Command('vagrant ssh', '''
Bringing machine 'default' up with 'virtualbox' provider...
A Vagrant environment or target machine is required to run this
command. Run `vagrant init` to create a new Vagrant environment. Or,
get an ID of a target machine from `vagrant global-status` to run
this command on. A final option is to change to a directory with a
Vagrantfile and to try again.
'''))

# Generated at 2022-06-14 11:06:43.840996
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("vagrant ssh", "Host machine isn't running. To start the machine, run `vagrant up`.",
                                   "vagrant")[0]) == [shell.and_("vagrant up", "vagrant ssh"),
                                                       shell.and_("vagrant up", "vagrant ssh")]
    assert get_new_command(Command("vagrant ssh web", "Host machine isn't running. To start the machine, run `vagrant up`.",
                                   "vagrant")[0]) == [shell.and_("vagrant up web", "vagrant ssh web"),
                                                       shell.and_("vagrant up", "vagrant ssh web")]

# Generated at 2022-06-14 11:06:48.062130
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("vagrant status --machine-readable") == 'vagrant up && vagrant status --machine-readable'
    assert get_new_command("vagrant status default --machine-readable") == 'vagrant up default && vagrant status default --machine-readable'

# Generated at 2022-06-14 11:07:18.991077
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

    assert get_new_command(Command('vagrant ssh', '', 'Machine not created')) == shell.and_('vagrant up', 'vagrant ssh')
    assert get_new_command(Command('vagrant ssh machinename', '', 'Machine not created')) == [shell.and_('vagrant up machinename', 'vagrant ssh machinename'), shell.and_('vagrant up', 'vagrant ssh machinename')]

# Generated at 2022-06-14 11:07:24.717462
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('fig build')) == shell.and_(u"vagrant up",
                                                               "fig build")
    assert get_new_command(Command('fig build atlantis')) == [
        shell.and_(u"vagrant up atlantis", "fig build atlantis"),
        shell.and_(u"vagrant up", "fig build atlantis")]

# Generated at 2022-06-14 11:07:34.742677
# Unit test for function match
def test_match():
    assert match(Command('vagrant ssh-config',
                         output=u"""There are errors in the configuration of this machine. Please fix
the following errors and try again:

vm:
* The box 'ubuntu/trusty64' could not be found.

A box specified with `config.vm.box` could not be found. Make sure the box
exists and is properly spelled. Also, if the box is located in a
non-standard location, make sure the proper box path is specified with
`config.vm.box_url`.

Run `vagrant up` to start your virtual machine.""",
                         ))
    assert not match(Command('vagrant ssh-config', output=u'''no vagrant instances'''))
    assert not match(Command(''))

