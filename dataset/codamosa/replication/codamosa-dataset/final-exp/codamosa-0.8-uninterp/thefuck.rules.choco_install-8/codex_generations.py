

# Generated at 2022-06-14 09:30:08.138490
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("choco install git",
                                   "Chocolatey v0.10.8\nInstalling the following packages:\ngit.install by chocolatey (v2.9.0) [Approved]\n  git.install package files install completed. Performing other installation steps.\n  The package git.install wants to run 'chocolateyInstall.ps1'.\n  Note: If you don't run this script, the installation will fail.\n  Note: To confirm automatically next time, use '-y' or consider setting 'allowGlobalConfirmation'. Run 'choco feature enable -n=allowGlobalConfirmation'\n  Do you want to run the script?([Y]es/[N]o/[P]rint): Y\n  Running choc...")) == \
           "choco install git.install"

# Generated at 2022-06-14 09:30:16.406243
# Unit test for function match
def test_match():
    from tests.tools import assert_equals
    assert_equals(match(Command('choco install chocolatey', '', 'Chocolatey v0.10.11')), False)
    assert_equals(match(Command('cinst chocolatey', '', 'Chocolatey v0.10.11')), False)
    assert_equals(match(Command('choco install chocolatey -y', '', 'Installing the following packages:')), True)
    assert_equals(match(Command('cinst chocolatey -y', '', 'Installing the following packages:')), True)



# Generated at 2022-06-14 09:30:21.792348
# Unit test for function get_new_command
def test_get_new_command():
    result = get_new_command(Command('choco install foo bar', ''))
    assert result == "choco install foo.install bar"

    result = get_new_command(Command('cinst foo bar', ''))
    assert result == "cinst foo.install bar"

# Generated at 2022-06-14 09:30:23.956755
# Unit test for function match
def test_match():
    assert match(Command('choco install chocolatey', 'Installing the following packages', ''))



# Generated at 2022-06-14 09:30:26.094611
# Unit test for function match
def test_match():
    command = Command('choco install chocolatey')
    assert match(command)


# Generated at 2022-06-14 09:30:33.036980
# Unit test for function match
def test_match():
    assert match(Command('choco install git -y'))
    assert match(Command('cinst git -y'))
    assert match(Command('choco install git'))
    assert match(Command('cinst git'))
    assert not match(Command('choco install --help'))
    assert not match(Command('cinst --help'))



# Generated at 2022-06-14 09:30:35.142646
# Unit test for function match
def test_match():
    command = Command('choco install python', "")
    assert match(command)



# Generated at 2022-06-14 09:30:44.348761
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('choco install chocolatey', '')) == 'choco install chocolatey.install'
    assert get_new_command(Command('cinst chocolatey', '')) == 'cinst chocolatey.install'
    assert get_new_command(Command('cinst chocolatey -y', '')) == 'cinst chocolatey.install -y'
    assert get_new_command(Command('cinst chocolatey -version 0.10.8', '')) == 'cinst chocolatey.install -version 0.10.8'

# Generated at 2022-06-14 09:30:51.704951
# Unit test for function match
def test_match():
    assert match(Command('choco install test', 'test', 'test'))
    assert match(Command('cinst test', 'test', 'test'))
    assert not match(Command('choco install test', 'test', ''))
    assert not match(Command('cinst test', 'test', 'test', ''))



# Generated at 2022-06-14 09:30:53.829996
# Unit test for function match
def test_match():
    # choco - install
    assert match(Command("cinst foo"))
    # choco install
    assert match(Command("choco install foo"))


# Generated at 2022-06-14 09:31:00.502424
# Unit test for function match
def test_match():
    assert (
        match(Command("choco install go -y"))
        is True
    ), "match should return True when it's a case of missing .install extension"
    assert (
        match(Command("choco install go -y"))
        is True
    ), "match should return True when it's a case of missing .install extension"
    assert (
        match(Command(
            "cinst go -y"
        )) is True
    ), "match should return True when it's a case of missing .install extension"
    assert (
        match(Command(
            "choco install go -y")) is True
    ), "match should return True when it's a case of missing .install extension"

# Generated at 2022-06-14 09:31:07.519448
# Unit test for function get_new_command
def test_get_new_command():
    # Check that unknown package behaves as usual
    assert get_new_command('choco install not-a-package') == 'choco install not-a-package.install'

    # Check that a known package is ignored
    assert get_new_command('choco install git') == 'choco install git'

    # Check that a known package is ignored
    assert get_new_command('cinst git') == 'cinst git'

# Generated at 2022-06-14 09:31:12.611845
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("choco install ruby") == "choco install ruby.install"
    assert get_new_command("cinst ruby") == "cinst ruby.install"

# Generated at 2022-06-14 09:31:23.253240
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('choco install r', 'not found')) == 'choco install r.install'
    assert get_new_command(Command('cinst r', 'not found')) == 'cinst r.install'
    assert get_new_command(Command('choco install notepad++', 'not found')) == 'choco install notepad++.install'
    assert get_new_command(Command('cinst notepad++', 'not found')) == 'cinst notepad++.install'

# Generated at 2022-06-14 09:31:32.389593
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script='choco install git.install',
                                   output='Installing the following packages:\r\n  git.install')) == 'choco install git.install.install'
    assert get_new_command(Command(script='cinst git.install -y',
                                   output='Installing the following packages:\r\n  git.install')) == 'cinst git.install.install -y'
    assert get_new_command(Command(script='cinst git.install',
                                   output='Installing the following packages:\r\n  git.install')) == 'cinst git.install.install'

# Generated at 2022-06-14 09:31:36.720772
# Unit test for function match
def test_match():
    assert match(Command(script="choco install cinst"))
    assert match(Command(script="cinst nodejs.install"))
    assert not match(Command(script="choco uninstall cinst"))
    assert not match(Command(script="cinst nodejs.uninstall"))



# Generated at 2022-06-14 09:31:47.357519
# Unit test for function match
def test_match():
    """
    Ensure that the match function in this module returns True/False correctly
    based on the input.
    """
    assert (
        match(Command("choco install chocolatey"))
        == True
    ), "Test failed in function match() (1)"
    assert (
        match(Command("cinst chocolatey"))
        == True
    ), "Test failed in function match() (2)"
    assert (
        match(Command("choco install --noop chocolatey"))
        == True
    ), "Test failed in function match() (3)"
    assert (
        match(Command("choco search chocolatey"))
        == False
    ), "Test failed in function match() (4)"


# Generated at 2022-06-14 09:32:01.012874
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.chocolatey import get_new_command
    from thefuck.types import Command

    command = Command('choco install chocolatey', 'Installing the following packages:\nchocolatey v0.9.9.11', '')
    assert get_new_command(command) == 'choco install chocolatey.install'

    command = Command('choco install chocolatey', 'Installing the following packages:\nchocolatey v0.9.9.11', '', 'chocolatey')
    assert get_new_command(command) == 'choco install chocolatey.install'

    command = Command('cinst chocolatey', 'Installing the following packages:\nchocolatey v0.9.9.11', '')
    assert get_new_command(command) == 'cinst chocolatey.install'


# Generated at 2022-06-14 09:32:09.379947
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("cinst nodejs.install -y")) == 'cinst nodejs -y'
    assert get_new_command(Command("choco install chocolatey -y")) == 'choco install chocolatey.install -y'
    assert get_new_command(Command("cinst hello")) == 'cinst hello.install'
    assert get_new_command(Command("cinst hello -y")) == 'cinst hello.install -y'
    assert get_new_command(Command("choco install hello -y")) == 'choco install hello.install -y'
    assert get_new_command(Command("cinst hello world -y")) == 'cinst hello world -y'
    assert get_new_command(Command("choco install hello world -y")) == 'choco install hello world -y'
    assert get_

# Generated at 2022-06-14 09:32:19.555416
# Unit test for function match
def test_match():
    assert match(Command("choco install foo")) is True
    assert match(Command('choco install foo bar')) is True
    assert match(Command('cinst foo bar')) is True
    assert match(Command('choco install foo bar --params="baz"')) is True
    assert match(Command('choco install foo bar -params="baz"')) is True
    assert match(Command('choco install foo bar -p="baz"')) is True
    assert match(Command('choco install foo bar -source="baz"')) is True
    assert match(Command('choco install foo bar -s="baz"')) is True
    assert match(Command('choco install foo bar -s="baz" -y')) is True
    assert match(Command('choco install foo bar -ignorechecksum=true')) is True
    assert match

# Generated at 2022-06-14 09:32:30.123473
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("choco install firefox", "")
    assert get_new_command(command) == "choco install firefox.install"

# Generated at 2022-06-14 09:32:33.915840
# Unit test for function get_new_command
def test_get_new_command():
    script = "find . | xargs choco install -y testapp"
    command = Command(script, "Installing the following packages: \ntestapp")
    assert get_new_command(command) == script.replace("testapp", "testapp.install")

# Generated at 2022-06-14 09:32:45.769084
# Unit test for function get_new_command
def test_get_new_command():
    cmd = Command(script='choco install packagename moo',
        stdout=None, stderr=None, env=None)
    assert get_new_command(
        cmd) == cmd.script.replace('packagename', 'packagename.install')

    cmd2 = Command(script='choco install packagename.install moo',
        stdout=None, stderr=None, env=None)
    assert get_new_command(cmd2) == []

    cmd3 = Command(script='cinst packagename moo',
        stdout=None, stderr=None, env=None)
    assert get_new_command(
        cmd3) == cmd3.script.replace('packagename', 'packagename.install')

# Generated at 2022-06-14 09:32:49.338172
# Unit test for function match
def test_match():
    assert match(Command("choco install chocolatey", "", "Installing the following packages"))
    assert not match(Command("choco install chocolatey", "", "Not the error msg you're looking for"))



# Generated at 2022-06-14 09:33:02.165437
# Unit test for function match

# Generated at 2022-06-14 09:33:08.955091
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("choco install nodejs", "")) == "choco install nodejs.install"
    assert get_new_command(Command("cinst nodejs", "")) == "cinst nodejs.install"
    assert get_new_command(Command("choco install nodejs.install -y", "")) == "choco install nodejs.install.install -y"
    assert get_new_command(Command(
        "choco install https://github.com/chocolatey/choco/archive/1.8.0.zip",
        "")) == "choco install https://github.com/chocolatey/choco/archive/1.8.0.zip.install"
    assert get_new_command(Command("choco install nodejs -y", "")) == "choco install nodejs.install -y"

# Generated at 2022-06-14 09:33:12.537909
# Unit test for function match
def test_match():
    assert match(Command('choco install git'))
    assert match(Command('cinst git'))
    assert not match(Command('choco upgrade git'))



# Generated at 2022-06-14 09:33:23.147907
# Unit test for function match
def test_match():
    assert match(Command('choco install something'))
    assert match(Command('cinst something'))
    assert match(Command('cinst something else'))
    assert match(Command('cinst something-else'))
    assert match(Command('cinst something-else --switch'))
    assert match(Command('cinst something-else --switch=param'))
    assert not match(Command('cinst something-else --switch="param=value"'))
    assert match(Command('choco install something -y'))
    assert match(Command('cinst something -y'))
    assert match(Command('cinst something\\else'))
    assert match(Command('cinst something\\else -y'))
    assert not match(Command('cinst something-else=param'))

# Generated at 2022-06-14 09:33:35.302226
# Unit test for function match
def test_match():
    assert match(Command('choco install --force something'))
    assert match(Command('choco install something'))
    assert match(Command('cinst i something'))
    assert match(Command('cinst something'))
    assert match(Command('choco install --version=1.0.0 something'))
    assert match(Command('cinst --version=1.0.0 something'))
    assert match(Command('cinst --version=1.0.0 something --yes'))
    assert match(Command('choco install -y something'))
    assert match(Command('choco install something --source="https://chocolatey.org/"'))
    assert match(Command('cinst something -source="https://chocolatey.org/"'))

# Generated at 2022-06-14 09:33:43.618011
# Unit test for function match
def test_match():
    assert match(Command('choco install chocolatey',
        'Installing the following packages:\nchocolatey\nBy installing you accept licenses for the packages.',
        '', 127))
    assert match(Command('choco install python -y',
        "Chocolatey v0.10.9\nInstalling the following packages:\n"
        "python\nBy installing you accept licenses for the packages.", '', 127))
    assert match(Command('cinst python -y',
        "Chocolatey v0.10.9\nInstalling the following packages:\n"
        "python\nBy installing you accept licenses for the packages.", '', 127))



# Generated at 2022-06-14 09:33:59.695796
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command("choco install chocolatey")
            == "choco install chocolatey.install")
    assert (get_new_command("cinst chocolatey")
            == "cinst chocolatey.install")

# Generated at 2022-06-14 09:34:10.120311
# Unit test for function match
def test_match():
    # `choco install` command that has failed
    assert match(Command("choco install packagename", "failed message"))
    # `cinst` command that has failed
    assert match(Command("cinst packagename", "failed message"))
    # `choco install` command that has succeeded
    assert not match(Command("choco install packagename", "success message"))
    # `choco subcommand` command that failed
    assert not match(Command("choco search packagename", "failed message"))
    # `choco install` command that uses `-Source` param
    assert match(Command("choco install packagenameSource", "failed message"))

# Generated at 2022-06-14 09:34:16.780177
# Unit test for function match

# Generated at 2022-06-14 09:34:20.876457
# Unit test for function match
def test_match():
    cmd = Command('choco install atom')
    output = 'Installing the following packages:'
    assert match(cmd, output)
    cmd = Command('cinst atom')
    assert match(cmd, output)


# Generated at 2022-06-14 09:34:31.589541
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(\
        script='cinst python python2 python3',\
        output='Installing the following packages:\n'\
               'python python2 python3\n'\
               '[Installation] Success\n')) == 'cinst python.install python2 python3'

    assert get_new_command(Command(\
        script='cinst "python" "python2" "python3"',\
        output='Installing the following packages:\n'\
               'python python2 python3\n'\
               '[Installation] Success\n')) == 'cinst "python".install "python2" "python3"'


# Generated at 2022-06-14 09:34:44.491251
# Unit test for function get_new_command

# Generated at 2022-06-14 09:34:50.869744
# Unit test for function get_new_command
def test_get_new_command():
    from tests.utils import Command

    assert get_new_command(Command("choco install cinst", """""")) == "choco install cinst.install"
    assert get_new_command(Command("cinst curl", """""")) == "cinst curl.install"

    assert get_new_command(Command("choco install cinst.install", """""")) == []

# Generated at 2022-06-14 09:35:02.404650
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('choco install python', '')
    assert get_new_command(command) == 'choco install python.install'
    command = Command('cinst python', '')
    assert get_new_command(command) == 'cinst python.install'
    command = Command('cinst python -y', '')
    assert get_new_command(command) == 'cinst python.install -y'
    command = Command('cinst python --unattended', '')
    assert get_new_command(command) == 'cinst python.install --unattended'
    command = Command('cinst python --yes', '')
    assert get_new_command(command) == 'cinst python.install --yes'

# Generated at 2022-06-14 09:35:05.498667
# Unit test for function match
def test_match():
    command = Command('choco install list')
    assert match(command)
    assert not match(Command('choco install test'))



# Generated at 2022-06-14 09:35:09.878112
# Unit test for function match
def test_match():
    """Unit test for function match."""
    assert match(Command("choco install one, two, three", "", "Installing the following packages:"))
    assert match(Command("cinst one, two, three", "", "Installing the following packages:"))



# Generated at 2022-06-14 09:35:40.743716
# Unit test for function match
def test_match():
    assert match(Command('cinst chocolatey', ''))
    assert match(Command('choco install chocolatey', 'Installing the following packages'))
    assert not match(Command('choco install chocolatey', ''))
    assert not match(Command('cinst chocolatey', 'Installing the following packages'))


# Generated at 2022-06-14 09:35:51.834938
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('choco install chocolatey', '')) == 'choco install chocolatey.install'
    assert get_new_command(Command('cinst chocolatey', '')) == 'cinst chocolatey.install'
    assert get_new_command(Command('choco install chocolatey -params', '')) == 'choco install chocolatey.install -params'
    assert get_new_command(Command('choco install chocolatey -params', '')) == 'choco install chocolatey.install -params'
    assert get_new_command(Command('choco install chocolatey -params=1', '')) == 'choco install chocolatey.install -params=1'
    assert get_new_command(Command('choco install chocolatey -params /switch', '')) == 'choco install chocolatey.install -params /switch'

# Generated at 2022-06-14 09:35:54.972567
# Unit test for function match
def test_match():
    assert match(Command("choco install chocolatey", "", ""))
    assert match(Command("cinst chocolatey", "", ""))



# Generated at 2022-06-14 09:36:00.766525
# Unit test for function get_new_command
def test_get_new_command():
    # Check that we have no error if the argument is already correct
    # This is used in unit test for correct build of the environment
    assert get_new_command(Command("choco install tortoisegit",
                                   "choco install tortoisegit\nInstalling the following packages:\ntortoisegit\nBy installing you accept licenses for the packages.")) == "choco install tortoisegit.install"
    # Test only the package name is capitalized
    assert get_new_command(Command("choco install tortoisegit mypackage",
                                   "choco install tortoisegit mypackage\nInstalling the following packages:\ntortoisegit mypackage\nBy installing you accept licenses for the packages.")) == "choco install tortoisegit.install mypackage"

    # Test several packages

# Generated at 2022-06-14 09:36:05.649731
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    script_parts = ["choco", "install", "-y", "git"]
    command = Command(script_parts, '', '')
    output = get_new_command(command)
    
    assert output == 'choco install -y git.install'

# Generated at 2022-06-14 09:36:12.343044
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('cinst foobar', '', 'Installing the following packages:', '')) == 'cinst foobar.install'
    assert get_new_command(Command('cinst foobar -y', '', 'Installing the following packages:', '')) == 'cinst foobar.install -y'
    assert get_new_command(Command('cinst -y foobar', '', 'Installing the following packages:', '')) == 'cinst -y foobar.install'
    assert get_new_command(Command('choco install foobar', '', 'Installing the following packages:', '')) == 'choco install foobar.install'

# Generated at 2022-06-14 09:36:23.660714
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.chocolatey import get_new_command

    command = Command("choco install googlechrome", "Installing the following packages",
                      "googlechrome already installed.\n"
                      "  googlechrome v8.0.552.225\n")
    assert get_new_command(command) == "choco install googlechrome.install"

    command = Command("cinst googlechrome", "Installing the following packages",
                      "googlechrome already installed.\n"
                      "  googlechrome v8.0.552.225\n")
    assert get_new_command(command) == "cinst googlechrome.install"

    command = Command("cinst googlechrome -y", "Installing the following packages",
                      "googlechrome already installed.\n"
                      "  googlechrome v8.0.552.225\n")


# Generated at 2022-06-14 09:36:29.782242
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('choco install jre8 -y',
    	'Installing the following packages:jre8\n'
        'By installing you accept licenses for the packages.\n'
        'Progress: Downloading ')) == 'choco install jre8.install -y'
    assert get_new_command(Command('cinst jre8 -y',
    	'Installing the following packages:jre8\n'
        'By installing you accept licenses for the packages.\n'
        'Progress: Downloading ')) == 'cinst jre8.install -y'

# Generated at 2022-06-14 09:36:41.761517
# Unit test for function match
def test_match():
    assert match(Command("choco install lsd"))
    assert match(Command("cinst lsd"))
    assert match(Command("cinst -source abc lsd"))
    assert match(Command("cinst -y lsd"))
    assert match(Command("cinst -whatif lsd"))
    assert match(Command("choco install --pre lsd"))
    assert match(Command("cinst -pre lsd"))
    assert match(Command("choco install --prerelease lsd"))
    assert match(Command("cinst -pre lsd"))
    assert not match(Command("lsd"))
    assert not match(Command("choco install lsd --package-parameters=silent"))
    assert not match(Command("cinst -package-parameters=silent lsd"))

# Generated at 2022-06-14 09:36:52.221108
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('choco install foo bar')) == 'choco install foo.install bar'
    assert get_new_command(Command('choco install foo bar baz')) == 'choco install foo.install bar baz'
    assert get_new_command(Command('cinst foo bar')) == 'cinst foo.install bar'
    assert get_new_command(Command('cinst foo bar baz')) == 'cinst foo.install bar baz'
    # Double check a prefix
    assert get_new_command(Command('cinst foo.bar baz')) == 'cinst foo.bar baz'

# Generated at 2022-06-14 09:37:52.037291
# Unit test for function get_new_command
def test_get_new_command():
    from tests.utils import Command
    # basic test
    command = Command("yay")
    assert get_new_command(command) == "yay.install"
    # basic test with spaces
    command = Command('echo "yay"')
    assert get_new_command(command) == 'echo "yay.install"'
    # basic test with spaces and quotes
    command = Command("echo 'yay'")
    assert get_new_command(command) == "echo 'yay.install'"
    # test with parameters
    command = Command("yay /s --force")
    assert get_new_command(command) == "yay.install /s --force"
    # test with other subcommands
    command = Command("choco uninstall yay")

# Generated at 2022-06-14 09:38:01.670867
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('choco install test', '', 'ERROR: The package was not found with the source(s) listed.\nIf you specified a particular version and are receiving this message, it is possible that the package name exists but the version does not.')) == 'choco install test.install'
    assert get_new_command(Command('choco install -y test', '', 'ERROR: The package was not found with the source(s) listed.\nIf you specified a particular version and are receiving this message, it is possible that the package name exists but the version does not.')) == 'choco install -y test.install'

# Generated at 2022-06-14 09:38:11.715686
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('cinst choco', 'Chocolatey v0.10.15', 'Installing the following packages:')) == "cinst choco.install"
    assert get_new_command(Command('cinst choco', 'Chocolatey v0.10.15', 'Installing the following packages:')) == "cinst choco.install"
    assert get_new_command(Command('cinst choco', 'Chocolatey v0.10.15', 'Installing the following packages:')) == "cinst choco.install"
    assert get_new_command(Command('cinst choco', 'Chocolatey v0.10.15', 'Installing the following packages:')) == "cinst choco.install"

# Generated at 2022-06-14 09:38:15.599747
# Unit test for function get_new_command
def test_get_new_command():
    from tests.utils import Command

    assert get_new_command(Command('cinst python')) == 'cinst python.install'
    assert get_new_command(Command('python.install')) == []

# Generated at 2022-06-14 09:38:20.338135
# Unit test for function match
def test_match():
    assert match(Command('choco install foo', '', '', 'Installing the following packages', 1))
    assert match(Command('cinst foo', '', '', 'Installing the following packages', 1))
    assert not match(Command('cinst foo', '', '', 'Foo installed', 1))



# Generated at 2022-06-14 09:38:33.522934
# Unit test for function get_new_command
def test_get_new_command():
    from tests.utils import Command
    assert get_new_command(Command("choco install git")) == "choco install git.install"
    assert get_new_command(Command("cinst git")) == "cinst git.install"
    assert get_new_command(Command("choco install git -y")) == "choco install git.install -y"
    assert get_new_command(Command("cinst git -y")) == "cinst git.install -y"
    assert get_new_command(Command("choco install git.reduced /pre")) == "choco install git.reduced.install /pre"
    assert get_new_command(Command("choco install git.reduced=1.2.3 /pre")) == "choco install git.reduced.install /pre"

# Generated at 2022-06-14 09:38:39.568500
# Unit test for function match
def test_match():
    assert match(Command('choco install foo',
        output='Installing the following packages:foo'))
    assert match(Command('cinst foo', output='Installing the following packages:foo'))
    assert not match(Command('choco install foo',
        output='Installing the following packages:what'))
    assert not match(Command('cinst foo', output='Installing the following packages:what'))



# Generated at 2022-06-14 09:38:43.034141
# Unit test for function get_new_command
def test_get_new_command():
    # function get_new_command returns a string
    assert isinstance(get_new_command(Command('ls', 'ls')), str)

# Generated at 2022-06-14 09:38:47.920879
# Unit test for function get_new_command
def test_get_new_command():
    output = 'Installing the following packages: package'
    command = MagicMock(script='choco install package',
                        script_parts=['choco', 'install', 'package'],
                        output=output)
    assert get_new_command(command) == 'choco install package.install'

# Generated at 2022-06-14 09:38:52.233177
# Unit test for function match
def test_match():
    assert not match(Command('choco upgrade htop', '', '', '', ''))
    assert match(Command('choco install htop', '', '', '', ''))
    assert match(Command('cinst htop', '', '', '', ''))



# Generated at 2022-06-14 09:39:58.720849
# Unit test for function get_new_command
def test_get_new_command():
    # Positive
    assert get_new_command(Command('cinst notepadplusplus', '', '')) == 'cinst notepadplusplus.install'
    assert get_new_command(Command('cinst notepadplusplus.install', '', '')) == 'cinst notepadplusplus.install.install'
    assert get_new_command(Command('cinst notepadplusplus.install -y', '', '')) == 'cinst notepadplusplus.install.install -y'
    assert get_new_command(Command('cinst notepadplusplus -y', '', '')) == 'cinst notepadplusplus.install -y'
    assert get_new_command(Command('cinst notepadplusplus -source test -y', '', '')) == 'cinst notepadplusplus.install -source test -y'