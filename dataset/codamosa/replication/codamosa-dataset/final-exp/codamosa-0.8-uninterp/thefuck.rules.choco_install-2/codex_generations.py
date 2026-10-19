

# Generated at 2022-06-14 09:30:03.466058
# Unit test for function match
def test_match():
    assert match(Command('choco install python2.7', '', ''))
    assert match(Command('cinst python2.7 -y', '', ''))
    assert match(Command('cinst python2.7 -s', '', ''))
    assert match(Command('cinst python2.7', '', ''))



# Generated at 2022-06-14 09:30:12.625088
# Unit test for function get_new_command
def test_get_new_command():
     command = type(
         'Command',
         (object,),
         {
             'script': 'choco install docker-compose',
             'script_parts': ['choco', 'install', 'docker-compose']
         })
     assert get_new_command(command) == 'choco install docker-compose.install'
     command = type(
         'Command',
         (object,),
         {
             'script': 'cinst docker-compose',
             'script_parts': ['cinst', 'docker-compose']
         })
     assert get_new_command(command) == 'cinst docker-compose.install'

# Generated at 2022-06-14 09:30:28.750446
# Unit test for function get_new_command
def test_get_new_command():
    command = type('Command', (object,), {
        'script': "cinst",
        'script_parts': ["cinst", "abc"],
        'output': "Installing the following packages:"
    })
    assert (get_new_command(command) == "cinst abc.install")
    command = type('Command', (object,), {
        'script': "choco install",
        'script_parts': ["choco", "install", "abc"],
        'output': "Installing the following packages:"
    })
    assert (get_new_command(command) == "choco install abc.install")


# Generated at 2022-06-14 09:30:39.815876
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("cinst firefox") == "cinst firefox.install"
    assert get_new_command("cinst firefox -y") == "cinst firefox.install -y"
    assert get_new_command("cinst firefox.install -y") == "cinst firefox.install.install -y"
    assert get_new_command("cinst firefox.install -y --version 3.1") == "cinst firefox.install.install -y --version 3.1"
    assert get_new_command("cinst firefox --version 3.1") == "cinst firefox.install --version 3.1"
    assert get_new_command("cinst -y --version 3.1 firefox") == "cinst -y --version 3.1 firefox.install"
    assert get_new_command

# Generated at 2022-06-14 09:30:41.543785
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("choco install testPleaseIgnore")) == "choco install testPleaseIgnore.install"

# Generated at 2022-06-14 09:30:51.013156
# Unit test for function match
def test_match():
    # choco install package should be matched
    command = Command("choco install sl", "", "Installing the following packages: sl")
    assert match(command)
    # cinst package should be matched
    command = Command("cinst sl", "", "Installing the following packages: sl")
    assert match(command)

    # choco install package --no-progress should not be matched
    command = Command("choco install sl --no-progress", "", "Installing the following packages: sl")
    assert not match(command)
    # cinst package --no-progress should not be matched
    command = Command("cinst sl --no-progress", "", "Installing the following packages: sl")
    assert not match(command)

    # choco list package should not be matched

# Generated at 2022-06-14 09:31:00.124863
# Unit test for function get_new_command
def test_get_new_command():
    assert "choco install f.install" == get_new_command(Command('choco install f', ''))
    assert "choco install f.install -y --force" == get_new_command(Command('choco install f -y --force', ''))
    assert "cinst f.install -y --force" == get_new_command(Command('cinst f -y --force', ''))
    assert "cinst f.install" == get_new_command(Command('cinst f', ''))
    assert "cinst f.install -y --force" == get_new_command(Command('cinst f -y --force', ''))

# Generated at 2022-06-14 09:31:04.262406
# Unit test for function match
def test_match():
    command = create_command('choco install foo')
    assert match(command)
    assert not match(create_command('choco install foo --params="stuff"'))



# Generated at 2022-06-14 09:31:10.384201
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('pip install sqlalchemy', '', '', 1)
    assert get_new_command(command) == ['pip', 'install', 'sqlalchemy.install']
    
    command = Command('cinst git -y', '', '', 1)
    assert get_new_command(command) == ['cinst', 'git.install', '-y']
    
    command = Command('choco install git -y', '', '', 1)
    assert get_new_command(command) == ['choco', 'install', 'git.install', '-y']

# Generated at 2022-06-14 09:31:14.060616
# Unit test for function match
def test_match():
    script = "choco install --no-progress -y terraform --version 0.9.8"
    command = Command(script, "")
    assert match(command) is True
    script = "cinst jira-core --y --params '/ApplicationBaseName:Atlassian Jira Core /DataCenter:false'"
    command = Command(script, "")
    assert match(command) is True



# Generated at 2022-06-14 09:31:22.268511
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('choco install chocolatey', '', '')) == 'choco install chocolatey.install'
    assert get_new_command(Command('cinst git', '', '')) == 'cinst git.install'

# Generated at 2022-06-14 09:31:32.685791
# Unit test for function match
def test_match():
    # Use the choco command for the test, leads to more stable tests
    script = "choco install mypackage"
    output = "Installing the following packages:"
    command = Command(script, output)
    assert match(command)

    script = "cinst mypackage"
    output = "Installing the following packages:"
    command = Command(script, output)
    assert match(command)

    script = "choco install -y mypackage"
    output = "Installing the following packages:"
    command = Command(script, output)
    assert match(command)

    script = "cinst -y mypackage"
    output = "Installing the following packages:"
    command = Command(script, output)
    assert match(command)



# Generated at 2022-06-14 09:31:37.046889
# Unit test for function get_new_command
def test_get_new_command():
    script_parts = ["choco", "cinst", "memcached", "install"]
    script = " ".join(script_parts)
    command = Command(script, "")
    assert get_new_command(command) == "choco cinst memcached.install"

# Generated at 2022-06-14 09:31:48.660213
# Unit test for function match
def test_match():
    assert match(type("Command", (object,), {
        "script": "choco install chocolatey",
        "script_parts": ["choco", "install", "chocolatey"],
        "output": "Installing the following packages:\nchocolatey\n"
    }))
    assert match(type("Command", (object,), {
        "script": "cinst chocolatey",
        "script_parts": ["cinst", "chocolatey"],
        "output": "Installing the following packages:\nchocolatey\n"
    }))
    assert not match(type("Command", (object,), {
        "script": "cinst chocolatey",
        "script_parts": ["cinst", "chocolatey"],
        "output": "Installed the following packages:\nchocolatey\n"
    }))

# Generated at 2022-06-14 09:31:52.626898
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(
        script="choco install package_name --version 2.0",
        stdout="Installing the following packages:",
        stderr="",
    )

    assert "choco install package_name.install --version 2.0" == get_new_command(command)

# Generated at 2022-06-14 09:31:57.330753
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

    assert get_new_command(Command('choco install foobarbaz')) == 'choco install foobarbaz.install'
    assert get_new_command(Command('cinst foobarbaz')) == 'cinst foobarbaz.install'

# Generated at 2022-06-14 09:32:04.492637
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("cinst vlc") == "cinst vlc.install"
    assert get_new_command("cinst vlc.portable") == "cinst vlc.portable.install"
    assert get_new_command("cinst -y vlc") == "cinst -y vlc.install"
    assert get_new_command("cinst -y vlc.portable") == "cinst -y vlc.portable.install"
    assert get_new_command("cinst -y=true vlc") == "cinst -y=true vlc.install"

# Generated at 2022-06-14 09:32:17.529092
# Unit test for function match
def test_match():
    assert not match("pip install --help")
    assert not match("cinst")
    assert match("cinst arg1 arg2 arg3 arg4 arg5 arg6 arg7 arg8 arg9 arg10 arg11 arg12 arg13 arg14")
    assert match("cinst arg1 arg2 arg3 arg4 arg5 arg6 arg7 arg8 arg9 arg10 arg11 arg12 arg13 arg14 arg15")
    assert match("choco install --pre args")
    assert match("choco install --debug args")
    assert match("choco install --pre -pre args")
    assert match("cinst --pre arg1 arg2 arg3 arg4 arg5 arg6 arg7 arg8 arg9 arg10 arg11 arg12 arg13 arg14")

# Generated at 2022-06-14 09:32:27.130821
# Unit test for function get_new_command
def test_get_new_command():
    # Case 1: 'choco install package'
    assert get_new_command(Command('choco install package')) == 'choco install package.install'

    # Case 2: 'choco install package --version=1.0.0'
    assert get_new_command(Command('choco install package --version=1.0.0')) == 'choco install package.install --version=1.0.0'

    # Case 3: 'choco install package --version=1.0.0'
    assert get_new_command(Command('cinst package')) == 'cinst package.install'

# Generated at 2022-06-14 09:32:30.320321
# Unit test for function match
def test_match():
    """
    Unit test for function match
    """

# Generated at 2022-06-14 09:32:42.127673
# Unit test for function get_new_command
def test_get_new_command():
    assert (
        get_new_command(Command(script="cinst chocolatey"))
        == "cinst chocolatey.install"
    )
    assert (
        get_new_command(Command(script="cinst -whatif googlechrome"))
        == "cinst -whatif googlechrome.install"
    )
    assert (
        get_new_command(Command(script="choco install 7zip"))
        == "choco install 7zip.install"
    )

# Generated at 2022-06-14 09:32:52.916341
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('choco install firefox', 'Installing the following packages:\nfirefox',
                                   '/tmp/test')) == 'choco install firefox.install'
    assert get_new_command(Command('cinst firefox', 'Installing the following packages:\nfirefox',
                                   '/tmp/test')) == 'cinst firefox.install'
    assert get_new_command(Command('cinst -y firefox', 'Installing the following packages:\nfirefox',
                                   '/tmp/test')) == 'cinst -y firefox.install'

# Generated at 2022-06-14 09:33:05.670246
# Unit test for function get_new_command
def test_get_new_command():
    command_1 = Command("choco install firefox", "Installing the following packages:\nfirefox\nBy installing you accept")

    command_2 = Command("install chrome", "Installing the following packages:\nchrome\nBy installing")

    command_3 = Command("cinst winwdgets -y", "Installing the following packages:\nwinwdgets\nBy installing")

    command_4 = Command("install gimp -f", "Installing the following packages:\ngimp\nBy installing")

    command_5 = Command("install atom -s", "Installing the following packages:\natom\nBy installing")

    command_6 = Command("cinst chrome -s", "Installing the following packages:\nchrome\nBy installing")

    assert get_new_command(command_1) == 'choco install firefox.install'
    assert get_new

# Generated at 2022-06-14 09:33:08.668412
# Unit test for function match
def test_match():
    assert match("choco install python")
    assert not match("choco install")
    assert not match("choco search python")
    assert not match("choco list python")


# Generated at 2022-06-14 09:33:11.145942
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('cinst python.install')
    assert get_new_command(command) == 'cinst python'


# Generated at 2022-06-14 09:33:22.778327
# Unit test for function match
def test_match():
    assert match(Command('choco install git', '', '', '', 1, None))
    assert match(Command('choco install git', '', 'Installing the following packages:\ngit', '', 1, None))
    assert not match(Command('choco install git', '', '', '', 1, None))
    assert not match(Command('choco install git', '', '', '', 1, None))
    assert match(Command('cinst choco', '', '', '', 1, None))
    assert match(Command('cinst choco', '', 'Installing the following packages:\nchoco', '', 1, None))
    assert not match(Command('cinst choco', '', '', '', 1, None))
    assert not match(Command('cinst choco', '', '', '', 1, None))

# Generated at 2022-06-14 09:33:35.298501
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('choco install pkg',
                                   'Installing the following packages:\n"pkg" (auto)\n')) == 'choco install pkg.install'
    assert get_new_command(Command('choco install pkg -- params',
                                   'Installing the following packages:\n"pkg" (auto)\n')) == 'choco install pkg.install -- params'
    assert get_new_command(Command('cinst pkg',
                                   'Installing the following packages:\n"pkg" (auto)\n')) == 'cinst pkg.install'
    assert get_new_command(Command('cinst pkg -- params',
                                   'Installing the following packages:\n"pkg" (auto)\n')) == 'cinst pkg.install -- params'
    assert get_new_command

# Generated at 2022-06-14 09:33:38.876647
# Unit test for function match
def test_match():
    assert match(
        Command(script="choco install somePackage",
                output="Installing the following packages: somePackage"))
    assert match(
        Command(
            script="cinst somePackage",
            output="Installing the following packages: somePackage"))
    assert not match(
        Command(script="choco install somePackage",
                output="Installing somePackage [2.0.0]"))
    assert not match(
        Command(script="cinst somePackage",
                output="Installing somePackage [2.0.0]"))



# Generated at 2022-06-14 09:33:46.009007
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('choco install chrome', '')) == 'choco install chrome.install'
    assert get_new_command(Command('cinst chrome', '')) == 'cinst chrome.install'
    assert get_new_command(Command('choco install google-chrome', '')) == 'choco install google-chrome.install'
    assert get_new_command(Command('choco install google-chrome --confirm', '')) == 'choco install google-chrome.install --confirm'

# Generated at 2022-06-14 09:33:56.437448
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('choco install python')
    new_command = get_new_command(command)
    assert new_command.script == 'choco install python.install'
    command2 = Command('choco install python -y')
    new_command2 = get_new_command(command2)
    assert new_command2.script == 'choco install python.install -y'
    command3 = Command('choco install python2.7')
    new_command3 = get_new_command(command3)
    assert new_command3.script == 'choco install python2.7.install'
    command4 = Command('cinst python')
    new_command4 = get_new_command(command4)
    assert new_command4.script == 'cinst python.install'

# Generated at 2022-06-14 09:34:11.829032
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('choco install jdk8')
    assert get_new_command(command) == 'choco install jdk8.install'

    command = Command('cinst jdk8')
    assert get_new_command(command) == 'cinst jdk8.install'

    command = Command('cinst jdk8 -params')
    assert get_new_command(command) == 'cinst jdk8.install -params'

    command = Command('cinst jdk8 --params')
    assert get_new_command(command) == 'cinst jdk8.install --params'

    command = Command('cinst -y jdk8')
    assert get_new_command(command) == 'cinst -y jdk8.install'

    command = Command('cinst -y jdk8 --params')
    assert get_

# Generated at 2022-06-14 09:34:13.754608
# Unit test for function match
def test_match():
    assert match(Command('choco install -y chocolatey',
                         'Installing the following packages','','','','','','','','','','','','')) is True


# Generated at 2022-06-14 09:34:24.848627
# Unit test for function match
def test_match():
    # Test that match doesn't return True if choco did not install the package
    output = "Chocolatey v0.10.8\n    Installing the following packages:\n      python3.6.8 by: chocolatey\n\n"
    assert not match(Command("choco install python 3.6.8", output))
    # Test that match returns True if choco installed the package

# Generated at 2022-06-14 09:34:38.210709
# Unit test for function get_new_command
def test_get_new_command():
    assert (
        get_new_command(
            Command(script="choco install luarocks", output="Bad stuff happening")
        )
        == "choco install luarocks.install"
    )
    assert (
        get_new_command(
            Command(script="cinst luarocks", output="Bad stuff happening")
        )
        == "cinst luarocks.install"
    )
    assert not get_new_command(Command(script="choco install", output="Bad stuff happening"))
    assert not get_new_command(
        Command(script="cinst -y", output="Bad stuff happening")
    )
    assert not get_new_command(
        Command(script="cinst chocolatey.extension", output="Bad stuff happening")
    )

# Generated at 2022-06-14 09:34:45.106165
# Unit test for function match
def test_match():
    assert (
        match(Command("choco install", "", "Installing the following packages"))
        == True
    )
    assert (
        match(Command("cinst", "", "Installing the following packages")) == True
    )
    assert match(Command("choco install", "", "Installing package")) == False
    assert match(Command("cinst", "", "Installing package")) == False

# Generated at 2022-06-14 09:34:51.842721
# Unit test for function get_new_command
def test_get_new_command():
    from tests.utils import Command
    # "choco install <pkg>"
    command = Command('choco install testpkg -y')
    assert get_new_command(command) == "choco install testpkg.install -y"

    # "cinst <pkg>"
    command = Command('cinst testpkg -y')
    assert get_new_command(command) == "cinst testpkg.install -y"

# Generated at 2022-06-14 09:34:56.442038
# Unit test for function match

# Generated at 2022-06-14 09:35:00.496416
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("cinst chocolatey", "chocolatey is already installed")) == "chocolatey.install"
    assert get_new_command(Command("cinst chocolatey xxx", "Something else went wrong")) == "chocolatey xxx.install"

# Generated at 2022-06-14 09:35:05.803671
# Unit test for function match
def test_match():
    output = '''
Installing the following packages:
choco
By installing you accept licenses for the packages.'''
    assert match(Command("cinst choco"))
    command = Command("cinst choco", output=output)
    assert match(command)



# Generated at 2022-06-14 09:35:12.853273
# Unit test for function match
def test_match():
    assert match(Command('choco install pink', '', 'Installing the following packages:\npink'))
    assert match(Command('cinst pink', '', 'Installing the following packages:\npink'))
    assert not match(Command('choco install pink', '', 'Installing the following packages:\npink\nand more'))



# Generated at 2022-06-14 09:35:28.200454
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('choco install git', '', '', '', '', '')) == 'choco install git.install'
    assert get_new_command(Command('cinst git', '', '', '', '', '')) == 'cinst git.install'
    assert get_new_command(Command('cinst git -y', '', '', '', '', '')) == 'cinst git.install -y'
    assert get_new_command(Command('cinst git --params=\'--params\'/\'value\'', '', '', '', '', '')) == 'cinst git.install --params=\'--params\'/\'value\''

# Generated at 2022-06-14 09:35:40.970101
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command.from_string("cinst chocolatey")) == "cinst chocolatey.install"
    assert get_new_command(Command.from_string("cinst -y chocolatey")) == "cinst -y chocolatey.install"
    assert get_new_command(Command.from_string("cinst chocolatey.extension")) == "cinst chocolatey.extension.install"
    assert get_new_command(Command.from_string("cinst -y chocolatey.extension")) == "cinst -y chocolatey.extension.install"
    assert get_new_command(Command.from_string("cinst chocolatey.extension -y")) == "cinst chocolatey.extension.install -y"
    assert get_new_command(Command.from_string("cinst chocolatey.extension --yes"))

# Generated at 2022-06-14 09:35:51.419392
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("choco install chrome")) == "choco install chrome.install"
    assert get_new_command(Command("cinst winpython")) == "cinst winpython.install"
    assert get_new_command(Command("choco install -source foo -y ctest")) == "choco install -source foo -y ctest.install"
    assert get_new_command(Command("cinst -y chrome")) == "cinst -y chrome.install"
    assert get_new_command(Command("choco install abc=1 foo 2.3")) == "choco install abc=1 foo 2.3"
    assert get_new_command(Command("cinst \"abc 2\"")) == "cinst \"abc 2.install\""

# Generated at 2022-06-14 09:35:57.104666
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('choco install test', '', '', '')
    assert get_new_command(command) == 'choco install test.install'
    command_2 = Command('cinst test', '', '', '')
    assert get_new_command(command_2) == 'cinst test.install'

# Generated at 2022-06-14 09:36:03.408328
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('choco install git')) == 'choco install git.install'
    assert get_new_command(Command('cinst git')) == 'cinst git.install'
    assert get_new_command(Command('cinst --version=1.0 git')) == 'cinst --version=1.0 git.install'

# Generated at 2022-06-14 09:36:13.577465
# Unit test for function get_new_command
def test_get_new_command():
    c = Command('choco install googlechrome')
    assert get_new_command(c) == 'choco install googlechrome.install'
    c = Command('cinst googlechrome')
    assert get_new_command(c) == 'cinst googlechrome.install'
    c = Command('cinst -y googlechrome')
    assert get_new_command(c) == 'cinst -y googlechrome.install'
    c = Command('choco install --version 1.0 googlechrome')
    assert get_new_command(c) == 'choco install --version 1.0 googlechrome.install'
    c = Command('cinst -y --version 1.0 googlechrome')
    assert get_new_command(c) == 'cinst -y --version 1.0 googlechrome.install'


# Generated at 2022-06-14 09:36:25.869653
# Unit test for function match
def test_match():
    assert bool(match(Command('choco install gitteh',
                              "Chocolatey v0.9.8.33\n"
                              "Installing the following packages:\n"
                              "gitteh (0.7.1)\n"
                              "By installing you accept licenses for the packages.",
                              '')))
    assert bool(match(Command('cinst gitteh',
                              "Chocolatey v0.9.8.33\n"
                              "Installing the following packages:\n"
                              "gitteh (0.7.1)\n"
                              "By installing you accept licenses for the packages.",
                              '')))

# Generated at 2022-06-14 09:36:32.536946
# Unit test for function match
def test_match():
    assert match(Command('choco install test', '', 'Installing the following packages:\n  test\n'))
    assert match(Command('cinst test', '', 'Installing the following packages:\n  test\n'))
    assert not match(Command('choco install test', '', ''))
    assert not match(Command('cinst test', '', ''))



# Generated at 2022-06-14 09:36:44.168335
# Unit test for function match
def test_match():
    assert match(c.Command('choco install uninstall', 'installed uninstall')) is True
    assert match(c.Command('choco install uninstall', 'not installed uninstall')) is False
    assert match(c.Command('choco uninstall uninstall', 'installed uninstall')) is False
    assert match(c.Command('choco uninstall uninstall', 'not installed uninstall')) is False
    assert match(c.Command('choco uninstall uninstall', '')) is False
    assert match(c.Command('choco install not-installed', 'not installed uninstall')) is True
    assert match(c.Command('cinst uninstall', 'installed uninstall')) is True
    assert match(c.Command('cinst uninstall', 'not installed uninstall')) is False
    assert match(c.Command('cinst -yv uninstall', 'installed uninstall')) is True

# Generated at 2022-06-14 09:36:50.571482
# Unit test for function match
def test_match():
    assert match(Command('choco install vim -y',
        output='Installing the following packages\r\nvim - A highly configurable text editor built to enable efficient text editing\r\n'))
    assert not match(Command('choco install vim -y',
        output='Installing vim - A highly configurable text editor built to enable efficient text editing\r\n'))


# Generated at 2022-06-14 09:37:11.034688
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('choco install package',
                                   'Installing the following packages:',
                                   'package\npackage.install')) == 'choco install package.install'
    assert get_new_command(Command('cinst package',
                                   'Installing the following packages:',
                                   'package\npackage.install')) == 'cinst package.install'

# Generated at 2022-06-14 09:37:22.906405
# Unit test for function match
def test_match():
    output = "Installing the following packages:\nchocolatey 0.10.3\nhello world 0.1"
    command = Command(script="choco install choco", output=output)
    assert match(command)
    command = Command(script="choco install choco", output="No packages match")
    assert not match(command)
    assert not match(Command(script="ls", output=output))



# Generated at 2022-06-14 09:37:26.360612
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('cinst ghc', '', '')) == 'cinst ghc.install'
    assert get_new_command(Command('choco install rustup', '', '')) == 'choco install rustup.install'

# Generated at 2022-06-14 09:37:28.669032
# Unit test for function match
def test_match():
    assert match(Command('choco install package',
            'Installing the following packages:', '/bin'))
    assert not match(Command('choco install package',
            'Installing 1 package', '/bin'))


# Generated at 2022-06-14 09:37:40.665305
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('choco install package', '')
    assert get_new_command(command) == 'choco install package.install'

    command = Command('cinst package', '')
    assert get_new_command(command) == 'cinst package.install'

    command = Command('choco install package --params /a', '')
    assert get_new_command(command) == 'choco install package.install --params /a'

    command = Command('choco install package_with_hyphen.install', '')
    assert get_new_command(command) == ''

    command = Command('choco install package_with_equals=1.install', '')
    assert get_new_command(command) == 'choco install package_with_equals=1.install.install'



# Generated at 2022-06-14 09:37:49.712445
# Unit test for function match
def test_match():
    output = '''Installing the following packages:
ruby
By installing you accept licenses for the packages.
Progress: Downloading ruby 2.2.2... 100%
Installing ruby 2.2.2...
The package ruby wants to run 'chocolateyInstall.ps1'.
Note: If you don't run this script, the installation will fail.
Note: To confirm automatically next time, use '-y' or consider:
choco feature enable -n allowGlobalConfirmation
Do you want to run the script?([Y]es/[N]o/[P]rint): '''
    assert match(Command('choco install ruby', output))
    assert match(Command('cinst ruby', output))
    assert match(Command('cinst -v not-ruby', output)) is False
    assert match(Command('cinst ruby -v', output))


# Unit test

# Generated at 2022-06-14 09:37:55.098226
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script="choco install nodejs.install xyz.install",
                      output="Installing the following packages: nodejs xyz")
    assert get_new_command(command) == "choco install nodejs.install.install xyz.install"

# Generated at 2022-06-14 09:38:02.959102
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('choco install Choco', '', 0, '')
    assert get_new_command(command) == 'choco install Choco.install'
    command = Command('cinst Choco', '', 0, '')
    assert get_new_command(command) == 'cinst Choco.install'
    command = Command('cinst Choco -y --ia', '', 0, '')
    assert get_new_command(command) == 'cinst Choco.install -y --ia'
    command = Command('choco install -y --ia Choco', '', 0, '')
    assert get_new_command(command) == 'choco install -y --ia Choco.install'
    command = Command('choco install -y --ia --usestdlib Choco', '', 0, '')
    assert get_

# Generated at 2022-06-14 09:38:06.855741
# Unit test for function get_new_command
def test_get_new_command():
    command = Command.from_string('choco install docker')
    assert get_new_command(command) == 'choco install docker.install'



# Generated at 2022-06-14 09:38:20.712415
# Unit test for function match

# Generated at 2022-06-14 09:38:38.400023
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('choco install vlc')) == 'choco install vlc.install'
    assert get_new_command(Command('cinst vlc')) == 'cinst vlc.install'

# Generated at 2022-06-14 09:38:48.248629
# Unit test for function match
def test_match():
    match_output = \
"""Installing the following packages:
python2
By installing you accept licenses for the packages.
python2 not installed. The package was not found with the source(s) listed.

If you specified a particular version and are receiving this message, it is possible that the package name exists but the version does not.
Version: """.encode('UTF-8')
    assert match(Command(script='choco install python2',
                         output=match_output))
    assert match(Command(script='cinst python2',
                         output=match_output))



# Generated at 2022-06-14 09:38:51.606790
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("choco install gufo") == "choco install gufo.install"
    assert get_new_command("cinst gufo") == 'cinst gufo.install'

# Generated at 2022-06-14 09:38:56.736822
# Unit test for function match
def test_match():
    assert match(Command('choco install python3 --yes', '', '', 1))
    assert not match(Command('choco install python3', '', '', 1))
    assert match(Command('cinst python3', '', '', 1))
    assert not match(Command('cinst python3 --yes', '', '', 1))


# Generated at 2022-06-14 09:39:00.581625
# Unit test for function get_new_command
def test_get_new_command():
    new_command = get_new_command(Command('cinst chocolatey', output='Installing the following packages'))
    assert new_command == 'cinst chocolatey.install'

# Generated at 2022-06-14 09:39:04.951421
# Unit test for function match
def test_match():
    assert match(Command('choco install blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah', '', '', 1))
    assert not match(Command('choco uninstall some_app', '', '', 1))


# Generated at 2022-06-14 09:39:10.556318
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('choco install -y chocolatey', None)) == 'choco install -y chocolatey.install'
    assert get_new_command(Command('cinst chocolatey', None)) == 'cinst chocolatey.install'

# Generated at 2022-06-14 09:39:17.628628
# Unit test for function match
def test_match():
    assert match(Command("choco install chocolatey", "", "Installing the following packages:"))
    assert not match(Command("choco install chocolatey", "", "Installing choco"))
    assert match(Command("cinst python2", "", "Installing the following packages:"))
    assert not match(Command("cinst python2", "", "Installing python2"))


# Generated at 2022-06-14 09:39:23.451359
# Unit test for function match
def test_match():
    assert match(Command("choco install foo")) 
    assert match(Command("choco install foo bar"))
    assert match(Command("choco install foo bar"))
    assert match(Command("cinst foo"))
    assert not match(Command("choco foo"))
    assert not match(Command("choco bar foo"))

# Unit test fo function get_new_command

# Generated at 2022-06-14 09:39:30.974988
# Unit test for function get_new_command
def test_get_new_command():
    from tests.utils import Command
    from thefuck.types import Command as TFCommand
    assert "choco install git" == get_new_command(TFCommand(Command("choco install git"), None))
    assert "choco install git.install" == get_new_command(TFCommand(Command("choco install git.install"), None))
    assert "choco install git -y" == get_new_command(TFCommand(Command("choco install git -y"), None))
    assert "choco install git --yes" == get_new_command(TFCommand(Command("choco install git --yes"), None))
    assert "choco install git.install -y" == get_new_command(TFCommand(Command("choco install git.install -y"), None))