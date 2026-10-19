

# Generated at 2022-06-14 09:30:00.499347
# Unit test for function match
def test_match():
    assert match(Command('cinst test -y', ''))
    assert match(Command(script='choco install test -y', output='Installing the following packages:'))
    assert not match(Command('cinst test -y', 'Installing the following packages:'))
    assert not match(Command('cinst test -y', ''))

# Generated at 2022-06-14 09:30:10.523937
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("choco install choco", "", "")) == "choco install choco.install"
    assert get_new_command(Command(
        "choco install choco -y",
        "",
        ""
    )) == "choco install choco.install -y"
    assert get_new_command(Command(
        "choco install choco -m",
        "",
        ""
    )) == "choco install choco.install -m"
    assert get_new_command(Command(
        "cinst choco",
        "",
        ""
    )) == "cinst choco.install"

# Generated at 2022-06-14 09:30:21.822302
# Unit test for function get_new_command
def test_get_new_command():
    # assume package is named "choco"
    command = Command("choco install choco")
    assert get_new_command(command) == "choco install choco.install"
    # assume package is named "cinst"
    command = Command("choco install cinst")
    assert get_new_command(command) == "choco install cinst.install"
    # assume package is named "git.install"
    command = Command("choco install git.install")
    assert get_new_command(command) == "choco install git.install.install"

    # assume package is named "choco"
    command = Command("cinst choco")
    assert get_new_command(command) == "cinst choco.install"
    # assume package is named "cinst"
    command = Command("cinst cinst")


# Generated at 2022-06-14 09:30:28.909573
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('choco install vcredist2015', '', '')
    new_command = get_new_command(command)
    assert new_command == 'choco install vcredist2015.install'

    command = Command('cinst vcredist2015', '', '')
    new_command = get_new_command(command)
    assert new_command == 'cinst vcredist2015.install'

    command = Command('choco install --params "\"/InstallDir:C:\\\\Program Files\\\\Foobar\"" foobar', '', '')
    new_command = get_new_command(command)
    assert new_command == 'choco install --params "\"/InstallDir:C:\\\\Program Files\\\\Foobar\"" foobar.install'


# Generated at 2022-06-14 09:30:39.892573
# Unit test for function match
def test_match():
    assert match(Command('choco install foobar', '', '', 0, '', ''))
    assert match(Command('cinst foobar', '', '', 0, '', ''))
    assert match(Command('myChocoInstall', '', '', 0, '', ''))
    assert match(Command('choco install -y foobar', '', '', 0, '', ''))
    assert match(Command('cinst -y foobar', '', '', 0, '', ''))
    assert not match(Command('choco uninstall foobar', '', '', 0, '', ''))
    assert not match(Command('cuninst foobar', '', '', 0, '', ''))
    assert not match(Command('choco install --y foobar', '', '', 0, '', ''))

# Generated at 2022-06-14 09:30:47.025301
# Unit test for function match
def test_match():
    # 1
    command = Command("choco install package", "")
    assert match(command)

    # 2
    command = Command("choco install package --yes", "")
    assert match(command)

    # 3
    command = Command("choco install package --yes -s", "")
    assert match(command)

    # 4
    command = Command("cinst package", "")
    assert match(command)

    # 5
    command = Command(
        "sudo cinst package --yes", "Installing the following packages:"
    )
    assert match(command)



# Generated at 2022-06-14 09:30:57.979231
# Unit test for function get_new_command
def test_get_new_command():
    try:
        from unittest.mock import Mock
        command = Mock()
        command.script_parts = ["choco", "install", "chocolatey", "--force"]
        command.output = "Installing the following packages:\nchocolatey\nBy installing"
        new_command = get_new_command(command)
        assert new_command == "choco install chocolatey.install --force"
    except ModuleNotFoundError:
        print("unittest.mock was not installed, aborting test of get_new_command")

# Generated at 2022-06-14 09:31:08.277736
# Unit test for function match
def test_match():
    output = "Installing the following packages:"
    assert match(Command('choco install --', stderr=output))
    assert match(Command('choco install --', output=output))
    assert match(Command('cinst -y --', stderr=output))
    assert match(Command('cinst -y --', output=output))

    assert not match(Command('choco install --', stderr="Text not matching"))
    assert not match(Command('choco install --', output="Text not matching"))
    assert not match(Command('cinst -y --', stderr="Text not matching"))
    assert not match(Command('cinst -y --', output="Text not matching"))


# Generated at 2022-06-14 09:31:12.612356
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script="choco install notepadplusplus")) == "choco install notepadplusplus.install"

# Generated at 2022-06-14 09:31:17.637886
# Unit test for function get_new_command
def test_get_new_command():
    assert (get_new_command(Command("choco install atom"))
            == "choco install atom.install")
    assert (get_new_command(Command("choco install atom -s"))
            == "choco install atom.install -s")
    assert get_new_command(Command("choco list")) == []
    assert get_new_command(Command("atom")) == []
    assert (get_new_command(Command("cinst atom"))
            == "cinst atom.install")
    assert (get_new_command(Command("cinst atom -y"))
            == "cinst atom.install -y")

# Generated at 2022-06-14 09:31:26.999184
# Unit test for function match
def test_match():
    assert match(Command("choco install  notepadplusplus", "", ""))
    assert not match(Command("choco uninstall  notepadplusplus", "", ""))
    assert not match(Command("cinst notepadplusplus", "", ""))



# Generated at 2022-06-14 09:31:34.669590
# Unit test for function get_new_command
def test_get_new_command():
    test_command = Command("choco install somepackage -y")
    assert get_new_command(test_command) == "choco install somepackage.install -y"
    test_command_two = Command("cinst somepackage2 -y")
    assert get_new_command(test_command_two) == "cinst somepackage2.install -y"

# Generated at 2022-06-14 09:31:39.703401
# Unit test for function match
def test_match():
    assert match(Command('choco install xmllint'))
    assert not match(Command('choco install xmllint', 'Note: '))
    assert not match(Command('choco install xmllint', 'The package xmllint was not found'))



# Generated at 2022-06-14 09:31:43.571978
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('cinst clean-dirs.install', 'Please specify a package to install')
    new_command = get_new_command(command)

    assert new_command == 'cinst clean-dirs.install'

# Generated at 2022-06-14 09:31:47.275222
# Unit test for function get_new_command

# Generated at 2022-06-14 09:31:53.582595
# Unit test for function match
def test_match():
    assert match(Command("choco install fx")), "Should match 'choco install'"
    assert match(Command("cinst fx")), "Should match 'cinst'"
    assert not match(Command("choco install")), "Shouldn't match 'choco install'"

# Generated at 2022-06-14 09:32:02.830425
# Unit test for function match
def test_match():
    script = 'choco install git'
    output = '''Installing the following packages:
git
By installing you accept licenses for the packages.
Progress: Downloading git 2.9.2... 100%
git v2.9.2 [Approved]
git package files install completed. Performing other installation steps.
The package git wants to run 'chocolateyInstall.ps1'.
Note: If you don't run this script, the installation will fail.
Note: To confirm automatically next time, use '-y' or consider:
choco feature enable -n allowGlobalConfirmation'''

    command = Command(script=script, output=output)
    assert match(command) is True

    # Test that it does not match an invalid chocolatey command
    script = 'choco install'

# Generated at 2022-06-14 09:32:08.404945
# Unit test for function match
def test_match():
    assert match(Command(script="choco install package",
            output="Installing the following packages:\n"
                   "package v1.0.0 by user."))
    assert match(Command(script="cinst package",
            output="Installing the following packages:\n"
                   "package v1.0.0 by user."))
    assert not match(Command(script="cinst package",
            output="package already installed"))
    assert not match(Command(script="choco install package",
            output="package already installed"))



# Generated at 2022-06-14 09:32:12.413265
# Unit test for function match
def test_match():
    input1 = Command("choco install git", "", "")
    assert match(input1)
    input2 = Command(
        "cinst git", "Installing the following packages:", "git not installed"
    )
    assert match(input2)



# Generated at 2022-06-14 09:32:21.137389
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("cinst choco") == "cinst choco.install"
    assert get_new_command("cinst -y notepadplusplus") == "cinst -y notepadplusplus.install"
    assert get_new_command("cinst -y virtualbox --x86") == "cinst -y virtualbox.install --x86"
    assert get_new_command("choco install choco") == "choco install choco.install"
    assert get_new_command("choco install -y notepadplusplus") == "choco install -y notepadplusplus.install"
    assert get_new_command("choco install -y virtualbox --x86") == "choco install -y virtualbox.install --x86"

# Generated at 2022-06-14 09:32:37.581999
# Unit test for function get_new_command
def test_get_new_command():
    test_input = Command("cinst test_package_name", "")
    test_input.script_parts = test_input.script.split()
    assert get_new_command(test_input) == ["cinst", "test_package_name.install"]

    test_input = Command("choco install test_package_name", "")
    test_input.script_parts = test_input.script.split()
    assert get_new_command(test_input) == ["choco", "install", "test_package_name.install"]

    test_input = Command("cinst --yes test_package_name", "")
    test_input.script_parts = test_input.script.split()
    assert get_new_command(test_input) == ["cinst", "--yes", "test_package_name.install"]



# Generated at 2022-06-14 09:32:49.218946
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('choco install chocolatey -y --no-progress', '', '')) == 'choco install chocolatey.install -y --no-progress'
    assert get_new_command(Command('cinst notepadplusplus', '', '')) == 'cinst notepadplusplus.install'
    assert get_new_command(Command('choco install 7zip -y --no-progress', '', '')) == 'choco install 7zip.install -y --no-progress'
    assert get_new_command(Command('choco install 7zip.install -y --no-progress', '', '')) == 'choco install 7zip.install.install -y --no-progress'

# Generated at 2022-06-14 09:32:57.618666
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("cinst package") == "cinst package.install"
    assert get_new_command("cinst package --interactive") == "cinst package.install --interactive"
    assert get_new_command("cinst package -s") == "cinst package.install -s"
    assert get_new_command("cinst package=1.2.3") == "cinst package=1.2.3"
    assert get_new_command("choco install package") == "choco install package.install"

# Generated at 2022-06-14 09:33:05.421380
# Unit test for function get_new_command
def test_get_new_command():
    assert isinstance(get_new_command(Command("choco install atom")), str)
    assert isinstance(get_new_command(Command("cinst atom")), str)
    assert isinstance(get_new_command(Command("cinst atom -pre")), str)
    assert isinstance(get_new_command(Command("choco install atom -pre")), str)
    assert isinstance(get_new_command(Command("choco install -y atom -pre")), str)
    assert isinstance(get_new_command(Command("choco install -y atom")), str)
    assert isinstance(get_new_command(Command("choco install -r atom -pre")), str)

# Generated at 2022-06-14 09:33:16.556947
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

    assert get_new_command(Command('"choco install" vim', 'vim is now installed.\n')) == '"choco install" vim.install'
    assert get_new_command(Command('"cinst" vim', '')) == '"cinst" vim.install'
    assert get_new_command(Command('"choco install" vim.install', '')) == []
    assert get_new_command(Command('"cinst" -params', '')) == []
    assert get_new_command(Command('"cinst" -params=test', '')) == []
    assert get_new_command(Command('"cinst" pkg=test', '')) == []
    assert get_new_command(Command('"cinst" pkg/test', '')) == []

# Generated at 2022-06-14 09:33:23.148104
# Unit test for function match
def test_match():
    assert match(Command('choco install package',
                         'Installing the following packages:',
                         'Installing package'))

    assert match(Command('cinst package',
                         'Installing the following packages:',
                         'Installing package'))

    assert match(Command('cinst -y package',
                         'Installing the following packages:',
                         'Installing package'))

    assert not match(Command('choco not-install',
                             'Installing the following packages:',
                             'Installing package'))


# Generated at 2022-06-14 09:33:27.843462
# Unit test for function get_new_command

# Generated at 2022-06-14 09:33:31.578191
# Unit test for function match
def test_match():
    assert match(Command("choco install foo"))
    assert match(Command("cinst foo"))
    assert not match(Command("choco search foo"))
    assert not match(Command("cinst --search foo"))


# Generated at 2022-06-14 09:33:35.576536
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('choco install <package>')) == 'choco install <package>.install'
    assert get_new_command(Command('cinst <package>')) == 'cinst <package>.install'

# Generated at 2022-06-14 09:33:40.524793
# Unit test for function match
def test_match():
    assert not match(Command("echo", "Installing the following packages:", ""))
    assert match(Command("choco install package", "Installing the following packages:", ""))
    assert match(Command("cinst package", "Installing the following packages:", ""))


# Generated at 2022-06-14 09:34:04.918775
# Unit test for function get_new_command
def test_get_new_command():
    # No command to validate
    assert not get_new_command(Command("ls six", "ls six"))

    # Command is not a chocolatey command
    assert not get_new_command(Command("pip install six", "pip install six"))

    # Command is a chocolatey command
    assert (
        get_new_command(Command("choco install six", "choco install six"))
        == "choco install six.install"
    )

    # Command is a chocolatey command with a version
    assert (
        get_new_command(
            Command("choco install six -version 1.11.0", "choco install six")
        )
        == "choco install six.install -version 1.11.0"
    )

    # Command is a chocolatey command with multiple additional arguments

# Generated at 2022-06-14 09:34:14.276712
# Unit test for function get_new_command
def test_get_new_command():

    # Choco
    command = Command(script = "choco instal test")
    assert get_new_command(command) == "choco install test.install"

    command = Command(script = "choco install test test")
    assert get_new_command(command) == "choco install test test.install"

    command = Command(script = "choco install test --version=1.0.0")
    assert get_new_command(command) == "choco install test.install --version=1.0.0"

    command = Command(script = "choco install test --source=chocolatey")
    assert get_new_command(command) == "choco install test.install --source=chocolatey"

    command = Command(script = "choco install test --yes")

# Generated at 2022-06-14 09:34:19.472166
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("cinst test")
    assert get_new_command(command) == "cinst test.install"
    command = Command("cinst test --version 1.0 --source 'test' -y")
    assert get_new_command(command) == "cinst test.install --version 1.0 --source 'test' -y"

# Generated at 2022-06-14 09:34:25.452626
# Unit test for function get_new_command
def test_get_new_command():
    import os
    from thefuck.types import Command

    os.environ["PATH"] = os.getcwd()
    command = Command("cinst git", 'Chocolatey v0.10.8 \r\n\r\nInstalling the following packages:\r\n\r\n  git\r\n\r\nInstalling git 2.17.1... \r\n  git 2.17.1 has been installed.')
    assert get_new_command(command) == "cinst git.install"


# Generated at 2022-06-14 09:34:33.562428
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("cinst lol", "", "", "", "", "")) == "cinst lol.install"
    assert get_new_command(Command("cinst lolhttp", "", "", "", "", "")) == "cinst lolhttp.install"
    assert get_new_command(Command("cinst lolhttp github", "", "", "", "", "")) == "cinst lolhttp.install github"
    assert get_new_command(Command("choco install lol", "", "", "", "", "")) == "choco install lol.install"
    assert get_new_command(Command("choco install lolhttp", "", "", "", "", "")) == "choco install lolhttp.install"

# Generated at 2022-06-14 09:34:46.121849
# Unit test for function get_new_command
def test_get_new_command():

    # Case 1
    command = Command("sudo choco install 7zip -y", "")
    new_command = "sudo choco install 7zip.install -y"
    assert (
        get_new_command(command) == new_command
    ), "get_new_command() failed wrong new command returned"

    # Case 2
    command = Command("sudo choco install cmake -a", "")
    new_command = "sudo choco install cmake.install -a"
    assert (
        get_new_command(command) == new_command
    ), "get_new_command() failed wrong new command returned"

    # Case 3
    command = Command("sudo cinst 7zip -y", "")
    new_command = "sudo cinst 7zip.install -y"

# Generated at 2022-06-14 09:34:57.909627
# Unit test for function get_new_command

# Generated at 2022-06-14 09:35:03.878659
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(
        script="cinst foo",
        output="Installing the following packages:",
        env={},
    )
    assert "cinst foo.install" == get_new_command(command)

    command = Command(
        script="choco install foo",
        output="Installing the following packages:",
        env={},
    )
    assert "choco install foo.install" == get_new_command(command)

# Generated at 2022-06-14 09:35:14.636683
# Unit test for function get_new_command
def test_get_new_command():
    command_1 = Command('cinst test')
    assert get_new_command(command_1) == 'cinst test.install'
    command_2 = Command('cinst test -y')
    assert get_new_command(command_2) == 'cinst test.install -y'
    command_3 = Command('cinst test1 test2')
    assert get_new_command(command_3) == 'cinst test1 test2.install'
    command_4 = Command('cinst test -source="c:\test"')
    assert get_new_command(command_4) == []
    command_5 = Command('cinst test -ia="c:\test"')
    assert get_new_command(command_5) == 'cinst test.install -ia=c:\\test'

# Generated at 2022-06-14 09:35:25.165971
# Unit test for function get_new_command
def test_get_new_command():
    # Command uses 'cinst' instead of 'choco install'
    assert (get_new_command(Command('cinst python2')) == 'cinst python2.install')

    # Command has additional flags
    assert (get_new_command(Command('cinst python2 -y')) == 'cinst python2 -y.install')

    # Command with multiple words
    assert (get_new_command(Command('cinst "docker compose"')) ==
            'cinst "docker compose".install')

    # Command with multiple words and hyphens
    assert (get_new_command(Command('cinst "azure-cli"')) == 'cinst "azure-cli".install')

    # Command with multiple words and an equals sign

# Generated at 2022-06-14 09:36:06.771539
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('cinst chocolatey.nodejs',
                      output='Installing the following packages. 1/2 chocolatey.nodejs By installing you accept licenses for the packages.')
    command2 = Command('cinst chocolatey-nodejs', output='Installing the following packages. 1/2 chocolatey-nodejs By installing you accept licenses for the packages.')
    assert get_new_command(command) == 'cinst chocolatey.nodejs.install'
    assert get_new_command(command2) == 'cinst chocolatey-nodejs.install'

# Generated at 2022-06-14 09:36:09.330190
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('choco install tmux', "")) == 'choco install tmux.install'
    assert get_new_command(Command('cinst tmux', "")) == 'cinst tmux.install'

# Generated at 2022-06-14 09:36:15.770754
# Unit test for function get_new_command
def test_get_new_command():
    command = "choco install notepadplusplus"
    new_command = "choco install notepadplusplus.install"
    assert get_new_command(Command(command, "", command.split()))[0] == new_command
    assert get_new_command(Command(command, "", command.split()))[0] == new_command

# Generated at 2022-06-14 09:36:18.377736
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("choco install packagename", "error message")
    assert get_new_command(command) == "choco install packagename.install"

# Generated at 2022-06-14 09:36:22.924546
# Unit test for function match
def test_match():
    command = Command('choco install atom', '', 0)
    assert match(command)
    command = Command('cinst atom', '', 0)
    assert match(command)
    command = Command('choco uninstall atom', '', 0)
    assert not match(command)



# Generated at 2022-06-14 09:36:29.520594
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("choco install test") == "choco install test.install"
    assert get_new_command("choco install test test2") == "choco install test.install test2"
    assert get_new_command("choco install test -d") == "choco install test.install -d"
    assert get_new_command("cinst test") == "cinst test.install"
    assert get_new_command("cinst test test2") == "cinst test.install test2"
    assert get_new_command("cinst test -d") == "cinst test.install -d"

# Generated at 2022-06-14 09:36:38.537832
# Unit test for function match
def test_match():
    """ Test that match returns the correct value for correctly- or incorrectly-spelled commands """
    command1 = Command('cinst chocolatey', '', '')
    assert match(command1) == True

    command2 = Command('cinst chocolatey', '', 'Installing the following packages')
    assert match(command2) == False

    command3 = Command('cinst chocolatey.install', '', 'Installing the following packages')
    assert match(command3) == False

    command4 = Command('cinst chocolatey.install', '', '')
    assert match(command4) == True


# Generated at 2022-06-14 09:36:43.021711
# Unit test for function match
def test_match():
    assert match(Command('choco install notepadplusplus', '', 'Installing the following packages', 0))
    assert not match(Command('choco install notepadplusplus', '', 'Installing the following packages', 0))
    assert not match(Command('choco install notepadplusplus', '', 'Installing the following packages', 1))

# Generated at 2022-06-14 09:36:52.466596
# Unit test for function get_new_command
def test_get_new_command():
    assert (
        get_new_command(Command("choco install vim", "vim already installed"))
        == "choco install vim.install"
    )
    assert get_new_command(Command("cinst vim", "vim already installed")) == "cinst vim.install"
    assert get_new_command(Command("choco install -y vim", "vim already installed")) == "choco install -y vim.install"
    params = "choco install something -y --force --debug"
    assert get_new_command(Command(params, "something already installed")) == params + ".install"

# Generated at 2022-06-14 09:36:56.948740
# Unit test for function get_new_command
def test_get_new_command():
    command = Mock(script="choco install", script_parts=['choco', 'install'])
    command.output = 'Chocolatey v0.10.15 Installing the following packages:'
    assert get_new_command(command) == 'choco install .install'

# Generated at 2022-06-14 09:38:07.433742
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.choco import get_new_command
    assert get_new_command("choco install choco") == "choco install choco.install"

# Generated at 2022-06-14 09:38:14.787414
# Unit test for function match
def test_match():
    assert match(Command('choco install appname', '', ''))
    assert not match(Command('choco list', '', ''))
    assert match(Command('cinst appname', '', ''))
    assert not match(Command('cinst', '', ''))


# Generated at 2022-06-14 09:38:20.875920
# Unit test for function match
def test_match():
    assert match(Command("choco install"))
    assert match(Command("choco install git"))
    assert match(Command("choco install git nodejs"))
    assert match(Command("choco install git nodejs -y"))
    assert match(Command("cinst nodejs"))
    assert not match(Command("choco upgrade"))
    assert not match(Command("chocolatey install git nodejs"))



# Generated at 2022-06-14 09:38:25.501062
# Unit test for function get_new_command
def test_get_new_command():
    get_new_command(Command("choco install chrome")) == \
        "choco.install chrome"
    get_new_command(Command("cinst chrome")) == \
        "cinst.install chrome"

# Generated at 2022-06-14 09:38:28.163957
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("choco install chocolatey", "Installing the following packages")) == "choco install chocolatey.install"

# Generated at 2022-06-14 09:38:39.193831
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("cinst choco", "Installing the following packages:\r\nchoco\r\n")) == "cinst choco.install"
    assert get_new_command(Command("choco install choco", "Installing the following packages:\r\nchoco\r\n")) == "choco install choco.install"
    assert get_new_command(Command("choco install choco foo", "Installing the following packages:\r\nchoco\r\n")) == "choco install choco.install foo"
    assert get_new_command(Command("choco install choco -y foo", "Installing the following packages:\r\nchoco\r\n")) == "choco install choco.install -y foo"

# Generated at 2022-06-14 09:38:52.281991
# Unit test for function match
def test_match():
    command1 = Command("choco install foo", "Installing the following packages:")
    command2 = Command("cinst foo", "Installing the following packages:")
    command3 = Command("cinst -y foo", "Installing the following packages:")
    command4 = Command("cinst -y foo=1.0.0", "Installing the following packages:")
    command5 = Command("cinst foo/3.0.2", "Installing the following packages:")
    command6 = Command("cinst foo=1.0.0", "Installing the following packages:")

    assert match(command1)
    assert match(command2)
    assert match(command3)
    assert match(command6)
    assert not match(command4)
    assert not match(command5)



# Generated at 2022-06-14 09:39:00.128043
# Unit test for function get_new_command

# Generated at 2022-06-14 09:39:10.817869
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("choco install googlechrome", "")) == "choco install googlechrome.install"
    assert get_new_command(Command("cinst googlechrome", "")) == "cinst googlechrome.install"
    assert get_new_command(Command("choco install -y googlechrome", "")) == "choco install -y googlechrome.install"
    assert get_new_command(Command("cinst -y googlechrome", "")) == "cinst -y googlechrome.install"

# Generated at 2022-06-14 09:39:23.124455
# Unit test for function get_new_command
def test_get_new_command():
    script = Config().from_json({
        'apps': {'choco': {'command': ['choco'], 'priority': 1}},
        'rules': [{'expect': '*Installing the following packages*',
                   'match': '* choco install *',
                   'get_new_command': 'return command.script.replace(script_part, script_part + ".install")'}]
    }).rules[0]
    assert get_new_command(Command('choco install a', None, 'some output')) == "choco install a.install"
    assert get_new_command(Command('choco install a b', None, 'some output')) == "choco install a.install b"