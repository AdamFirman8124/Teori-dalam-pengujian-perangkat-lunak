

# Generated at 2022-06-14 09:18:59.040963
# Unit test for function match
def test_match():
   assert match(Command('brew install foo',
    'Error: No available formula for foo\n'
    '==> Searching for similarly named formulae...\n'
    "==> Searching local taps...\n"
    'Error: No similarly named formulae found.\n'
    '==> Searching taps...\n'
    'Error: No formulae found in taps.'))



# Generated at 2022-06-14 09:19:02.695956
# Unit test for function match
def test_match():
    result = match(Command(script='brew install postgresql',
                 output='Error: No available formula for postgresql'))
    assert result


# Generated at 2022-06-14 09:19:06.231531
# Unit test for function match
def test_match():
    assert match(
        Command("brew install pytho3", "Error: No available formula for pytho3"))
    assert not match(
        Command("brew install python3", "Error: No available formula for python3"))

# Generated at 2022-06-14 09:19:09.929486
# Unit test for function match
def test_match():
    assert match(Command('brew install git', 'No available formula'))
    assert not match(Command('brew install git', ''))
    assert not match(Command('brew update', 'No available formula'))



# Generated at 2022-06-14 09:19:12.379112
# Unit test for function match
def test_match():
    expected = False
    result = match(command)
    assert result == expected


# Generated at 2022-06-14 09:19:18.634345
# Unit test for function match
def test_match():
    assert _get_similar_formula('auto') == 'autoconf'
    assert match(Command('brew install auto',
                         'Error: No available formula for auto'))
    assert not match(Command('brew install autoconf',
                         'Error: No available formula for autoconf'))
    assert not match(Command('brew install auto',
                         'Error: No available formula for auto\\n'))


# Generated at 2022-06-14 09:19:20.647632
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('brew install foo') == 'brew install food'

# Generated at 2022-06-14 09:19:28.595200
# Unit test for function match
def test_match():
    assert match(Command('brew install foo', 'Error: No available formula for foo'))
    assert match(Command('brew install foo', 'Error: No available formula for foo\nbar'))
    assert match(Command('brew install foo', 'Error: No available formula for foo\nbar\baz'))
    assert not match(Command('brew install foo', 'Error: No available formula for bar'))
    assert not match(Command('brew install foo', 'Error: No available formula for bar\nfoo'))


# Generated at 2022-06-14 09:19:33.968441
# Unit test for function match
def test_match():
    assert match(Command('brew install gas',
            'Error: No available formula for gas\n'))
    assert not match(Command('brew install git',
            'Error: No available formula for git\n'))
    assert not match('brew install git')



# Generated at 2022-06-14 09:19:46.960680
# Unit test for function get_new_command
def test_get_new_command():
    assert not match(
        ("brew install", "Error: No available formula for teal\n"))
    assert not match(
        ("brew install",
         "Error: No available formula for teal\n"
         "Searching pull requests...\n"
         "+----+-------+-------------------+-------------------+\n"
         "| ID | Title | Opened            | Updated           |\n"
         "+----+-------+-------------------+-------------------+\n"
         "|  1 |       | 2016-11-24 09:13: | 2016-11-24 09:13: |\n"
         "+----+-------+-------------------+-------------------+\n"))
    assert match(
        ("brew install",
         "Error: No available formula for teal\n"
         "Did you mean tealdeer?\n"))

# Generated at 2022-06-14 09:19:59.217084
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

    script = 'brew install lnk'
    output = 'Error: No available formula for lnk'

    command = Command(script, output)
    new_command = get_new_command(command)
    assert new_command == 'brew install link'

    script = 'brew install curl'
    output = 'Error: No available formula for curl'

    command = Command(script, output)
    new_command = get_new_command(command)
    assert new_command == 'brew install curl'

# Generated at 2022-06-14 09:20:09.921490
# Unit test for function get_new_command

# Generated at 2022-06-14 09:20:17.347674
# Unit test for function match
def test_match():
    type_cmd = 'brew install sratoolkit'
    type_output = 'Error: No available formula for sratoolkit'

    assert match(cmd=type_cmd, output=type_output)

    type_cmd = 'brew install safd'
    type_output = 'Error: No available formula for safd'

    assert match(cmd=type_cmd, output=type_output) is False



# Generated at 2022-06-14 09:20:29.048793
# Unit test for function match
def test_match():
    assert match(Command('brew install python3', 'Error: No available formula for python3'))
    assert match(Command('brew install xunlei', 'Error: No available formula for xunlei'))
    assert match(Command('brew install python3', 'Error: No available formula for python3\nError: No available formula for fukc'))
    assert not match(Command('brew install python3', 'Error: No available formula for python3\nError: No available formula for fukc', error=True))
    assert not match(Command('brew install abc', 'Error: No available formula for python3'))
    assert not match(Command('brew ln python3', 'Error: No available formula for python3'))
    assert not match(Command('brew install', 'Error: No available formula for python3'))

# Generated at 2022-06-14 09:20:31.902440
# Unit test for function match
def test_match():
    assert match(Command('brew install git'))
    assert match(Command('brew install tree'))
    assert not match(Command('brew install treee'))


# Generated at 2022-06-14 09:20:36.400767
# Unit test for function match
def test_match():
    assert not match(Command('brew install', output='\U0001F62D'))
    assert match(Command('brew install foo',
                         output='Error: No available formula for foo'))
    assert not match(Command('brew install foo',
                             output='Error: No available formula for foo'))



# Generated at 2022-06-14 09:20:39.524505
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.shells import Shell
    command = Shell().and_('brew install something', 'Error: No available formula for something')
    assert get_new_command(command) == 'brew install somefile'

# Generated at 2022-06-14 09:20:50.880801
# Unit test for function match
def test_match():
    command = type(
        'Command', (object,),
        {'script': 'brew install docker',
         'output': 'Error: No available formula for docker\n'}
    )
    assert match(command)

    command = type(
        'Command', (object,),
        {'script': 'brew install docker',
         'output': 'Error: No available formula for docker\n',
         'debug': True}
    )
    assert not match(command)



# Generated at 2022-06-14 09:20:58.559625
# Unit test for function match
def test_match():
    from thefuck.rules.brew_install import match

    #  brew install
    assert match(Command('brew install feh',
                         'Error: No available formula for feh'))
    assert match(Command('brew install ZZ',
                         'Error: No available formula for ZZ'))
    assert not match(Command('brew install feh',
                             "Error: No available formula with the name \"feh\""))
    assert not match(Command('brew install feh',
                             "Error: feh-2.22 is already installed"))

    #  brew cask install
    assert match(Command('brew cask install feh',
                         'Error: No available formula for feh'))
    assert match(Command('brew cask install ZZ',
                         'Error: No available formula for ZZ'))

# Generated at 2022-06-14 09:21:01.550665
# Unit test for function match
def test_match():
    assert match(Command('brew install foo', 'Error: No available formula for foo'))
    assert match(Command('brew install telegram-cli', 'Error: No available formula for telegram-cli'))
    assert not match(Command('brew install foo', 'Error: No available formula'))
    assert not match(Command('brew install foo', ''))
    assert not match(Command('foo', 'Error: No available formula for telegram-cli'))


# Generated at 2022-06-14 09:21:16.377157
# Unit test for function match
def test_match():
    assert match(Command('brew install ack',
                         'Error: No available formula for ack\r\n'))
    assert match(Command('brew install ack',
                         'Error: No available formula for ack\r\n'))
    assert not match(Command('brew install ack',
                             'Error: No available formula for ack\r\n'))
    assert not match(Command('brew install ack',
                             'Error: No available formula for ack\r\n'))



# Generated at 2022-06-14 09:21:22.854113
# Unit test for function match
def test_match():
    assert match(Command('brew install darwinia', ''))
    assert not match(Command('brew install darwinia', 'Error: unknown command install'))
    assert not match(Command('brew install darwinia', 'Error: No available formula for darwinia'))
    assert not match(Command('brew install darwinia', 'Error: No available formula'))


# Generated at 2022-06-14 09:21:24.700633
# Unit test for function match
def test_match():
    assert match(Command('brew install kubectl', '', 'No available formula for kubectl'))


# Generated at 2022-06-14 09:21:29.883729
# Unit test for function get_new_command
def test_get_new_command():
    test_script = 'brew install pytnon3'
    test_output = 'Error: No available formula for pytnon3'
    command = Command(script=test_script, output=test_output)
    new_command = get_new_command(command)
    assert new_command == 'brew install python3'

# Generated at 2022-06-14 09:21:33.298435
# Unit test for function get_new_command
def test_get_new_command():
    import thefuck.specific.brew as brew
    from thefuck.types import Command
    brew.get_brew_path_prefix = lambda: '.'
    assert brew.get_new_command(Command('brew install firefox', '', '', None, None)) == 'brew install Caskroom/cask/firefox'

# Generated at 2022-06-14 09:21:44.413905
# Unit test for function match
def test_match():
    assert match(
        Command('brew install vlc ',
        'Error: No available formula for vlc\nSearching formulae...\n'
        'Searching taps...\nNo formulae found in taps.'))
    assert not match(
        Command('brew install vlc ',
        'Error: No available formula for vlc\nSearching formulae...\n'
        'Searching taps...\nNo formulae found in taps.\nError: No available formula for vlc'))
    assert not match(
        Command('brew install vlc ',
        'Error: No available formula for vlc\nSearching formulae...\n'
        'Searching taps...\n'))



# Generated at 2022-06-14 09:21:46.947021
# Unit test for function match
def test_match():
    assert match(Command('brew install tmux-xd', 'Error: No available formula for tmux-xd')) == True
    assert match(Command('brew install tmuxx', 'Error: No available formula for tmuxx')) == True
    assert match(Command('brew install node', 'Error: No available formula for node')) == False



# Generated at 2022-06-14 09:21:54.497038
# Unit test for function match
def test_match():
    script = 'brew install some_random_stuff'
    output = 'Error: No available formula for some_random_stuff'
    assert match(Script(script, output)) is False

    output = 'Error: No available formula for tmux-cssh'
    assert match(Script(script, output)) is True

    output = 'Error: No available formula for tmux-cssh and something else'
    assert match(Script(script, output)) is True



# Generated at 2022-06-14 09:21:59.980400
# Unit test for function get_new_command
def test_get_new_command():
    from tests.utils import Command

    script = 'brew install git2'
    output = u"""Error: No available formula for git2
Searching formulae...
Searching taps...
No similarly named formulae found.
Searching local taps..."""

    assert get_new_command(Command(script, output)) == 'brew install git'

# Generated at 2022-06-14 09:22:04.777755
# Unit test for function match
def test_match():
    from tests.utils import Command

    assert match(Command('brew install foo',
                         'Error: No available formula for foo'))
    assert not match(Command('brew install foo', ''))
    assert not match(Command('foo install foo',
                             'Error: No available formula for foo'))
    assert not match(Command('brew foo foo',
                             'Error: No available formula for foo'))


# Generated at 2022-06-14 09:22:21.661547
# Unit test for function match
def test_match():
    assert match(Command('brew install thefuct',
                         'Error: No available formula for thefuct\n'))
    assert not match(Command('brew install thefuck',
                             'Error: No such keg: /usr/local/Cellar/thefuck'))

# Generated at 2022-06-14 09:22:28.320414
# Unit test for function match
def test_match():
    from thefuck.types import Command
    from thefuck.rules.brew_install_did_you_mean import match

    assert match(Command('brew install tmux',
                         'Error: No available formula for tmux'))
    assert match(Command('brew install emacs',
                         'Error: No available formula for emacs'))
    assert match(Command('brew install foo',
                         'Error: No available formula for foo'))



# Generated at 2022-06-14 09:22:34.812819
# Unit test for function match
def test_match():
    script = 'brew install mongo'
    output = 'Error: No available formula for mondgo'
    command = Command(script, output)
    assert False == match(command)

    script = 'brew install mongo'
    output = 'Error: No available formula for mongo'
    command = Command(script, output)
    assert True == match(command)



# Generated at 2022-06-14 09:22:40.312834
# Unit test for function get_new_command
def test_get_new_command():
    command_script = 'brew install pythong'
    command = type('', (), {})
    command.script = 'brew install pythong'
    command.output = 'Error: No available formula for pythong'
    assert get_new_command(command) == 'brew install python'

# Generated at 2022-06-14 09:22:46.352941
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('brew install asdasd') == 'brew install asdf'
    assert get_new_command('brew install asdasd asdasdasdasd') == 'brew install asdf asdasdasdasd'
    assert get_new_command('brew install asdasd asdasdasdasd') != 'brew install asdf'

# Generated at 2022-06-14 09:22:48.242159
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('brew install kmnop') == 'brew install vim'

# Generated at 2022-06-14 09:22:52.359764
# Unit test for function match
def test_match():
    assert match(Command('brew install aaa', '')) is False
    assert match(Command('brew install aaa', 'Error: No available formula for aaa')) is False
    assert match(Command('brew install aaa', 'Error: No available formula for aaa\n')) is True



# Generated at 2022-06-14 09:22:59.532690
# Unit test for function match
def test_match():
    assert match(Command('brew install tesseract',
                         stderr='Error: No available formula for tesseract'))
    assert not match(Command('brew install tesseract', stderr='Error: No available formula for tesseract\nError: No available formula for tesseract'))
    assert not match(Command('brew install tesseract'))
    assert not match(Command('brew uninstall tesseract'))


# Generated at 2022-06-14 09:23:07.044191
# Unit test for function match
def test_match():
    assert match(Command('brew install xxx',
                         """
                         Error: No available formula for xxx
                         Searching formulae...
                         xxx-yyy
                         xxx-yyy-zzz
                         Searching taps...
                         xxx/xxx-yyy
                         xxx/xxx-yyy-zzz
                         """))
    assert not match(Command('brew install xxx',
                             """
                             Error: No available formula for xxx
                             Searching formulae...
                             xxx-yyy
                             xxx-yyy-zzz
                             Searching taps...
                             xxx/xxx-yyy
                             xxx/xxx-yyy-zzz
                             """))

# Generated at 2022-06-14 09:23:12.044893
# Unit test for function match
def test_match():
    assert not match(
        Command('brew install vim', 'Error: No available formula with the name "vim"'))
    assert not match(
        Command('brew install vim', ''))
    assert match(
        Command('brew install vim', 'Error: No available formula for vim'))


# Generated at 2022-06-14 09:23:42.106570
# Unit test for function match
def test_match():
    assert match(Command('brew install mongodb', 'No available formula'))
    assert not match(Command('brew install mongodb', ''))
    assert not match(Command('brew install mongodb', 'No available formula for something'))


# Generated at 2022-06-14 09:23:45.844065
# Unit test for function match
def test_match():
    assert match(Command('brew install ag', 'Error: No available formula for ag'))
    assert not match(Command('brew install ag', 'Error: No available formula'))

# Generated at 2022-06-14 09:23:50.875272
# Unit test for function match
def test_match():
    assert_true(match({'script': 'Error: No available formula for test', 'output': 'Error: No available formula for test'}))
    assert_false(match({'script': 'Error: No available formula for test', 'output': 'Error: No available formu for test'}))


# Generated at 2022-06-14 09:24:03.042853
# Unit test for function match
def test_match():
    command = type('', (), {})()
    # Check if function return `True` when formula does not exist in command's output
    # and there is similar formula to it.
    command.script = 'brew install not_exist_formula'
    command.output = 'Error: No available formula for not_exist_formula\nSomething Else'
    assert match(command) == True

    # Check if function return `False` when formula does not exist in command's output
    # and there is not similar formula to it.
    command.script = 'brew install not_exist_formula'
    command.output = 'Error: No available formula for not_exist_formula\nSomething Else'
    assert match(command) == True

    # Check if function return `False` when formula does exist in command's output.

# Generated at 2022-06-14 09:24:11.093896
# Unit test for function match
def test_match():
    assert match(Command('brew install git',
                         "Error: No available formula for git",
                        ""))
    assert match(Command('brew install screenfetch',
                         "Error: No available formula for screenfetch",
                        ""))
    assert match(Command('brew install vr',
                         "Error: No available formula for vr",
                        ""))
    assert match(Command('brew install ghq',
                         "Error: No available formula for ghq",
                        ""))
    assert not match(Command('brew install sl',
                         "Error: No available formula for sl",
                        ""))
    assert not match(Command('brew install lolcat',
                         "Error: No available formula for lolcat",
                        ""))



# Generated at 2022-06-14 09:24:18.054484
# Unit test for function match
def test_match():
    assert match('$ brew install hummus')
    assert match('$ brew install hummus2')
    assert not match('$ brew install ')
    assert not match('$ brew install --devel hummus')
    assert not match('$ brew remove hummus')
    assert not match('$ brew update hummus')

test_match()

# Generated at 2022-06-14 09:24:20.940799
# Unit test for function match
def test_match():
    assert not match(Command('ls', ''))
    assert match(Command('brew install opensshl', 'Error: No available formula for opensshl'))



# Generated at 2022-06-14 09:24:30.094106
# Unit test for function get_new_command

# Generated at 2022-06-14 09:24:32.311686
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('brew install htop') == 'brew install homebrew/gui/htop'

# Generated at 2022-06-14 09:24:37.488138
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.brew_similar_formula import get_new_command
    from thefuck.types import Command

    command = Command('brew install mysql',
                      'Error: No available formula for mysql')
    new_command = get_new_command(command)
    assert new_command == 'brew install mariadb'

# Generated at 2022-06-14 09:25:28.389787
# Unit test for function get_new_command
def test_get_new_command():
    pass

# Generated at 2022-06-14 09:25:31.997895
# Unit test for function match
def test_match():
    command = type('obj', (object,),
                   {'script': 'brew install tmux',
                    'output': 'Error: No available formula for tmux'})
    assert match(command) is True



# Generated at 2022-06-14 09:25:36.080496
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command

    assert get_new_command(Command('brew install formula', '')) == 'brew install formula'


# Generated at 2022-06-14 09:25:40.875830
# Unit test for function get_new_command
def test_get_new_command():
    script = 'brew install myapp'
    output = 'Error: No available formula for myapp'
    command = type('command', (object,), {'script': script, 'output': output})

    assert(get_new_command(command) == 'brew install myapps')


# Generated at 2022-06-14 09:25:49.587687
# Unit test for function match
def test_match():
    def make_script(formula):
        return 'brew install %s' % formula

    assert match(Command(script=make_script('airline')))
    assert match(Command(script=make_script('zsh-syntax-highlighting')))
    assert match(Command(script='brew install zgen'))
    assert match(Command(script='brew install zsh-syntax-highlighting'))
    assert not match(Command(script=make_script('zsh-syntax-highlighting'),
                             output='Error: No available formula'))
    assert not match(Command(script='brew install zhen',
                             output='Error: No available formula for zhen'))
    assert not match(Command(script='brew install airline',
                             output='Error: No available formula with airline'))


# Generated at 2022-06-14 09:25:56.691322
# Unit test for function match
def test_match():
    assert not match(Command('brew install', ''))
    assert not match(Command('brew install', 'Error: No such keg: /usr/local/Cellar/fish'))
    assert match(Command('brew install', 'Error: No available formula for fish'))
    assert match(Command('brew install', 'Error: No available formula for tezt'))


# Generated at 2022-06-14 09:26:01.004763
# Unit test for function match
def test_match():
    assert match(Command('brew install hello', '')) == False
    assert match(Command('brew install hello', 'Error: No available formula for hello\n')) == False
    assert match(Command('brew install foo', 'Error: No available formula for foo\n')) == True



# Generated at 2022-06-14 09:26:06.371244
# Unit test for function match
def test_match():
    assert match({'script': 'brew install not-exist',
                  'output': 'Error: No available formula for not-exist'})

    assert not match({'script': 'brew install not-exist',
                      'output': 'Error: No available formula for not-exist'})



# Generated at 2022-06-14 09:26:13.477245
# Unit test for function match
def test_match():
    assert match(Command('brew install a_formula'))
    assert match(Command('brew install a_formula',
                         'Error: No available formula for a_formula'))
    assert not match(Command('brew install',
                             'Error: No available formula for a_formula'))
    assert not match(Command('brew search a_formula'))


# Generated at 2022-06-14 09:26:17.398404
# Unit test for function get_new_command
def test_get_new_command():
    command = type('Command', (object,),
                   {'script': 'brew install gbalr',
                    'output': 'Error: No available formula for gbalr'})

    assert get_new_command(command) == 'brew install nbalr'

# Generated at 2022-06-14 09:27:10.767128
# Unit test for function match
def test_match():
    assert match(command.Command('brew install foo',
                                 'Error: No available formula for foo\nInstall a formula with `brew install <formula>`.'))
    assert not match(command.Command('brew install foo', 'foo'))

# Generated at 2022-06-14 09:27:22.234424
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.brew_install_command import get_new_command

    script = 'brew install telegram'
    output = 'Error: No available formula for telegram'

    command = Command(script, output)
    new_command = get_new_command(command)

    assert new_command == 'brew install telegram-cli'



# Generated at 2022-06-14 09:27:28.208565
# Unit test for function match
def test_match():
    assert not match(Command(script='brew'))
    assert not match(Command(script='brew install',
                             output='Error: No available formula for xxx'))
    assert not match(Command(script='brew install',
                             output='Error: No available formula for xxx xxx'))
    assert not match(Command(script='brew install', output='No package xxx available'))
    assert not match(Command(script='brew install xxx', output='Error: No available formula with the name "xxx"'))
    assert match(Command(script='brew install xxx', output='Error: No available formula for xxx'))

# Generated at 2022-06-14 09:27:41.503952
# Unit test for function match
def test_match():
    assert match(Command('brew install vim --override-system-vim',
                         'Error: No available formula for vim'))
    assert match(Command('brew install vim --override-system-vim',
                         'Error: No available formula for vim\n'))
    assert match(Command('brew install vim --override-system-vim',
                         'Error: No available formula for vim\nwfefew'))
    assert match(Command('brew install vim --override-system-vim',
                         'Error: No available formula for vim\n'
                         'Error: No available formula for vim\n'))
    assert not match(Command('brew install vim --override-system-vim',
                             'Error: No available formula for vim\n'
                             'Error: No available formula for python\n'))



# Generated at 2022-06-14 09:27:50.920815
# Unit test for function match
def test_match():
    # Return True
    command = Command("brew install google-chrome",
                      "Error: No available formula for google-chrome")
    assert match(command)
    command = Command("brew install chromium",
                      "Error: No available formula for chromium")
    assert match(command)

    # Return False
    command = Command("brew install google-chrome",
                      "Error: No such file or directory")
    assert not match(command)
    command = Command("brew install google-chrome",
                      "Error: No available formula for chromuim")
    assert not match(command)


# Generated at 2022-06-14 09:27:52.855717
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('brew install git') == 'brew install git'

# Generated at 2022-06-14 09:28:01.356478
# Unit test for function match
def test_match():
    import os
    import pytest
    from thefuck.specific.brew import (match, _get_formulas, _get_similar_formula)
    from thefuck.types import Command
    from tests.utils import CommandStub

    # Check if brew is available and brew has at least one formula on the system
    if (not brew_available or
            not len(list(formula for formula in _get_formulas()))):
        pytest.skip('brew is not available or has no formulas')

    # Notify if a formula is not installed yet
    command_type = CommandStub(script='brew install scala',
                               stdout=('Error: No available formula for scala\n'
                                       'Searching formulae...\n'
                                       'Searching taps...\n'))
    assert match(command_type)



# Generated at 2022-06-14 09:28:06.323236
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    assert get_new_command(Command('brew install cloc',
                                   'Error: No available formula for cloc\n'
                                   'Searching formulae...\nSearching taps...\n')) == \
        'brew install count-lines-of-code'

# Generated at 2022-06-14 09:28:13.629054
# Unit test for function get_new_command
def test_get_new_command():
    not_exist_command = 'brew install traceroutt'
    not_exist_formula = 'traceroutt'
    exist_formula = 'mtr'

    command = type('', (object,), {'script': not_exist_command, 'output':'Error: No available formula for traceroutt'})

    assert get_new_command(command) == \
        'brew install mtr'

# Generated at 2022-06-14 09:28:16.992143
# Unit test for function match
def test_match():
    assert match(Command('brew install bower',
                         "Error: No available formula for bower"))
    assert match(Command('brew install bower',
                         "Error: No available formula for bower\n"))